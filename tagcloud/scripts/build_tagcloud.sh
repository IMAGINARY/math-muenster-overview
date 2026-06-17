#!/usr/bin/env bash
# build_tagcloud.sh
# Reads tagcloud/data/vocabulary.json and counts every term in the combined corpus.
# Produces two CSVs:
#   exports/tagcloud_independent.csv  — every alias counted independently, no masking
#   exports/tagcloud_masked.csv       — longest-alias-first greedy masking (no double-count)
#
# Requirements: jq, rg (ripgrep), coreutils
# Usage: bash tagcloud/scripts/build_tagcloud.sh  (from repo root)

set -euo pipefail

REPO="$(cd "$(dirname "$0")/../.." && pwd)"
VOCAB="$REPO/tagcloud/data/vocabulary.json"
CORPUS="$REPO/tagcloud/data/corpus_all.txt"
OUT="$REPO/tagcloud/exports"
mkdir -p "$OUT"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Corpus: $CORPUS"
echo "Vocabulary: $VOCAB"
echo ""

# ── Extract all (canonical, alias) pairs from vocabulary.json ─────────────────
# For each entry: emit  canonical TAB alias  for every alias (+ canonical itself)
jq -r '
  .[] |
  .canonical as $c |
  ([$c] + (.variants // [])) |
  .[] |
  select(length > 0) |
  [$c, .] |
  @tsv
' "$VOCAB" > "$TMP/pairs.tsv"

echo "Total (canonical, alias) pairs: $(wc -l < "$TMP/pairs.tsv")"

# ── MODE 1: Independent counting ──────────────────────────────────────────────
# Count every alias independently; sum per canonical.
echo ""
echo "Running independent counting..."

> "$TMP/indep_counts.tsv"   # canonical TAB count

while IFS=$'\t' read -r canonical alias; do
  # Case-insensitive, whole-word match; count all non-overlapping occurrences
  # rg -oi: output each match on its own line; count lines
  cnt=$(rg -oi --pcre2 "(?<![a-zA-Z0-9\-])$(printf '%s' "$alias" | sed 's/[.[\*^$()+?{|]/\\&/g')(?![a-zA-Z0-9\-])" \
        "$CORPUS" 2>/dev/null | wc -l || echo 0)
  echo -e "${canonical}\t${cnt}" >> "$TMP/indep_counts.tsv"
done < "$TMP/pairs.tsv"

# Sum counts per canonical
sort "$TMP/indep_counts.tsv" | \
  awk -F'\t' '{sum[$1]+=$2} END {for(c in sum) print c"\t"sum[c]}' | \
  sort -t$'\t' -k2 -rn > "$TMP/indep_sorted.tsv"

echo "text,weight" > "$OUT/tagcloud_independent.csv"
while IFS=$'\t' read -r canonical cnt; do
  [[ "$cnt" -gt 0 ]] && printf '%s,%s\n' "$canonical" "$cnt"
done < "$TMP/indep_sorted.tsv" >> "$OUT/tagcloud_independent.csv"

INDEP_TERMS=$(tail -n +2 "$OUT/tagcloud_independent.csv" | wc -l)
echo "  -> $INDEP_TERMS terms with weight > 0"

# ── MODE 2: Masked counting (longest alias first, no double-count) ─────────────
echo ""
echo "Running masked counting..."

# Build a flat list of (alias, canonical) sorted by alias length desc
jq -r '
  .[] |
  .canonical as $c |
  ([$c] + (.variants // [])) |
  .[] |
  select(length > 0) |
  [$c, .] |
  @tsv
' "$VOCAB" | \
  awk -F'\t' '{print length($2)"\t"$2"\t"$1}' | \
  sort -rn > "$TMP/aliases_by_length.tsv"   # len TAB alias TAB canonical

# Work on a mutable copy of the corpus (replace matched spans with underscores)
cp "$CORPUS" "$TMP/corpus_work.txt"

declare -A masked_counts

while IFS=$'\t' read -r _len alias canonical; do
  # Count matches in current (masked) working corpus
  pat=$(printf '%s' "$alias" | sed 's/[.[\*^$()+?{|]/\\&/g')
  cnt=$(rg -oi --pcre2 "(?<![a-zA-Z0-9\-])${pat}(?![a-zA-Z0-9\-])" \
        "$TMP/corpus_work.txt" 2>/dev/null | wc -l || echo 0)

  if [[ "$cnt" -gt 0 ]]; then
    # Accumulate count for this canonical
    masked_counts["$canonical"]=$(( ${masked_counts["$canonical"]:-0} + cnt ))
    # Blank out matched spans so shorter aliases inside them aren't recounted
    # Replace each match with same-length underscores (preserves byte offsets isn't needed;
    # simple sed replacement is sufficient since we only care about counts)
    sed -i.bak "s/${pat}/____MASKED____/gI" "$TMP/corpus_work.txt" 2>/dev/null || true
  fi
done < "$TMP/aliases_by_length.tsv"

# Write masked CSV
{
  echo "text,weight"
  for canonical in "${!masked_counts[@]}"; do
    cnt=${masked_counts[$canonical]}
    [[ "$cnt" -gt 0 ]] && printf '%s,%s\n' "$canonical" "$cnt"
  done
} | (head -1; tail -n +2 | sort -t, -k2 -rn) > "$OUT/tagcloud_masked.csv"

MASKED_TERMS=$(tail -n +2 "$OUT/tagcloud_masked.csv" | wc -l)
echo "  -> $MASKED_TERMS terms with weight > 0"

echo ""
echo "Done."
echo "  $OUT/tagcloud_independent.csv"
echo "  $OUT/tagcloud_masked.csv"
