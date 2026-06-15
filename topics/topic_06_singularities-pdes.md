# Topic 6 — Singularities and Partial Differential Equations

> **Objective (part of MM "O4"): approach open questions in the theory of PDEs.**
> We address singularity and rigidity phenomena for Riemannian and Lorentzian
> Einstein manifolds and try to prove the **stability of the Kerr family of black
> holes** in general relativity. The goal is to use and develop nonlinear PDE theory
> to understand singular phenomena in geometry and physics.

Source: [T6: Singularities and partial differential equations](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_singularities-pdes.shtml)

Three research units:
1. **Geometric analysis** (Einstein manifolds, gravitational instantons, minimal hypersurfaces).
2. **Dynamics of evolutionary PDEs** (black hole stability, Euler equations, cross-diffusion).
3. **Regularity** (stochastic PDEs, regularity structures, Monge–Ampère, thin-film).

---

## Core concept 1: Partial differential equations (PDEs)

![Geometric analysis](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_4568fcf8acb262db9ea1b08d20ff7d8e_topic6a-interaktion-dsc_3721.jpg)

### Level 0 — High school
Most laws of nature say how things *change*: how heat spreads, how waves travel,
how planets pull. A PDE is an equation that relates these rates of change across
space and time. Solving it predicts the future from the present.

### Level 1 — Bachelor
A **PDE** relates an unknown function $u(x_1,\dots,x_n)$ and its partial
derivatives. Three classical archetypes:
$$
\underbrace{\Delta u = 0}_{\text{elliptic (Laplace)}}\qquad
\underbrace{\partial_t u = \Delta u}_{\text{parabolic (heat)}}\qquad
\underbrace{\partial_{tt} u = \Delta u}_{\text{hyperbolic (wave)}}
$$
where $\Delta = \sum_i \partial_{x_i}^2$. Elliptic equations describe equilibria
(and are smoothing); parabolic equations describe diffusion; hyperbolic equations
describe propagation at finite speed.

