# Topic 4 — Groups and Actions

> **Objective (part of MM "O3"): answer open questions in C\*-algebras, study group theory and group actions.**
> Research linked to group theory and group actions, approached using tools from
> functional analysis, probability theory, and combinatorics, with a specific
> emphasis on Cartan subalgebras in simple nuclear C\*-algebras.

Source: [T4: Groups and actions](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_groups-actions.shtml)

Symmetry, expressed through **groups and their actions**, cuts across the whole
cluster. Three research units:
1. **Groups, dynamics and C\*-algebras** (amenability, freeness, property (T)).
2. **Entropy, probability and geometry of groups** (orbit equivalence, invariant percolation).
3. **Algebraic groups and Lie groups** (representations of $p$-adic groups, Bruhat–Tits buildings).

---

## Core concept 1: Groups and group actions

![Groups blackboard](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_5c296905990ed9a822ccff3f54aa9618_topic4a-tafel-dsc_2024.jpg)

### Level 0 — High school
A **group** is the mathematics of symmetry: the collection of all moves that leave
something looking the same (rotating a square by 90°, flipping it). A group
**acts** on an object when each of its moves rearranges that object. Studying the
moves tells you about the object, and vice versa.

### Level 1 — Bachelor
A group $(G,\cdot)$ has an associative product, identity $e$, and inverses. An
**action** of $G$ on a set/space $X$ is a homomorphism $G\to \mathrm{Sym}(X)$
(or $\mathrm{Homeo}(X)$, $GL(V)$, …), equivalently a map $G\times X\to X$,
$(g,x)\mapsto g\cdot x$ with $e\cdot x = x$ and $g\cdot(h\cdot x) = (gh)\cdot x$.
**Orbits** $G\cdot x$ partition $X$; **stabilisers** $G_x=\{g: g\cdot x = x\}$
satisfy the orbit–stabiliser relation $|G\cdot x| = [G:G_x]$. **Geometric group
theory** treats a finitely generated group itself as a metric space via its Cayley
graph.

