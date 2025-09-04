

Introduction
========================

The **CFSpy** Python package is developed to compute numerically the 
Chen-Fliess series representation of the output of
nonlinear input-output control systems. These systems are described by

.. math::
    \begin{eqnarray}
    \dot{z} &=& g_0(z) + \sum_{i = 1}^{m} g_i(z) u_i\\
    y &=& h(z)
    \end{eqnarray}


where the vector fields :math:`g_i` and the output function :math:`h` are analytic.
The Chen-Fliess series has the form:

.. math::
    \begin{eqnarray}
    F_c[u](t) = \sum_{\eta \in X^*} (c, \eta) E_{\eta}[u](t)
    \end{eqnarray}

