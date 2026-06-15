#!/usr/bin/env python3
"""
build_graph.py
==============
Build a knowledge graph from the Mathematics Münster markdown repo.

Outputs:
  graph.json            — Kumu.io-compatible JSON (elements + connections)
  nodes_with_text.json  — per-node JSON with full body text (for LLM inference step)

Node types:
  objective   — MM research objectives O1–O8 (from EXPLORATION.md)
  topic       — 10 research topic groups (from topic_XX_*.md files)
  concept     — "Core concept N: ..." sections within topic files
  term        — glossary entries from GLOSSARY.md (<a id="..."> anchors)

Edge types:
  belongs-to  — topic → objective  (extracted from the MM "Ox" code in topic files)
  uses        — topic/concept → term  (explicit markdown links to GLOSSARY.md#slug)
  related-to  — term → term  (explicit markdown links within GLOSSARY.md)
  requires    — concept → term  (explicit links inside Level 0/1/2 sections)

LLM-inference prep:
  nodes_with_text.json stores each node's full body text so a second-pass LLM
  can suggest additional semantic/prerequisite edges without re-parsing markdown.
"""

import csv
import json
import re
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────

REPO        = Path(__file__).parent.parent.parent
GLOSSARY    = REPO / "GLOSSARY.md"
EXPLORATION = REPO / "EXPLORATION.md"
TOPICS_DIR  = REPO / "topics"
OUT_DIR     = REPO / "graphs" / "exports" / "full-graph"
OUT_GRAPH       = OUT_DIR / "graph.json"
OUT_NODES       = OUT_DIR / "nodes_with_text.json"
OUT_COSMO_EDGES = OUT_DIR / "cosmograph_edges.csv"
OUT_COSMO_NODES = OUT_DIR / "cosmograph_nodes.csv"

# ─── Helpers ──────────────────────────────────────────────────────────────────

def slug_to_id(slug: str, node_type: str) -> str:
    """Build a stable node id from type + slug."""
    return f"{node_type}:{slug}"


def md_links_to_glossary(text: str) -> list[str]:
    """
    Return list of glossary slugs referenced by explicit markdown links of the form
    [label](../GLOSSARY.md#slug) or [label](GLOSSARY.md#slug) or just #slug anchors.
    """
    pattern = r'\[([^\]]*)\]\([^)]*GLOSSARY\.md#([\w\-]+)\)'
    return [m.group(2) for m in re.finditer(pattern, text)]


def md_links_to_glossary_within(text: str) -> list[str]:
    """
    Inside GLOSSARY.md itself, cross-links look like [label](#slug) or
    [label](GLOSSARY.md#slug). Return target slugs.
    """
    # links to other glossary entries within the same file: (#slug)
    pattern_local = r'\[([^\]]*)\]\(#([\w\-]+)\)'
    # links that explicitly name GLOSSARY.md
    pattern_full  = r'\[([^\]]*)\]\([^)]*GLOSSARY\.md#([\w\-]+)\)'
    slugs = [m.group(2) for m in re.finditer(pattern_local, text)]
    slugs += [m.group(2) for m in re.finditer(pattern_full, text)]
    return slugs


# ─── 1. Parse GLOSSARY.md — produce term nodes ────────────────────────────────

def parse_glossary(path: Path) -> tuple[list[dict], dict[str, str]]:
    """
    Returns:
      nodes   — list of node dicts (type=term)
      bodies  — dict slug → full body text (for nodes_with_text.json)
    """
    text = path.read_text(encoding="utf-8")

    # Split on anchor tags: each entry starts with <a id="..."></a>
    # Pattern captures: slug, bold label (first **...** after anchor), rest of block
    entry_pattern = re.compile(
        r'<a id="([\w\-]+)"></a>\s*\n\*\*([^*]+)\*\*\s*\n(.*?)(?=\n<a id=|\n---\n|\Z)',
        re.DOTALL
    )

    nodes = []
    bodies = {}

    for m in entry_pattern.finditer(text):
        slug  = m.group(1)
        label = m.group(2).strip()
        body  = m.group(3).strip()

        # Strip trailing external link lines for the description
        # (lines that are pure link lists like "[Wikipedia](...) · [nLab](...)")
        desc_lines = []
        for line in body.splitlines():
            stripped = line.strip()
            # skip lines that are only markdown links / separators
            if re.match(r'^\[.*\]\(.*\)', stripped) and '·' in stripped or stripped == '---':
                continue
            desc_lines.append(line)
        description = ' '.join(l.strip() for l in desc_lines if l.strip())
        # Truncate for Kumu display (keep full in bodies)
        description_short = description[:300] + '…' if len(description) > 300 else description

        node_id = slug_to_id(slug, "term")
        nodes.append({
            "id":          node_id,
            "label":       label,
            "type":        "term",
            "slug":        slug,
            "description": description_short,
        })
        bodies[node_id] = body

    return nodes, bodies


