"""Independent numerical checks for the unfolded-ordinate paper.

Reads Hypnos' certified zero table (first 100000 ordinates, 200 digits) and
checks, at mp.dps = 40:

  (A) the displacement identity  x_n - n = -Sbar(gamma_n), where
      x_n = theta(gamma_n)/pi + 3/2 and Sbar is the mean of the one-sided
      limits of S at the ordinate, with S computed INDEPENDENTLY by
      continuous continuation of arg zeta from sigma = 2 (a sample of n);
  (B) the block-sum identity
      sum_{a<gamma<b} Sbar(gamma) = (1/pi) int_a^b theta'(t) S(t) dt
                                    + (S(b)^2 - S(a)^2)/2
      for random non-ordinate endpoints a < b (S from the table count);
  (C) Kadec / Avdonin statistics: first crossing of 1/4, sup, block means
      D(M) for dyadic M, and the optimally centred sup;
  (D) the last-N-zeros-before-a-peak bound used in Theorem 2.
"""
import gzip, json, sys, random
from pathlib import Path
from mpmath import mp, mpf, pi, siegeltheta, zeta, log, arg, floor

# The certified zero table lives in the repository (paper/unfolded-zeros/scripts -> repo root).
ROOT = Path(__file__).resolve().parents[3] / "artifacts" / "zeros" / "dps200"
mp.dps = 40

def load_zeros(nmax):
    zs = []
    k = 0
    while len(zs) < nmax:
        lo = k * 1000 + 1
        hi = min(lo + 999, 100000)
        p = ROOT / f"shard-{lo:06d}-{hi:06d}.txt.gz"
        with gzip.open(p, "rt") as f:
            for line in f:
                line = line.strip()
                if line:
                    zs.append(mpf(line))
                    if len(zs) >= nmax:
                        break
        k += 1
    return zs

def S_by_continuation(t, steps=600):
    """S(t) = (1/pi) arg zeta(1/2+it) by continuous continuation from 2+it.
    arg zeta(2+it) is the principal argument (|zeta(2+it)-1| < 1)."""
    s0 = mp.mpc(2, t)
    a = arg(zeta(s0))
    prev = zeta(s0)
    sig = mpf(2)
    h = (mpf(2) - mpf(1) / 2) / steps
    for i in range(1, steps + 1):
        sig = mpf(2) - i * h
        cur = zeta(mp.mpc(sig, t))
        # increment of the argument along the step, unwrapped
        a += arg(cur / prev)
        prev = cur
    return a / pi

