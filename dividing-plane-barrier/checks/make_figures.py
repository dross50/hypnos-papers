"""Figure for the dividing-plane paper.

fig_midplane.pdf: the swirl shear a(X, 0) along the dividing plane of a stress-free core, from the
midplane angular momentum equation (M) of the paper,

    D_X^2 H - [1 + (X/2)(1 - w)] D_X H - (h X / 2) H = 0,   D_X = X d/dX,

integrated in y = log X from the rigid-rotation axis form H = 2X + c X^2 (c = ((1 - w(0)) + h)/2):
three strain profiles at h = 1/100 (left), and constant strain w = 4 at h in {0, 1/100, 1/10} against
the margin bound 2 - a >= 2h/(w - 1) (right). The integrator is the one in
docs/research/2026-10-01-ns-open-map/checks/midplane_barrier.py (part B1), copied here so that the
figure needs only numpy, scipy and matplotlib.

Run from the paper directory: python scripts/make_figures.py
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def integrate_midplane(wfun, hh, y0=math.log(1e-4), y1=math.log(20.0), npts=3001):
    X0 = math.exp(y0)
    c = ((1 - wfun(0.0)) + hh) / 2
    H0 = 2 * X0 + c * X0**2
    Hp0 = 2 * X0 + 2 * c * X0**2

    def rhs(y, s):
        Xv = math.exp(y)
        Hv, Hpv = s
        return [Hpv, (1 + (Xv / 2) * (1 - wfun(Xv))) * Hpv + (hh * Xv / 2) * Hv]

    ys = np.linspace(y0, y1, npts)
    sol = solve_ivp(rhs, (y0, y1), [H0, Hp0], t_eval=ys, method="DOP853", rtol=1e-12, atol=0.0)
    Hs, Hps = sol.y
    assert Hps.min() > 0 and Hs.min() > 0
    return np.exp(ys), 2 - 2 * Hps / Hs


HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({"font.size": 9, "font.family": "serif", "axes.linewidth": 0.6})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.6, 2.7))

h = 0.01
profiles = {
    r"$w\equiv 4$": lambda X: 4.0,
    r"$w = 1 + 3e^{-X}$": lambda X: 1 + 3 * math.exp(-X),
    r"$w = 4 + 2\sin X$": lambda X: 4 + 2 * math.sin(X),
}
for label, wf in profiles.items():
    Xs, a = integrate_midplane(wf, h)
    ax1.plot(Xs, a, lw=1.1, label=label)
ax1.axhline(2.0, color="k", lw=0.6, ls="--")
ax1.set_xscale("log")
ax1.set_xlim(1e-3, 20)
ax1.set_ylim(-0.1, 2.1)
ax1.set_xlabel(r"$X$")
ax1.set_ylabel(r"$a(X,0)$")
ax1.set_title(r"three strains, $h = 1/100$", fontsize=9)
ax1.legend(frameon=False, fontsize=8, loc="lower right")

for hh, ls in ((0.0, ":"), (0.01, "-"), (0.1, "-.")):
    Xs, a = integrate_midplane(lambda X: 4.0, hh)
    ax2.plot(Xs, 2 - a, lw=1.1, ls=ls, label=rf"$h = {hh:g}$")
    if hh > 0:
        ax2.axhline(2 * hh / 3, color="gray", lw=0.5)
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlim(1e-3, 20)
ax2.set_ylim(1e-3, 3)
ax2.set_xlabel(r"$X$")
ax2.set_ylabel(r"$2 - a(X,0)$")
ax2.set_title(r"$w \equiv 4$: the margin against $2h/(w-1)$", fontsize=9)
ax2.legend(frameon=False, fontsize=8, loc="lower left")
fig.tight_layout()
fig.savefig(OUT / "fig_midplane.pdf")
print("wrote", OUT / "fig_midplane.pdf")
