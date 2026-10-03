"""Reproducible falsification checks for the antiunitary matching theorem.

The analytic proof is in main.tex. Numerical checks do not certify a theorem.
This program uses no Hypnos runtime, model service, or live database.
"""
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import platform

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import scipy
from scipy.linalg import expm, expm_frechet
from scipy.optimize import check_grad, minimize

ROOT = Path(__file__).resolve().parent
SEED = 20260928
RNG = np.random.default_rng(SEED)


def haar(n):
    q, r = np.linalg.qr(RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n)))
    d = np.diag(r)
    return q @ np.diag(d / np.abs(d))


def objective(u, c, tau):
    n = len(u)
    return float(np.sum(c * np.abs(u) ** 2) +
                 tau * np.linalg.norm(u @ u.conj() + np.eye(n), "fro") ** 2)


def matching_solution(c, tau):
    n = len(c)
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            # The verification inputs make this an exact integer.
            weight = 8 * tau - 2 * c[i, j]
            if float(weight).is_integer():
                weight = int(weight)
            graph.add_edge(i, j, weight=weight)
    matching = sorted(tuple(sorted(e)) for e in nx.max_weight_matching(graph))
    value = 2 * sum(c[i, j] for i, j in matching) + 4 * tau * (n - 2 * len(matching))
    u = np.eye(n, dtype=complex)
    for i, j in matching:
        u[i, i] = u[j, j] = 0
        u[i, j], u[j, i] = 1, -1
    return float(value), matching, u


def exhaustive_value(c, tau):
    """Independent exact integer/rational-valued recurrence on all subsets."""
    n = len(c)

    @lru_cache(None)
    def solve(mask):
        if not mask:
            return 0
        low = mask & -mask
        i = low.bit_length() - 1
        remaining = mask ^ low
        best = 4 * tau + solve(remaining)
        for j in range(i + 1, n):
            if remaining & (1 << j):
                best = min(best, 2 * int(c[i, j]) + solve(remaining ^ (1 << j)))
        return best

    return solve((1 << n) - 1)


def path_value(values, tau):
    f = [0, 4 * tau]
    for k in range(2, len(values) + 1):
        f.append(min(f[-1] + 4 * tau,
                     f[-2] + 2 * (values[k - 1] - values[k - 2]) ** 2))
    return f[len(values)]


def hermitian(x, n):
    h = np.diag(x[:n]).astype(complex)
    k = n
    for i in range(n):
        for j in range(i + 1, n):
            h[i, j] = x[k] + 1j * x[k + 1]
            h[j, i] = h[i, j].conjugate()
            k += 2
    return h


def continuous_value_grad(x, c, tau):
    n = len(c)
    a = 1j * hermitian(x, n)
    u = expm(a)
    # The transpose identity is valid on U(n). The gradient below is for its
    # smooth extension; every exponential and derivative stay on U(n).
    value = np.sum(c * np.abs(u) ** 2) + tau * np.linalg.norm(u + u.T, "fro") ** 2
    g = 2 * c * u + 4 * tau * (u + u.T)
    hgrad = -1j * expm_frechet(a.conj().T, g, compute_expm=False)
    grad = list(np.real(np.diag(hgrad)))
    for i in range(n):
        for j in range(i + 1, n):
            grad.extend([float((hgrad[i, j] + hgrad[j, i]).real),
                         float((hgrad[i, j] - hgrad[j, i]).imag)])
    return float(value), np.array(grad)


