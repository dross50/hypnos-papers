"""Arena for the two dividing-plane obstructions (docs/research/2026-10-01-ns-open-map/attempts/midplane-obstructions.md).

Theorem I: a stress-free leading-order core with no axial velocity on the dividing plane
has D_X H(X, 0) > 0, hence a(X, 0) < 2 and v_s(X, 0) < 2 (Rayleigh-stable), with the
quantitative margin a <= max(0, 2 - 2h/(sup w - 1)). Theorem II: Theorem 4.6(v) forces
int U(X, eta)^2 dX = (1/2) int E(X, eta)^2 dX for every eta, so a profile without axial
velocity on the dividing plane cannot satisfy it. The checker rederives the manuscript's
identities symbolically (part A), integrates the midplane ODE (part B1), solves the full
stress-free system as a power series with symmetric axis data (part B2), and solves the
two eta-ODEs behind the sharp form of Theorem II (part C). This arena would fail if the
derivation were wrong (A), if the barrier failed on any tested profile (B1), if the
midplane restriction of the full system did not satisfy the claimed ODE (B2), or if the
exterior and tail conditions admitted other solutions (C)."""
from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import sympy as sp

CHECK = Path(__file__).resolve().parents[1] / "docs" / "research" / "2026-10-01-ns-open-map" / "checks" / "midplane_barrier.py"
spec = importlib.util.spec_from_file_location("midplane_barrier", CHECK)
mb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mb)


def test_part_A_derivation_holds_symbolically():
    A = mb.part_A()
    for key, val in A.items():
        if isinstance(val, bool):
            assert val, key


def test_part_B1_barrier_on_every_tested_profile():
    B1 = mb.part_B1()
    for key, case in B1.items():
        assert case["min_DX_H"] > 0, key
        assert case["a_below_2"], key
        assert case["a_below_astar"], key
    # the quantitative margin is asymptotically sharp for constant w = 4 at h = 1/100
    c = B1["h=0.01|w=4"]
    assert abs(c["margin_2_minus_sup_a"] - 2 * 0.01 / 3) < 2e-3


def test_part_B2_full_system_series_matches_midplane_ODE():
    B2 = mb.part_B2(12)
    assert B2["U_n_at_0_all_zero"]
    assert B2["parity_U_odd_phi_even"]
    assert B2["midplane_ODE_holds_to_order_N"], B2["midplane_ODE_residual_coefficients_0_to_N"]
    assert B2["a_series_below_2"]
    assert B2["series_matches_ODE_1e-6"], B2["max_abs_diff_series_vs_ODE"]
    assert B2["asymmetric_breaks_hypothesis"]
    assert B2["S_partial_midplane_negative"]


def test_part_C_eta_odes():
    C = mb.part_C()
    assert C["M_solution_even"]
    assert C["M_solution_matches_(1-eta2)^D"]
    assert C["S_solution_matches_(1-eta2)^(-2h)"]
    assert C["S_candidate_exponent_negative_for_h_positive"]


def test_barrier_fails_without_the_h_term_only_in_margin_not_in_sign():
    # at h = 0 the barrier is still D_X H > 0 (a < 2) but the margin 2h/(w-1) is zero
    Xs, a, minHp, _ = mb.integrate_midplane(lambda X: 4.0, 0.0, y1=math.log(20.0))
    assert minHp > 0 and a.max() < 2
    assert 2 - a.max() < 1e-3
