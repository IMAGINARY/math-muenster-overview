# Topic 10 — Deep Learning and Surrogate Methods

> **Objective (MM "O8"): develop innovative simulation tools by combining model- and data-based approaches.**
> We advance the fundamental mathematical understanding of artificial neural
> networks (e.g. designing and rigorously analysing **stochastic gradient descent**
> for training). Combining data-driven machine learning with **model order
> reduction**, we develop fully **certified multi-fidelity** frameworks for
> parametrised PDEs, higher-order deep-learning schemes for parametric SPDEs, and
> cost-optimal surrogates for PDE-constrained optimisation and inverse problems.

Source: [T10: Deep learning and surrogate methods](https://www.uni-muenster.de/MathematicsMuenster/research/programme/topic_deepl-surrogate-methods.shtml)

Three research units:
1. **Training of deep neural networks** (convergence of SGD/Adam).
2. **Learning methods for PDEs** (deep approximations, SPDEs, certification).
3. **Surrogate methods for optimal control and inverse problems** (multi-fidelity).

---

## Core concept 1: Artificial neural networks

![Training DNNs](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_52d9f1b955f3710174eec1997e66a0aa_topic10a-dsc_3040.jpg)

### Level 0 — High school
A neural network is a flexible mathematical "function machine": you feed it inputs,
it produces outputs, and by adjusting many internal dials you can make it imitate
almost any pattern from examples. It is the engine behind modern AI.

### Level 1 — Bachelor
A **feedforward neural network** with $L$ layers is a composition of affine maps and
a nonlinear **activation** $\sigma$ (e.g. ReLU $\sigma(x)=\max(x,0)$):
$$
\Phi_\theta(x) = A_L\,\sigma\big(A_{L-1}\,\sigma(\cdots \sigma(A_1 x + b_1)\cdots) + b_{L-1}\big) + b_L,
$$
with parameters $\theta=(A_i,b_i)$. The **universal approximation theorem**: even
one hidden layer can approximate any continuous function on a compact set to
arbitrary accuracy (given enough width).

### Level 2 — Master
Quantitative theory asks about **expressivity vs. cost**: depth can yield
exponential savings, and for certain high-dimensional PDE solution operators deep
networks **overcome the curse of dimensionality** (approximation error and parameter
count grow only polynomially in $d$) — but MM (Grohs–Jentzen) also proves **lower
bounds** showing shallow networks *cannot*. References:
[Artificial neural network](https://en.wikipedia.org/wiki/Artificial_neural_network),
[Universal approximation theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem),
[ANNs overcome the curse of dimensionality for Black–Scholes PDEs, Memoirs AMS 2023](https://doi.org/10.1090/memo/1410).

---

## Core concept 2: Stochastic gradient descent (and its analysis)

### Level 0 — High school
To train the network you tweak its dials to reduce its mistakes, step by step,
always heading "downhill" on an error landscape. To go fast you estimate the
downhill direction from a small random handful of examples each step. That is
stochastic gradient descent.

### Level 1 — Bachelor
Training minimises a **loss** $\mathcal{L}(\theta)=\frac1N\sum_{i=1}^N
\ell(\Phi_\theta(x_i),y_i)$. **Gradient descent** updates
$\theta_{k+1}=\theta_k-\eta\,\nabla\mathcal{L}(\theta_k)$. **Stochastic gradient
descent (SGD)** replaces the full gradient by an estimate from a random mini-batch
$B_k$:
$$
\theta_{k+1} = \theta_k - \eta_k\,\nabla_\theta \Big(\tfrac1{|B_k|}\sum_{i\in B_k}\ell(\Phi_\theta(x_i),y_i)\Big).
$$
Cheap per step, noisy, and widely successful — but its convergence is not obvious.

### Level 2 — Master
The loss landscape is **non-convex**, with saddle points and many minima, so
guaranteeing convergence (with rates) is a hard open problem. MM (Jentzen, Dereich,
Riekert, Kassing) proves convergence/non-convergence results using **martingale
theory, Lyapunov functions, real algebraic geometry, and Łojasiewicz inequalities**:
existence of minimisers in (shallow residual) ReLU landscapes, escape from saddle
points, **convergence rates for Adam**, and—strikingly—**non-convergence of Adam/SGD
to global minimisers** for non-vanishing learning rates. References:
[Stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent),
[Convergence rates for the Adam optimizer, arXiv:2407.21078](https://arxiv.org/abs/2407.21078).

---

## Core concept 3: Deep learning methods for (S)PDEs

![Learning methods for PDEs](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_da79c602bd383159508d0bbdaa19b0f7_topic10b-tafel-dsc_3111.jpg)

### Level 0 — High school
Classical methods solve a physics equation by chopping space into a fine grid —
impossible when there are too many dimensions. Instead, train a neural network to
*be* the solution. The equation itself becomes the teacher.

### Level 1 — Bachelor
A network $\Phi_\theta(x,t)$ is trained so that it satisfies a PDE. In
**physics-informed neural networks (PINNs)** the loss penalises the PDE residual and
boundary/initial conditions:
$$
\mathcal{L}(\theta)=\big\|\partial_t\Phi_\theta - \mathcal{D}[\Phi_\theta]\big\|^2
+ \big\|\Phi_\theta - g\big\|^2_{\partial}.
$$
For many high-dimensional parabolic PDEs there are stochastic (Feynman–Kac)
reformulations that let networks learn the solution from simulated paths
(**deep BSDE** methods).

### Level 2 — Master
MM (Jentzen, Ohlberger, Weber, Rave, Engwer) designs and *analyses* deep
approximation schemes with **error estimates and certification**, including
low-regularity **[stochastic PDEs](../GLOSSARY.md#stochastic-pde)** via **[rough paths](../GLOSSARY.md#rough-paths) / regularity structures**
combined with ML (higher-order schemes), and **deep operator learning** (learning
solution operators $\mathcal{G}:\mu\mapsto u_\mu$ between function spaces). Emphasis:
provable accuracy, not just empirical performance. References:
[Physics-informed neural networks](https://en.wikipedia.org/wiki/Physics-informed_neural_networks),
[Overview on ML methods for PDEs (PINNs to operator learning), arXiv:2408.13222](https://arxiv.org/abs/2408.13222).

---

## Core concept 4: Surrogate models and multi-fidelity / certification

![Surrogates for control & inverse problems](https://www.uni-muenster.de/imperia/md/images/MathematicsMuenster/research/fittosize_528_396_99ed9ec3c12e2168737088ba12a83531_topic10c-tafel-dsc_3129.jpg)

### Level 0 — High school
Use a fast rough estimator most of the time and an expensive accurate one only
occasionally, then blend them so the final answer is both cheap *and* trustworthy.
A "certified" surrogate even tells you how wrong it might be.

### Level 1 — Bachelor
A **surrogate model** $\hat{u}\approx u$ is a cheap stand-in for an expensive
simulation. A **multi-fidelity** method combines a few high-fidelity (accurate,
costly) evaluations with many low-fidelity (cheap, approximate) ones to reach a
target accuracy at minimal total cost. **Certified** means equipped with a rigorous,
computable error bound $\|u-\hat u\|\le \Delta(\mu)$.

### Level 2 — Master
MM (Ohlberger, Schindler, Kleikamp, Wirth, Jentzen) builds **hierarchical,
adaptive RB–ML–ROM** surrogates: reduced-basis / model-order-reduction backbones
(Topic 9) augmented by machine-learned (e.g. deep-kernel) components, with
*a posteriori* certification, deployed for **PDE-constrained optimal control** and
**inverse problems**. Prior knowledge enters as regularisation; cost-optimal
multi-fidelity frameworks balance the fidelities. References:
[Surrogate model](https://en.wikipedia.org/wiki/Surrogate_model),
[Certified hierarchical adaptive RB-ML-ROM surrogate, SIAM J. Sci. Comput. 2023](https://doi.org/10.1137/22M1493318).

---

## Core concept 5: Inverse problems

### Level 0 — High school
A CT scanner never sees inside you directly — it measures shadows and reconstructs
the interior. Working backwards from effects to hidden causes is an inverse problem,
and small measurement errors can blow up, so it must be done carefully.

### Level 1 — Bachelor
A forward model $F$ maps unknown parameters $x$ to data $y=F(x)$. An **inverse
problem** recovers $x$ from noisy $y$. These are typically **ill-posed** (Hadamard):
solutions may not exist, be non-unique, or depend unstably on data. **Regularisation**
(e.g. Tikhonov: minimise $\|F(x)-y\|^2 + \alpha\|x\|^2$) restores stability.

### Level 2 — Master
MM integrates **data-driven and model-based** approaches: learning the forward
operator or dynamics from data while encoding **prior knowledge as regularisation**,
and using certified surrogates to make repeated forward solves (needed in iterative
inversion / optimal control) affordable. This unifies Topics 9 and 10 around
high-dimensional, PDE-constrained optimisation. References:
[Inverse problem](https://en.wikipedia.org/wiki/Inverse_problem),
[Regularization (mathematics)](https://en.wikipedia.org/wiki/Regularization_(mathematics)).

---

**Further reading**
- Jentzen–Kuckuck–von Wurstemberger, *Mathematical Introduction to Deep Learning* — [arXiv:2310.20360](https://arxiv.org/abs/2310.20360)
- Goodfellow–Bengio–Courville, *Deep Learning* (MIT Press, free online)
- Engl–Hanke–Neubauer, *Regularization of Inverse Problems*
