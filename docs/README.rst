CFSpy
======================================

.. raw:: html

   <div align="center">

.. image:: https://img.shields.io/pypi/pyversions/cfspy
   :target: https://pypi.org/project/cfspy/
   :alt: PyPI - Python Version

.. image:: https://img.shields.io/pypi/v/cfspy
   :target: https://pypi.org/project/cfspy/
   :alt: PyPI - Version

.. image:: https://img.shields.io/pypi/status/cfspy
   :alt: PyPI - Status

.. image:: https://static.pepy.tech/personalized-badge/cfspy?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads
   :target: https://pepy.tech/projects/cfspy
   :alt: PyPI Downloads

.. image:: https://img.shields.io/pypi/l/cfspy
   :target: https://pypi.org/project/cfspy/
   :alt: PyPI - License

.. raw:: html

   </div>

Welcome to the documentation of the CFSpy Python package.

Overview
--------

CFSpy is used for the computation of Chen-Fliess series and their applications in control and reachability theory. This documentation provides a comprehensive guide to using and contributing to the project.

The package provides the following functionalities:

- The list of iterated integrals indexed by words of a certain length or less.
- The list of Lie derivatives indexed by words of a certain length or less.
- A single iterated integral indexed by a given word.
- A single Lie derivative indexed by a given word.
- The symbolic polynomial that represents the Chen-Fliess series for a constant input.

The implementation is based on Chen's identity, which provides recursive relations between iterated integrals and Lie derivatives, significantly reducing redundant computation.

This package is the first publicly available open‑source implementation of these tools in the Python ecosystem, relying only on NumPy and SymPy for minimal and efficient dependencies.


What are Chen–Fliess series?
-----------------------------

Chen–Fliess series provide an input–output representation of analytic nonlinear control‑affine systems.

They express the output as a formal power series whose coefficients are Lie derivatives of the output function and whose terms are iterated integrals of the input.

Formally:

.. math::

    F_c[u](t) = \sum_{\eta \in X^*} (c,\eta)\, E_\eta[u](t),

where:

- :math:`\eta` is a word over the alphabet :math:`X = \{x_0,\ldots,x_m\}`,
- :math:`(c,\eta)` is the coefficient given by a Lie derivative,
- :math:`E_\eta[u](t)` is the iterated integral associated with :math:`\eta`.

These series play a central role in nonlinear control theory, system approximation, and operator‑theoretic analysis.

Why Python?
-----------

CFSpy is written in Python to leverage:

- **High performance**: JIT compilation and type specialization enable tight inner loops for iterated integrals and Lie derivatives.
- **Multiple dispatch**: Natural expression of different system types, vector field representations, and numeric backends.
- **Symbolic–numeric synergy**: Seamless integration with Symbolics.jl for symbolic Lie derivatives and LinearAlgebra for efficient evaluation.
- **Interactive workflows**: Notebooks and REPL‑driven exploration make it easy to prototype, visualize, and benchmark Chen–Fliess expansions.


Citing this package
-------------------

If you use **CFSpy** in academic work, please cite it as::

    title        = {CFSpy},
    author       = {Perez Avellaneda, Ivan},
    year         = {2024},
    url          = {https://github.com/iperezav/CFSpy},
    note         = {Python package version 1.2.3}


A `CITATION.bib <content/CITATION.bib>`_ file is also included in the repository.

Content
-------

1. :doc:`Introduction <content/Introduction>`
    - `Why Chen–Fliess series? <content/Introduction.html#why-chenfliess-series>`_
    - `Understanding the algebraic structure <content/Introduction.html#understanding-the-algebraic-structure>`_
    - `Definition of iterated integrals <content/Introduction.html#definition-of-iterated-integrals>`_
    - `Definition of Lie derivatives <content/Introduction.html#definition-of-lie-derivatives>`_
    - `A concrete example <content/Introduction.html#a-concrete-example>`_
    - `Practical use and truncation <content/Introduction.html#practical-use-and-truncation>`_
    - `What the package does <content/Introduction.html#what-the-package-does>`_
    - `Summary of the Chen–Fliess pipeline <content/Introduction.html#summary-of-the-chenfliess-pipeline>`_
2. :doc:`Getting Started <content/Getting-started>`
    - `Installation <content/Getting-started.html#installation>`_
    - `Basic Usage (High-Level Overview) <content/Getting-started.html#basic-usage-high-level-overview>`_
    - `Computing iterated integrals <content/Getting-started.html#computing-iterated-integrals>`_
    - `Defining vector fields and outputs <content/Getting-started.html#defining-vector-fields-and-outputs>`_
    - `Computing Lie derivatives <content/Getting-started.html#computing-lie-derivatives>`_
    - `Computing truncated Chen–Fliess series <content/Getting-started.html#computing-truncated-chenfliess-series>`_
    - `Comparing with ODE simulation <content/Getting-started.html#comparing-with-ode-simulation>`_
    - `Common pitfalls <content/Getting-started.html#common-pitfalls>`_
    - `More examples <content/Getting-started.html#more-examples>`_
3. :doc:`Examples <content/Examples>`
    - `Lotka-Volterra <content/Examples.html#lotka-volterra>`_
        - `System dynamics <content/Examples.html#system-dynamics>`_
        - `Defining the system in Python <content/Examples.html#defining-the-system-in-python>`_
        - `Input signal <content/Examples.html#input-signal>`_
        - `Computing iterated integrals <content/Examples.html#computing-iterated-integrals>`_
        - `Computing Lie derivatives <content/Examples.html#computing-lie-derivatives>`_
        - `Assembling the truncated Chen-Fliess series <content/Examples.html#assembling-the-truncated-chen-fliess-series>`_
        - `Simulating the true Lotka-Volterra dynamics <content/Examples.html#simulating-the-true-lotka-volterra-dynamics>`_
        - `Comparison plot <content/Examples.html#comparison-plot>`_
    - `SEIRS <content/Examples.html#seirs>`_
        - `System dynamics <content/Examples.html#system-dynamics-1>`_
        - `Defining the system in Python <content/Examples.html#defining-the-system-in-python-1>`_
        - `Input signal <content/Examples.html#input-signal-1>`_
        - `Computing iterated integrals <content/Examples.html#computing-iterated-integrals-1>`_
        - `Computing Lie derivatives <content/Examples.html#computing-lie-derivatives-1>`_
        - `Assembling the truncated Chen–Fliess series <content/Examples.html#assembling-the-truncated-chenfliess-series>`_
        - `Simulating the true SEIRS dynamics <content/Examples.html#simulating-the-true-seirs-dynamics>`_
        - `Comparison plot <content/Examples.html#comparison-plot-1>`_
        - `Optimization and Reachability <content/Examples.html#optimization-and-reachability>`_
        - `Interpretation <content/Examples.html#interpretation>`_
4. :doc:`Contributing <content/Contributing>`
    - `How to Contribute <content/Contributing.html#how-to-contribute>`_
    - `Guidelines <content/Contributing.html#guidelines>`_