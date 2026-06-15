#!/usr/bin/env python3
"""
build_bipartite.py
==================
Produces a strict bipartite graph:

  LEFT  side  — 10 topic nodes (one per topic file)
  RIGHT side  — mathematical terms (GLOSSARY) + core concepts (topic files)

Edges only cross between left and right; no intra-side edges.

Edge sources
  1. explicit GLOSSARY.md links inside topic intro + concept bodies  → "uses"
  2. term-label name-matching in topic full text                     → "mentions"
     (catches terms referenced by name but not hyperlinked)

Outputs (Cosmograph-ready CSV)
  bipartite_nodes.csv   — id, label, side, type, description
  bipartite_edges.csv   — source, target, type, weight

  weight = number of distinct mentions/links within that topic's text
           (useful for edge thickness in Cosmograph)

Also writes bipartite_graph.json in Kumu format for reference.
"""

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO        = Path(__file__).parent.parent.parent
GLOSSARY    = REPO / "GLOSSARY.md"
EXPLORATION = REPO / "EXPLORATION.md"
TOPICS_DIR  = REPO / "topics"
OUT_DIR     = REPO / "graphs" / "exports" / "bipartite"
OUT_NODES  = OUT_DIR / "bipartite_nodes.csv"
OUT_EDGES  = OUT_DIR / "bipartite_edges.csv"
OUT_KUMU   = OUT_DIR / "bipartite_graph.json"

# ─── Helpers ──────────────────────────────────────────────────────────────────

def md_links_to_glossary(text: str) -> list[str]:
    """Return glossary slugs from explicit markdown links to GLOSSARY.md."""
    pattern = r'\[([^\]]*)\]\([^)]*GLOSSARY\.md#([\w\-]+)\)'
    return [m.group(2) for m in re.finditer(pattern, text)]


def strip_md(text: str) -> str:
    """Strip markdown links, bold/italic, headings for plain-text matching."""
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links → label
    text = re.sub(r'[*_#`>]', ' ', text)
    return text


# ─── 1. Parse GLOSSARY → term nodes ──────────────────────────────────────────

