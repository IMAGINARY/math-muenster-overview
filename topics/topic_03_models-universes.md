# Topic 3 — Models and Universes

> **Objective (part of MM "O3"): build models and study their theories and external properties.**
> We develop and explore models encompassing various strengths and properties to
> address questions across algebra, geometry, and set theory, and analyse the
> interplay of **determinacy hypotheses** with strong **large cardinal hypotheses**.

Source: [T3: Models and universes](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_models-universes.shtml)

Two research units:
1. **Model theory** — classification of groups/fields under model-theoretic
   assumptions; automorphism groups of homogeneous structures.
2. **Set theory** — inner model theory, forcing axioms, axiom of determinacy,
   large cardinals, $\mathbb{P}_{\max}$-style forcing.

This topic studies the **foundations**: what mathematical structures can exist,
which statements are provable, and which require new axioms.

---

## Core concept 1: Model theory and first-order structures

![Model theory](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_f530249a1fbffd5eb96311fb45ff0d95_topic3a-dsc_3792-bearbeitet2.jpg)

### Level 0 — High school
A "rule book" (axioms) can be obeyed by different "worlds". For example "every
element has an opposite" is obeyed by the integers and by many other systems.
Model theory studies all the worlds that obey a given rule book, and what they
must have in common.

### Level 1 — Bachelor
A **structure** $\mathcal{M} = (M; \text{functions}, \text{relations},
\text{constants})$ interprets a first-order **language**. It is a **model** of a
theory $T$ (a set of sentences) if every sentence of $T$ is true in $\mathcal{M}$,
written $\mathcal{M}\models T$. Key early theorems:
- **Compactness**: if every finite subset of $T$ has a model, so does $T$.
- **Löwenheim–Skolem**: a theory with an infinite model has models of every
  infinite cardinality.

Example: the theory of algebraically closed fields of characteristic $0$ is
*complete* — any two such fields satisfy exactly the same first-order sentences.

### Level 2 — Master
Modern model theory classifies theories by **tameness** (the *stability
hierarchy*: stable $\subset$ NIP / simple $\subset$ …). MM's unit attacks
classification conjectures:
- **Algebraicity (Cherlin–Zilber) conjecture**: every simple $\omega$-stable
  (more precisely, simple group of finite Morley rank) is an algebraic group over
  an algebraically closed field.
