# Topic 5 — Curvature, Shape and Global Analysis

> **Objective (part of MM "O4"): approach fundamental open questions in differential geometry through method transfer.**
> We study the interplay between the (local) geometry of [Riemannian manifolds](../GLOSSARY.md#riemannian-geometry) (like
> [curvature](../GLOSSARY.md#curvature)) and (global) topological and analytic properties. A goal is to complete
> the **[Grove programme](../GLOSSARY.md#grove-programme)**, generalising structure results for positively curved and
> Einstein manifolds toward arbitrary symmetry, and ultimately none.

Source: [T5: Curvature, shape and global analysis](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_curvature-shape-analysis.shtml)

Central theme: **local geometry $`\leftrightarrow`$ global topology/analysis**. Three units:
1. **[Curvature](../GLOSSARY.md#curvature) and geometric flows** (positive curvature, Ricci flow, metric measure spaces).
2. **Geodesics** (existence/regularity in infinite-dimensional shape spaces).
3. **[Index theory](../GLOSSARY.md#index-theory)** ([scalar curvature](../GLOSSARY.md#scalar-curvature) bounds via Dirac operators).

---

## Core concept 1: Riemannian manifolds

![Curvature/flows](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_ea344f159ec8033ef547addc227721dd_topic5a-dsc_1993-neu.jpg)

### Level 0 — High school
The surface of the Earth is curved: triangles drawn on it have angles adding to
*more* than 180°. A **Riemannian manifold** is any smooth curved space — of any
dimension — where we can still measure lengths and angles, hence distances and
"straightest possible" paths.

### Level 1 — Bachelor
A **Riemannian manifold** $`(M,g)`$ is a smooth manifold with a smoothly varying
inner product $`g_p`$ on each tangent space $`T_pM`$. It gives lengths of curves
$`L(\gamma)=\int \sqrt{g(\dot\gamma,\dot\gamma)}\,dt`$ and a distance
$`d(p,q)=\inf_\gamma L(\gamma)`$. The **Levi-Civita connection** $`\nabla`$ is the
unique torsion-free metric connection, defining parallel transport and covariant
differentiation.

### Level 2 — Master
[Curvature](../GLOSSARY.md#curvature) is encoded in the **Riemann curvature tensor**
$`R(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z`$, with
contractions giving **Ricci** $`\mathrm{Ric}`$ and **[scalar](../GLOSSARY.md#scalar-curvature)** $`\mathrm{scal}`$
curvature. MM also studies **infinite-dimensional** Riemannian and geodesic metric
spaces, where the finite-dimensional ODE theory of geodesics is replaced by PDEs,
and the Lie group / Lie algebra correspondence breaks down. References:
[Riemannian manifold](https://en.wikipedia.org/wiki/Riemannian_manifold),
[Curvature tensor](https://en.wikipedia.org/wiki/Riemann_curvature_tensor).

---

## Core concept 2: Curvature and topological obstructions

### Level 0 — High school
The amount and sign of curvature limits what shapes are possible. You cannot comb a
hairy ball flat, and you cannot wrap a sphere onto a doughnut without distortion —
curvature "knows" the global shape.

### Level 1 — Bachelor
Curvature comes in flavours: **sectional** $`K(\sigma)`$ (of a 2-plane $`\sigma`$),
**Ricci**, **scalar**. Sign assumptions force global topology:
- **Gauss–Bonnet**: $`\int_M K\,dA = 2\pi\chi(M)`$ for a closed surface — total
  curvature is the topological Euler characteristic.
- **Bonnet–Myers**: $`\mathrm{Ric}\ge (n-1)k>0 \Rightarrow`$ $`M`$ compact with finite
  $`\pi_1`$ and diameter $`\le \pi/\sqrt{k}`$.
- **Cartan–Hadamard**: $`K\le 0`$, complete, simply connected $`\Rightarrow`$
  diffeomorphic to $`\mathbb{R}^n`$.

### Level 2 — Master
Positive **sectional** curvature is rare and rigid; known examples are scarce, and
classification is open. The **[Grove programme](../GLOSSARY.md#grove-programme)** studies positively curved manifolds
*with symmetry* (isometric torus actions), proving structure/classification under a
symmetry assumption and then trying to lower it. MM (Wilking, Wiemeler, Kennard)
proves results linking positive curvature, torus symmetry and matroids, e.g.
classifying positively curved $`10`$-manifolds with $`T^3`$-symmetry. Reference:
[Positive curvature, torus symmetry, matroids — arXiv:2212.08152](https://arxiv.org/abs/2212.08152).

---

## Core concept 3: Ricci flow and geometric flows

### Level 0 — High school
Imagine a lumpy ball of dough that automatically smooths itself out, the bumps
flowing away until it becomes a perfect sphere. **Ricci flow** is an equation that
makes a curved space evolve and smooth its curvature over time — the tool Perelman
used to prove the Poincaré conjecture.

### Level 1 — Bachelor
**Ricci flow** evolves a metric by
$$
\frac{\partial}{\partial t} g(t) = -2\,\mathrm{Ric}\big(g(t)\big),
$$
a (weakly parabolic) heat-type equation that tends to homogenise curvature. On the
round sphere it shrinks self-similarly; in general singularities can form and must
be analysed (neck-pinches, surgery).

### Level 2 — Master
Hamilton–Perelman theory uses monotonicity ($`\mathcal{F}`$- and
$`\mathcal{W}`$-entropy), $`\kappa`$-noncollapsing, and surgery to classify
singularities, proving the **Poincaré** and **geometrisation** conjectures. MM
(Wilking, Böhm) studies preserved curvature conditions (cone constructions in the
space of curvature operators), Ricci flow under *almost* non-negative curvature,
and **Ebin geodesics** / scalar curvature in the space of metrics. References:
[Ricci flow](https://en.wikipedia.org/wiki/Ricci_flow),
[Ricci flow under almost non-negative curvature, Invent. Math. 2019](https://doi.org/10.1007/s00222-019-00864-7).

---

## Core concept 4: Geodesics and infinite-dimensional shape spaces

![Geodesics](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_3b01d4a7dd7290079f9f6e1b559a00a9_topic5b-dsc_2001-neu.jpg)

### Level 0 — High school
The shortest flight path between two cities curves across the globe — that is a
geodesic. Now imagine a "space" whose points are entire *shapes* (say, all possible
outlines of a hand). A geodesic there is the most efficient way to morph one shape
into another — useful in computer graphics and medical imaging.

### Level 1 — Bachelor
A **geodesic** is a locally length-minimising curve; it satisfies the geodesic
equation $`\nabla_{\dot\gamma}\dot\gamma = 0`$, an ODE in finite dimensions
guaranteeing local existence/uniqueness. The Riemannian distance is realised by
shortest geodesics (Hopf–Rinow, when complete).

### Level 2 — Master
On **infinite-dimensional shape spaces** (e.g. the space of curves/surfaces with an
$`L^2`$ or Sobolev metric, or the space of Riemannian metrics) the geodesic equation
becomes a **PDE**, and existence/regularity is subtle (the $`L^2`$ metric can have
vanishing geodesic distance). MM (Rumpf, Wirth, Effland) develops and rigorously
analyses **variational time-discretisations** and numerical schemes, proving
convergence rates for discrete (cubic Riemannian spline) approximations, with
applications to data science and inverse problems. Reference:
[Quartic $`L^p`$-convergence of cubic Riemannian splines, IMA JNA 2022](https://doi.org/10.1093/imanum/drab077).

---

## Core concept 5: Index theory and scalar curvature

![Index theory](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_702897ed42069ee3eaa7839633a48f71_topic5c-dsc_2007.jpg)

### Level 0 — High school
There is a deep bridge between *analysis* (solving equations on a shape) and
*topology* (the shape's holes). Counting the solutions of a special equation
secretly counts holes — and this forbids certain shapes from being curved a
certain way.

### Level 1 — Bachelor
The **[Atiyah–Singer index theorem](../GLOSSARY.md#atiyah-singer-index-theorem)** equates an analytic quantity, the **index**
$`\mathrm{ind}(D)=\dim\ker D - \dim\mathrm{coker}\,D`$ of an [elliptic operator](../GLOSSARY.md#elliptic-operator) $`D`$,
with a topological integral of [characteristic classes](../GLOSSARY.md#characteristic-class). For the **Dirac operator**
on a spin manifold, $`\mathrm{ind}(D) = \hat{A}(M)`$. The **Lichnerowicz formula**
$`D^2 = \nabla^*\nabla + \tfrac14\mathrm{scal}`$ then shows: if $`\mathrm{scal}>0`$,
$`D`$ has no harmonic spinors, so $`\hat{A}(M)=0`$ — a topological obstruction to
positive [scalar curvature](../GLOSSARY.md#scalar-curvature).

### Level 2 — Master
MM (Zeidler, Ebert, Deninger) develops **higher [index theory](../GLOSSARY.md#index-theory)** in [C\*-algebraic
K-theory](../GLOSSARY.md#k-theory) (the **Rosenberg index** in $`KO_*(C^*_r\pi_1)`$, higher $`\rho`$-invariants)
and **comparison/rigidity** results: band-width estimates, scalar-and-mean-curvature
comparison via Dirac operators, positive mass theorems in the spin setting. This
ties Topic 5 directly to Topic 1 (K-theory) and Topic 2 (spaces of PSC metrics).
References: [Atiyah–Singer index theorem](https://en.wikipedia.org/wiki/Atiyah%E2%80%93Singer_index_theorem),
[Zeidler, band width estimates via the Dirac operator, JDG 2022](https://doi.org/10.4310/jdg/1668186790).

---

**Further reading**
- do Carmo, *Riemannian Geometry*; Lee, *Introduction to Riemannian Manifolds*
- Petersen, *Riemannian Geometry* (Springer GTM 171)
- Lawson–Michelsohn, *Spin Geometry* (index theory & scalar curvature)
