"""Checker for the two dividing-plane obstructions (attempts/midplane-obstructions.md).

Every formula rests on OpenAI, "Finite Time Blowup for Navier-Stokes" (166 pp., sha256
0e779481...): the similarity variables (4.1) p. 24, Lemma 4.1 p. 25, the ansatz (4.3)
p. 25, the profile identities (4.7) and the definitions (4.8)-(4.11) pp. 26-27, the
stress-free equations (4.13) p. 27, the cumulative integrals (4.15) and Lemma 4.3's
identity (4.16) p. 28. Nothing else is assumed. The checker rederives those identities
from Lemma 4.1 and the axisymmetric momentum equation, so the attempt does not rest on
the ledger's or the explanations' readings of them.

Part A (sympy): the derivation, symbol by symbol.
  A1  the material derivative of q^{-h} H under (4.2)-(4.3) and (4.7) is
      q^{-h-1} L^{-1} {W D_X H + H_c H_eta + h (1 - 2 eta U) H}            [(4.14)]
  A2  (d_rr + d_r / r - 1/r^2)(H / r) = (4 / r^3) D_X (D_X - 1) H with X = r^2/(2q)
  A3  hence the azimuthal residual without axial viscosity vanishes iff
      (2 / X) D_X (D_X - 1) H = L^{-1} {W D_X H + H_c H_eta + h (1 - 2 eta U) H},
      and with H = 2 X phi / C this is (4.13)_1: -2 L (X phi_XX + 2 phi_X) / phi = S_q
  A4  on eta = 0 with U(X, 0) = 0 the equation is the linear ODE
      D_X^2 H - [1 + (X/2)(1 - w)] D_X H - (h X / 2) H = 0,  w = A_X(U_eta)(X, 0)
  A5  the a-equation D_X a = X S_q / L - (1 - a/2) a follows from (4.9) with X Q_s / L = a,
      and the Riccati form of A4 is equivalent to the linear ODE through l = D_X log H
  A6  Lemma 4.3's axial identity (4.16): d_X (X N_s) = S_n on explicit test profiles
  A7  the pressure integration by parts int_0^X Pi dx = X Pi - int_0^X E^2/2 dx
Part B (numerics):
  B1  the midplane ODE integrated for several w(X) and h: D_X H > 0, a < 2,
      a <= a*(w) := max(0, 2 - 2h / (sup w - 1)); the margin 2 - sup a against 2h/(w - 1)
  B2  the full stress-free system (4.13) + (4.7) solved as a power series in X with
      reflection-symmetric analytic axis data, in exact rational arithmetic (the
      eta-dependence of every coefficient is carried as a Taylor polynomial at eta = 0,
      truncated at degree K = N + 2, which is exact for every coefficient the midplane
      needs because each order consumes at most one eta-derivative): U_n(0) = 0 for every
      n; U_n odd and phi_n even; the midplane restriction satisfies the ODE of A4 to every
      computed order; a(X, 0) < 2 on the region of convergence; the series a agrees with
      the ODE of B1 driven by the series w(X); an asymmetric datum (j0 > 0) breaks the
      hypothesis
Part C (Theorem II): the exterior condition 2 D eta M + d M' = 0 has only the even
  solutions c (1 - eta^2)^D; the relaxed axial tail condition 4 h eta S = d S' has only
  c (1 - eta^2)^{-2h}, unbounded at eta = +-1 unless c = 0 when h > 0.

Run: python checks/midplane_barrier.py [--order N] [--json PATH]. The committed receipt
is regenerated with --json checks/midplane_barrier.json; without --json nothing is written,
so a reviewer's run leaves the research record untouched. Budget: a few CPU seconds at the
default order.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

# ----------------------------------------------------------------------------- symbols
X, eta, h, r, q, Xs = sp.symbols("X eta h r q X_s", positive=True)


def consts(hh):
    """A, D, d, L of (4.1) for a given h (symbol or number)."""
    A = sp.Rational(1, 2) + hh
    D = sp.Rational(1, 2) - hh
    d = 1 - eta**2
    L = 1 - 2 * hh * eta**2
    return A, D, d, L


def T_op(b, f, hh):
    """Lemma 4.1: d_t (q^b f) = q^{b-1} T_b f."""
    A, D, d, L = consts(hh)
    return (-b * f + D * eta * sp.diff(f, eta) + X * sp.diff(f, X)) / L


def Z_op(b, f, hh):
    """Lemma 4.1: d_z (q^b f) = q^{b-D} Z_b f."""
    A, D, d, L = consts(hh)
    return (2 * b * eta * f + d * sp.diff(f, eta) - 2 * eta * X * sp.diff(f, X)) / L


# ----------------------------------------------------------------------------- part A
def part_A(verbose=False):
    out = {}
    _t = [time.process_time()]

    def lap(name):
        if verbose:
            now = time.process_time()
            print(f"  {name}: {now - _t[0]:.1f} s", file=sys.stderr, flush=True)
            _t[0] = now

    A, D, d, L = consts(h)
    H = sp.Function("H")(X, eta)
    U = sp.Function("U")(X, eta)
    Ub = sp.Function("Ub")(X, eta)  # A_X(U), the radial average; D_X Ub = U - Ub

    # (4.7): V0 = (X/L)(2 eta U - 2 D eta A_X(U) - d d_eta A_X(U)); (4.8): W, H_c.
    V0 = (X / L) * (2 * eta * U - 2 * D * eta * Ub - d * sp.diff(Ub, eta))
    W = 1 - 2 * D * eta * Ub - d * sp.diff(Ub, eta)
    Hc = D * eta + d * U
    DX = lambda f: X * sp.diff(f, X)

    # A1: coefficient of q^{-h-1} in (d_t + u_r d_r + u_z d_z)(q^{-h} H).
    #   d_t(q^{-h} H)      = q^{-h-1} T_{-h} H
    #   u_z d_z(q^{-h} H)  = q^{-A} U q^{-h-D} Z_{-h} H = q^{-h-1} U Z_{-h} H   (A + D = 1)
    #   u_r d_r(q^{-h} H)  = (V0 / r) q^{-h} H_X d_r X = q^{-h-1} V0 H_X        (d_r X = r/q)
    mat = T_op(-h, H, h) + U * Z_op(-h, H, h) + V0 * sp.diff(H, X)
    claim = (W * DX(H) + Hc * sp.diff(H, eta) + h * (1 - 2 * eta * U) * H) / L
    out["A1_material_derivative_is_4_14"] = sp.simplify(mat - claim) == 0
    lap("A1")

    # A2: radial swirl operator in X.
    Hr = sp.Function("Hr")
    Xr = r**2 / (2 * q)
    uth = Hr(Xr) / r
    lhs = sp.diff(uth, r, 2) + sp.diff(uth, r) / r - uth / r**2
    g = sp.Function("Hr")(Xs)
    DXg = Xs * sp.diff(g, Xs)
    rhs = (4 / r**3) * (Xs * sp.diff(DXg, Xs) - DXg).subs(Xs, Xr)
    out["A2_viscous_operator_is_4_over_r3_DX_DX_minus_1"] = sp.simplify(lhs - rhs) == 0
    lap("A2")

    # A3: stress-free azimuthal equation <=> (4.13)_1.
    #   D_t(q^{-h} H) = r * [visc of u_theta] = q^{-h} (4/r^2) D_X(D_X-1) H = q^{-h-1} (2/X) D_X(D_X-1) H
    phi = sp.Function("phi")(X, eta)
    C = sp.symbols("C", positive=True)
    H2 = 2 * X * phi / C
    eq_H = (2 / X) * (DX(DX(H2)) - DX(H2)) - claim.subs(H, H2).doit()
    l = 1 + X * sp.diff(phi, X) / phi
    Sq = -W * l - h * (1 - 2 * eta * U) - Hc * sp.diff(phi, eta) / phi
    eq_413 = -2 * L * (X * sp.diff(phi, X, 2) + 2 * sp.diff(phi, X)) / phi - Sq
    # By hand: (2/X) D_X(D_X - 1)(2 X phi / C) = (4X/C)(X phi_XX + 2 phi_X) and the transport side is
    # -(2 X phi/(C L)) S_q, so eq_H = -(2 X phi/(C L)) * eq_413 exactly.
    out["A3_stress_free_equation_is_4_13"] = sp.simplify(eq_H + (2 * X * phi / (C * L)) * eq_413) == 0
    lap("A3")

    # A4: midplane reduction with U(X, 0) = 0. Write U = eta u, Ub = eta ub.
    u = sp.Function("u")(X, eta)
    ub = sp.Function("ub")(X, eta)
    sub = {U: eta * u, Ub: eta * ub}
    # expected form, built from the same objects before eta is set to zero:
    # (2/X)(D_X^2 H - D_X H) - (1 - ub) D_X H - h H, with ub(X, 0) = w(X)
    expected = (2 / X) * (DX(DX(H2)) - DX(H2)) - (1 - ub) * DX(H2) - h * H2
    diff = sp.expand(eq_H.subs(sub).doit() - expected)
    out["A4_midplane_ODE_from_full_equation"] = sp.simplify(diff.subs(eta, 0)) == 0
    lap("A4")

    # A5: the a-equation from (4.9) with X Q_s/L = a, and Riccati <=> linear ODE.
    a = sp.Function("a")(X)
    lsym = sp.Function("l")(X)
    Sq_s = sp.Function("Sq")(X)
    Ls = sp.symbols("L_s", positive=True)
    Qs = Ls * a / X
    lhs49 = X * sp.diff(Qs, X) + (1 + lsym) * Qs - Sq_s
    rhs49 = (Ls / X) * (X * sp.diff(a, X) + lsym * a - X * Sq_s / Ls)
    out["A5_a_equation_from_4_9"] = sp.simplify(lhs49 - rhs49) == 0
    # Riccati from the linear ODE: with l = D_X log H, D_X l = l(1 - l - (X/2)(w-1)) + hX/2.
    w = sp.Function("w")(X)
    Hf = sp.Function("Hf")(X)
    lin = X * sp.diff(X * sp.diff(Hf, X), X) - (1 + (X / 2) * (1 - w)) * X * sp.diff(Hf, X) - (h * X / 2) * Hf
    lH = X * sp.diff(Hf, X) / Hf
    ricc = X * sp.diff(lH, X) - (lH * (1 - lH - (X / 2) * (w - 1)) + h * X / 2)
    out["A5_riccati_equals_linear_ODE_over_H"] = sp.simplify(ricc - lin / Hf) == 0
    # the barrier value: at a = 2 the midplane source is -h, so D_X a = -h X (L(0) = 1).
    Sq_mid = -(1 - w) * (1 - a / 2) - h
    out["A5_source_at_a_equals_2_is_minus_h"] = sp.simplify(Sq_mid.subs(a, 2) + h) == 0
    lap("A5")

    # A6: Lemma 4.3's axial identity on explicit profiles: d_X (X N_s) = S_n.
    Uex = X * sp.exp(-X) * (eta + eta**3 / 3)
    Eex = X * sp.exp(-X) * (1 + eta**2) / 2
    x = sp.symbols("x", positive=True)
    Mex = sp.integrate(Uex.subs(X, x), (x, 0, X))
    Sex = sp.integrate((Uex**2 - Eex**2 / 2).subs(X, x), (x, 0, X))
    Pi0 = -sp.Rational(5, 2) / (1 + eta**2) ** 2
    Cp = sp.integrate((Eex**2 / (2 * x)).subs(X, x), (x, 0, X))
    Piex = Pi0 + Cp
    Ubex = Mex / X
    Wex = 1 - 2 * D * eta * Ubex - d * sp.diff(Ubex, eta)
    Hcex = D * eta + d * Uex
    Sn = (-Wex * X * sp.diff(Uex, X) - A * (1 - 2 * eta * Uex) * Uex - Hcex * sp.diff(Uex, eta)
          - d * sp.diff(Piex, eta) + 4 * A * eta * Piex + 2 * eta * X * sp.diff(Piex, X))
    XNs = (-X * Wex * Uex + D * (Mex - eta * sp.diff(Mex, eta)) + 4 * h * eta * Sex - d * sp.diff(Sex, eta)
           + X * (4 * A * eta * Piex - d * sp.diff(Piex, eta)))
    out["A6_lemma_4_3_axial_identity_4_16"] = sp.simplify(sp.expand(sp.diff(XNs, X) - Sn)) == 0
    lap("A6")

    # A7: int_0^X Pi dx = X Pi - int_0^X E^2/2 dx when Pi_X = E^2/(2X).
    Pi_f = sp.Function("Pi")(X)
    E_f = sp.Function("E")(X)
    ident = sp.diff(X * Pi_f, X) - E_f**2 / 2 - Pi_f
    out["A7_pressure_integration_by_parts"] = sp.simplify(ident.subs(sp.diff(Pi_f, X), E_f**2 / (2 * X))) == 0
    return out


# ----------------------------------------------------------------------------- part B1
def integrate_midplane(wfun, hh, y0=math.log(1e-6), y1=math.log(20.0), npts=2001):
    """Integrate D_X^2 H - [1 + (X/2)(1-w)] D_X H - (hX/2) H = 0 in y = log X.

    Start from the rigid-rotation axis form H = 2X + c X^2, c = ((1 - w(0)) + h)/2.
    Returns X grid, a = 2 - 2 D_X H / H, min D_X H, min H.
    """
    import numpy as np
    from scipy.integrate import solve_ivp

    X0 = math.exp(y0)
    c = ((1 - wfun(0.0)) + hh) / 2
    H0 = 2 * X0 + c * X0**2
    Hp0 = 2 * X0 + 2 * c * X0**2

    def rhs(y, s):
        Xv = math.exp(y)
        Hv, Hpv = s
        return [Hpv, (1 + (Xv / 2) * (1 - wfun(Xv))) * Hpv + (hh * Xv / 2) * Hv]

    ys = np.linspace(y0, y1, npts)
    # atol = 0: pure relative control, so a component that decays exponentially (h = 0 cases)
    # keeps its sign instead of being treated as zero to tolerance.
    sol = solve_ivp(rhs, (y0, y1), [H0, Hp0], t_eval=ys, method="DOP853", rtol=1e-12, atol=0.0)
    Hs, Hps = sol.y
    Xs_ = np.exp(ys)
    a = 2 - 2 * Hps / Hs
    return Xs_, a, float(Hps.min()), float(Hs.min())


def part_B1():
    import numpy as np

    cases = {
        "w=4": lambda X_: 4.0,
        "w=0.5": lambda X_: 0.5,
        "w=1+3exp(-X)": lambda X_: 1 + 3 * math.exp(-X_),
        "w=1+X/2": lambda X_: 1 + X_ / 2,
        "w=4+2sin(X)": lambda X_: 4 + 2 * math.sin(X_),
    }
    out = {}
    for hh in (0.0, 0.01, 0.1):
        for name, wf in cases.items():
            Xs_, a, minHp, minH = integrate_midplane(wf, hh)
            wbar = np.maximum.accumulate([wf(x) for x in Xs_])
            astar = np.where(wbar > 1 + hh, 2 - 2 * hh / np.maximum(wbar - 1, 1e-300), 0.0)
            astar = np.maximum(astar, 0.0)
            ok_bound = bool(np.all(a <= astar + 1e-9))
            # a < 2 is exactly D_X H > 0 (a = 2 - 2 D_X H / H with H > 0); judged on the sign of
            # D_X H because at h = 0 the gap 2 - a can fall below double precision (e.g. 1e-21).
            out[f"h={hh}|{name}"] = {
                "min_DX_H": minHp,
                "min_H": minH,
                "sup_a": float(a.max()),
                "a_below_2": bool(minHp > 0 and minH > 0),
                "a_below_astar": ok_bound,
                "astar_at_end": float(astar[-1]),
                "margin_2_minus_sup_a": float(2 - a.max()),
            }
    return out


# ----------------------------------------------------------------------------- part B2
# Truncated Taylor polynomials in eta at eta = 0, degree <= K, exact Fractions.
def _add(f, g):
    return [a + b for a, b in zip(f, g)]


def _sub(f, g):
    return [a - b for a, b in zip(f, g)]


def _scal(c, f):
    return [c * a for a in f]


def _mul(f, g, K):
    out = [Fr(0)] * (K + 1)
    for i, a in enumerate(f):
        if a == 0:
            continue
        for j in range(K + 1 - i):
            b = g[j]
            if b:
                out[i + j] += a * b
    return out


def _deta(f, K):
    out = [Fr(0)] * (K + 1)
    for j in range(1, K + 1):
        out[j - 1] = j * f[j]
    return out


def _shift(f, K):
    """Multiply by eta."""
    out = [Fr(0)] * (K + 1)
    out[1:] = f[: K]
    return out


def _const(c, K):
    out = [Fr(0)] * (K + 1)
    out[0] = Fr(c)
    return out


def stress_free_series(N, phi0, U0, Pi0, hh, K=None):
    """Power series in X of the stress-free system (4.13) with (4.7), C = 1.

    phi = sum phi_n X^n, U = sum U_n X^n, Pi = Pi0 + sum (phi^2)_m X^{m+1}/(m+1);
    each coefficient is a Taylor polynomial in eta (list of Fractions, degree <= K).
    (4.13)_1: -2L n(n+1) phi_n = [phi S_q]_{n-1}, phi S_q = -W(phi + X phi_X) - h(1 - 2 eta U) phi - H_c phi_eta
    (4.13)_2: -2L n^2 U_n = [S_n]_{n-1},           S_n as in (4.9)
    with A_X(U)_n = U_n/(n+1), W = 1 - 2 D eta A_X(U) - d d_eta A_X(U), H_c = D eta + d U.
    Each order consumes at most one eta-derivative, so the degree-j coefficient of order n is
    exact whenever j + n <= K. phi0, U0, Pi0 are lists of Fractions (Taylor coefficients).
    """
    hh = Fr(hh)
    K = (N + 2) if K is None else K
    A = Fr(1, 2) + hh
    D = Fr(1, 2) - hh
    one = _const(1, K)
    d = _const(1, K)
    d[2] = Fr(-1)
    etas = _shift(one, K)
    # 1/L = sum (2h)^k eta^{2k}
    invL = [Fr(0)] * (K + 1)
    for k in range(0, K // 2 + 1):
        invL[2 * k] = (2 * hh) ** k
    pad = lambda f: (list(f) + [Fr(0)] * (K + 1))[: K + 1]
    phi = [pad(phi0)]
    U = [pad(U0)]
    Pi = [pad(Pi0)]

    def conv(f, g, m):
        acc = [Fr(0)] * (K + 1)
        for k in range(m + 1):
            if k < len(f) and m - k < len(g):
                acc = _add(acc, _mul(f[k], g[m - k], K))
        return acc

    for n in range(1, N + 1):
        m = n - 1
        Ub = [_scal(Fr(1, k + 1), U[k]) for k in range(m + 1)]
        W = []
        Hc = []
        for k in range(m + 1):
            wk = _sub(_scal(-2 * D, _shift(Ub[k], K)), _mul(d, _deta(Ub[k], K), K))
            if k == 0:
                wk = _add(wk, one)
            W.append(wk)
            hk = _mul(d, U[k], K)
            if k == 0:
                hk = _add(hk, _scal(D, etas))
            Hc.append(hk)
        # phi_n
        t = [Fr(0)] * (K + 1)
        for k in range(m + 1):
            t = _add(t, _scal(Fr(n - k), _mul(W[k], phi[m - k], K)))
        t = _add(t, _scal(hh, _sub(phi[m], _scal(Fr(2), _shift(conv(U, phi, m), K)))))
        for k in range(m + 1):
            t = _add(t, _mul(Hc[k], _deta(phi[m - k], K), K))
        phi_n = _mul(_scal(Fr(1, 2 * n * (n + 1)), t), invL, K)
        while len(Pi) <= m:
            kk = len(Pi)
            Pi.append(_scal(Fr(1, kk), conv(phi, phi, kk - 1)))
        # U_n
        s = [Fr(0)] * (K + 1)
        for k in range(m + 1):
            s = _add(s, _scal(Fr(m - k), _mul(W[k], U[m - k], K)))          # W D_X U
        s = _add(s, _scal(A, _sub(U[m], _scal(Fr(2), _shift(conv(U, U, m), K)))))  # A(1 - 2 eta U) U
        for k in range(m + 1):
            s = _add(s, _mul(Hc[k], _deta(U[m - k], K), K))                  # H_c U_eta
        s = _add(s, _mul(d, _deta(Pi[m], K), K))                              # d Pi_eta
        s = _sub(s, _scal(4 * A, _shift(Pi[m], K)))                           # -4 A eta Pi
        s = _sub(s, _scal(Fr(2 * m), _shift(Pi[m], K)))                       # -2 eta D_X Pi
        # S_n coefficient = -s ; U_n = -S_n/(2 L n^2) = s / (2 L n^2)
        U_n = _mul(_scal(Fr(1, 2 * n * n), s), invL, K)
        phi.append(phi_n)
        U.append(U_n)
    while len(Pi) <= N:
        kk = len(Pi)
        Pi.append(_scal(Fr(1, kk), conv(phi, phi, kk - 1)))
    return phi, U, Pi, K


def _taylor_Pi0(K):
    """-(5/2)(1 + eta^2)^{-2} = -(5/2) sum (-1)^k (k+1) eta^{2k}."""
    out = [Fr(0)] * (K + 1)
    for k in range(K // 2 + 1):
        out[2 * k] = Fr(-5, 2) * (-1) ** k * (k + 1)
    return out


def part_B2(N):
    import numpy as np
    from scipy.integrate import quad

    hh = Fr(1, 100)
    out = {"order": N}
    t0 = time.process_time()
    K = N + 2
    phi, U, Pi, K = stress_free_series(N, [Fr(1)], [Fr(0), Fr(4)], _taylor_Pi0(K), hh, K)
    out["series_cpu_s"] = time.process_time() - t0
    out["eta_truncation_degree_K"] = K
    # exactness window: degree j of order n is exact when j + n <= K
    out["U_n_at_0_all_zero"] = all(U[n][0] == 0 for n in range(N + 1))
    out["parity_U_odd_phi_even"] = all(
        all(U[n][j] == 0 for j in range(0, K - n + 1, 2)) and all(phi[n][j] == 0 for j in range(1, K - n + 1, 2))
        for n in range(N + 1))
    phi0 = [phi[n][0] for n in range(N + 1)]
    w0 = [U[n][1] / (n + 1) for n in range(N + 1)]   # w = A_X(U_eta)(X, 0) = sum U_n'(0)/(n+1) X^n
    out["phi_n_at_0"] = [str(c) for c in phi0]
    out["w_n_at_0"] = [str(c) for c in w0]
    # midplane ODE residual on the truncated series, exact rational arithmetic:
    #   H = 2 X phi(X, 0); R := D_X^2 H - [1 + (X/2)(1 - w)] D_X H - (h X/2) H; coefficients 0..N vanish.
    Hc_ = [Fr(0)] + [2 * phi0[n] for n in range(N + 1)]   # H_k X^k, k = 0..N+1
    DXH = [k * Hc_[k] for k in range(N + 2)]
    DX2H = [k * k * Hc_[k] for k in range(N + 2)]
    one_minus_w = [(1 if j == 0 else 0) - w0[j] for j in range(N + 1)]
    res = []
    for k in range(N + 2):
        term = DX2H[k] - DXH[k]
        ssum = sum((one_minus_w[j] * DXH[k - 1 - j] for j in range(0, k) if j <= N and 0 <= k - 1 - j <= N + 1), Fr(0))
        term -= ssum / 2
        if k >= 1:
            term -= hh * Hc_[k - 1] / 2
        res.append(term)
    out["midplane_ODE_residual_coefficients_0_to_N"] = [str(c) for c in res[: N + 1]]
    out["midplane_ODE_holds_to_order_N"] = all(c == 0 for c in res[: N + 1])
    # radius estimate and a(X, 0) < 2 on half the estimated radius
    mags = [abs(float(c)) for c in phi0[1:]]
    ratios = [mags[i + 1] / mags[i] for i in range(len(mags) - 1) if mags[i] > 0]
    growth = max(ratios[-3:]) if len(ratios) >= 3 else (ratios[-1] if ratios else 1.0)
    Xmax = 0.5 / growth if growth > 0 else 1.0
    out["radius_estimate_from_ratio_test"] = 1.0 / growth if growth > 0 else None
    out["X_max_tested"] = Xmax
    phif = [float(c) for c in phi0]
    wf = [float(c) for c in w0]

    def a_series(Xv):  # a = 1 - 2 D_X log E = -2 X phi_X / phi
        ph = sum(phif[n] * Xv**n for n in range(N + 1))
        dph = sum(n * phif[n] * Xv ** (n - 1) for n in range(1, N + 1))
        return -2 * Xv * dph / ph

    grid = [Xmax * i / 200 for i in range(1, 201)]
    avals = [a_series(x) for x in grid]
    out["sup_a_series_on_[0,Xmax]"] = max(avals)
    out["a_series_below_2"] = max(avals) < 2
    # compare with the ODE of B1 driven by the series w(X)
    wser = lambda Xv: sum(wf[n] * Xv**n for n in range(N + 1))
    Xs_, a_ode, _, _ = integrate_midplane(wser, float(hh), y0=math.log(1e-6), y1=math.log(Xmax), npts=4001)
    a_ser_on_grid = np.array([a_series(x) for x in Xs_[::40]])
    dmax = float(np.max(np.abs(a_ser_on_grid - a_ode[::40])))
    out["max_abs_diff_series_vs_ODE"] = dmax
    out["series_matches_ODE_1e-6"] = dmax < 1e-6
    # asymmetric datum: the hypothesis fails as designed (U_0(0) = j0 and U_1(0) = -Z*(0)/(2L) nonzero)
    phiA, UA, PiA, _ = stress_free_series(3, [Fr(1)], [Fr(1, 20), Fr(4)], _taylor_Pi0(5), hh, 5)
    out["asymmetric_U0_at_0"] = str(UA[0][0])
    out["asymmetric_U1_at_0"] = str(UA[1][0])
    out["asymmetric_breaks_hypothesis"] = UA[0][0] != 0 or UA[1][0] != 0
    # Theorem II illustration on the truncated midplane profile: S(Xmax, 0) < 0 since U(X, 0) = 0
    Eser = lambda Xv: math.sqrt(2 * Xv) * sum(phif[n] * Xv**n for n in range(N + 1))
    S_mid = quad(lambda x: 0 - Eser(x) ** 2 / 2, 0, Xmax)[0]
    out["S_partial_midplane_negative"] = S_mid < 0
    out["S_partial_midplane_value"] = S_mid
    return out


# ----------------------------------------------------------------------------- part C
def part_C():
    """Both eta-ODEs are first-order, linear and homogeneous on (-1, 1), so their solution
    spaces are one-dimensional; it is enough to exhibit one nonzero solution each."""
    out = {}
    hh = sp.symbols("h", positive=True)
    A, D, d, L = consts(hh)
    Mc = (1 - eta**2) ** D
    Sc = (1 - eta**2) ** (-2 * hh)
    # (4.7) in the exterior with U = 0: V0 = -(2 D eta M + d M')/L = 0  <=>  d M' + 2 D eta M = 0
    out["M_candidate_solves_exterior_condition"] = sp.simplify(d * sp.diff(Mc, eta) + 2 * D * eta * Mc) == 0
    out["M_solution_even"] = sp.simplify(Mc.subs(eta, -eta) - Mc) == 0
    out["M_solution_matches_(1-eta2)^D"] = out["M_candidate_solves_exterior_condition"]
    # the relaxed axial tail condition with M = 0: 4 h eta S - d S' = 0
    out["S_candidate_solves_tail_condition"] = sp.simplify(4 * hh * eta * Sc - d * sp.diff(Sc, eta)) == 0
    out["S_solution_matches_(1-eta2)^(-2h)"] = out["S_candidate_solves_tail_condition"]
    # unbounded at eta -> 1 for h > 0: the exponent of (1 - eta^2) is negative
    out["S_candidate_exponent_negative_for_h_positive"] = bool((-2 * hh).is_negative)
    out["note"] = "first-order linear homogeneous ODEs: one-dimensional solution spaces"
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--order", type=int, default=12)
    ap.add_argument("--json", type=str, default=None,
                    help="write the receipt here (the committed one is checks/midplane_barrier.json); "
                         "omitted: print only, so a run never rewrites the record")
    ap.add_argument("--skip-B2", action="store_true")
    args = ap.parse_args(argv)
    t0 = time.process_time()
    rec = {"generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    rec["A"] = part_A()
    rec["B1"] = part_B1()
    rec["B1_note"] = ("a_below_2 is read from the sign of D_X H (min_DX_H > 0 and min_H > 0), since "
                      "a = 2 - 2 D_X H / H; sup_a is a sampled double and prints as 2.0 where the gap "
                      "2 - a is below double precision (h = 0 cases)")
    if not args.skip_B2:
        rec["B2"] = part_B2(args.order)
    rec["C"] = part_C()
    rec["cpu_seconds"] = time.process_time() - t0
    flags = [v for v in rec["A"].values() if isinstance(v, bool)]
    flags += [c["a_below_2"] and c["a_below_astar"] and c["min_DX_H"] > 0 for c in rec["B1"].values()]
    if not args.skip_B2:
        B2 = rec["B2"]
        flags += [B2["U_n_at_0_all_zero"], B2["parity_U_odd_phi_even"], B2["midplane_ODE_holds_to_order_N"],
                  B2["a_series_below_2"], B2["series_matches_ODE_1e-6"], B2["asymmetric_breaks_hypothesis"],
                  B2["S_partial_midplane_negative"]]
    flags += [rec["C"]["M_solution_even"], rec["C"]["M_solution_matches_(1-eta2)^D"],
              rec["C"]["S_solution_matches_(1-eta2)^(-2h)"], rec["C"]["S_candidate_exponent_negative_for_h_positive"]]
    rec["all_checks_pass"] = all(flags)
    if args.json:
        Path(args.json).write_text(json.dumps(rec, indent=1), encoding="utf-8")
    print(json.dumps(rec, indent=1))
    return 0 if rec["all_checks_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
