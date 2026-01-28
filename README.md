# CFSpy
--------------------------------------

<div align ="center">

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cfspy)](https://pypi.org/project/cfspy/)
[![PyPI - Version](https://img.shields.io/pypi/v/cfspy)](https://pypi.org/project/cfspy/)
![PyPI - Status](https://img.shields.io/pypi/status/cfspy)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/cfspy?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/cfspy)
[![PyPI - License](https://img.shields.io/pypi/l/cfspy)](https://pypi.org/project/cfspy/)
</div>

Welcome to the documentation of the CFSpy Python package.

## Overview

CFSpy is used for the computation of Chen-Fliess series and their applications in control and reachability theory. This documentation provides a comprehensive guide to using and contributing to the project.

The package provides the following functionalities:

- The list of iterated integrals indexed by words of a certain length or less.
- The list of Lie derivatives indexed by words of a certain length or less.
- A single iterated integral indexed by a given word.
- A single Lie derivative indexed by a given word.
- The symbolic polynomial that represents the Chen-Fliess series for a constant input.

The implementation is based on Chen’s identity, which provides recursive relations between iterated integrals and Lie derivatives, significantly reducing redundant computation.

This package is the first publicly available open‑source implementation of these tools in the Python ecosystem, relying only on NumPy and SymPy for minimal and efficient dependencies.


## What are Chen–Fliess series?

Chen–Fliess series provide an input–output representation of analytic
nonlinear control‑affine systems.  
They express the output as a formal power series whose coefficients are
Lie derivatives of the output function and whose terms are iterated
integrals of the input.

Formally:

```{math}
    F_c[u](t) = \sum_{\eta \in X^*} (c,\eta)\, E_\eta[u](t),
```

where:

- $\eta$ is a word over the alphabet $X = \{x_0,\ldots,x_m\}$,
- $(c,\eta)$ is the coefficient given by a Lie derivative,
- $E_\eta[u](t)$ is the iterated integral associated with $\eta$.

These series play a central role in nonlinear control theory, system
approximation, and operator‑theoretic analysis.

## Why Python?
CFSpy is written in Python to leverage:

- **High performance**: JIT compilation and type specialization enable tight inner loops for iterated integrals and Lie derivatives.
- **Multiple dispatch**: Natural expression of different system types, vector field representations, and numeric backends.
- **Symbolic–numeric synergy**: Seamless integration with Symbolics.jl for symbolic Lie derivatives and LinearAlgebra for efficient evaluation.
- **Interactive workflows**: Notebooks and REPL‑driven exploration make it easy to prototype, visualize, and benchmark Chen–Fliess expansions.


## Citing this package

If you use **CFSpy** in academic work, please cite it as:

    title        = {CFSpy},
    author       = {Perez Avellaneda, Ivan},
    year         = {2024},
    url          = {https://github.com/iperezav/CFSpy},
    note         = {Python package version 1.2.3}


A [CITATION.bib](content/CITATION.bib) file is also included in the repository.

## Content

1. [Introduction](content/Introduction.md)
    - [Why Chen–Fliess series?](content/Introduction.md#why-chenfliess-series)
    - [Understanding the algebraic structure](content/Introduction.md#understanding-the-algebraic-structure)
    - [Definition of iterated integrals](content/Introduction.md#definition-of-iterated-integrals)
    - [Definition of Lie derivatives](content/Introduction.md#definition-of-lie-derivatives)
    - [A concrete example](content/Introduction.md#a-concrete-example)
    - [Practical use and truncation](content/Introduction.md#practical-use-and-truncation)
    - [What the package does](content/Introduction.md#what-the-package-does)
    - [Summary of the Chen–Fliess pipeline](content/Introduction.md#summary-of-the-chenfliess-pipeline)
2. [Getting Started](content/Getting-started.md)
    - [Installation](content/Getting-started.md#installation)
    - [Basic Usage (High-Level Overview)](content/Getting-started.md#basic-usage-high-level-overview)
    - [Computing iterated integrals](content/Getting-started.md#computing-iterated-integrals)
    - [Defining vector fields and outputs](content/Getting-started.md#defining-vector-fields-and-outputs)
    - [Computing Lie derivatives](content/Getting-started.md#computing-lie-derivatives)
    - [Computing truncated Chen–Fliess series](content/Getting-started.md#computing-truncated-chenfliess-series)
    - [Comparing with ODE simulation](content/Getting-started.md#comparing-with-ode-simulation)
    - [Common pitfalls](content/Getting-started.md#common-pitfalls)
    - [More examples](content/Getting-started.md#more-examples)
3. [Examples](content/Examples.md)
    - [Lotka-Volterra](content/Examples.md#lotka-volterra)
        - [System dynamics](content/Examples.md#system-dynamics)
        - [Defining the system in Python](content/Examples.md#defining-the-system-in-python)
        - [Input signal](content/Examples.md#input-signal)
        - [Computing iterated integrals](content/Examples.md#computing-iterated-integrals)
        - [Computing Lie derivatives](content/Examples.md#computing-lie-derivatives)
        - [Assembling the truncated Chen-Fliess series](content/Examples.md#assembling-the-truncated-chen-fliess-series)
        - [Simulating the true Lotka-Volterra dynamics](content/Examples.md#simulating-the-true-lotka-volterra-dynamics)
        - [Comparison plot](content/Examples.md#comparison-plot)
    - [SEIRS](content/Examples.md#seirs)
        - [System dynamics](content/Examples.md#system-dynamics-1)
        - [Defining the system in Python](content/Examples.md#defining-the-system-in-python-1)
        - [Input signal](content/Examples.md#input-signal-1)
        - [Computing iterated integrals](content/Examples.md#computing-iterated-integrals-1)
        - [Computing Lie derivatives](content/Examples.md#computing-lie-derivatives-1)
        - [Assembling the truncated Chen–Fliess series](content/Examples.md#assembling-the-truncated-chenfliess-series)
        - [Simulating the true SEIRS dynamics](content/Examples.md#simulating-the-true-seirs-dynamics)
        - [Comparison plot](content/Examples.md#comparison-plot-1)
        - [Optimization and Reachability](content/Examples.md#optimization-and-reachability)
        - [Interpretation](content/Examples.md#interpretation)
4. [Contributing](content/Contributing.md)
    - [How to Contribute](content/Contributing.md#how-to-contribute)
    - [Guidelines](content/Contributing.md#guidelines)