# ─── 2. Parse EXPLORATION.md — produce objective nodes ────────────────────────

def parse_exploration(path: Path) -> tuple[list[dict], dict[str, str]]:
    """
    Returns objective nodes and their body texts.
    Objectives are lines like '## O1 — Push frontiers ...'
    """
    text = path.read_text(encoding="utf-8")

    # Match '## O1 — Title' headings; capture body until next '## O' or end
    obj_pattern = re.compile(
        r'^## (O\d+) — (.+?)\n(.*?)(?=^## O|\Z)',
        re.MULTILINE | re.DOTALL
    )

    nodes = []
    bodies = {}

    for m in obj_pattern.finditer(text):
        code  = m.group(1)          # e.g. 'O1'
        title = m.group(2).strip()  # e.g. 'Push frontiers in K-theory...'
        body  = m.group(3).strip()

        slug    = code.lower()      # 'o1'
        node_id = slug_to_id(slug, "objective")
        label   = f"{code} — {title}"

        # Short description: look for "Plain explanation" paragraph; fall back to
        # first paragraph that doesn't start with '#' or '-' or '**Key'
        plain_m = re.search(r'\*\*Plain explanation\.\*\*\s*(.*?)(?:\n\n|\Z)', body, re.DOTALL)
        if plain_m:
            description = plain_m.group(1).strip()
            # strip markdown links
            description = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', description)
            description = description[:300]
        else:
            paras = [p.strip() for p in body.split('\n\n') if p.strip()
                     and not p.strip().startswith('#')
                     and not p.strip().startswith('-')
                     and not p.strip().startswith('**Key')]
            description = paras[0][:300] if paras else title
        description = re.sub(r'\s+', ' ', description).strip()

        nodes.append({
            "id":          node_id,
            "label":       label,
            "type":        "objective",
            "code":        code,
            "description": description,
        })
        bodies[node_id] = body

    return nodes, bodies


# ─── 3. Parse topic files — produce topic + concept nodes ─────────────────────

