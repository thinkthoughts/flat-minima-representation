# Representation Demystifies Flat Minima

<p align="center">
  <img src="figures/2605-05209.png" width="900">
</p>

**Notebooks and experiments inspired by arXiv:2605.05209**, exploring flat minima, Hessian geometry, reparameterization, and why representation may matter more than sharpness when explaining neural network generalization.

## Core Question

Classical deep learning theory often associates **flat minima** with better generalization.

But what happens when the same computation is expressed in a different parameterization?

If sharpness changes while predictions remain identical, is sharpness measuring the computation—or merely its representation?

This repository builds a sequence of toy experiments investigating that question.

---

## Engineering Statement

> Curvature measures geometry.
>
> Geometry depends on representation.
>
> Computation survives representation.
>
> Scientific explanations should identify what survives.

---

## Repository Roadmap

| Notebook | Focus                                | Colab |
| -------- | ------------------------------------ | ----- |
| 00       | Context and paper overview           | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/00_context.ipynb">📓</a>  |
| 07       | Classical flat-minima hypothesis     | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/07_flat_vs_sharp.ipynb">📓</a>    |
| 13       | Hessian geometry and curvature       | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/13_hessian_geometry.ipynb">📓</a>    |
| 17       | Reparameterization changes sharpness | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/17_reparameterization.ipynb">📓</a>    |
| 23       | Same function different sharpness       | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/23_same_function_different_sharpness.ipynb">📓</a>    |
| 29       | Correlation versus causation               | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/29_correlation_vs_causation.ipynb">📓</a>    |
| 37       | Representation matters   | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/37_representation_matters.ipynb">📓</a>    |

---


## Notebook Sequence

00 — Context

Introduces the paper and the central question:

Does sharpness explain generalization, or does it depend on representation?

07 — Flat vs Sharp

Builds the classical intuition behind flat minima.

Key ideas:

Flat minima have smaller curvature.
Sharp minima have larger curvature.
Hessians measure local curvature.

Classical hypothesis:

Flat minima → robustness → better generalization.

13 — Hessian Geometry

Introduces the geometric language used throughout the paper.

Experiments visualize:

Curvature families
Eigenvalues
Eigenvectors
Isotropic and anisotropic bowls

Key takeaway:

Sharpness is a geometric measurement derived from Hessian curvature.

17 — Reparameterization

Shows that the same computation can appear flat or sharp depending on coordinates.

Key takeaway:

Measured sharpness depends on parameterization.

23 — Same Function, Different Sharpness

Constructs equivalent functions whose predictions remain identical while Hessian measurements change substantially.

Key takeaway:

Sharpness can vary even when computation does not.

29 — Correlation vs Causation

Investigates whether observed sharpness-generalization correlations survive representation changes.

Key takeaway:

Correlation alone does not establish sharpness as a causal explanation.

37 — Representation Matters

Synthesizes the repository.

Distinguishes:

Computation

Function
Predictions
Test error

from

Representation

Coordinates
Parameter norms
Hessian sharpness
Local curvature

Key takeaway:

Computation survives representation changes. Geometry may not.

## Figures

Generated figures are saved to:

```text
figures/
```

Structured outputs are saved to:

```text
results/
```

Each notebook also exports downloadable ZIP archives containing generated figures and summaries.

---

## Paper

**Representation Demystifies Flat Minima**

Source paper:

* arXiv:2605.05209

This repository is an educational and computational companion exploring the paper's ideas through simplified experiments and visualizations.

---

## Citation

If you use these notebooks, please cite the original paper and link back to this repository.
