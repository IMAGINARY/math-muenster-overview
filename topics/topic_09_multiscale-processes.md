# Topic 9 — Multiscale Processes and Effective Behaviour

> **Objective (MM "O7"): analyse structures in multiscale processes and derive effective models.**
> We analyse multiscale phenomena in physical, engineering, and biological systems
> and develop models and numerical methods to predict their behaviour: optimisation
> and design across scales, approximation algorithms for optimal control,
> convergence rates in **nonlinear homogenisation**, and mixing/equilibration in
> fluid dynamics and kinetic equations. Identifying the relevant scales to derive
> **scaling limits** is the unifying theme.

Source: [T9: Multiscale processes and effective behaviour](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_multiscale-processes_effective-behaviour.shtml)

Three research units:
1. **Determination and optimisation of structures** (optimal design, HJB without curse of dimensionality).
2. **[Homogenisation](../GLOSSARY.md#homogenisation) and multiscale methods** (nonlinear homogenisation, model order reduction).
3. **Mixing and equilibration** (fluid mixing, kinetic equations, transport).

---

## Core concept 1: Multiple scales and effective models

![Optimisation of structures](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_b4dacec85d04b44fe9314f6e08488539_topic9a-dsc_2948.jpg)

### Level 0 — High school
A sponge looks solid from far away but is full of tiny holes up close. To predict
how it soaks up water you don't track every pore — you find an "effective" rule for
the whole sponge. Multiscale maths is the art of jumping from tiny details to
big-picture rules.

### Level 1 — Bachelor
Many systems have a small parameter $`\varepsilon`$ (ratio of fine to coarse scale).
One seeks the **effective behaviour** as $`\varepsilon\to 0`$: a simpler model that
captures the macroscopic response without resolving every microscopic feature. The
mathematics quantifies *which* scales matter via **sharp scaling laws** and
**convergence rates** (how fast the fine model approaches the effective one).

### Level 2 — Master
The unifying tool is the rigorous **scaling limit**: identify the dominant balance
among competing energy/time scales and derive a *scale-free* effective theory, with
error estimates. MM emphasises **balancing parameters** in multiscale numerical
methods so accuracy and cost are controlled simultaneously, including within
iterative optimisation loops. See concepts below for the two main mechanisms
(homogenisation, optimal control). Reference:
[Multiscale modeling](https://en.wikipedia.org/wiki/Multiscale_modeling).

---

## Core concept 2: Homogenisation

![Homogenisation](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_c2aa5ea738e3dc3b07d51f18a9858fe1_topic9b-dsc_2957.jpg)

### Level 0 — High school
A finely striped material (alternating metal and plastic) behaves, overall, like a
single new material with averaged properties. Homogenisation computes those average
properties from the fine pattern.

### Level 1 — Bachelor
**Homogenisation** replaces a PDE with rapidly oscillating coefficients
$`a(x/\varepsilon)`$ by an effective PDE with constant (homogenised) coefficients
$`a^{\mathrm{hom}}`$. Prototype: for
$`-\nabla\!\cdot\!\big(a(x/\varepsilon)\nabla u_\varepsilon\big) = f`$, the solutions
$`u_\varepsilon \to u_0`$ where $`u_0`$ solves
$`-\nabla\!\cdot\!\big(a^{\mathrm{hom}}\nabla u_0\big)=f`$. The effective coefficient
is *not* the naive average — it is found by solving a **cell problem** on the unit
period.

### Level 2 — Master
MM (Zeppieri, Mukherjee, Ohlberger, Rave) studies **nonlinear** and **stochastic**
homogenisation: convergence rates for systems of nonlinear elliptic PDEs in
**randomly perforated domains** (overlapping perforations), and homogenisation of
viscous **Hamilton–Jacobi–Bellman equations on continuum percolation clusters**
(challenges: non-stationarity, non-ellipticity, no global Lipschitz bound),
linking to large deviations (Topic 8). Framework: [Γ-convergence](../GLOSSARY.md#gamma-convergence), two-scale
convergence, correctors. References:
[Homogenization (mathematics)](https://en.wikipedia.org/wiki/Homogenization_(mathematics)),
[Γ-convergence](https://en.wikipedia.org/wiki/%CE%93-convergence).

---

## Core concept 3: Optimal control and the curse of dimensionality

### Level 0 — High school
A pilot steering a rocket wants the *best* path — least fuel, fastest arrival. Find
the best control among infinitely many options. But when there are many knobs to
turn at once, the number of possibilities explodes — the "curse of dimensionality".

### Level 1 — Bachelor
**Optimal control** seeks an input $`u(t)`$ minimising a cost
$`J(u)=\int_0^T \ell(x,u)\,dt + g(x(T))`$ subject to dynamics $`\dot x = f(x,u)`$. The
**value function** $`V`$ solves the **Hamilton–Jacobi–Bellman (HJB)** PDE
$$
\partial_t V + \min_{u}\big\{f(x,u)\cdot\nabla V + \ell(x,u)\big\} = 0.
$$
In dimension $`d`$ a naive grid has $`N^d`$ points — infeasible for large $`d`$ (the
**curse of dimensionality**).

### Level 2 — Master
MM (Jentzen, Wirth, Simon) designs **approximation algorithms that provably
overcome the curse of dimensionality** for HJB / nonlinear parabolic PDEs (e.g.
multilevel Monte Carlo / nonlinear Monte Carlo with polynomial runtime in $`d`$), and
studies **PDE-constrained optimal design** where fine-scale (micro)structures emerge
as optimisers (compliance minimisation, branched transport). References:
[Hamilton–Jacobi–Bellman equation](https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi%E2%80%93Bellman_equation),
[Overcoming the curse of dimensionality for semilinear parabolic PDEs, Proc. R. Soc. A 2020](https://doi.org/10.1098/rspa.2019.0630).

---

## Core concept 4: Model order reduction

### Level 0 — High school
If you must re-run a slow, expensive simulation thousands of times (for different
settings), you first build a cheap "mini-model" that captures the essentials, then
run that instead. You trade a little accuracy for enormous speed.

### Level 1 — Bachelor
**Model order reduction (MOR)** approximates a high-dimensional parametrised system
by a low-dimensional surrogate. The **reduced basis method** computes a few
representative solution "snapshots" $`u(\mu_1),\dots,u(\mu_n)`$ for sample parameters
$`\mu_i`$, spanning a small space $`V_n`$, then solves the PDE projected onto $`V_n`$ for
any new $`\mu`$ — with rigorous, computable **a posteriori error bounds**.

### Level 2 — Master
MM (Ohlberger, Rave, Keil, Schindler) develops **localised / two-scale reduced
basis** and **localised orthogonal decomposition (LOD)** methods for multiscale
PDEs, **trust-region RB** for PDE-constrained optimisation and parameter
identification, and certified surrogates that feed into Topic 10 (machine learning).
Key issues: offline/online splitting, greedy basis generation, certified error
control. References:
[Model order reduction](https://en.wikipedia.org/wiki/Model_order_reduction),
[Relaxed localized trust-region RB, ESAIM:M2AN 2024](https://doi.org/10.1051/m2an/2023089).

---

## Core concept 5: Mixing, equilibration and kinetic equations

![Mixing and equilibration](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_4a21404c4cf3acaa81cb9ccf8e17bbbe_topic9c-tafel-dsc_3005.jpg)

### Level 0 — High school
Stir milk into coffee: streaks stretch and fold until the colour is uniform. How
fast can stirring mix things, and how fast does a gas settle to equilibrium? These
rates are what this unit pins down.

### Level 1 — Bachelor
**Mixing** measures how a flow homogenises a passive scalar; **enhanced
dissipation** is the speed-up of diffusion caused by stirring. **Kinetic equations**
(e.g. Boltzmann, Fokker–Planck) describe gases via a density $`f(t,x,v)`$ on
position–velocity space and relax toward Maxwellian equilibrium. A guiding question:
the maximal rate of mixing/equilibration achievable.

### Level 2 — Master
MM (Seis, Pirner, Engwer, Stevens) studies **optimal mixing rates** and enhanced
dissipation for advection–diffusion, **hypocoercivity** and reaction–diffusion
limits for kinetic Fokker–Planck / BGK models for gas mixtures, and numerical
methods minimising artificial dissipation for transport and **conservation laws**
(stabilised DG cut-cell schemes). References:
[Kinetic theory of gases](https://en.wikipedia.org/wiki/Kinetic_theory_of_gases),
[Bounds on the rate of enhanced dissipation, CMP 2023](https://doi.org/10.1007/s00220-022-04588-3).

---

**Further reading**
- Pavliotis–Stuart, *Multiscale Methods: Averaging and Homogenization*
- Hesthaven–Rozza–Stamm, *Certified Reduced Basis Methods for Parametrized PDEs*
- Villani, *Hypocoercivity* (Memoirs AMS)