### Level 2 — Master
MM works with **nonlinear** PDEs of geometric and physical origin. The character
(elliptic/parabolic/hyperbolic) dictates the analytic toolkit: a priori estimates,
energy methods, Sobolev/Hölder spaces, weak solutions, and the calculus of
variations. A recurring question is **well-posedness** versus **singularity
formation**. References: [Partial differential equation](https://en.wikipedia.org/wiki/Partial_differential_equation).

---

## Core concept 2: Singularities

### Level 0 — High school
Sometimes a smooth process suddenly breaks down: a wave crests and shatters, a
droplet pinches off, gravity collapses matter into a black hole. These breakdown
points are **singularities** — and they are usually the most interesting and
hardest part to understand.

### Level 1 — Bachelor
A **singularity** is a point/time where a solution loses regularity: a derivative
or the solution itself blows up, or smoothness fails. Example: Burgers' equation
$\partial_t u + u\,\partial_x u = 0$ develops a **shock** (gradient blow-up) in
finite time even from smooth data. Understanding **whether**, **when**, and **what
type** of singularity forms is the central question.

### Level 2 — Master
MM studies singularity formation across regimes: degenerations of sequences of
**4-dimensional Einstein manifolds** (bubbling, gravitational instantons,
collapsing Calabi–Yau/Kähler–Ricci flows à la Hein–Tosatti), singularities of
**minimal hypersurfaces**, and finite-time blow-up vs. global existence in
**cross-diffusion**/Keller–Segel chemotaxis systems. Tools include blow-up
analysis, monotonicity formulae, and $\varepsilon$-regularity. References:
[Singularity (mathematics)](https://en.wikipedia.org/wiki/Singularity_(mathematics)),
[Collapsing immortal Kähler–Ricci flows, Forum Math Pi 2025](https://doi.org/10.1017/fmp.2025.10).

---

## Core concept 3: Einstein manifolds and general relativity

### Level 0 — High school
Einstein discovered that gravity *is* the curving of spacetime by mass. The
equation governing this is one of the most important PDEs in physics, and the
shapes (geometries) it allows include black holes.

### Level 1 — Bachelor
A Riemannian (or Lorentzian) manifold is **Einstein** if its Ricci curvature is
proportional to the metric:
$$
\mathrm{Ric}(g) = \lambda\, g,\qquad \lambda\in\mathbb{R}.
$$
In Lorentzian signature, the (vacuum) **Einstein field equations**
$\mathrm{Ric}(g) - \tfrac12 \mathrm{scal}\,g + \Lambda g = 0$ govern gravity;
spacetime is a 4-manifold with signature $(-,+,+,+)$.

### Level 2 — Master
MM (Böhm, Hein, Lafuente) studies **rigidity** of Einstein manifolds under symmetry
and the structure of **non-compact Einstein manifolds with symmetry**, plus the
fine geometry of **gravitational instantons** (complete Ricci-flat 4-manifolds) and
their compactifications/renormalised volume. The Lorentzian side connects to unit 2
via the underlying causal/Lorentzian geometry. References:
[Einstein manifold](https://en.wikipedia.org/wiki/Einstein_manifold),
[Non-compact Einstein manifolds with symmetry, JAMS 2023](https://doi.org/10.1090/jams/1022).

---

## Core concept 4: Black hole stability (the Kerr problem)

![Evolutionary PDEs](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_255ac7fc4d609aaf7fa5b55e08a259aa_topic6b-dsc_4659.jpg)

### Level 0 — High school
If you "poke" a spinning black hole, does it wobble and settle back down, or fall
apart? Physically we expect it to settle — but proving this from the equations is
one of the great open challenges of mathematical physics.

### Level 1 — Bachelor
The **Kerr metric** is the exact rotating-black-hole solution of the vacuum
Einstein equations, a family parametrised by mass $M$ and angular momentum $a$.
**Nonlinear stability** asks: do small perturbations of Kerr data evolve, under the
Einstein equations, to a spacetime that asymptotically settles to a (nearby) Kerr
solution? This is a question about a quasilinear hyperbolic PDE system.

### Level 2 — Master
MM (Holzegel, with Dafermos–Rodnianski–Taylor) develops the analysis of
**quasilinear wave equations on asymptotically flat spacetimes**, decay estimates
(redshift, $r^p$-weighted energies, vector-field method), and mode stability,
building toward full nonlinear stability of Kerr — paralleling the proven nonlinear
stability of the Schwarzschild family. Closely tied are the **Euler equations** of
fluid dynamics (two-phase flow with singular vorticity, bubble rings). References:
[Kerr metric](https://en.wikipedia.org/wiki/Kerr_metric),
[Nonlinear stability of Schwarzschild, arXiv:2104.08222](https://arxiv.org/abs/2104.08222).

---

## Core concept 5: Regularity theory and singular stochastic PDEs

### Level 0 — High school
"Regularity" asks how smooth a solution is. When you add random noise everywhere
(like static), solutions become so jagged that the equation barely makes sense.
New mathematics was invented to give these noisy equations a precise meaning.

### Level 1 — Bachelor
**Regularity estimates** bound derivatives of solutions (e.g. Schauder estimates:
elliptic solutions gain two derivatives in Hölder spaces). A **stochastic PDE
(SPDE)** adds random forcing, e.g. the dynamical $\Phi^4$ model
$$
\partial_t \phi = \Delta\phi - \phi^3 + \xi,
$$
with $\xi$ space-time white noise. The noise is so rough that $\phi^3$ is
classically ill-defined, requiring **renormalisation** (subtracting infinities).

### Level 2 — Master
The breakthroughs of **regularity structures** (Hairer) and **paracontrolled
calculus** (Gubinelli–Imkeller–Perkowski) give a solution theory for singular SPDEs
in the **subcritical** regime. MM (Weber, Tempelmayr, Chandra) proves **a priori
bounds** for $\Phi^4$ and the parabolic Anderson model in the full subcritical
regime and pushes toward **quasilinear** equations (stochastic porous medium). The
deterministic side includes regularity for the complex **Monge–Ampère** and
**thin-film** equations. References:
[Regularity structures](https://en.wikipedia.org/wiki/Regularity_structure),
[A priori bounds for $\Phi^4$ in the full subcritical regime, ARMA 2023](https://doi.org/10.1007/s00205-023-01876-7).

---

**Further reading**
- Evans, *Partial Differential Equations* (AMS GSM 19)
- Dafermos–Rodnianski lecture notes on the analysis of black hole spacetimes
- Hairer, *A theory of regularity structures*, Invent. Math. 198 (2014)