def parse_topic_file(path: Path) -> tuple[list[dict], list[dict], dict[str, str]]:
    """
    Returns:
      topic_nodes   — 1-element list (the topic node)
      concept_nodes — list of concept nodes within this topic
      bodies        — node_id → full text
    """
    text = path.read_text(encoding="utf-8")

    # ── Topic node ────────────────────────────────────────────────────────────
    # Title line: '# Topic N — Name'
    title_m = re.match(r'^# Topic (\d+) — (.+)', text, re.MULTILINE)
    if not title_m:
        return [], [], {}
    topic_num   = title_m.group(1)          # '1'
    topic_title = title_m.group(2).strip()  # 'K-groups and Cohomology'

    topic_slug  = f"topic-{int(topic_num):02d}"
    topic_id    = slug_to_id(topic_slug, "topic")
    topic_label = f"Topic {topic_num}: {topic_title}"

    # Objective code: look for 'MM "Ox"' or '(MM "Ox")' in the blockquote
    obj_m = re.search(r'MM\s+"(O\d+)"', text)
    objective_code = obj_m.group(1) if obj_m else None

    # Body: everything up to first '## Core concept'
    body_end = text.find('\n## Core concept')
    topic_body = text[:body_end].strip() if body_end > 0 else text[:500]

    # Short description from the blockquote
    quote_m = re.search(r'>\s+\*\*(Objective[^)]*)\*\*[:\s]*(.*?)(?:\n)', text, re.DOTALL)
    if quote_m:
        desc = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', quote_m.group(0))  # strip links
        desc = re.sub(r'[>*]', '', desc).strip()[:300]
    else:
        desc = topic_title

    topic_node = {
        "id":             topic_id,
        "label":          topic_label,
        "type":           "topic",
        "topic_number":   int(topic_num),
        "objective_code": objective_code,
        "description":    desc,
    }

    bodies = {topic_id: topic_body}
    topic_nodes = [topic_node]

    # ── Concept nodes ─────────────────────────────────────────────────────────
    # '## Core concept N: Name'
    concept_pattern = re.compile(
        r'^## Core concept (\d+): (.+?)\n(.*?)(?=^## Core concept|\Z)',
        re.MULTILINE | re.DOTALL
    )
    concept_nodes = []

    for cm in concept_pattern.finditer(text):
        con_num   = cm.group(1)
        con_title = cm.group(2).strip()
        con_body  = cm.group(3).strip()

        con_slug  = f"{topic_slug}-concept-{con_num}"
        con_id    = slug_to_id(con_slug, "concept")
        con_label = con_title

        # Short description: first Level 0 paragraph (most accessible)
        level0_m = re.search(r'### Level 0[^\n]*\n(.*?)(?=###|\Z)', con_body, re.DOTALL)
        if level0_m:
            l0 = level0_m.group(1).strip()
            desc_short = l0[:300] + '…' if len(l0) > 300 else l0
        else:
            desc_short = con_title

        concept_nodes.append({
            "id":           con_id,
            "label":        con_label,
            "type":         "concept",
            "topic_id":     topic_id,
            "concept_num":  int(con_num),
            "description":  desc_short,
        })
        bodies[con_id] = con_body

    return topic_nodes, concept_nodes, bodies


# ─── 4. Build edges ───────────────────────────────────────────────────────────

