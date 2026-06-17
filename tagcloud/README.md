# Tag Cloud — Mathematics Münster Mathematical Terms

Tag-cloud frequency data for mathematical terms appearing across the Mathematics Münster research programme.

## Outputs

| File | Description |
|------|-------------|
| [exports/tagcloud.html](exports/tagcloud.html) | **Interactive tag cloud** — serve over HTTP and open in a browser. Toggle counting mode, scale, and minimum weight live. |
| `exports/tagcloud_independent.csv` | `text,weight` — weight = total occurrences of the term (and all its aliases) across the full corpus. Each alias counted independently; counts summed per canonical term. 326 terms. |
| `exports/tagcloud_masked.csv` | `text,weight` — same corpus, but using **longest-match-first greedy masking**: once a longer alias is matched and blanked out, shorter aliases nested inside it are not recounted. 324 terms. |

Both files use the standard tag-cloud schema `text,weight` (CSV, header row, values quoted) accepted directly by d3-cloud, wordcloud2.js, Python `wordcloud`, and R `wordcloud`.

## Corpus

Two sources, concatenated into `data/corpus_all.txt`:

**Repo** (`data/corpus_repo.txt`) — local markdown files:
- `GLOSSARY.md`, `EXPLORATION.md`, `README.md`
- `topics/topic_*.md` (10 files)
- `connections/*.md`

**Web** (`data/corpus_web.txt`) — snapshots of the 10 Mathematics Münster research-programme subpages (fetched June 2026), saved to `data/raw/topic_NN_*.md`:
- T1: K-groups and cohomology
- T2: Moduli spaces in arithmetic and geometry
- T3: Models and universes
- T4: Groups and actions
- T5: Curvature, shape and global analysis
- T6: Singularities and partial differential equations
- T7: Field theory and randomness
- T8: Random discrete structures and their limits
- T9: Multiscale processes and effective behaviour
- T10: Deep learning and surrogate methods

Each subpage snapshot includes the topic overview, all publication titles from the "Selected" and "Recent publications" sections, and the research unit descriptions.

## Vocabulary

`data/vocabulary.json` — **267 canonical terms** with alias lists and provenance, produced by LLM extraction (one agent per subpage + repo files) followed by a reconciliation pass. Each entry:

```json
{
  "canonical": "K-theory",
  "variants": ["K-groups", "algebraic K-theory", "topological K-theory", ...],
  "provenance": ["T1", "T2", "T4", "repo"]
}
```

The vocabulary determines what counts as a term. The counting step is fully deterministic given a fixed `vocabulary.json`.

## Counting method

**Independent mode** (`tagcloud_independent.csv`):
- For every alias in the vocabulary, count case-insensitive fixed-string occurrences in the full corpus (`rg -io --fixed-strings`).
- Sum across all aliases for the same canonical term.
- Counts are alias-folded but not span-exclusive: "algebraic K-theory" and "K-theory" are each counted wherever they appear; a phrase like "algebraic K-theory" contributes to `K-theory` twice (once for the full phrase alias, once for the bare alias).
- Use this mode when you want maximum term visibility.

**Masked mode** (`tagcloud_masked.csv`):
- Process aliases sorted **longest-first**.
- After counting an alias, replace all its occurrences in a working copy of the corpus with a placeholder string.
- Shorter aliases (e.g. bare "K-theory") are then counted only in the spans not already consumed by a longer match.
- Each text span is credited to at most one canonical term (the most specific one that covers it).
- Use this mode for a cleaner frequency signal without inflation from nested terms.

## Reproducing the counts

Requirements: `jq`, `rg` (ripgrep), `perl`.

```bash
# From repo root:
bash tagcloud/scripts/build_tagcloud.sh
```

The script reads `data/vocabulary.json` and `data/corpus_all.txt` and writes both CSVs to `exports/`. Intermediate files land in `data/tmp/`.

To refresh the web corpus, re-fetch the 10 subpages and overwrite `data/raw/`, then re-concatenate:

```bash
cat data/corpus_repo.txt data/raw/*.md > data/corpus_all.txt
bash tagcloud/scripts/build_tagcloud.sh
```

## Using the CSVs

**Python wordcloud:**
```python
import pandas as pd
from wordcloud import WordCloud
df = pd.read_csv("tagcloud/exports/tagcloud_masked.csv")
freq = dict(zip(df["text"], df["weight"]))
wc = WordCloud(width=1600, height=800).generate_from_frequencies(freq)
wc.to_file("tagcloud.png")
```

**R wordcloud:**
```r
library(wordcloud)
df <- read.csv("tagcloud/exports/tagcloud_masked.csv")
wordcloud(words=df$text, freq=df$weight, min.freq=2, scale=c(4,0.5))
```

**wordcloud2.js / d3-cloud:** load the CSV, map `text` → word, `weight` → size.

## Top 20 terms (masked mode)

| Term | Weight |
|------|--------|
| partial differential equation | 129 |
| K-theory | 110 |
| cohomology | 104 |
| model order reduction | 101 |
| artificial neural network | 83 |
| curvature | 81 |
| manifold | 68 |
| moduli space | 47 |
| machine learning | 41 |
| homogenisation | 34 |
| quantum field theory | 32 |
| C*-algebra | 31 |
| Langlands programme | 30 |
| percolation | 28 |
| stochastic gradient descent | 23 |
| geodesic | 22 |
| Phi^4 equation | 21 |
| operator algebra | 21 |
| amenable group | 21 |
| optimal control | 19 |
