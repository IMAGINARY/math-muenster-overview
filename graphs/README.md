# Knowledge Graphs — Mathematics Münster

Knowledge graphs extracted from the Mathematics Münster research overview.
Two graph types are available, each with its own export folder.

## Folder structure

```
graphs/
├── scripts/
│   ├── build_graph.py       — builds the full knowledge graph
│   └── build_bipartite.py   — builds the bipartite topic ↔ term/concept graph
└── exports/
    ├── full-graph/          — output of build_graph.py
    └── bipartite/           — output of build_bipartite.py
```

Source files read by both scripts (from the repo root):

- `GLOSSARY.md` — 115 mathematical terms with definitions
- `EXPLORATION.md` — 8 MM research objectives (O1–O8)
- `topics/topic_01_*.md` … `topic_10_*.md` — 10 research topics, 5 core concepts each

## Running the scripts

```bash
python3 graphs/scripts/build_graph.py
python3 graphs/scripts/build_bipartite.py
```

No dependencies beyond the Python standard library.

---

## Graph 1 — Full knowledge graph (`exports/full-graph/`)

A general-purpose knowledge graph covering all node and edge types.

### Nodes (183 total)

| Type | Count | Source |
|------|-------|--------|
| `term` | 115 | GLOSSARY.md entries |
| `concept` | 50 | Core concepts within topic files |
| `topic` | 10 | Topic files |
| `objective` | 8 | EXPLORATION.md objectives O1–O8 |

### Edges (199 total)

| Type | Count | Meaning |
|------|-------|---------|
| `related-to` | 106 | Term mentioned by name in another term's definition |
| `requires` | 60 | Concept links to a glossary term |
| `uses` | 23 | Topic intro links to a glossary term |
| `belongs-to` | 10 | Topic belongs to an MM objective |

### Output files

| File | Format | Use |
|------|--------|-----|
| `graph.json` | Kumu.io JSON | Import directly into [Kumu.io](https://kumu.io) |
| `cosmograph_nodes.csv` | CSV | Metadata file for Cosmograph |
| `cosmograph_edges.csv` | CSV | Edge list for Cosmograph |
| `nodes_with_text.json` | JSON | Full node body text for LLM post-processing |

### Loading in Cosmograph

1. Go to [run.cosmograph.app](https://run.cosmograph.app) → **Graph** mode
2. Upload `cosmograph_edges.csv` as the graph data file
3. Upload `cosmograph_nodes.csv` as the metadata file
4. Set **Node Color** → `type` to distinguish objectives / topics / concepts / terms
5. Set **Link Color** → `type` to distinguish edge types

---

## Graph 2 — Bipartite graph (`exports/bipartite/`)

A cleaner, focused graph that shows only the relationships between the 10
research topics and the mathematical terms and concepts they reference.
No term–term or concept–concept edges; no isolated terms.

### Nodes (115 total)

| Column | Description |
|--------|-------------|
| `side` | `left` = terms, `centre` = topics, `right` = concepts |
| `type` | `term`, `topic`, or `concept` |
| `x`, `y` | Pre-computed layout coordinates (see below) |

60 glossary terms that are never referenced by any topic file are excluded.

### Edges (127 total)

| Type | Count | Meaning |
|------|-------|---------|
| `uses` | 59 | Topic explicitly links to a glossary term (markdown hyperlink) |
| `contains` | 50 | Topic contains a core concept |
| `mentions` | 18 | Topic mentions a term by name (no hyperlink) |

Edge `weight` = raw mention/link count within that topic's full text.

### Layout coordinates

Nodes carry `x`/`y` coordinates that seed the Cosmograph force simulation
into a readable three-column layout:

```
x = -200   connected terms   (left)
x =    0   topics            (centre)
x = +200   concepts          (right)
```

Concepts are fanned vertically around their parent topic's y-position.
Terms are grouped by the topic that references them most.

### Output files

| File | Format | Use |
|------|--------|-----|
| `bipartite_graph.json` | Kumu.io JSON | Import into [Kumu.io](https://kumu.io) |
| `bipartite_nodes.csv` | CSV | Metadata file for Cosmograph |
| `bipartite_edges.csv` | CSV | Edge list for Cosmograph |

### Loading in Cosmograph

1. Go to [run.cosmograph.app](https://run.cosmograph.app) → **Graph** mode
2. Upload `bipartite_edges.csv` as the graph data file
3. Upload `bipartite_nodes.csv` as the metadata file
4. Set **Node Color** → `type` (term / topic / concept)
5. Set **Link Width** → `weight` (thicker = more mentions)
6. Reduce **Repulsion** and increase **Bond strength** so the sim respects the seeded column layout