def build_edges(
    term_nodes:    list[dict],
    obj_nodes:     list[dict],
    topic_nodes:   list[dict],
    concept_nodes: list[dict],
    bodies:        dict[str, str],
    glossary_text: str,
) -> list[dict]:
    """
    Four edge types:
      belongs-to   topic → objective
      uses         topic/concept → term  (explicit GLOSSARY links)
      related-to   term → term           (cross-links within GLOSSARY)
      requires     concept → term        (links inside Level sections)
    """
    edges = []
    edge_set = set()  # deduplicate

    def add_edge(from_id, to_id, edge_type, label=None):
        key = (from_id, to_id, edge_type)
        if key not in edge_set and from_id != to_id:
            edge_set.add(key)
            e = {"from": from_id, "to": to_id, "type": edge_type}
            if label:
                e["label"] = label
            edges.append(e)

    # Index: slug → node_id  (for term lookups)
    slug_to_node = {n["slug"]: n["id"] for n in term_nodes}

    # Index: objective code → node_id
    obj_code_to_id = {n["code"]: n["id"] for n in obj_nodes}

    # ── belongs-to: topic → objective ─────────────────────────────────────────
    for t in topic_nodes:
        if t["objective_code"] and t["objective_code"] in obj_code_to_id:
            add_edge(t["id"], obj_code_to_id[t["objective_code"]], "belongs-to")

    # ── uses: topic nodes → terms (links in topic intro/body) ─────────────────
    for t in topic_nodes:
        body = bodies.get(t["id"], "")
        for slug in md_links_to_glossary(body):
            if slug in slug_to_node:
                add_edge(t["id"], slug_to_node[slug], "uses")

    # ── requires + uses: concept nodes → terms ────────────────────────────────
    # For concept nodes we use ALL links found (across all Level sections).
    # We label them "requires" because they appear in pedagogical level text.
    for c in concept_nodes:
        body = bodies.get(c["id"], "")
        for slug in md_links_to_glossary(body):
            if slug in slug_to_node:
                add_edge(c["id"], slug_to_node[slug], "requires")

    # ── related-to: term → term (name-matching within GLOSSARY body text) ───────
    # GLOSSARY definitions mention other terms by their bold label in prose
    # (no markdown links between entries). We match term labels case-insensitively
    # as whole words / phrases in each entry's body text.
    #
    # Build a sorted label list (longest first to avoid partial matches).
    term_label_map: list[tuple[str, str]] = []  # (label_lower, node_id)
    for n in term_nodes:
        # Use the main label; also strip trailing parenthetical variants
        label = n["label"]
        # Normalise: strip trailing "(Bounded Mean Oscillation)" style suffixes
        base = re.sub(r'\s*\([^)]+\)$', '', label).strip()
        term_label_map.append((base.lower(), n["id"]))
    # Sort longest first to match "algebraic K-theory" before "K-theory"
    term_label_map.sort(key=lambda x: -len(x[0]))

    entry_pattern = re.compile(
        r'<a id="([\w\-]+)"></a>\s*\n\*\*([^*]+)\*\*\s*\n(.*?)(?=\n<a id=|\n---\n|\Z)',
        re.DOTALL
    )
    for m in entry_pattern.finditer(glossary_text):
        from_slug  = m.group(1)
        from_label = m.group(2).strip().lower()
        entry_body = m.group(3)
        if from_slug not in slug_to_node:
            continue
        from_id = slug_to_node[from_slug]

        # Also catch any explicit markdown cross-links (future-proof)
        for to_slug in md_links_to_glossary_within(entry_body):
            if to_slug in slug_to_node:
                add_edge(from_id, slug_to_node[to_slug], "related-to")
        for to_slug in md_links_to_glossary(entry_body):
            if to_slug in slug_to_node:
                add_edge(from_id, slug_to_node[to_slug], "related-to")

        # Name-matching: look for other term labels in this entry's body
        body_lower = entry_body.lower()
        for label_lower, to_id in term_label_map:
            if to_id == from_id:
                continue
            if from_label == label_lower:
                continue  # don't self-link by name
            # Require whole-word match (word boundary on both sides)
            # Escape special regex chars in label
            escaped = re.escape(label_lower)
            if re.search(r'\b' + escaped + r'\b', body_lower):
                add_edge(from_id, to_id, "related-to")

    return edges


# ─── 5. Assemble and write outputs ────────────────────────────────────────────

def kumu_element(node: dict) -> dict:
    """Convert internal node dict to Kumu element format."""
    el = {
        "id":    node["id"],
        "label": node["label"],
        "type":  node["type"],
    }
    if node.get("description"):
        el["description"] = node["description"]
    # Kumu supports arbitrary extra attributes
    for extra_key in ("code", "topic_number", "concept_num", "objective_code"):
        if extra_key in node:
            el[extra_key] = node[extra_key]
    return el


def kumu_connection(edge: dict) -> dict:
    """Convert internal edge dict to Kumu connection format."""
    conn = {
        "from":  edge["from"],
        "to":    edge["to"],
        "type":  edge["type"],
    }
    if edge.get("label"):
        conn["label"] = edge["label"]
    return conn


def write_cosmograph_csv(
    all_nodes: list[dict],
    edges:     list[dict],
    nodes_path: Path,
    edges_path: Path,
) -> None:
    """
    Write Cosmograph-compatible CSV files.

    cosmograph_nodes.csv  — one row per node
      columns: id, label, type, description, [code, topic_number, concept_num, objective_code]

    cosmograph_edges.csv  — one row per edge (the edge list Cosmograph requires)
      columns: source, target, type
      • 'source' and 'target' are node ids matching the nodes file

    Cosmograph auto-detects the 'source'/'target' columns and treats all other
    numeric columns as edge attributes; text columns become filterable categories.
    Node ids must be consistent between both files.
    """
    # ── Nodes CSV ─────────────────────────────────────────────────────────────
    # Determine all attribute columns present across nodes
    attr_keys = ["id", "label", "type", "description",
                 "code", "topic_number", "concept_num", "objective_code"]

    with nodes_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=attr_keys, extrasaction="ignore")
        writer.writeheader()
        for n in all_nodes:
            row = {k: n.get(k, "") for k in attr_keys}
            # Cosmograph displays node id as label by default; we put the human
            # label in the 'label' column so it can be selected in the UI.
            writer.writerow(row)

    # ── Edges CSV ─────────────────────────────────────────────────────────────
    with edges_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["source", "target", "type"])
        writer.writeheader()
        for e in edges:
            writer.writerow({
                "source": e["from"],
                "target": e["to"],
                "type":   e["type"],
            })