def parse_glossary(path: Path) -> tuple[list[dict], dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    entry_pattern = re.compile(
        r'<a id="([\w\-]+)"></a>\s*\n\*\*([^*]+)\*\*\s*\n(.*?)(?=\n<a id=|\n---\n|\Z)',
        re.DOTALL,
    )
    nodes, bodies = [], {}
    for m in entry_pattern.finditer(text):
        slug  = m.group(1)
        label = m.group(2).strip()
        body  = m.group(3).strip()

        desc_lines = []
        for line in body.splitlines():
            s = line.strip()
            if re.match(r'^\[.*\]\(.*\)', s) and '·' in s or s == '---':
                continue
            desc_lines.append(line)
        description = ' '.join(l.strip() for l in desc_lines if l.strip())
        description = description[:250] + '…' if len(description) > 250 else description

        node_id = f"term:{slug}"
        nodes.append({
            "id":          node_id,
            "label":       label,
            "type":        "term",
            "side":        "right",
            "slug":        slug,
            "description": description,
        })
        bodies[node_id] = body
    return nodes, bodies


# ─── 2. Parse topic files → topic + concept nodes ────────────────────────────

def parse_topic_file(path: Path) -> tuple[dict | None, list[dict], dict[str, str]]:
    text = path.read_text(encoding="utf-8")

    title_m = re.match(r'^# Topic (\d+) — (.+)', text, re.MULTILINE)
    if not title_m:
        return None, [], {}
    topic_num   = title_m.group(1)
    topic_title = title_m.group(2).strip()

    topic_slug  = f"topic-{int(topic_num):02d}"
    topic_id    = f"topic:{topic_slug}"
    topic_label = f"Topic {topic_num}: {topic_title}"

    obj_m = re.search(r'MM\s+"(O\d+)"', text)
    obj_code = obj_m.group(1) if obj_m else None

    # Short description from blockquote
    quote_m = re.search(r'>\s+\*\*(Objective[^)]*)\*\*[:\s]*(.*?)(?:\n)', text, re.DOTALL)
    if quote_m:
        desc = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', quote_m.group(0))
        desc = re.sub(r'[>*]', '', desc).strip()[:250]
    else:
        desc = topic_title

    topic_node = {
        "id":             topic_id,
        "label":          topic_label,
        "type":           "topic",
        "side":           "left",
        "topic_number":   int(topic_num),
        "objective_code": obj_code,
        "description":    desc,
        "full_text":      text,   # kept for name-matching, not written to CSV
    }

    concept_pattern = re.compile(
        r'^## Core concept (\d+): (.+?)\n(.*?)(?=^## Core concept|^## How|\Z)',
        re.MULTILINE | re.DOTALL,
    )
    concept_nodes = []
    bodies = {}

    for cm in concept_pattern.finditer(text):
        con_num   = cm.group(1)
        con_title = cm.group(2).strip()
        con_body  = cm.group(3).strip()

        con_id = f"concept:{topic_slug}-concept-{con_num}"

        level0_m = re.search(r'### Level 0[^\n]*\n(.*?)(?=###|\Z)', con_body, re.DOTALL)
        if level0_m:
            l0 = level0_m.group(1).strip()
            desc_short = l0[:250] + '…' if len(l0) > 250 else l0
        else:
            desc_short = con_title

        concept_nodes.append({
            "id":          con_id,
            "label":       con_title,
            "type":        "concept",
            "side":        "right",
            "topic_id":    topic_id,
            "concept_num": int(con_num),
            "description": desc_short,
        })
        bodies[con_id] = con_body

    return topic_node, concept_nodes, bodies


# ─── 3. Build bipartite edges ─────────────────────────────────────────────────

def build_bipartite_edges(
    topic_nodes:   list[dict],
    concept_nodes: list[dict],
    term_nodes:    list[dict],
    concept_bodies: dict[str, str],
) -> list[dict]:
    """
    Return edges ONLY between topic (left) and term/concept (right).

    Strategy:
      A) Each concept belongs to a topic → aggregate concept→term links up to
         the topic level (topic –uses→ term).
      B) Topic intro text may also link to glossary directly.
      C) Name-matching: scan each topic's full text for term labels not already
         captured by explicit links.

    Weight = raw mention/link count within that topic's full text.
    """

    slug_to_term_id = {n["slug"]: n["id"] for n in term_nodes}

    # Build label→term_id map for name-matching (longest label first)
    label_map: list[tuple[str, str]] = []
    for n in term_nodes:
        base = re.sub(r'\s*\([^)]+\)$', '', n["label"]).strip()
        label_map.append((base.lower(), n["id"]))
    label_map.sort(key=lambda x: -len(x[0]))

    # concept_id → topic_id lookup
    con_to_topic = {c["id"]: c["topic_id"] for c in concept_nodes}

    # Collect raw (topic_id, right_id, type) with counts
    raw: dict[tuple[str, str, str], int] = defaultdict(int)

    for topic in topic_nodes:
        topic_id  = topic["id"]
        full_text = topic["full_text"]
        plain     = strip_md(full_text).lower()

        # A) Explicit GLOSSARY links in full topic text (intro + all concepts)
        for slug in md_links_to_glossary(full_text):
            if slug in slug_to_term_id:
                raw[(topic_id, slug_to_term_id[slug], "uses")] += 1

        # B) Name-matching for terms not explicitly linked
        for label_lower, term_id in label_map:
            escaped = re.escape(label_lower)
            count = len(re.findall(r'\b' + escaped + r'\b', plain))
            if count > 0:
                key_uses = (topic_id, term_id, "uses")
                key_men  = (topic_id, term_id, "mentions")
                # Only add "mentions" if not already captured as "uses"
                if key_uses not in raw:
                    raw[key_men] += count

        # C) topic → concept edges (concept belongs to this topic)
        for concept in concept_nodes:
            if concept["topic_id"] == topic_id:
                raw[(topic_id, concept["id"], "contains")] += 1

    # Convert to edge list
    edges = []
    for (from_id, to_id, etype), weight in raw.items():
        if from_id == to_id:
            continue
        edges.append({
            "from":   from_id,
            "to":     to_id,
            "type":   etype,
            "weight": weight,
        })

    return edges


# ─── 4. Assign bipartite layout coordinates ───────────────────────────────────

def assign_coordinates(
    topic_nodes:   list[dict],
    concept_nodes: list[dict],
    term_nodes:    list[dict],
    edges:         list[dict],
) -> set[str]:
    """
    Assign x/y so Cosmograph starts with topics centred between concepts and terms.

    Column layout (x values):
      x = -200   connected terms   (left)
      x =    0   topics            (centre)
      x = +200   concepts          (right)

    Isolated terms (no edges to any topic) are excluded entirely — they are
    background glossary vocabulary not referenced by the MM research programme.
    Their ids are returned so main() can filter them out of the node/edge lists.

    Topics are spaced TOPIC_STEP apart on y.
    Concepts: 5 per topic, fanned around their topic's y-centre (same step).
    Terms: grouped by primary topic (highest total edge weight), placed in the
           same y-band; multiple terms per band stacked with TERM_STEP spacing.
    """
    from collections import defaultdict as _dd

    TOPIC_STEP = 100          # vertical gap between topic centres
    CON_STEP   = TOPIC_STEP / 6   # gap between sibling concepts

    # ── Topics (x=0, centre) ──────────────────────────────────────────────────
    for i, t in enumerate(topic_nodes):
        t["x"] = 0
        t["y"] = i * TOPIC_STEP

    topic_y = {t["id"]: t["y"] for t in topic_nodes}

    # ── Concepts (x=+200, right) grouped by topic ─────────────────────────────
    concepts_by_topic: dict[str, list[dict]] = _dd(list)
    for c in concept_nodes:
        concepts_by_topic[c["topic_id"]].append(c)

    for topic_id, cons in concepts_by_topic.items():
        cy_base = topic_y[topic_id]
        n = len(cons)
        offsets = [(j - (n - 1) / 2) * CON_STEP for j in range(n)]
        for c, off in zip(cons, offsets):
            c["x"] = 200
            c["y"] = cy_base + off

    # ── Terms (x=-200, left) — connected only ─────────────────────────────────
    # Accumulate per-term, per-topic edge weight
    term_topic_weight: dict[str, dict[str, float]] = _dd(lambda: _dd(float))
    for e in edges:
        src, tgt = e["from"], e["to"]
        if src.startswith("topic:") and tgt.startswith("term:"):
            term_topic_weight[tgt][src] += e["weight"]

    connected_term_ids = set(term_topic_weight.keys())
    isolated_term_ids  = {n["id"] for n in term_nodes} - connected_term_ids

    def primary_topic_index(term_id: str) -> tuple[int, str]:
        weights = term_topic_weight[term_id]
        best    = max(weights, key=weights.__getitem__)
        idx     = next((i for i, t in enumerate(topic_nodes) if t["id"] == best), 999)
        return (idx, term_id)

    connected_terms = sorted(
        [n for n in term_nodes if n["id"] in connected_term_ids],
        key=lambda n: primary_topic_index(n["id"]),
    )

    # Place connected terms: stack within each topic's y-band
    TERM_STEP = 12
    band_cursor: dict[int, float] = {}

    for term in connected_terms:
        idx, _ = primary_topic_index(term["id"])
        if idx not in band_cursor:
            band_cursor[idx] = idx * TOPIC_STEP - (TOPIC_STEP / 2 - TERM_STEP)
        term["x"] = -200
        term["y"] = band_cursor[idx]
        band_cursor[idx] += TERM_STEP

    return isolated_term_ids


# ─── 5. Write outputs ─────────────────────────────────────────────────────────

def write_csv(nodes: list[dict], edges: list[dict]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    node_keys = ["id", "label", "side", "type", "description", "x", "y"]
    with OUT_NODES.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=node_keys, extrasaction="ignore")
        w.writeheader()
        for n in nodes:
            w.writerow({k: n.get(k, "") for k in node_keys})

    edge_keys = ["source", "target", "type", "weight"]
    with OUT_EDGES.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=edge_keys)
        w.writeheader()
        for e in edges:
            w.writerow({
                "source": e["from"],
                "target": e["to"],
                "type":   e["type"],
                "weight": e["weight"],
            })


