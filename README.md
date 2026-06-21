# Representation Demystifies Flat Minima

<p align="center">
  <img src="figures/2605-05209.png" width="900">
</p>

**Notebooks and experiments inspired by arXiv:2605.05209**, exploring flat minima, Hessian geometry, reparameterization, Sharpness-Aware Minimization (SAM), and function-space robustness.

## Core Question

Classical deep learning theory often associates **flat minima** with better generalization.

But what happens when the same computation is expressed in a different parameterization?

If sharpness changes while predictions remain identical, is sharpness measuring the computation—or merely its representation?

This repository builds a sequence of experiments investigating that question.

The central result is:

> Flatness is representation-dependent.
>
> Computation is not.
>
> Any causal explanation of generalization must survive reparameterization.

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

| Notebook | Focus | Colab |
|----------|--------|--------|
| 00 | Context and paper overview | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/00_context.ipynb">📓</a> |
| 07 | Classical flat-minima hypothesis | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/07_flat_vs_sharp.ipynb">📓</a> |
| 13 | Hessian geometry and curvature | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/13_hessian_geometry.ipynb">📓</a> |
| 17 | Reparameterization changes sharpness | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/17_reparameterization.ipynb">📓</a> |
| 23 | Same function, different sharpness | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/23_same_function_different_sharpness.ipynb">📓</a> |
| 29 | Correlation versus causation | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/29_correlation_vs_causation.ipynb">📓</a> |
| 37 | Representation matters | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/37_representation_matters.ipynb">📓</a> |
| 43 | SAM versus representation | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/43_sam_vs_representation.ipynb">📓</a> |
| 49 | Function-space robustness | <a href="https://colab.research.google.com/github/thinkthoughts/flat-minima-representation/blob/main/notebooks/49_function_space_robustness.ipynb">📓</a> |

---

## Main Findings

### Finding 1 — Sharpness depends on representation

Equivalent parameterizations can produce substantially different Hessian spectra and sharpness measurements.

Sharpness is therefore not invariant under reparameterization.

### Finding 2 — Computation survives representation

Functions, predictions, and test behavior can remain unchanged while geometric measurements vary.

This separates computational properties from representational properties.

### Finding 3 — Correlation is not causation

Observed correlations between flatness and generalization do not establish flatness as the causal mechanism.

Any proposed cause must remain meaningful after reparameterization.

### Finding 4 — SAM may be exploiting a deeper invariant

Sharpness-Aware Minimization often improves generalization, but the experiments suggest its success may not come from minimizing sharpness itself.

Instead, SAM may be steering optimization toward solutions that are more robust in function space.

### Finding 5 — Function-space robustness is a stronger candidate

Function-space behavior survives transformations that invalidate parameter-space sharpness.

This suggests that robustness of the learned function may be a more fundamental explanatory target than local curvature.

---

## Repository Conclusion

The experiments support a simple distinction:

### Representation

* Coordinates
* Parameter norms
* Hessian spectra
* Local curvature
* Flatness measurements

### Computation

* Functions
* Predictions
* Test performance
* Behavioral robustness

Representation can change while computation remains fixed.

Flatness therefore appears to be a property of representation rather than a universal property of computation.

The deeper question is not:

> Why do flat minima generalize?

but:

> What invariant survives reparameterization and predicts generalization?

This repository argues that answer is more likely to be found in function-space behavior than in parameter-space geometry.
