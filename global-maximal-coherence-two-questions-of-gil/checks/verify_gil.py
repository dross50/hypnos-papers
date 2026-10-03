"""Reproducible checks for "Global Maximal Coherence for Prescribed Intrinsic
Populations". Standard scientific-Python stack only; no Hypnos runtime.

Checks (numbered as in the manuscript):
  A. Free Youla values (Theorem 3.1): random real skew contractions M never
     exceed 2 sum_k a_{2k-1} a_{2k}; projected gradient ascent over the
     contraction ball (the Euclidean projection clips the singular values at
     1; a final snap sets them to 1) from 20 random starts per instance. Both
     the maximum and the MINIMUM over instances of (best - bound) are
     recorded, so a shortfall of the search is visible, not hidden.
  B. Prescribed Youla values (Theorem 4.1): random orientations and
     Nelder-Mead maximization over SO(n) through the exponential
     parametrization (a coordinate sign flip preserves squared entries, so
     this covers O(n)) never exceed 2 sum_k s_k^2 a_{2k-1} a_{2k}; maximum
     and minimum over instances of (best - value) recorded.
  C. The inequality family of Proposition 4.2: the LP over the full family
     {2x(E(C)) + x(C, B \\ C) <= R(|C|,|B|)} equals the Theorem 4.1 value;
     the subfamily C = B alone can exceed it; C = B with the degree
     constraints can still exceed it; the prefix subfamily C = [p], B = [q]
     alone (the inequalities the proof uses) equals it.
  D. Odd-set inequalities for random real skew contractions (floating-point
     checks of Lemma 2.1).
Writes verification-gil.json.
"""
import itertools, json, hashlib, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize, linprog
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent
SEED = 20260929
RNG = np.random.default_rng(SEED)


def cohesion(a, M):
    return float(np.sum(np.outer(a, a) * M ** 2))  # = 2 sum_{i<j} a_i a_j M_ij^2


def youla_block(s, n):
    M = np.zeros((n, n))
    for k, sk in enumerate(s):
        M[2 * k, 2 * k + 1] = sk; M[2 * k + 1, 2 * k] = -sk
    return M


def skew_from_params(p, n):
    M = np.zeros((n, n)); k = 0
    for i in range(n):
        for j in range(i + 1, n):
            M[i, j] = p[k]; M[j, i] = -p[k]; k += 1
    return M


def orth(p, n):
    return expm(skew_from_params(p, n))


def clip_ball(M):
    """Euclidean projection of a real skew matrix onto the operator-norm unit ball
    (clip the singular values at 1), re-skewed against roundoff."""
    U, s, Vt = np.linalg.svd(M)
    K = (U * np.minimum(s, 1.0)) @ Vt
    return 0.5 * (K - K.T)


def snap_isometry(M):
    """Set every nonzero singular value to 1: a skew partial isometry of the same
    rank (a polish step; the maximizers of the convex objective over the ball
    lie among the partial isometries of maximal rank)."""
    U, s, Vt = np.linalg.svd(M)
    K = (U * (s > 1e-9).astype(float)) @ Vt
    return 0.5 * (K - K.T)


def pga_free(a, n, starts=20, iters=4000, eta0=0.5, eta1=1e-4):
    """Projected gradient ascent for check A: maximize cohesion(a, M) over real
    skew M with ||M||_op <= 1. In the independent upper-triangular coordinates
    the gradient of sum_{i,j} a_i a_j M_ij^2 is 4 (a a^T) * M (it is
    2 (a a^T) * M under the Frobenius inner product on skew matrices; the
    direction is normalized, so the factor does not matter); steps follow a
    geometric step schedule, each followed by the projection; the best value
    seen, including after a final snap to a partial isometry, is returned."""
    aa = np.outer(a, a); best = -np.inf
    for _ in range(starts):
        Z = RNG.normal(size=(n, n)); M = clip_ball(Z - Z.T)
        for t in range(iters):
            eta = eta0 * (eta1 / eta0) ** (t / (iters - 1))
            D = 4 * aa * M; nd = np.linalg.norm(D)
            if nd == 0:
                break
            M = clip_ball(M + eta * D / nd)
            best = max(best, cohesion(a, M))
        best = max(best, cohesion(a, clip_ball(snap_isometry(M))))
    return best