def main():
    print("Parsing GLOSSARY.md …")
    term_nodes, term_bodies = parse_glossary(GLOSSARY)
    print(f"  {len(term_nodes)} term nodes")

    print("Parsing EXPLORATION.md …")
    obj_nodes, obj_bodies = parse_exploration(EXPLORATION)
    print(f"  {len(obj_nodes)} objective nodes")

    print("Parsing topic files …")
    all_topic_nodes   = []
    all_concept_nodes = []
    topic_bodies      = {}

    topic_files = sorted(TOPICS_DIR.glob("topic_*.md"))
    for tf in topic_files:
        tnodes, cnodes, bodies = parse_topic_file(tf)
        all_topic_nodes.extend(tnodes)
        all_concept_nodes.extend(cnodes)
        topic_bodies.update(bodies)
        if tnodes:
            print(f"  {tf.name}: 1 topic, {len(cnodes)} concepts")

    print(f"  Total: {len(all_topic_nodes)} topic nodes, {len(all_concept_nodes)} concept nodes")

    # Combined bodies dict for edge building
    all_bodies = {**term_bodies, **obj_bodies, **topic_bodies}

    print("Building edges …")
    glossary_text = GLOSSARY.read_text(encoding="utf-8")
    edges = build_edges(
        term_nodes    = term_nodes,
        obj_nodes     = obj_nodes,
        topic_nodes   = all_topic_nodes,
        concept_nodes = all_concept_nodes,
        bodies        = all_bodies,
        glossary_text = glossary_text,
    )
    print(f"  {len(edges)} edges")

    # Edge type breakdown
    from collections import Counter
    for etype, count in Counter(e["type"] for e in edges).most_common():
        print(f"    {etype}: {count}")

    # ── Write graph.json (Kumu format) ────────────────────────────────────────
    all_nodes = term_nodes + obj_nodes + all_topic_nodes + all_concept_nodes

    kumu_graph = {
        "elements":    [kumu_element(n) for n in all_nodes],
        "connections": [kumu_connection(e) for e in edges],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_GRAPH.open("w", encoding="utf-8") as f:
        json.dump(kumu_graph, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {OUT_GRAPH}  ({len(all_nodes)} nodes, {len(edges)} edges)")

    # ── Write nodes_with_text.json (for LLM inference step) ───────────────────
    nodes_with_text = []
    for n in all_nodes:
        entry = {
            "id":    n["id"],
            "label": n["label"],
            "type":  n["type"],
            "body":  all_bodies.get(n["id"], ""),
        }
        nodes_with_text.append(entry)

    with OUT_NODES.open("w", encoding="utf-8") as f:
        json.dump(nodes_with_text, f, ensure_ascii=False, indent=2)
    print(f"Wrote {OUT_NODES}  ({len(nodes_with_text)} entries)")

    # ── Write Cosmograph CSV files ─────────────────────────────────────────────
    write_cosmograph_csv(
        all_nodes   = all_nodes,
        edges       = edges,
        nodes_path  = OUT_COSMO_NODES,
        edges_path  = OUT_COSMO_EDGES,
    )
    print(f"Wrote {OUT_COSMO_EDGES}  ({len(edges)} rows)")
    print(f"Wrote {OUT_COSMO_NODES}  ({len(all_nodes)} rows)")

    # ── Summary stats ─────────────────────────────────────────────────────────
    print("\n── Summary ──────────────────────────────────────────────────────────")
    type_counts = Counter(n["type"] for n in all_nodes)
    for ntype, count in type_counts.most_common():
        print(f"  {ntype:12s}: {count} nodes")
    print(f"  {'TOTAL':12s}: {len(all_nodes)} nodes, {len(edges)} edges")


if __name__ == "__main__":
    main()
