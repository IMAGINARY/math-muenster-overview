# Topic 8 — Random Discrete Structures and Their Limits

> **Objective (MM "O6"): analyse structures and their limits in stochastic models.**
> We study random geometric structures and their influence on interacting particle
> systems, investigating fluctuations and the role of disorder in **scaling limits**.
> Key objects include random tessellations, random graphs and networks, and
> percolation on groups.

Source: [T8: Random discrete structures and their limits](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_random-discrete-structures-limits.shtml)

Discrete structures pervade mathematics, CS, statistical physics and optimisation;
their random versions show rich **macroscopic behaviour** and **phase transitions**.
Three research units:
1. **Random tessellations and polytopes** (stochastic geometry).
2. **Random graphs and percolation**.
3. **Limits of large particle systems** (KPZ, hydrodynamic limits).

---

## Core concept 1: Random graphs

![Random graphs](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_8c4819a3f4477c4cc39cc8bdaf222d31_topic8b-dsc_3956.jpg)

### Level 0 — High school
Draw some dots and connect each pair by flipping a coin. The result is a random
network — a toy model of a friendship network or the web. Surprisingly, as you add
dots, a giant connected cluster appears almost suddenly once links are frequent
enough.

### Level 1 — Bachelor
The **Erdős–Rényi graph** $G(n,p)$ has $n$ vertices, each of the $\binom{n}{2}$
edges present independently with probability $p$. A landmark **phase transition**:
with $p=c/n$, as $n\to\infty$ the largest component is
$$
\begin{cases} O(\log n) & c<1\ (\text{subcritical}),\\
\Theta(n) \ \text{(a "giant component")} & c>1\ (\text{supercritical}).\end{cases}
$$
The threshold for connectivity is $p=\frac{\log n}{n}$.

