# Topic 1 — K-groups and Cohomology

> **Objective (MM "O1"): Push frontiers in K-theory and attack open questions in topology.**
> We explore various cohomology theories and their utility across algebra, geometric
> topology and operator algebras. Central among them is **K-theory**, studied from
> several perspectives: new computations of K-groups, new cases of the
> **Farrell–Jones conjecture**, the **Borel conjecture** on topological rigidity,
> curvature bounds on manifolds, and the classification of C\*-algebras.

Source: [T1: K-groups and cohomology](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_kgroups-cohomology.shtml)

The topic is organised into three research units:
1. **Cohomology theories in arithmetic geometry** (coherent, étale, prismatic, topological periodic homology).
2. **Algebraic K-theory and stable $\infty$-categories**.
3. **Topological K-theory and group cohomology**.

The guiding idea: *attach computable algebraic invariants to geometric or
algebraic objects* (schemes, stacks, C\*-algebras, stable $\infty$-categories,
topological spaces), so that hard geometric questions become algebra.

---

## Core concept 1: Cohomology

![Blackboard](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_d90704dfa96d542ee3684c872eac0e51_topic1a-dsc_2265.jpg)

### Level 0 — High school
Imagine you want to tell shapes apart without touching them: a ball, a doughnut,
a pretzel. A doughnut has **one hole**, a pretzel has **two**. Cohomology is a
careful way of *counting holes of different kinds* (gaps you can loop a string
around, hollow cavities, etc.) and recording the answer as a list of numbers. If
two shapes give different lists, they are genuinely different shapes.

### Level 1 — Bachelor
Cohomology assigns to a space $X$ a sequence of abelian groups $H^0(X), H^1(X),
H^2(X), \dots$ . For singular cohomology with coefficients in a field, $\dim
H^k(X)$ is the $k$-th **Betti number**, counting independent $k$-dimensional
"holes". For the $n$-sphere,
$$
H^k(S^n) \cong \begin{cases} \mathbb{Z} & k = 0 \text{ or } k = n,\\ 0 & \text{otherwise.}\end{cases}
$$
Cohomology is a **functor**: a continuous map $f\colon X\to Y$ induces
$f^*\colon H^k(Y)\to H^k(X)$, so it converts topology into algebra. Cup product
makes $H^\bullet(X)$ a ring, a finer invariant than the Betti numbers alone.