def main():
    report = {"seed": SEED, "scope": "Finite falsification and implementation checks; not a formal proof",
              "versions": {"python": platform.python_version(), "numpy": np.__version__,
                           "scipy": scipy.__version__, "networkx": nx.__version__}}
    exact_cells = 0
    witness_error = 0.0
    for n in range(1, 11):
        for _ in range(20):
            upper = np.triu(RNG.integers(0, 21, size=(n, n)), 1)
            c = upper + upper.T
            for tau in (0, 0.25, 0.5, 2, 10):
                value, matching, u = matching_solution(c, tau)
                exact = exhaustive_value(c, tau)
                assert value == exact, (n, tau, value, exact)
                error = abs(objective(u, c, tau) - value)
                witness_error = max(witness_error, error)
                assert error < 1e-10
                exact_cells += 1
    report["matching_vs_exhaustive"] = {"cells": exact_cells, "dimensions": [1, 10],
                                         "failures": 0, "max_witness_error": witness_error}

    unitary_samples = 0
    max_identity_error = 0.0
    min_energy_gap = float("inf")
    max_odd_operator_error = 0.0
    max_odd_set_excess = 0.0
    for n in range(1, 13):
        upper = np.triu(RNG.integers(0, 21, size=(n, n)), 1)
        c = upper + upper.T
        for tau in (0.25, 0.5, 2, 10):
            value, _, _ = matching_solution(c, tau)
            for _ in range(100):
                u = haar(n)
                s, k = (u + u.T) / 2, (u - u.T) / 2
                x = np.abs(k) ** 2
                lhs = objective(u, c, tau)
                rhs = (4 * tau * n + np.sum((c - 4 * tau) * x) +
                       np.sum(c * np.abs(s) ** 2))
                max_identity_error = max(max_identity_error, abs(lhs - rhs))
                gap = lhs - value
                min_energy_gap = min(min_energy_gap, gap)
                assert gap > -1e-8 and abs(lhs - rhs) < 1e-8
                if n % 2:
                    op = np.linalg.norm(u @ u.conj() + np.eye(n), 2)
                    max_odd_operator_error = max(max_odd_operator_error, abs(op - 2))
                    assert abs(op - 2) < 1e-10
                # Every odd subset, not just the full set, in dimensions <= 8.
                if n <= 8:
                    for size in range(3, n + 1, 2):
                        for subset in itertools.combinations(range(n), size):
                            mass = np.sum(x[np.ix_(subset, subset)]) / 2
                            excess = float(mass - (size - 1) / 2)
                            max_odd_set_excess = max(max_odd_set_excess, excess)
                            assert excess < 1e-10
                unitary_samples += 1
    report["haar_unitaries"] = {"samples": unitary_samples, "dimensions": [1, 12],
        "min_energy_minus_exact_minimum": min_energy_gap,
        "max_decomposition_error": max_identity_error,
        "max_odd_operator_norm_error": max_odd_operator_error,
        "max_odd_set_constraint_excess": max_odd_set_excess, "failures": 0}

    # General complex skew contractions, independent of unitary skew parts.
    skew_samples = 0
    for n in range(2, 10):
        for _ in range(30):
            a = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
            k = a - a.T
            k /= np.linalg.norm(k, 2) * (1 + RNG.random())
            x = np.abs(k) ** 2
            assert np.max(x.sum(axis=1)) <= 1 + 1e-12
            for size in range(3, n + 1, 2):
                for subset in itertools.combinations(range(n), size):
                    assert np.sum(x[np.ix_(subset, subset)]) <= size - 1 + 1e-10
            skew_samples += 1
    report["independent_skew_contractions"] = {"samples": skew_samples, "failures": 0}

    path_cells = 0
    for n in range(1, 31):
        for _ in range(10):
            values = np.sort(RNG.integers(-30, 31, n))
            c = (values[:, None] - values[None, :]) ** 2
            for tau in (0, 0.25, 1, 10, 100):
                assert path_value(values, tau) == matching_solution(c, tau)[0]
                path_cells += 1
    report["scalar_dynamic_program"] = {"cells": path_cells, "dimensions": [1, 30], "failures": 0}

    gradient_c = np.array([[0, 2, 7], [2, 0, 3], [7, 3, 0]])
    gradient_x = RNG.normal(size=9)
    grad_error = check_grad(lambda x: continuous_value_grad(x, gradient_c, 2)[0],
                            lambda x: continuous_value_grad(x, gradient_c, 2)[1], gradient_x)
    assert grad_error < 2e-5, grad_error
    trials = []
    for n in range(2, 7):
        for case in range(2):
            upper = np.triu(RNG.integers(0, 13, size=(n, n)), 1)
            c = upper + upper.T
            for tau in (0.5, 2, 8):
                exact, _, _ = matching_solution(c, tau)
                for restart in range(4):
                    result = minimize(continuous_value_grad, RNG.normal(size=n*n),
                                      args=(c, tau), method="BFGS", jac=True,
                                      options={"gtol": 1e-8, "maxiter": 500})
                    u = expm(1j * hermitian(result.x, n))
                    direct = objective(u, c, tau)
                    gap = direct - exact
                    assert gap >= -1e-7, (n, tau, gap)
                    trials.append({"n": n, "case": case, "tau": tau, "restart": restart,
                                   "exact": exact, "value": direct, "gap": gap,
                                   "optimizer_success": bool(result.success),
                                   "iterations": int(result.nit)})
    report["continuous_optimization"] = {"trials": len(trials), "gradient_check_error": grad_error,
        "reached_global_within_1e-7": sum(t["gap"] <= 1e-7 for t in trials),
        "optimizer_success_count": sum(t["optimizer_success"] for t in trials),
        "min_gap": min(t["gap"] for t in trials), "max_gap": max(t["gap"] for t in trials),
        "details": trials}

    # Original-basis covariance and robustness beyond commuting tuples.
    robust_cases = 0
    covariance_error = 0.0
    for n in range(2, 9):
        for _ in range(10):
            points = RNG.integers(-5, 6, size=(n, 3))
            c = np.sum((points[:, None, :] - points[None, :, :]) ** 2, axis=2)
            exact, _, u = matching_solution(c, 3)
            v = haar(n)
            ds = [v @ np.diag(points[:, r]) @ v.conj().T for r in range(3)]
            original_u = v @ u @ v.T
            f = sum(np.linalg.norm(d @ original_u - original_u @ d.conj(), "fro") ** 2 for d in ds)
            f += 3 * np.linalg.norm(original_u @ original_u.conj() + np.eye(n), "fro") ** 2
            covariance_error = max(covariance_error, abs(f-exact))
            assert abs(f-exact) < 1e-8
            hs, epsilon_sq = [], 0
            for d in ds:
                e = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
                e = 0.01 * (e + e.conj().T)
                hs.append(d + e)
                epsilon_sq += np.linalg.norm(e, "fro") ** 2
            candidate = haar(n)
            costs = []
            for tuple_ in (ds, hs):
                val = sum(np.linalg.norm(h @ candidate-candidate @ h.conj(), "fro") ** 2 for h in tuple_)
                val += 3 * np.linalg.norm(candidate @ candidate.conj()+np.eye(n), "fro") ** 2
                costs.append(np.sqrt(val))
            assert abs(costs[0] - costs[1]) <= 2 * np.sqrt(epsilon_sq) + 1e-9
            robust_cases += 1
    report["covariance_and_perturbation"] = {"cases": robust_cases,
            "max_witness_covariance_error": covariance_error, "failures": 0}

    # Exact rational controls: the odd-set cut and rewiring thresholds.
    report["exact_controls"] = {
        "triangle": {"n": 3, "c": 0, "tau": 1, "dual_odd_set_weight": 8,
                     "matching_profit": 8, "minimum": 4, "degree_only_relaxation": 0},
        "rewiring": {"spectrum": [0, 2, 3, 5], "cardinality_costs": [0, 2, 16],
                     "breakpoints": ["1/4", "7/4"]}}
    assert matching_solution(np.zeros((3, 3), dtype=int), 1)[0] == 4
    values = np.array([0, 2, 3, 5])
    c = (values[:, None] - values[None, :]) ** 2
    for tau in (0, 0.25, 0.5, 1.75, 2, 4):
        assert matching_solution(c, tau)[0] == min(16*tau, 2+8*tau, 16)

    fig, ax = plt.subplots(figsize=(6.6, 3.35), constrained_layout=True)
    taus = np.linspace(0, 2.5, 501)
    for y, label in ((16*taus, "No pairs"), (2+8*taus, "One pair: (2, 3)"),
                     (np.full_like(taus, 16), "Two pairs: (0, 2), (3, 5)")):
        ax.plot(taus, y, "--", lw=1, alpha=0.7, label=label)
    ax.plot(taus, np.minimum.reduce([16*taus, 2+8*taus, np.full_like(taus, 16)]),
            color="#183b56", lw=2.7, label="Exact minimum")
    for t in (0.25, 1.75):
        ax.axvline(t, color="#777777", lw=0.7, alpha=0.5)
    ax.set(xlabel=r"Penalty $\tau$", ylabel=r"Minimum $\Phi_\tau$", ylim=(0, 23), xlim=(0, 2.5))
    ax.spines[["right", "top"]].set_visible(False)
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    fig.savefig(ROOT / "matching-curve.pdf")
    fig.savefig(ROOT / "matching-curve.png", dpi=180)
    plt.close(fig)

    report["completed_utc"] = datetime.now(timezone.utc).isoformat()
    report["verify_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    compact = dict(report)
    compact["continuous_optimization"] = {k: v for k, v in report["continuous_optimization"].items() if k != "details"}
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
