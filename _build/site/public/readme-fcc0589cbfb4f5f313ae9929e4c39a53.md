# CFSpy

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

$$
    F_c[u](t) = \sum_{\eta \in X^*} (c,\eta)\, E_\eta[u](t),
$$

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

1. [Introduction]
    - [Why Chen–Fliess series?]()
    - [Understanding the algebraic structure]()
    - [Definition of iterated integrals]()
    - [Definition of Lie derivatives]()
    - [A concrete example]()
    - [Practical use and truncation]()
    - [What the package does]()
    - [Summary of the Chen–Fliess pipeline]()
2. [Getting Started]()
    - [Installation]
    - [Basic Usage (High-Level Overview)]()
    - [Computing iterated integrals]()
    - [Defining vector fields and outputs]()
    - [Computing Lie derivatives]()
    - [Computing truncated Chen–Fliess series]()
    - [Comparing with ODE simulation]()
    - [Common pitfalls]()
    - [More examples]()
3. [Examples]
    3.1 [2D Planar Quadrotor]()
        - [System dynamics]()
        - [Defining the system in Python]()
        - [Input signal]()
        - [Computing iterated integrals]()
        - [Computing Lie derivatives]()
        - [Assembling the truncated Chen-Fliess series]()
        - [Simulating the true 2D planar quadrotor dynamics]()
        - [Comparison plot]()
    3.2 [Pendulum]()
        - [System dynamics]()
        - [Defining the system in Julia]()
        - [Input signal]()
        - [Computing iterated integrals]()
        - [Computing Lie derivatives]()
        - [Assembling the truncated Chen–Fliess series]()
        - [Simulating the true pendulum dynamics]()
        - [Comparison plot]()
        - [Error analysis]()
        - [Interpretation]
4. [Contributing]
    - [How to Contribute]()
    - [Guidelines]()