def main(nmax=20000, nsample=40, seed=1, steps=600):
    random.seed(seed)
    global S_by_continuation
    _S = S_by_continuation
    S_by_continuation = lambda t: _S(t, steps=steps)
    zs = load_zeros(nmax)
    n_list = list(range(1, nmax + 1))
    u = [siegeltheta(g) / pi for g in zs]          # theta(gamma_n)/pi
    x = [u[i] + mpf(3) / 2 for i in range(nmax)]    # unfolded ordinates
    d = [x[i] - (i + 1) for i in range(nmax)]       # displacements

    out = {}
    # (A) independent S at gamma_n +/- eps
    eps = mpf(10) ** -8
    worst_A = mpf(0)
    rows_A = []
    for i in sorted(random.sample(range(nmax), nsample)):
        g = zs[i]
        Sp = S_by_continuation(g + eps)
        Sm = S_by_continuation(g - eps)
        Sbar = (Sp + Sm) / 2
        # predicted: Sbar(gamma_n) = n - 3/2 - theta/pi = -d_n, up to O(eps*log)
        resid = Sbar + d[i]
        worst_A = max(worst_A, abs(resid))
        rows_A.append((i + 1, float(g), float(Sp), float(Sm), float(-d[i]), float(resid)))
    out["A_worst_resid"] = float(worst_A)
    out["A_rows"] = rows_A[:8]

    # (B) block-sum identity with S from the table count
    def S_table(t):
        # N(t) = number of ordinates <= t (t not an ordinate)
        # binary search
        lo, hi = 0, nmax
        while lo < hi:
            mid = (lo + hi) // 2
            if zs[mid] <= t:
                lo = mid + 1
            else:
                hi = mid
        N = lo
        return N - siegeltheta(t) / pi - 1

    def int_thetaprime_S(a, b):
        # exact piecewise closed form: on (gamma_k, gamma_{k+1}) S = k-1-theta/pi
        # (1/pi) int theta' S dt = int_{u(a)}^{u(b)} (N - 1 - u) du piecewise
        total = mpf(0)
        # indices of zeros in (a,b)
        ks = [k for k in range(nmax) if a < zs[k] < b]
        pts = [a] + [zs[k] for k in ks] + [b]
        Nleft = sum(1 for k in range(nmax) if zs[k] <= a)
        for j in range(len(pts) - 1):
            ua = siegeltheta(pts[j]) / pi
            ub = siegeltheta(pts[j + 1]) / pi
            Ncur = Nleft + j
            total += (Ncur - 1) * (ub - ua) - (ub ** 2 - ua ** 2) / 2
        return total, ks

    worst_B = mpf(0)
    rows_B = []
    for _ in range(nsample):
        i = random.randrange(10, nmax - 200)
        j = i + random.randrange(1, 150)
        a = (zs[i] + zs[i + 1]) / 2 + (zs[i + 1] - zs[i]) * (random.random() - 0.5) * 0.9
        b = (zs[j] + zs[j + 1]) / 2 + (zs[j + 1] - zs[j]) * (random.random() - 0.5) * 0.9
        lhs_int, ks = int_thetaprime_S(a, b)
        Sa, Sb = S_table(a), S_table(b)
        rhs = lhs_int + (Sb ** 2 - Sa ** 2) / 2
        lhs = sum(-d[k] for k in ks)        # sum of Sbar over ordinates in (a,b)
        resid = lhs - rhs
        worst_B = max(worst_B, abs(resid))
        rows_B.append((float(a), float(b), len(ks), float(lhs), float(rhs), float(resid)))
    out["B_worst_resid"] = float(worst_B)
    out["B_rows"] = rows_B[:5]

    # (C) Kadec / Avdonin statistics
    absd = [abs(v) for v in d]
    first_cross = next((i + 1 for i, v in enumerate(absd) if v >= mpf(1) / 4), None)
    out["first_cross_index"] = first_cross
    out["first_cross_gamma"] = float(zs[first_cross - 1]) if first_cross else None
    out["sup_abs_d"] = float(max(absd))
    out["argmax_abs_d"] = int(max(range(nmax), key=lambda i: absd[i]) + 1)
    dmax, dmin = max(d), min(d)
    out["cstar"] = float((dmax + dmin) / 2)
    out["Dstar_centered_sup"] = float((dmax - dmin) / 2)
    out["mean_d"] = float(sum(d) / nmax)
    out["rms_d"] = float(mp.sqrt(sum(v * v for v in d) / nmax))
    # block means, dyadic M, over ALL windows of consecutive indices
    pref = [mpf(0)]
    for v in d:
        pref.append(pref[-1] + v)
    DM = {}
    M = 1
    while M <= 4096 and M <= nmax:
        best = mpf(0)
        for s in range(0, nmax - M + 1):
            m = abs(pref[s + M] - pref[s]) / M
            if m > best:
                best = m
        DM[M] = float(best)
        M *= 2
    out["D_M"] = DM
    # optimally centred block means: sup over windows of |mean(d) - c| minimized over c
    DMc = {}
    M = 1
    while M <= 4096 and M <= nmax:
        means = [(pref[s + M] - pref[s]) / M for s in range(0, nmax - M + 1)]
        DMc[M] = float((max(means) - min(means)) / 2)
        M *= 2
    out["D_M_centered"] = DMc

    # (D) the peak argument: at the argmax of -d (largest Sbar), check the last N zeros
    i0 = max(range(nmax), key=lambda i: -d[i])
    A = float(-d[i0])
    rows_D = {}
    for N in (2, 4, 8, 16, 32):
        blk = [-d[k] for k in range(max(0, i0 - N + 1), i0 + 1)]
        rows_D[N] = (float(min(blk)), float(sum(blk) / len(blk)), A - N)
    out["D_peak_index"] = i0 + 1
    out["D_peak_Sbar"] = A
    out["D_rows(N: min Sbar in last N, block mean, A-N)"] = rows_D

    print(json.dumps(out, indent=1, default=str))

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    nsample = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    steps = int(sys.argv[3]) if len(sys.argv) > 3 else 600
    main(nmax, nsample=nsample, steps=steps)