### Level 2 — Master
Cohomology is best understood as a **(generalised) cohomology theory**: a
sequence of contravariant functors satisfying the Eilenberg–Steenrod axioms
(homotopy invariance, excision, long exact sequence of a pair), with the
dimension axiom dropped for *generalised* theories. Representable by a
spectrum $E$ via $E^n(X) = [X, \Omega^\infty \Sigma^n E]$ (Brown
representability). In arithmetic geometry one replaces topological spaces by
schemes and uses Grothendieck's site-theoretic theories: **étale**,
**crystalline**, and the more recent **prismatic** cohomology of
Bhatt–Scholze, which interpolates between $p$-adic étale and crystalline
cohomology. These are the structural backbone of the Langlands programme and of
Deninger's conjectural dynamical/cohomological interpretation of zeta functions.
See [Wikipedia: Cohomology](https://en.wikipedia.org/wiki/Cohomology),
[prismatic cohomology](https://en.wikipedia.org/wiki/Prismatic_cohomology).

---

## Core concept 2: K-theory (algebraic and topological)

![Blackboard K-theory](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_4233243c48fe30e25408362e9cb3e162_topic1b-dsc_2256.jpg)

### Level 0 — High school
Think of all the ways you can lay down arrows (little vectors) smoothly over a
shape — for example combing the hair on a ball. Some arrangements can be undone
to nothing, others are "stuck". K-theory bundles up all these arrangements and
turns them into a number system you can add and subtract with. It measures how
twisted such families can be.

### Level 1 — Bachelor
Topological K-theory starts from **vector bundles** over a space $X$. Isomorphism
classes of bundles form a monoid under $\oplus$; the **Grothendieck group**
completion (formally adding inverses, like building $\mathbb{Z}$ from
$\mathbb{N}$) gives
$$
K^0(X) = \operatorname{Groth}\bigl(\{\text{vector bundles}/X\},\ \oplus\bigr).
$$
For rings, the analogue uses finitely generated projective modules: $K_0(R)$. The
next group $K_1(R) = GL(R)^{\mathrm{ab}} = GL(R)/[GL(R),GL(R)]$. **Bott
periodicity** for complex topological K-theory says $K^n(X)\cong K^{n+2}(X)$, a
striking simplification with no analogue in ordinary cohomology.

### Level 2 — Master
Algebraic K-theory is, in the modern view (Waldhausen, Blumberg–Gepner–Tabuada),
an invariant of **stable $\infty$-categories**: $K\colon \mathrm{Cat}^{\mathrm{ex}}_\infty
\to \mathrm{Sp}$, the universal additive (or, after Calmès–Dotto–Harpaz–…–Nikolaus,
"Poincaré"/Hermitian) invariant, defined via the $S_\bullet$-construction with
homotopy groups $K_n$. Trace methods (Dennis trace to $THH$, cyclotomic structure,
$TC$ via Nikolaus–Scholze) compute $K$ in terms of topological cyclic homology;
this drives recent computations such as $K(\mathbb{Z}/p^n)$. The MM unit links
these structural advances to the categorical $p$-adic Langlands programme and to
the classification of $C^*$-algebras via topological K-theory (the K-theoretic
invariant in the Elliott programme). References:
[algebraic K-theory](https://en.wikipedia.org/wiki/Algebraic_K-theory),
[K(Z/pⁿ), Antieau–Krause–Nikolaus, arXiv:2405.04329](https://arxiv.org/abs/2405.04329).

---

## Core concept 3: The Farrell–Jones conjecture

### Level 0 — High school
Some mathematical objects attached to a group are very hard to compute directly.
This conjecture says: you can always build the hard global answer out of easy
local pieces — namely the small, simple subgroups. Like reconstructing a whole
mosaic if you know just a few special tiles.

### Level 1 — Bachelor
For a group $G$, the conjecture predicts that the algebraic K-theory (and
L-theory) of the group ring $R[G]$ is **assembled** from the K-theory of its
*virtually cyclic* subgroups via an assembly map
$$
H^G_n\bigl(\underline{\underline{E}}G;\, \mathbf{K}_R\bigr)\ \xrightarrow{\ \cong\ }\ K_n(R[G]),
$$
an isomorphism. In plain terms: a hard invariant of an infinite group is computed
by an equivariant homology theory evaluated on a classifying space for the family
of virtually cyclic subgroups.

### Level 2 — Master
The conjecture is an isomorphism statement for the assembly map relative to the
family $\mathcal{VCyc}$, with deep consequences: it implies the **Borel
conjecture** (topological rigidity of aspherical manifolds of dimension $\ge 5$),
the **Novikov conjecture** (homotopy invariance of higher signatures), and the
**Kaplansky idempotent conjecture** for torsion-free $G$. Bartels–Lück and
collaborators established it for large classes (hyperbolic groups, CAT(0)
groups, lattices, mapping class groups) using controlled topology and flow-space
methods; recent MM work extends inheritance properties and the case of
**Hecke algebras of reductive $p$-adic groups**. References:
[Farrell–Jones conjecture](https://en.wikipedia.org/wiki/Farrell%E2%80%93Jones_conjecture),
[Bartels–Lück–Reich survey](https://arxiv.org/abs/2306.01510).

---

## Core concept 4: The Borel conjecture and topological rigidity

### Level 0 — High school
If two rubbery shapes have the *same kind of fundamental loops*, are they really
the same shape? For a special well-behaved family the answer is conjectured to be
yes — they cannot be secretly different.

### Level 1 — Bachelor
A closed manifold $M$ is **aspherical** if its universal cover is contractible
(equivalently $\pi_k(M)=0$ for $k\ge 2$). The Borel conjecture states: two closed
aspherical manifolds with isomorphic fundamental groups $\pi_1$ are
**homeomorphic**, and moreover any homotopy equivalence is homotopic to a
homeomorphism. This is a topological analogue of Mostow rigidity (which is
geometric).

### Level 2 — Master
Borel rigidity is measured by the **structure set** $\mathcal{S}^{\mathrm{TOP}}(M)$
of the surgery exact sequence
$$
\cdots \to L_{n+1}(\mathbb{Z}\pi_1) \to \mathcal{S}^{\mathrm{TOP}}(M) \to
\mathcal{N}(M) \to L_n(\mathbb{Z}\pi_1).
$$
Triviality of $\mathcal{S}^{\mathrm{TOP}}(M)$ (so rigidity) follows from the
$L$-theoretic Farrell–Jones isomorphism plus vanishing of relevant
$\widetilde{K}_0$ and Whitehead groups. Thus K- and L-theory computations feed
directly into the manifold classification. See
[Borel conjecture](https://en.wikipedia.org/wiki/Borel_conjecture).

---

## Core concept 5: C\*-algebras and their classification

![Blackboard topology](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_67cb5716e96f6af9a50e3cc8c9905ad8_topic1c-dsc_2278-2.jpg)

### Level 0 — High school
Quantum physics needs a number system where multiplication order matters
($a\times b \ne b\times a$). C\*-algebras are such systems of "operators".
K-theory gives each one a fingerprint; mathematicians want to prove that the
fingerprint alone tells them apart.

### Level 1 — Bachelor
A **C\*-algebra** is a complex Banach algebra $A$ with an involution $*$
satisfying the C\*-identity $\lVert a^*a\rVert = \lVert a\rVert^2$. Model example:
$A = B(H)$, bounded operators on a Hilbert space, or $C(X)$, continuous functions
on a compact space (the commutative case — by Gelfand duality *every* commutative
unital C\*-algebra is $C(X)$). Topological K-theory $K_0(A), K_1(A)$ are computable
invariants and form the core of classification.

### Level 2 — Master
The **Elliott classification programme** seeks to classify separable, simple,
nuclear C\*-algebras by an invariant (the *Elliott invariant*: ordered K-theory,
trace simplex, pairing). The landmark result classifies those that are
$\mathcal{Z}$-stable and satisfy the UCT via $K$-theory and traces; **nuclear
dimension** (Winter et al.) is the key regularity property. MM's unit studies
existence/classification of **Cartan subalgebras** in simple nuclear
C\*-algebras (linking to groupoid models and topological dynamics) and uses
topological K-theory as an invariant of operator algebras, tied back to group
cohomology of arithmetic groups. References:
[C*-algebra](https://en.wikipedia.org/wiki/C*-algebra),
[Nuclear dimension of simple C*-algebras (Castillejos et al., 2021)](https://doi.org/10.1007/s00222-020-01013-1).

---

## How the pieces fit

```
        geometric/algebraic object
        (scheme, space, C*-algebra, ∞-category)
                     │  attach invariant
                     ▼
         cohomology  ◄─────►  K-theory
          (étale,             (algebraic / topological)
           prismatic)              │
                     ┌─────────────┼──────────────┐
                     ▼             ▼              ▼
              Langlands      Farrell–Jones    C*-classification
              programme       ⇒ Borel/Novikov   (Elliott)
```

**Further reading**
- Bartels–Lück, *Algebraic K-theory of reductive p-adic groups* — [arXiv:2306.03452](https://arxiv.org/abs/2306.03452)
- Antieau–Krause–Nikolaus, *On the K-theory of $\mathbb{Z}/p^n$* — [arXiv:2405.04329](https://arxiv.org/abs/2405.04329)
- Atiyah, *K-theory* (classic textbook); Weibel, *The K-book* (free online)
