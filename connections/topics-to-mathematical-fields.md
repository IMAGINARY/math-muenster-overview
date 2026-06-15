# Topics to Mathematical Fields

Relation of excellence cluster topics to mathematical fields.
Source: [Mathematics Münster Research Programme](https://www.uni-muenster.de/MathematicsMuenster/research/programme/index.shtml)

| Mathematical Field | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Arithmetic geometry and representation theory | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | | | |
| Model theory and set theory | | | | ✓ | | | | ✓ | | |
| Topology | ✓ | ✓ | | ✓ | ✓ | | | | | |
| Operator algebras and mathematical physics | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ | | |
| Differential geometry | | ✓ | | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| Analysis of partial differential equations | | | | | ✓ | ✓ | ✓ | ✓ | ✓ | |
| Stochastic analysis | | | | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Theory of stochastic processes | | | | | | | ✓ | ✓ | | ✓ |
| Optimisation and calculus of variations | | | | | ✓ | ✓ | | | ✓ | ✓ |
| Numerical analysis, machine learning and scientific computing | | | | | ✓ | | ✓ | | ✓ | ✓ |

**Topics:**
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

  AG["Arithmetic geometry and representation theory"]
  MS["Model theory and set theory"]
  TO["Topology"]
  OA["Operator algebras and mathematical physics"]
  DG["Differential geometry"]
  AP["Analysis of partial differential equations"]
  SA["Stochastic analysis"]
  SP["Theory of stochastic processes"]
  OC["Optimisation and calculus of variations"]
  NA["Numerical analysis, machine learning and scientific computing"]

  T1 --- AG
  T1 --- TO
  T1 --- OA

  T2 --- AG
  T2 --- TO
  T2 --- OA
  T2 --- DG

  T3 --- AG
  T3 --- OA

  T4 --- MS
  T4 --- AG
  T4 --- TO
  T4 --- OA
  T4 --- DG
  T4 --- SA

  T5 --- AG
  T5 --- TO
  T5 --- DG
  T5 --- AP
  T5 --- SA
  T5 --- OC
  T5 --- NA

  T6 --- DG
  T6 --- AP
  T6 --- SA
  T6 --- OC

  T7 --- AG
  T7 --- OA
  T7 --- DG
  T7 --- AP
  T7 --- SA
  T7 --- SP
  T7 --- NA

  T8 --- MS
  T8 --- OA
  T8 --- AP
  T8 --- SA
  T8 --- SP

  T9 --- AP
  T9 --- SA
  T9 --- OC
  T9 --- NA

  T10 --- DG
  T10 --- SA
  T10 --- SP
  T10 --- OC
  T10 --- NA
```
