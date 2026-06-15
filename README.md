# Mathematics Münster — Research Overview

## About Mathematics Münster

[Mathematics Münster: Dynamics – Geometry – Structure](https://www.uni-muenster.de/MathematicsMuenster/aboutus/index.shtml) is a Cluster of Excellence at the University of Münster, funded since 2019 through Germany's Excellence Strategy. Around 200 mathematicians from diverse fields conduct research together, treating mathematics as an integrated whole and explicitly promoting cross-disciplinary method transfer.

Research is organized around eight research objectives (O1–O8) and two structural objectives (O9–O10, governing cross-disciplinary integration, international visibility, and early-career researcher support).

---

## This Repository

This repository contains research materials produced for an IMAGINARY exhibition about Mathematics Münster. It maps the cluster's research landscape — objectives, topics, terms, and concepts — and makes the relationships between them explorable.

### Contents

- **[EXPLORATION.md](EXPLORATION.md)** — Human-readable overview of all 8 research objectives and 10 topic groups, with inline concept definitions and cross-links into the glossary.

- **[GLOSSARY.md](GLOSSARY.md)** — Reference glossary covering the mathematical terms and concepts appearing across the research programme. Entries include KaTeX-rendered definitions and links to Wikipedia, nLab, and Encyclopedia of Mathematics.

- **[graphs/](graphs/README.md)** — Knowledge graphs encoding the relationships between objectives, topics, concepts, and terms. Includes a full graph and a bipartite graph, with exports for [Kumu.io](https://kumu.io) and [Cosmograph](https://cosmograph.app), plus Python build scripts.

- **[connections/](connections/)** — Relation tables extracted from the cluster's research programme subpages.
  - [topics-to-mathematical-fields.md](connections/topics-to-mathematical-fields.md) — Which mathematical fields each topic spans.
  - [topics-to-topics.md](connections/topics-to-topics.md) — Collaboration links between topic groups.

- **topics/** — Detailed companion files to EXPLORATION.md. Each file covers one topic group, explaining its core concepts at three levels: Level 0 (high school), Level 1 (undergraduate), Level 2 (master's).

  | # | Topic group | Objective | File |
  |---|-------------|-----------|------|
  | 1 | K-groups and cohomology | O1 — K-theory, cohomology, Farrell–Jones and Borel conjectures, C\*-algebra classification | [topic_01_kgroups-cohomology.md](topics/topic_01_kgroups-cohomology.md) |
  | 2 | Moduli spaces in arithmetic and geometry | O2 — Moduli spaces, Langlands programme, diffeomorphism groups, curvature metrics | [topic_02_moduli-spaces.md](topics/topic_02_moduli-spaces.md) |
  | 3 | Models and universes | O3 — C\*-algebras, group actions, set-theoretic models, large cardinals | [topic_03_models-universes.md](topics/topic_03_models-universes.md) |
  | 4 | Groups and actions | O3 — C\*-algebras, group actions, set-theoretic models, large cardinals | [topic_04_groups-actions.md](topics/topic_04_groups-actions.md) |
  | 5 | Curvature, shape and global analysis | O4 — PDEs, Riemannian/Lorentzian geometry, black hole stability (Kerr conjecture) | [topic_05_curvature-shape-analysis.md](topics/topic_05_curvature-shape-analysis.md) |
  | 6 | Singularities and PDEs | O4 — PDEs, Riemannian/Lorentzian geometry, black hole stability (Kerr conjecture) | [topic_06_singularities-pdes.md](topics/topic_06_singularities-pdes.md) |
  | 7 | Field theory and randomness | O5 — Non-commutative field theory, stochastic quantisation, free probability | [topic_07_field-theory-randomness.md](topics/topic_07_field-theory-randomness.md) |
  | 8 | Random discrete structures and their limits | O6 — Random discrete structures, random graphs, percolation, scaling limits | [topic_08_random-discrete-structures.md](topics/topic_08_random-discrete-structures.md) |
  | 9 | Multiscale processes and effective behaviour | O7 — Multiscale processes, homogenisation, fluid dynamics, kinetic equations | [topic_09_multiscale-processes.md](topics/topic_09_multiscale-processes.md) |
  | 10 | Deep learning and surrogate methods | O8 — Deep learning, surrogate methods, neural networks, parameterised PDEs | [topic_10_deepl-surrogate-methods.md](topics/topic_10_deepl-surrogate-methods.md) |

### Formatting notes

- Math is written in GitHub/LaTeX style (`$...$` inline, `$$...$$` display). GitHub renders this natively; other viewers need a KaTeX/MathJax previewer.
- Images are hot-linked from the Mathematics Münster website (© MM/vl) and require an internet connection to display.
- Web links point to original publications (DOI/arXiv) and encyclopaedic references for each concept.
