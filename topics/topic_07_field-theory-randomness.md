# Topic 7 — Field Theory and Randomness

> **Objective (MM "O5"): exploit stochastic analysis tools in the context of non-commutative field theories.**
> By combining stochastic analysis, free probability, and topological recursion, we
> aim to construct field theories on [non-commutative spaces](../GLOSSARY.md#non-commutative-geometry) in the **critical
> dimension**, developing stochastic quantisation for scalar non-commutative QFTs
> and, ultimately, the first rigorous construction of a critical bosonic [quantum
> field theory](../GLOSSARY.md#quantum-field-theory).

Source: [T7: Field theory and randomness](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_field-theory-randomness.shtml)

Three research units:
1. **Integrability** (quartic Kontsevich model, topological recursion).
2. **Stochastic analysis of quantum fields** (non-commutative QFT via SPDEs).
3. **Effective theories and disorder** (polaron, SPDEs as scaling limits).

---

## Core concept 1: Quantum field theory (QFT)

![Integrability](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_f14a1ff9a733a03f538a2a66623908ab_topic7a-dsc_2865.jpg)

### Level 0 — High school
At the smallest scales, particles are ripples in invisible "fields" filling all of
space. Quantum field theory is the rulebook for these ripples — it powers the
Standard Model of particle physics. But making its mathematics fully rigorous is a
million-dollar open problem.

### Level 1 — Bachelor
A (Euclidean, scalar) QFT is formally defined by a **path integral**: averages of
observables $`F`$ are
$$
\langle F\rangle = \frac{1}{Z}\int F(\phi)\, e^{-S(\phi)}\,\mathcal{D}\phi,\qquad
S(\phi)=\int \Big(\tfrac12|\nabla\phi|^2 + \tfrac{m^2}{2}\phi^2 + \tfrac{\lambda}{4}\phi^4\Big)\,dx,
$$
an integral over the *infinite-dimensional* space of field configurations $`\phi`$.
The measure $`\mathcal{D}\phi`$ does not exist rigorously, so giving this meaning is
the mathematical challenge (**constructive QFT**).

### Level 2 — Master
Constructing a nonlinear QFT in the physical **4 space-time dimensions** is part of
the **Yang–Mills Clay Millennium Problem**. In $`d=2,3`$, scalar models
($`P(\phi)_2`$, $`\Phi^4_3`$) are constructed perturbatively around the free (Gaussian)
field. In $`d=4`$ the theory is **critical**: linear and nonlinear terms scale
identically, so perturbation around the linear theory fails. MM attacks scalar QFTs
on **non-commutative geometries**, where exact solvability is available.
References: [Quantum field theory](https://en.wikipedia.org/wiki/Quantum_field_theory),
[Constructive QFT](https://en.wikipedia.org/wiki/Constructive_quantum_field_theory).

---

## Core concept 2: Stochastic quantisation

![Stochastic analysis of fields](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_5139281886f521cb26e73e1196468f6e_topic7b-dsc_2874.jpg)

### Level 0 — High school
Instead of building a field "all at once", let it wiggle randomly over time like a
jittering elastic sheet until it settles into a stable random pattern. That
equilibrium pattern *is* the quantum field. Randomness becomes a construction tool.

### Level 1 — Bachelor
**Stochastic quantisation** (Parisi–Wu) realises the QFT measure
$`\propto e^{-S(\phi)}\mathcal{D}\phi`$ as the **invariant measure** of a stochastic
PDE — the Langevin dynamics
$$
\partial_t \phi = -\frac{\delta S}{\delta \phi} + \sqrt{2}\,\xi
= \Delta\phi - m^2\phi - \lambda\phi^3 + \sqrt{2}\,\xi,
$$
with $`\xi`$ space-time white noise. Construct/analyse the long-time behaviour of the
SPDE, and you construct the field theory.

### Level 2 — Master
This route requires the **regularity-structures / paracontrolled** machinery
(cf. Topic 6) because $`\phi^3`$ is ill-defined for the rough invariant field;
renormalisation is essential. MM (Weber, Wulkenhaar, Song) pursues **stochastic
quantisation of $`\lambda\phi^4`$ on Moyal ([non-commutative](../GLOSSARY.md#non-commutative-geometry)) space**, combining exact
solvability with [SPDE](../GLOSSARY.md#stochastic-pde) analysis, and connects discrete approximations (dynamical
Ising–Kac $`\to \Phi^4_3`$). Reference:
[Stochastic quantization](https://en.wikipedia.org/wiki/Stochastic_quantization),
[Stochastic quantization of $`\lambda\phi^4_2`$ in 2-d Moyal space, arXiv:2502.02355](https://arxiv.org/abs/2502.02355).

---

## Core concept 3: Non-commutative geometry and the Moyal space

### Level 0 — High school
Normally $`3\times 5 = 5\times 3`$. But in quantum mechanics, measuring position then
momentum differs from the reverse order. "Non-commutative spaces" build geometry
out of such order-sensitive coordinates — a geometry where $`xy \ne yx`$.

### Level 1 — Bachelor
On the **Moyal plane**, coordinates satisfy $`[x^\mu, x^\nu] = i\theta^{\mu\nu}`$
(constant antisymmetric $`\theta`$), implemented by replacing pointwise multiplication
with the **Moyal star product** $`\star`$. Functions become operators / infinite
matrices; integration becomes a trace. A scalar field theory has action with
$`\phi\star\phi\star\phi\star\phi`$ interactions.

### Level 2 — Master
Non-commutative field theories realise interactions as **matrix models**; the
$`\theta\to\infty`$ limit links them to large-$`N`$ matrix integrals. Connes' **spectral
triple** $`(\mathcal{A},H,D)`$ formalises non-commutative Riemannian geometry. MM
exploits the special integrability of the **Grosse–Wulkenhaar** $`\Phi^4`$ model on
Moyal space, which is renormalisable to all orders and exactly solvable in certain
limits. References:
[Noncommutative geometry](https://en.wikipedia.org/wiki/Noncommutative_geometry),
[Moyal product](https://en.wikipedia.org/wiki/Moyal_product).

---

## Core concept 4: Free probability and topological recursion

### Level 0 — High school
Ordinary probability adds independent random numbers (giving the bell curve). When
the "random numbers" are huge matrices that don't commute, a new kind of
probability is needed — and counting the shapes (surfaces) that appear organises
the answers into an elegant recursive pattern.

### Level 1 — Bachelor
**Free probability** (Voiculescu) replaces independence with **freeness** for
non-commuting random variables (operators). The free analogue of the central limit
theorem yields the **semicircle law** $`\rho(x)=\tfrac{1}{2\pi}\sqrt{4-x^2}`$ — the
eigenvalue distribution of large random Hermitian matrices (Wigner). **Topological
recursion** computes correlation functions of matrix models by a recursion indexed
by the genus and number of boundaries of surfaces.

### Level 2 — Master
**Topological recursion** (Eynard–Orantin) takes a spectral curve and recursively
produces invariants $`\omega_{g,n}`$ generating intersection numbers on
$`\overline{\mathcal{M}}_{g,n}`$ (Topic 2) — Kontsevich's solution of the Witten
conjecture is the prototype. MM (Wulkenhaar, Branahl, Hock, Schürmann) develops the
**blobbed topological recursion** of the **quartic Kontsevich model**, connecting
integrable structure, moduli spaces, and non-commutative QFT. References:
[Free probability](https://en.wikipedia.org/wiki/Free_probability),
[Topological recursion](https://en.wikipedia.org/wiki/Topological_recursion),
[Blobbed topological recursion of the quartic Kontsevich model, CMP 2022](https://doi.org/10.1007/s00220-022-04392-z).

---

## Core concept 5: Disorder, scaling limits and the polaron

![Effective theories and disorder](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_c9cb5154a9327185d1e896dcb1ee61ec_topic7c-dsc_4538.jpg)

### Level 0 — High school
A single electron dragging a cloud of distortion through a crystal behaves like a
heavier "dressed" particle — a polaron. Zoom out from many small random effects and
clean, universal behaviour emerges. Studying these limits links physics and
probability.

### Level 1 — Bachelor
A **scaling limit** rescales space/time so that a microscopic random model converges
to a continuum object (e.g. random walk $`\to`$ [Brownian motion](../GLOSSARY.md#brownian-motion)). The **polaron** is
modelled by the Fröhlich Hamiltonian; its large-coupling behaviour is governed by a
self-interacting (Pekar) variational problem and an **effective mass**.

### Level 2 — Master
MM (Mukherjee, Weber, Löwe) studies probabilistic field-theory questions at the
**statistical-mechanics interface**: large-deviation and path-measure analysis of
the **Fröhlich polaron** (Landau–Pekar–Spohn conjecture on effective mass),
**Gaussian multiplicative chaos** in Wiener space, and SPDEs arising as scaling
limits (including supercritical regimes). References:
[Polaron](https://en.wikipedia.org/wiki/Polaron),
[Effective mass of the Fröhlich polaron, arXiv:2307.13058](https://arxiv.org/abs/2307.13058).

---

**Further reading**
- Glimm–Jaffe, *Quantum Physics: A Functional Integral Point of View*
- Mingo–Speicher, *Free Probability and Random Matrices*
- Grosse–Wulkenhaar papers on the noncommutative $`\Phi^4`$ model
