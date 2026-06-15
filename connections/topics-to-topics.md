# Topics to Topics (Collaborations)

Relation of excellence cluster topics to each other via stated collaborations.
Source: [Mathematics Münster Research Programme](https://www.uni-muenster.de/MathematicsMuenster/research/programme/index.shtml)

| | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **T1** K-groups and cohomology | — | ✓ | ✓ | ✓ | ✓ | | | | | |
| **T2** Moduli spaces in arithmetic and geometry | ✓ | — | | ✓ | ✓ | ✓ | ✓ | | | |
| **T3** Models and universes | ✓ | | — | ✓ | | | | ✓ | | |
| **T4** Groups and actions | ✓ | ✓ | ✓ | — | ✓ | | | ✓ | | |
| **T5** Curvature, shape and global analysis | ✓ | ✓ | | ✓ | — | ✓ | | | ✓ | ✓ |
| **T6** Singularities and partial differential equations | | ✓ | | | ✓ | — | ✓ | | ✓ | |
| **T7** Field theory and randomness | | ✓ | | | | ✓ | — | ✓ | | ✓ |
| **T8** Random discrete structures and their limits | | | ✓ | ✓ | | | ✓ | — | ✓ | ✓ |
| **T9** Multiscale processes and effective behaviour | | | | | ✓ | ✓ | | ✓ | — | ✓ |
| **T10** Deep learning and surrogate methods | | | | | ✓ | | ✓ | ✓ | ✓ | — |

Each ✓ indicates that at least one of the two topics lists the other as a collaboration partner on its subpage.

## Graph

```mermaid
graph LR
  subgraph IF["Invariants &amp; Foundations"]
    T1["T1: K-groups and cohomology"]
    T2["T2: Moduli spaces in arithmetic and geometry"]
    T3["T3: Models and universes"]
  end
  subgraph NL["Non-linear Spaces &amp; Operators"]
    T4["T4: Groups and actions"]
    T5["T5: Curvature, shape and global analysis"]
    T6["T6: Singularities and PDEs"]
    T7["T7: Field theory and randomness"]
  end
  subgraph MA["Models, Approximations &amp; Data"]
    T8["T8: Random discrete structures and their limits"]
    T9["T9: Multiscale processes and effective behaviour"]
    T10["T10: Deep learning and surrogate methods"]
  end

  T1 --- T2
  T1 --- T3
  T1 --- T4
  T1 --- T5
  T2 --- T4
  T2 --- T5
  T2 --- T6
  T2 --- T7
  T3 --- T4
  T3 --- T8
  T4 --- T5
  T4 --- T8
  T5 --- T6
  T5 --- T9
  T5 --- T10
  T6 --- T7
  T6 --- T9
  T7 --- T8
  T7 --- T10
  T8 --- T9
  T8 --- T10
  T9 --- T10
```