def R(p, q, s2):
    ss = np.concatenate([s2, np.zeros(max(p, q) + 2)])
    return float(np.sum(ss[: min((p + 1) // 2, q // 2)]) + np.sum(ss[: p // 2]))


def lp_family(a, s, mode):
    """Maximize sum_{i<j} a_i a_j x_ij over x >= 0 subject to a subfamily of the
    inequalities (13): mode = "full" (every C subset of B), "CB" (C = B only),
    "CB+deg" (C = B and the degree constraints |C| = 1 inside every B),
    "prefix" (C = [p], B = [q], p <= q). Returns the LP value in the units of
    sum_{i<j} a_i a_j x_ij (half the squared cohesion)."""
    n = len(a); pairs = list(itertools.combinations(range(n), 2)); idx = {e: k for k, e in enumerate(pairs)}
    s2 = np.array(s) ** 2; A_ub, b_ub = [], []
    if mode == "prefix":
        CB_list = [(tuple(range(p)), tuple(range(q))) for q in range(2, n + 1) for p in range(1, q + 1)]
    else:
        CB_list = []
        for q in range(2, n + 1):
            for B in itertools.combinations(range(n), q):
                if mode == "full":
                    CB_list += [(C, B) for p in range(1, q + 1) for C in itertools.combinations(B, p)]
                elif mode == "CB":
                    CB_list.append((B, B))
                elif mode == "CB+deg":
                    CB_list.append((B, B)); CB_list += [((i,), B) for i in B]
                else:
                    raise ValueError(mode)
    for C, B in CB_list:
        Cs = set(C); row = np.zeros(len(pairs))
        for e in itertools.combinations(B, 2):
            inC = (e[0] in Cs) + (e[1] in Cs)
            row[idx[e]] = 2 if inC == 2 else (1 if inC == 1 else 0)
        A_ub.append(row); b_ub.append(R(len(C), len(B), s2))
    cobj = -np.array([a[i] * a[j] for i, j in pairs])
    res = linprog(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=[(0, None)] * len(pairs), method="highs")
    return -res.fun


def main():
    rep = {"seed": SEED, "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__}}
    # A. free Youla values
    worst_rand = -np.inf; diffs = []; nA = 0
    for n in range(2, 8):
        for _ in range(5):
            a = np.sort(RNG.uniform(0, 1, n))[::-1]; a /= a.sum()
            bound = 2 * sum(a[2 * k] * a[2 * k + 1] for k in range(n // 2))
            for _ in range(300):
                Z = RNG.normal(size=(n, n)); M = Z - Z.T; M /= np.linalg.norm(M, 2) * (1 + 0.2 * RNG.random())
                worst_rand = max(worst_rand, cohesion(a, M) - bound)
            diffs.append(pga_free(a, n) - bound); nA += 1
    rep["A_free_youla"] = {"instances": nA, "random_samples_per_instance": 300, "max_random_excess": worst_rand,
                           "method": "projected gradient ascent, 20 starts x 4000 steps, singular values clipped at 1, final snap to a partial isometry",
                           "max_optimized_excess": float(max(diffs)), "min_optimized_excess": float(min(diffs)),
                           "worst_shortfall": float(max(0.0, -min(diffs))),
                           "instances_within_1e-6": int(sum(1 for d in diffs if d > -1e-6)),
                           "instances_within_1e-4": int(sum(1 for d in diffs if d > -1e-4))}
    # B. prescribed Youla values
    worst_rand = -np.inf; diffs = []; nB = 0
    lp_full_diff = 0.0; lp_prefix_diff = 0.0; lp_cb_excess = 0.0; lp_cbdeg_excess = 0.0; lp_cbdeg_fail = 0
    for n in range(2, 8):
        for trial in range(5):
            a = np.sort(RNG.uniform(0, 1, n))[::-1]; a /= a.sum(); m = n // 2
            s = np.ones(m) if trial == 0 else np.sort(RNG.uniform(0, 1, m))[::-1]
            val = 2 * sum(s[k] ** 2 * a[2 * k] * a[2 * k + 1] for k in range(m)); Sig = youla_block(s, n)
            for _ in range(300):
                Q = orth(1.5 * RNG.normal(size=n * (n - 1) // 2), n)
                worst_rand = max(worst_rand, cohesion(a, Q @ Sig @ Q.T) - val)
            best = max(-minimize(lambda p: -cohesion(a, orth(p, n) @ Sig @ orth(p, n).T), RNG.normal(size=n * (n - 1) // 2),
                                 method="Nelder-Mead", options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-13}).fun for _ in range(20))
            diffs.append(best - val); nB += 1
            lp_full_diff = max(lp_full_diff, abs(2 * lp_family(a, s, "full") - val))
            lp_prefix_diff = max(lp_prefix_diff, abs(2 * lp_family(a, s, "prefix") - val))
            lp_cb_excess = max(lp_cb_excess, 2 * lp_family(a, s, "CB") - val)
            e = 2 * lp_family(a, s, "CB+deg") - val
            lp_cbdeg_excess = max(lp_cbdeg_excess, e); lp_cbdeg_fail += int(e > 1e-9)
    rep["B_prescribed_youla"] = {"instances": nB, "max_random_excess": worst_rand,
                                 "method": "Nelder-Mead over SO(n) via expm of a skew parameter, 20 starts",
                                 "max_optimized_excess": float(max(diffs)), "min_optimized_excess": float(min(diffs)),
                                 "worst_shortfall": float(max(0.0, -min(diffs))),
                                 "instances_within_1e-6": int(sum(1 for d in diffs if d > -1e-6))}
    rep["C_inequality_family"] = {"units": "squared cohesion ||N||_F^2 = 2 x (LP value); halve for the LP's own units",
                                  "max_abs_diff_full_family_LP_vs_theorem": lp_full_diff,
                                  "max_abs_diff_prefix_family_LP_vs_theorem": lp_prefix_diff,
                                  "max_excess_coarse_family_LP_over_theorem": lp_cb_excess,
                                  "max_excess_CB_plus_degree_LP_over_theorem": lp_cbdeg_excess,
                                  "instances_CB_plus_degree_LP_exceeds_theorem": lp_cbdeg_fail,
                                  "instances": nB}
    # D. odd-set inequalities
    nD = 0; max_excess = -np.inf
    for n in range(3, 9):
        for _ in range(40):
            Z = RNG.normal(size=(n, n)); M = Z - Z.T; M /= np.linalg.norm(M, 2) * (1 + RNG.random())
            x = M ** 2
            for size in range(3, n + 1, 2):
                for A in itertools.combinations(range(n), size):
                    max_excess = max(max_excess, np.sum(x[np.ix_(A, A)]) / 2 - (size - 1) / 2); nD += 1
    rep["D_odd_sets"] = {"checks": nD, "max_excess": float(max_excess)}
    rep["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT / "verification-gil.json").write_text(json.dumps(rep, indent=2) + "\n")
    print(json.dumps(rep, indent=2))


if __name__ == "__main__":
    main()
