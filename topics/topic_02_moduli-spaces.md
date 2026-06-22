# Topic 2 — Moduli Spaces in Arithmetic and Geometry

> **Objective (MM "O2"): Study moduli spaces to advance the Langlands programme and other fields.**
> Our research advances the (local) [Langlands Programme](../GLOSSARY.md#langlands-programme) through the arithmetic
> properties of associated [moduli spaces](../GLOSSARY.md#moduli-space) and representation categories. More
> broadly, moduli spaces appear in differential topology (diffeomorphism groups of
> high-dimensional manifolds), differential geometry (deformations of positive
> [scalar curvature](../GLOSSARY.md#scalar-curvature) metrics), and mathematical physics (moduli of stable curves and
> of Strebel differentials).

Source: [T2: Moduli spaces in arithmetic and geometry](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_moduli-spaces.shtml)

The term *moduli space* was coined by Riemann for the space $`\mathfrak{M}_g`$
parametrising all compact Riemann surfaces (1-dimensional complex manifolds) of
genus $`g`$. MM's three research units are:
1. **Construction and existence** ([Shimura varieties](../GLOSSARY.md#shimura-variety), $`G`$-shtukas, Galois deformation spaces).
2. **Compactification and stratifications**.
3. **Invariants and cohomology** (intersection theory, [derived categories](../GLOSSARY.md#derived-category), topological recursion).

---

## Core concept 1: Moduli space

![Moduli blackboard](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_c6cba45a4c554e2061acfe314593468c_topic2a-dsc_2269.jpg)

### Level 0 — High school
Instead of studying one triangle, imagine a "map of all triangles", where each
point of the map stands for one possible triangle shape. Walking across the map
continuously morphs one triangle into another. A **moduli space** is exactly such
a "map of all shapes of a given type" — its points *are* geometric objects.

### Level 1 — Bachelor
A moduli space parametrises isomorphism classes of objects. The classic example
$`\mathfrak{M}_g`$ parametrises smooth projective curves of genus $`g`$; it has
dimension $`3g-3`$ for $`g\ge 2`$. Building such a space requires forming a quotient
by an automorphism/equivalence relation, which is delicate (quotients can be
badly behaved). For genus $`1`$ with a marked point, the moduli space is the
**modular curve** $`\mathrm{SL}_2(\mathbb{Z})\backslash \mathbb{H}`$ with the famous
$`j`$-invariant as coordinate:
$$
j(\tau),\qquad \tau\in\mathbb{H}=\{z\in\mathbb{C}: \operatorname{Im} z>0\}.
$$

### Level 2 — Master
Rigorously, a moduli problem is a functor $\mathcal{M}\colon
(\mathrm{Sch})^{\mathrm{op}}\to \mathrm{Set}$`, `$S\mapsto \{\text{families over } S\}$.
A **fine** moduli space represents this functor; obstructions from automorphisms
force one to work with **algebraic stacks** (e.g. the [Deligne–Mumford stack](../GLOSSARY.md#deligne-mumford-stack)
$`\overline{\mathcal{M}}_{g,n}`$). Construction uses **Geometric Invariant Theory**
(Mumford): $`\mathcal{M} = X^{\mathrm{ss}}/\!\!/ G`$ as a GIT quotient of a Hilbert
scheme by $`\mathrm{PGL}`$. Teichmüller theory presents $\mathfrak{M}_g =
\mathcal{T}_g/\mathrm{MCG}(\Sigma_g)$ as a quotient of [Teichmüller space](../GLOSSARY.md#teichmuller-space) by the
[mapping class group](../GLOSSARY.md#mapping-class-group), linking it to the [classifying space](../GLOSSARY.md#classifying-space) $`B\,\mathrm{Diff}(\Sigma_g)`$
— the perspective behind the Madsen–Weiss theorem proving the Mumford conjecture.
References: [Moduli space](https://en.wikipedia.org/wiki/Moduli_space),
[Deligne–Mumford stack](https://en.wikipedia.org/wiki/Deligne%E2%80%93Mumford_stack).

---

## Core concept 2: The Langlands programme

### Level 0 — High school
There are two very different worlds in mathematics: one about whole numbers and
equations, another about waves and symmetry. The Langlands programme is a giant
dictionary claiming these two worlds secretly say the same things — a "Rosetta
Stone" of mathematics.

### Level 1 — Bachelor
The programme predicts a correspondence between
- **Galois representations**: continuous homomorphisms
  $`\rho\colon \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to GL_n(\mathbb{C})`$
  (or $`p`$-adic), encoding symmetries of number fields, and
- **automorphic representations**: certain infinite-dimensional representations of
  groups like $`GL_n(\mathbb{A})`$ over the adeles, generalising modular forms.

The simplest nontrivial case ($`n=1`$) is class field theory; $`n=2`$ over
$`\mathbb{Q}`$ includes the modularity behind Fermat's Last Theorem (Wiles).

### Level 2 — Master
MM studies the **local** [Langlands correspondence](../GLOSSARY.md#langlands-programme) and its geometrisation. Moduli
spaces enter as **[Shimura varieties](../GLOSSARY.md#shimura-variety)** and **moduli of (local/global)
$`G`$-shtukas**, whose étale cohomology is conjectured to realise the
correspondence. The modern **categorical / geometric** form (Fargues–Scholze,
Emerton–Gee–Hellmann) phrases it as an equivalence of [derived categories](../GLOSSARY.md#derived-category) of
sheaves on the stack $`\mathrm{Bun}_G`$ (or on a stack of Galois/Langlands
parameters), with the **Fargues–Fontaine curve** and $`B_{dR}^+`$-Grassmannian
(Viehmann's Newton strata) as central geometric objects. References:
[Langlands program](https://en.wikipedia.org/wiki/Langlands_program),
[Emerton–Gee–Hellmann, categorical p-adic Langlands, arXiv:2210.01404](https://arxiv.org/abs/2210.01404).

---

## Core concept 3: Compactification and stratification

![Compactification](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_84ad90517c8930bf48edaaaaf5c641a5_topic2b-dsc_3873.jpg)

### Level 0 — High school
A map of all shapes often has "edges" where shapes degenerate (a circle pinching
to a figure-eight). To study the map fully you add those boundary cases, like
adding the horizon to a landscape so nothing runs off the edge.

### Level 1 — Bachelor
Many moduli spaces are non-compact: families can degenerate. A **compactification**
adds boundary points for the limiting (singular) objects. The Deligne–Mumford
compactification $`\overline{\mathfrak{M}}_g`$ adds **stable nodal curves**. A
**stratification** decomposes a space into locally closed pieces (strata),
$`X = \bigsqcup_\alpha X_\alpha`$, each smoother/simpler, organising the geometry by
type of degeneration.

### Level 2 — Master
$`\overline{\mathcal{M}}_{g,n}`$ is a smooth proper DM stack with normal-crossings
boundary $`\partial\overline{\mathcal{M}}_{g,n}`$ stratified by dual graphs of
stable curves. In arithmetic geometry, **Newton** and **Kottwitz–Rapoport**
stratifications of (the special fibres of) Shimura varieties and of affine
Grassmannians/$`B_{dR}^+`$-Grassmannians control reduction behaviour of Galois
representations; Harder–Narasimhan strata classify degeneration of bundles. MM
work (Viehmann, Nguyen, Lourenço) analyses these strata on the
$`B_{dR}^+`$-Grassmannian. Reference:
[Deligne–Mumford compactification](https://en.wikipedia.org/wiki/Moduli_of_algebraic_curves#Deligne%E2%80%93Mumford_compactification).

---

## Core concept 4: Cohomological invariants and intersection theory

![Invariants](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_015bdc042257d0f42724b5734b7e6f09_topic2c-dsc_3884.jpg)

### Level 0 — High school
Once you have your map of shapes, you can ask geometric questions about the map
itself: how many curves pass through given points? Counting such things cleverly
reveals hidden patterns and even connects to physics.

### Level 1 — Bachelor
**Intersection theory** counts how subvarieties meet: in the Chow ring or
cohomology ring of a moduli space, classes multiply and their product, integrated
("$`\int_{\overline{\mathcal{M}}_{g,n}}`$"), gives **intersection numbers**. On
$`\overline{\mathcal{M}}_{g,n}`$ the **$`\psi`$-classes** (cotangent line classes at
marked points) give numbers $`\langle \tau_{d_1}\cdots\tau_{d_n}\rangle`$ studied by
Witten and Kontsevich.

### Level 2 — Master
The **Witten conjecture** (Kontsevich's theorem) states that the generating
function of $`\psi`$-intersection numbers on $`\overline{\mathcal{M}}_{g,n}`$ is a
$`\tau`$-function of the KdV hierarchy. Kontsevich's proof uses a cell decomposition
via **Strebel differentials** and a matrix-model ("$`\mathrm{Airy}`$") integral.
This is the seed of **topological recursion** (Eynard–Orantin), which MM
(Wulkenhaar, Schürmann) generalises — including a *quartic* analogue of the
Kontsevich model. On the arithmetic side, the conjectural [Langlands correspondence](../GLOSSARY.md#langlands-programme)
is refined to an equivalence of **[derived categories](../GLOSSARY.md#derived-category) of (constructible/coherent)
sheaves** on moduli of parameters. In differential topology the same circle of
ideas controls the cohomology of $`B\,\mathrm{Diff}(M)`$ and the space
$`\mathcal{R}^+(M)`$ of positive [scalar curvature](../GLOSSARY.md#scalar-curvature) metrics. References:
[Witten conjecture](https://en.wikipedia.org/wiki/Witten_conjecture),
[Topological recursion](https://en.wikipedia.org/wiki/Topological_recursion).

---

## Core concept 5: Diffeomorphism groups and spaces of metrics

### Level 0 — High school
Take a rubber shape; all the ways of smoothly stretching it without tearing form
their own "space of stretches". And all the ways of measuring distances on it
(its possible geometries) form yet another space. Studying these spaces tells us
which shapes are flexible and which are rigid.

### Level 1 — Bachelor
$`\mathrm{Diff}(M)`$, the group of diffeomorphisms of a manifold $`M`$, is an
infinite-dimensional topological group; its classifying space $`B\,\mathrm{Diff}(M)`$
is the moduli space of smooth $`M`$-bundles. Separately, the space
$`\mathcal{R}^+(M)`$ of Riemannian metrics of **positive scalar curvature** is a
subspace of all metrics; asking whether it is empty, connected, or has nontrivial
topology is a central question.

### Level 2 — Master
For high-dimensional manifolds, $`B\,\mathrm{Diff}(M)`$ is studied via **Goodwillie–
Weiss embedding calculus**, **[surgery theory](../GLOSSARY.md#surgery-theory)**, and **pseudoisotopy/[Waldhausen K-theory](../GLOSSARY.md#waldhausen-k-theory)**;
MM (Ebert, Reinhold, Wiemeler, Randal-Williams collaboration) computes its
rational cohomology and the homotopy type of $`\mathcal{R}^+(M)`$. The
**positive [scalar curvature](../GLOSSARY.md#scalar-curvature) cobordism category** and index-theoretic obstructions
(the Rosenberg index in $`KO_*(C^*\pi_1)`$) link this directly back to Topic 1
(K-theory) and Topic 5 (curvature). Reference:
[Ebert–Randal-Williams, PSC cobordism category, Duke 2022](https://doi.org/10.1215/00127094-2022-0023).

---

**Further reading**
- Harris–Morrison, *Moduli of Curves* (Springer GTM 187)
- Viehmann, *On Newton strata in the $`B_{dR}^+`$-Grassmannian* — [Duke 2024](https://doi.org/10.1215/00127094-2024-0005)
- Fargues–Scholze, *Geometrization of the local Langlands correspondence* — [arXiv:2102.13459](https://arxiv.org/abs/2102.13459)
