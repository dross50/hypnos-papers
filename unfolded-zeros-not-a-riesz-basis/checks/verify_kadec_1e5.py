"""Independent recomputation of the Kadec / Avdonin statistics over the whole
certified table (first 100000 ordinates), at mp.dps = 30.

Outputs: sup |d_n|, its index and height, the first index with |d_n| >= 1/4,
the optimally centered sup, mean and rms of d_n, the dyadic block-mean table
D(M) for M = 1..4096, and the smallest unfolded gap.
"""
import gzip, json, sys
from pathlib import Path
from mpmath import mp, mpf, pi, siegeltheta

ROOT = Path(__file__).resolve().parents[3] / "artifacts" / "zeros" / "dps200"
mp.dps = 30
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 100000

zs = []
k = 0
while len(zs) < NMAX:
    lo = k * 1000 + 1
    hi = min(lo + 999, 100000)
    with gzip.open(ROOT / f"shard-{lo:06d}-{hi:06d}.txt.gz", "rt") as f:
        for line in f:
            line = line.strip()
            if line:
                zs.append(mpf(line))
                if len(zs) >= NMAX:
                    break
    k += 1

d = [siegeltheta(g) / pi + mpf(3) / 2 - (i + 1) for i, g in enumerate(zs)]
absd = [abs(v) for v in d]
imax = max(range(NMAX), key=lambda i: absd[i])
first = next(i + 1 for i, v in enumerate(absd) if v >= mpf(1) / 4)
dmax, dmin = max(d), min(d)
pref = [mpf(0)]
for v in d:
    pref.append(pref[-1] + v)
DM = {}
M = 1
while M <= 4096:
    DM[M] = float(max(abs(pref[s + M] - pref[s]) for s in range(0, NMAX - M + 1)) / M)
    M *= 2
x = [d[i] + (i + 1) for i in range(NMAX)]
gaps = [x[i + 1] - x[i] for i in range(NMAX - 1)]
igap = min(range(NMAX - 1), key=lambda i: gaps[i])
out = {
    "n": NMAX,
    "sup_abs_d": float(absd[imax]), "argmax": imax + 1, "gamma_argmax": float(zs[imax]),
    "first_cross_index": first, "gamma_first_cross": float(zs[first - 1]),
    "centered_sup": float((dmax - dmin) / 2), "cstar": float((dmax + dmin) / 2),
    "mean_d": float(sum(d) / NMAX), "rms_d": float(mp.sqrt(sum(v * v for v in d) / NMAX)),
    "count_abs_ge_quarter": sum(1 for v in absd if v >= mpf(1) / 4),
    "D_M": DM,
    "min_gap": float(gaps[igap]), "min_gap_index": igap + 1, "gamma_at_min_gap": float(zs[igap]),
}
print(json.dumps(out, indent=1))