def write_kumu(nodes: list[dict], edges: list[dict]) -> None:
    elements = []
    for n in nodes:
        el = {"id": n["id"], "label": n["label"], "type": n["type"]}
        if n.get("description"):
            el["description"] = n["description"]
        if n.get("side"):
            el["side"] = n["side"]
        elements.append(el)

    connections = []
    for e in edges:
        connections.append({
            "from":   e["from"],
            "to":     e["to"],
            "type":   e["type"],
            "weight": e["weight"],
        })

    with OUT_KUMU.open("w", encoding="utf-8") as f:
        json.dump({"elements": elements, "connections": connections},
                  f, ensure_ascii=False, indent=2)


# ─── 5. Main ──────────────────────────────────────────────────────────────────

def main() -> None:
    print("Parsing GLOSSARY.md …")
    term_nodes, _term_bodies = parse_glossary(GLOSSARY)
    print(f"  {len(term_nodes)} term nodes  (right side)")

    print("Parsing topic files …")
    topic_nodes    = []
    concept_nodes  = []
    concept_bodies = {}

    for tf in sorted(TOPICS_DIR.glob("topic_*.md")):
        tnode, cnodes, cbodies = parse_topic_file(tf)
        if tnode:
            topic_nodes.append(tnode)
            concept_nodes.extend(cnodes)
            concept_bodies.update(cbodies)
            print(f"  {tf.name}: 1 topic, {len(cnodes)} concepts")

    print(f"  {len(topic_nodes)} topic nodes  (left side)")
    print(f"  {len(concept_nodes)} concept nodes  (right side)")

    print("Building bipartite edges …")
    edges = build_bipartite_edges(
        topic_nodes    = topic_nodes,
        concept_nodes  = concept_nodes,
        term_nodes     = term_nodes,
        concept_bodies = concept_bodies,
    )

    # Stats
    type_counts = Counter(e["type"] for e in edges)
    for etype, count in type_counts.most_common():
        print(f"  {etype}: {count}")
    print(f"  TOTAL: {len(edges)} edges")

    # All nodes = left (topics) + right (terms + concepts)
    # Strip internal 'full_text' key before writing
    clean_topics = [{k: v for k, v in n.items() if k != "full_text"}
                    for n in topic_nodes]

    print("Assigning layout coordinates …")
    isolated_term_ids = assign_coordinates(
        topic_nodes   = clean_topics,
        concept_nodes = concept_nodes,
        term_nodes    = term_nodes,
        edges         = edges,
    )
    print(f"  Dropping {len(isolated_term_ids)} isolated terms (not referenced by any topic)")

    # Filter out isolated terms from nodes and edges
    all_nodes = (
        clean_topics
        + [n for n in term_nodes    if n["id"] not in isolated_term_ids]
        + concept_nodes
    )
    edges = [e for e in edges
             if e["from"] not in isolated_term_ids
             and e["to"]   not in isolated_term_ids]

    print("\nWriting outputs …")
    write_csv(all_nodes, edges)
    print(f"  {OUT_NODES}  ({len(all_nodes)} rows)")
    print(f"  {OUT_EDGES}  ({len(edges)} rows)")

    write_kumu(all_nodes, edges)
    print(f"  {OUT_KUMU}")

    print("\n── Summary ──────────────────────────────────────────────────────────")
    left   = [n for n in all_nodes if n.get("x", 0) == -200]
    centre = [n for n in all_nodes if n.get("x", 0) ==    0]
    right  = [n for n in all_nodes if n.get("x", 0) ==  200]
    print(f"  Left   (terms, connected):  {len(left)}")
    print(f"  Centre (topics):            {len(centre)}")
    print(f"  Right  (concepts):          {len(right)}")
    print(f"  Edges:                      {len(edges)}")


if __name__ == "__main__":
    main()