### Level 2 — Master
MM studies $G(n,p)$ as a random **environment for spin systems** (Ising/Curie–Weiss
on Erdős–Rényi graphs: magnetisation fluctuations, low-temperature and critical
regimes) and richer models like **preferential attachment** (scale-free networks)
and the **stochastic block model** (community detection, spectral methods,
random-walk hitting times). References:
[Erdős–Rényi model](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model),
[Stochastic block model](https://en.wikipedia.org/wiki/Stochastic_block_model).

---

## Core concept 2: Percolation and phase transitions

### Level 0 — High school
Imagine randomly opening or blocking the tiny channels in a porous rock. Below a
critical fraction of open channels, water cannot cross; above it, it suddenly can.
That sharp switch is a phase transition — the same idea as water freezing.

### Level 1 — Bachelor
In **bond percolation** on $\mathbb{Z}^d$, each edge is open with probability $p$
independently. There is a critical $p_c\in(0,1)$ such that
$$
\theta(p) = \mathbb{P}_p(\text{origin in an infinite open cluster})
\begin{cases} =0 & p<p_c,\\ >0 & p>p_c.\end{cases}
$$
For $d=2$, $p_c=\tfrac12$ for bond percolation (Kesten). This is the simplest model
exhibiting a genuine phase transition with critical phenomena.

### Level 2 — Master
MM (Mukherjee, Recke, Kerr) studies **percolation on groups** and
**group-invariant percolation**, where the geometry/representation theory of the
group (amenability, **property (T)**, **Haagerup property**) interacts with the
existence and uniqueness of infinite clusters, analysed through **Schur multipliers**
and **Roe / group C\*-algebras** — a bridge to Topic 4. References:
[Percolation theory](https://en.wikipedia.org/wiki/Percolation_theory),
[Haagerup property and group-invariant percolation, arXiv:2303.17429](https://arxiv.org/abs/2303.17429).

---

## Core concept 3: Random tessellations and polytopes (stochastic geometry)

![Random tessellations](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_8233581121d560093d2084ac82491d20_topic8a-dsc_3820.jpg)

### Level 0 — High school
Scatter points at random, then give each point the territory closest to it — you get
a random patchwork of cells, like cracked mud or a giraffe's coat. Mathematicians
measure the typical shapes, areas and number of sides of these random tiles.

### Level 1 — Bachelor
A **Voronoi tessellation** of a point set $\{x_i\}$ assigns to each $x_i$ the cell
$\{y: |y-x_i|\le |y-x_j|\ \forall j\}$. With the points a **Poisson point process**,
one gets the Poisson–Voronoi tessellation and studies expected cell volume, number
of faces, etc. A **random polytope** is the convex hull of random points; its
expected number of vertices/faces is a classical question (Sylvester's problem).

### Level 2 — Master
MM (Gusakova, Kabluchko, Huesmann) analyses **beta / beta-prime polytopes**,
**Poisson–Voronoi and Laguerre tessellations**, sectional tessellations, and
high-dimensional limits and threshold phenomena (expected $f$-vectors, angle sums of
random simplices). A second thread uses **optimal transport** of stationary point
processes (Benamou–Brenier formulae, hyperuniformity, matching problems). References:
[Stochastic geometry](https://en.wikipedia.org/wiki/Stochastic_geometry),
[Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram).

---

## Core concept 4: Interacting particle systems and scaling limits

![Particle systems](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_f560fa46564515b8be369e321b9d77df_topic8c-interaktion-dsc_4609.jpg)

### Level 0 — High school
Many simple agents following local random rules — cars on a road, particles hopping
on a line — together produce complex large-scale patterns. Zooming out turns the
jiggling crowd into a smooth flowing equation.

### Level 1 — Bachelor
An **interacting particle system** is a continuous-time Markov process on a large
configuration space with local update rules. Example: the **(weakly) asymmetric
simple exclusion process** (ASEP/WASEP) — particles hop left/right on $\mathbb{Z}$
but never share a site. A **scaling limit** rescales space and time so the random
particle density converges to a deterministic/stochastic PDE.

### Level 2 — Master
MM (Weber, Huesmann, Mukherjee) proves convergence of **WASEP to the KPZ equation**
and of static **Ising–Kac models to $\Phi^4_3$** using **regularity structures**
(cf. Topics 6–7), and uses **large deviation principles** for random walks in random
environments to study **stochastic homogenisation** of the Hamilton–Jacobi–Bellman
equation (link to Topic 9). The **KPZ equation**
$$
\partial_t h = \partial_x^2 h + (\partial_x h)^2 + \xi
$$
is the canonical scaling limit governing random interface growth (the **KPZ
universality class**). References:
[KPZ equation](https://en.wikipedia.org/wiki/Kardar%E2%80%93Parisi%E2%80%93Zhang_equation),
[Exclusion process](https://en.wikipedia.org/wiki/Asymmetric_simple_exclusion_process).

---

## Core concept 5: Fluctuations, disorder and universality

### Level 0 — High school
Add many independent random things and you almost always get the same bell-shaped
curve — no matter the details. This "universality" is why averages are predictable.
Researchers hunt for which random systems share such universal large-scale laws.

### Level 1 — Bachelor
The **central limit theorem** is the prototype: normalised sums of i.i.d. variables
converge to a Gaussian, regardless of the underlying distribution. In statistical
mechanics, **fluctuations** of macroscopic quantities (e.g. magnetisation) around
their mean reveal the phase: Gaussian away from criticality, non-Gaussian at a
critical point. **Disorder** (frozen randomness in the environment) can change these
laws.

### Level 2 — Master
MM studies fluctuation theorems for **Curie–Weiss** and Ising models on random
graphs (including critical scaling and "when chaos stops to propagate"), zeros of
**random polynomials** under heat flow, and **large deviations** quantifying the
impact of disorder (quenched vs. annealed) in random environments. Universality
classes (Gaussian, KPZ, random-matrix) organise the possible limiting laws.
References: [Central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem),
[KPZ universality](https://en.wikipedia.org/wiki/KPZ_universality_class).

---

**Further reading**
- van der Hofstad, *Random Graphs and Complex Networks* (Vols. 1–2)
- Grimmett, *Percolation*; Schneider–Weil, *Stochastic and Integral Geometry*
- Corwin, *The Kardar–Parisi–Zhang equation and universality class* (survey)