- **Stable fields conjecture**: every infinite stable field is separably closed.
- Work on **NIP henselian fields** (Anscombe–Jahnke) and **Ax–Kochen–Ershov
  principles**. Tools include independence/forking, Morley rank, and valuation
  theory. References: [Model theory](https://en.wikipedia.org/wiki/Model_theory),
  [Group of finite Morley rank](https://en.wikipedia.org/wiki/Group_of_finite_Morley_rank).

---

## Core concept 2: Homogeneous structures and Fraïssé limits

### Level 0 — High school
Some objects look "the same from everywhere" — like an infinite perfectly regular
network where every point has an identical view. You can build such an object by
gluing together all its small finite pieces in the most generic way.

### Level 1 — Bachelor
A countable structure is **(ultra)homogeneous** if every isomorphism between
finite substructures extends to an automorphism of the whole. **Fraïssé's
theorem**: a class $\mathcal{K}$ of finite structures with the amalgamation
property has a unique countable homogeneous limit, its **Fraïssé limit**. The
**random graph** (Rado graph) is the Fraïssé limit of all finite graphs; the
rationals $(\mathbb{Q},<)$ are the Fraïssé limit of finite linear orders.

### Level 2 — Master
The **automorphism group** $\mathrm{Aut}(\mathcal{M})$ of a Fraïssé limit is a
non-archimedean Polish group; its dynamics (extreme amenability,
Ramsey theory via Kechris–Pestov–Todorcevic correspondence) link model theory to
**descriptive set theory**, **ergodic theory**, and **C\*-algebras**. MM
(Kwiatkowska et al.) studies **projective Fraïssé limits** (e.g. Ważewski
dendrites, the random poset) and stationary weak independence relations.
Reference: [Fraïssé limit](https://en.wikipedia.org/wiki/Fra%C3%AFss%C3%A9_limit).

---

## Core concept 3: Universes of set theory and forcing

![Set theory](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_45ee08296d9b9d695c766e479fc825c0_interaktion-debondt-schindler-dsc_2581.jpg)

### Level 0 — High school
All of mathematics can be built from "sets". But there is not just one possible
universe of sets — there are many, and some questions (like exactly how many real
numbers there are) get *different answers* in different universes. Set theorists
build and compare these universes.

### Level 1 — Bachelor
The standard axioms are **ZFC** (Zermelo–Fraenkel + Choice). Gödel showed some
statements are **independent**: neither provable nor refutable. The prime example
is the **Continuum Hypothesis** (CH): $2^{\aleph_0} = \aleph_1$ (no cardinality
strictly between $\mathbb{N}$ and $\mathbb{R}$). **Forcing** (Cohen) is a method to
build a new model $M[G]$ from a model $M$ by adjoining a "generic" object $G$,
controlling which sentences become true — used to make CH true or false at will.

### Level 2 — Master
MM's set-theory unit (Schindler et al.) works at the interface of:
- **Inner model theory** — canonical fine-structural models ($L$, and
  $L[\vec{E}]$ with extender sequences) approximating $V$ and calibrating
  large-cardinal strength.
- **Forcing axioms** — Martin's Maximum $\mathrm{MM}^{++}$ and its relation to
  Woodin's axiom $(*)$; the celebrated Asperó–Schindler theorem
  $\mathrm{MM}^{++}\Rightarrow (*)$.
- $\mathbb{P}_{\max}$ forcing over models of determinacy to force fragments of
  $\mathrm{MM}$ and analyse the **nonstationary ideal** on $\omega_1$.
References: [Forcing](https://en.wikipedia.org/wiki/Forcing_(mathematics)),
[Asperó–Schindler, MM⁺⁺ ⇒ (∗), Annals 2021](https://doi.org/10.4007/annals.2021.193.3.3).

---

## Core concept 4: Large cardinals

### Level 0 — High school
Infinity comes in many sizes. "Large cardinals" are sizes of infinity so vast
that their mere existence cannot be proved from the usual rules — yet assuming
them settles many otherwise-undecidable questions far below.

### Level 1 — Bachelor
Beyond $\aleph_0, \aleph_1, \dots$ lie cardinals with strong **closure/reflection**
properties: **inaccessible**, **measurable** (carrying a nontrivial
$\kappa$-complete ultrafilter), **Woodin**, **supercompact**. They form a linearly
ordered hierarchy of **consistency strength**: assuming a larger cardinal proves
the consistency of theories with smaller ones, so by Gödel's incompleteness their
existence is unprovable in ZFC.

### Level 2 — Master
A measurable cardinal $\kappa$ is equivalent to the existence of a nontrivial
elementary embedding $j\colon V\to M$ with critical point $\kappa$; stronger
notions strengthen the closure of $M$. **Woodin cardinals** are the pivot for the
theory of determinacy: $n$ Woodins give $\boldsymbol{\Pi}^1_{n+1}$-determinacy,
and infinitely many give $\mathrm{AD}^{L(\mathbb{R})}$. Reference:
[Large cardinal](https://en.wikipedia.org/wiki/Large_cardinal).

---

## Core concept 5: The Axiom of Determinacy

### Level 0 — High school
Imagine an infinite game where two players alternately pick numbers forever. One
of them is declared the winner by some rule. Determinacy says: in such games one
side always has a guaranteed winning strategy. Surprisingly, whether this holds
depends on which mathematical universe you live in.

### Level 1 — Bachelor
For $A\subseteq \mathbb{N}^{\mathbb{N}}$, the game $G_A$ has players alternately
choosing naturals to build $x\in\mathbb{N}^{\mathbb{N}}$; player I wins iff $x\in
A$. $A$ is **determined** if one player has a winning strategy. The **Axiom of
Determinacy (AD)** asserts *every* $A$ is determined. AD contradicts the full
axiom of choice, but **all Borel sets are determined** (Martin, in ZFC).

### Level 2 — Master
AD holds in $L(\mathbb{R})$ under sufficiently many Woodin cardinals
(Martin–Steel–Woodin), making **$\mathrm{AD}^{L(\mathbb{R})}$** a benchmark. MM's
unit studies the interplay of AD with large cardinals and combinatorial
principles, including **Chang-type models** of determinacy and forcing strong
fragments of Martin's Maximum by $\mathbb{P}_{\max}$ over them. Determinacy
imposes strong **regularity** (Lebesgue measurability, perfect set property, Baire
property) on definable sets of reals. Reference:
[Axiom of determinacy](https://en.wikipedia.org/wiki/Axiom_of_determinacy).

---

**Further reading**
- Marker, *Model Theory: An Introduction* (Springer GTM 217)
- Jech, *Set Theory* (3rd ed.); Kanamori, *The Higher Infinite* (large cardinals)
- Schindler, *Set Theory: Exploring Independence and Truth* (Springer)