### Level 2 — Master
MM treats infinite discrete groups as geometric/combinatorial objects and studies
their actions on compact spaces and measure spaces. Key dividing lines:
**amenability** (existence of an invariant mean), **property (T)** (rigidity:
trivial representation isolated in the unitary dual), the **Haagerup property**
(a-T-menability), and **hyperbolicity** (Gromov). These properties control the
dynamics and the associated operator algebras. References:
[Group action](https://en.wikipedia.org/wiki/Group_action),
[Geometric group theory](https://en.wikipedia.org/wiki/Geometric_group_theory).

---

## Core concept 2: C\*-algebras, crossed products and Cartan subalgebras

### Level 0 — High school
When a symmetry group acts on a space, you can package the whole "space + symmetry"
into a single algebraic object (a crossed product). Inside it sometimes hides a
simpler, well-organised "coordinate grid" called a Cartan subalgebra, which makes
the whole thing far easier to understand.

### Level 1 — Bachelor
Given an action of $G$ on a C\*-algebra $A$ (e.g. $A=C(X)$), the **crossed
product** $A\rtimes G$ is a new C\*-algebra encoding both. For $X$ a point this is
the **group C\*-algebra** $C^*(G)$. A **Cartan subalgebra** $B\subseteq A$ is a
maximal abelian subalgebra that is regular (its normalisers generate $A$) and
carries a faithful conditional expectation $A\to B$ — an operator-algebraic
analogue of a coordinate system / maximal torus.

### Level 2 — Master
By **Renault's theorem**, a Cartan pair $(A,B)$ corresponds to a twisted étale
groupoid: $A = C^*_r(\mathcal{G},\Sigma)$, $B=C_0(\mathcal{G}^{(0)})$. MM's
emphasis is proving **existence and uniqueness of Cartan subalgebras** in simple
separable nuclear C\*-algebras (the classifiable ones), connecting the abstract
classification (Topic 1) to topological dynamics. Recent MM work (Gardella–Geffen–
Kranz–Naryshkin–Vaccaro) proves **$\mathcal{Z}$-stability** and classifiability of
crossed products under dynamical conditions (almost finiteness, dynamical
comparison, tracial amenability) even for nonamenable acting groups. References:
[Crossed product C*-algebra](https://en.wikipedia.org/wiki/Crossed_product),
[Dynamical comparison & Z-stability, Adv. Math. 2024](https://doi.org/10.1016/j.aim.2023.109471).

---

## Core concept 3: Amenability and property (T)

![Entropy/probability](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_902f2b4e53eae6a15e3ff4ed40214f2f_topic4b-dsc_2097.jpg)

### Level 0 — High school
Some groups are "easygoing" (you can average over them in a consistent way) and
some are "rigid" (they resist small deformations and approximations). These two
extremes behave very differently and lead to very different geometry.

### Level 1 — Bachelor
A group $G$ is **amenable** if it admits a finitely additive, left-invariant
probability measure (mean) on all subsets — equivalently Følner sets exist
(almost-invariant finite sets). Abelian and solvable groups are amenable; the free
group $F_2$ is **not** (Banach–Tarski lives here). **Kazhdan's property (T)** is an
opposite rigidity: the trivial representation is isolated in the unitary dual, so
$G$ has "no almost-invariant vectors". $SL_3(\mathbb{Z})$ has (T); $SL_2(\mathbb{Z})$
does not.

### Level 2 — Master
These properties are detected and refined through **operator algebras**: nuclearity
of $C^*_r(G)$ characterises amenability (Lance); property (T) and the **Haagerup
property** have spectral-gap and a-T-menability formulations. MM studies them via
**invariant percolation** and **Roe algebras** (coarse geometry), and via finite
approximation (soficity, quasidiagonality). Reference:
[Amenable group](https://en.wikipedia.org/wiki/Amenable_group),
[Kazhdan's property (T)](https://en.wikipedia.org/wiki/Kazhdan%27s_property_(T)).

---

## Core concept 4: Entropy and orbit equivalence

### Level 0 — High school
Take a system that evolves by repeating a symmetry over and over. "Entropy"
measures how unpredictable or complex this evolution is. Two systems can look
different but secretly be re-labellings of each other — that is orbit equivalence.

### Level 1 — Bachelor
A measure-preserving action of $G$ on a probability space $(X,\mu)$ has a numerical
invariant, **(Kolmogorov–Sinai) entropy**, measuring information produced per step.
Two actions are **orbit equivalent** if there is a measure isomorphism carrying
orbits to orbits. Ornstein theory: for $\mathbb{Z}$, entropy is a *complete*
invariant for Bernoulli shifts.

### Level 2 — Master
MM (Kerr, Mukherjee) advances **Shannon orbit equivalence**, **sofic/Rokhlin
entropy** for actions of general amenable/sofic groups, and rigidity of Bernoulli
actions. A second strand develops **noncommutative cyclotomy** to decide when an
algebraic action of an amenable/sofic group has zero entropy, and uses
**group-invariant percolation** to probe property (T) / Haagerup through the
operator-algebraic lens of **Roe algebras**. References:
[Measure-preserving dynamical system](https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system),
[Orbit equivalence](https://en.wikipedia.org/wiki/Orbit_equivalence).

---

## Core concept 5: Algebraic groups, Lie groups and Bruhat–Tits buildings

![Algebraic/Lie groups](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_b3b53e1d9d46097b7acfc75ad1268af4_topic4c-dsc_2064.jpg)

### Level 0 — High school
Beyond finite symmetry there are *continuous* symmetries — like all rotations of a
sphere, which form a smooth, flowing family. These richer symmetry objects come
with their own geometric "skeletons" that help us understand them.

### Level 1 — Bachelor
A **Lie group** is a group that is also a smooth manifold with smooth operations
(e.g. $SO(3)$, $GL_n(\mathbb{R})$); its tangent space at the identity is a **Lie
algebra** $\mathfrak{g}$, capturing the group infinitesimally via the exponential
map. An **algebraic group** is a group defined by polynomial equations (e.g.
$SL_n$ as a variety). Over the $p$-adic numbers $\mathbb{Q}_p$ one gets $p$-adic
Lie groups like $GL_n(\mathbb{Q}_p)$.

### Level 2 — Master
For a reductive group $G$ over a $p$-adic field, the **Bruhat–Tits building** is a
contractible CAT(0) simplicial complex on which $G$ acts, encoding its maximal
compact subgroups and parahoric structure — the combinatorial geometry behind
smooth representation theory and the local Langlands programme (cf. Topic 2). MM's
unit (Schneider, Hellmann, Hartl, Lourenço, Kramer, Böhm) studies smooth mod-$p$
and $p$-adic representations, moment-map/GIT flows on real reductive groups, and
polyhedral compactifications of buildings. References:
[Lie group](https://en.wikipedia.org/wiki/Lie_group),
[Bruhat–Tits building](https://en.wikipedia.org/wiki/Building_(mathematics)).

---

**Further reading**
- Brown, *Cohomology of Groups*; de la Harpe, *Topics in Geometric Group Theory*
- Brown–Ozawa, *C\*-algebras and Finite-Dimensional Approximations*
- Kerr–Li, *Ergodic Theory: Independence and Dichotomies*
