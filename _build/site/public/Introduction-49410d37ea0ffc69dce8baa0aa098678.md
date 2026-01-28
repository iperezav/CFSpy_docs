# Introduction

This is meant to be a quick introduction to the subject.
The **CFSpy** Python package is developed to
compute Chen–Fliess series numerically.
Chen–Fliess series provide an input–output representation
of nonlinear control-affine systems described in general
by the following set of equations:

```{math}
    \begin{aligned}
        \dot{z} &= g_0(z) + \sum_{i = 1}^{m} g_i(z) u_i\\
        y&= h(z)
    \end{aligned}
```

The vector fields $g_i$ and the output function $h$ are analytic,
and $u_i$, $y$, $z$ denote the input, output, and state of the system,
respectively.

## Why Chen–Fliess series?

The Chen–Fliess series provides a powerful way to describe the input–output
behavior of nonlinear systems without explicitly solving the underlying
differential equations. It converts the dynamics into an infinite formal
power series whose coefficients encode the geometry of the vector fields
and whose terms depend on iterated integrals of the input.

This representation is particularly useful for:

- approximating system outputs,
- analyzing nonlinear controllability,
- computing high-order expansions,
- benchmarking numerical methods,
- and studying operator-theoretic properties of control systems.

The Chen–Fliess series has the form:

```{math}
    \begin{aligned}
        F_c[u](t) = \sum_{\eta \in X^*} (c, \eta) E_{\eta}[u](t)
    \end{aligned}
```

## Understanding the algebraic structure


To understand the elements of this series, consider the
[free monoid](<https://en.wikipedia.org/wiki/Free_monoid>)
$(X^\ast, \cdot, \emptyset)$ where $X^*$ is the set of all words
over the alphabet $X = \{x_0, \ldots, x_m\}$.

Intuitively, each word $\eta = x_{i_1}\cdots x_{i_k}$ represents a
composition of vector fields applied in a specific order.
The symbol $x_0$ corresponds to the drift vector field $g_0$,
while $x_i$ corresponds to the controlled vector field $g_i$.

The coefficients $(c, \eta)$ correspond to the word $\eta$
in the generating series $c=\sum_{\eta\in X^\ast}(c,\eta)\eta$,
and $E_{\eta}[u](t)$ is the iterated integral corresponding to the word
$\eta$ and the input function $u$.

## Definition of iterated integrals


The iterated integral is defined recursively as $E_{\emptyset}[u](t)=1$ and

```{math}
    \begin{aligned}
        E_{x_{i}\eta}[u](t) = \int_0^t u_{x_i}(\tau)\,E_{\eta}[u](\tau)\,d\tau
    \end{aligned}
```


## Definition of Lie derivatives


The Lie derivative of $h$ associated to the word $\eta$ is defined as

```{math}
    \begin{aligned}
        L_{\eta}h = L_{x_{i_1}}\cdots L_{x_{i_k}}h
    \end{aligned}
```

where $L_{x_{i_j}}h=\frac{\partial h}{\partial z}\cdot g_{i_j}$.

Under the [proper conditions (Fliess, 1983)](<https://proceedings.scipy.org/articles/mfwm5796>),
we have the identity

```{math}
    (c, \eta) = L_{\eta}h
```

## A concrete example


For example, the word $\eta = x_2 x_0 x_1$ corresponds to the Lie derivative

```{math}
    L_{x_2 x_0 x_1} h
    = L_{x_2}(L_{x_0}(L_{x_1} h)).
```

The associated iterated integral is

```{math}
    E_{x_2 x_0 x_1}[u](t)
    = \int_0^t u_2(\tau_3)
        \int_0^{\tau_3} u_0(\tau_2)
            \int_0^{\tau_2} u_1(\tau_1)\, d\tau_1\, d\tau_2\, d\tau_3.
```


## Practical use and truncation


In applications, the infinite series is truncated at some depth $N$.
Under analyticity assumptions, the truncated series converges uniformly on compact
time intervals for sufficiently small inputs. The truncation depth controls the
accuracy of the approximation, and **CFSpy** provides tools to study
this trade-off numerically.

## What the package does


The **CFSpy** package implements these constructions efficiently by:

- computing Lie derivatives symbolically or numerically,
- generating all words up to a chosen truncation depth,
- evaluating iterated integrals using high-performance numerical routines,
- assembling truncated Chen–Fliess approximations,
- and comparing them with ODE solutions for validation.

This allows users to explore high-order expansions, benchmark algorithms,
and study nonlinear systems without manually handling the combinatorial
complexity of words and iterated integrals.

## Summary of the Chen–Fliess pipeline


1. Define the vector fields $g_i$ and output $h$.
2. Generate all words $\eta$ up to length $N$.
3. Compute Lie derivatives $L_\eta h$.
4. Compute iterated integrals $E_\eta[u](t)$.
5. Form the truncated series
   $F_c^{N} = \sum_{|\eta|\le N} (c,\eta) E_\eta[u](t)$.
6. Compare with the true system output if desired.