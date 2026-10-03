# Final review of "A dividing-plane barrier in the OpenAI forced Navier-Stokes blow-up construction"

Reviewer: Claude Opus 5.5 (Anthropic), a fresh agent with no part in writing or revising the paper,
launched as the last review before the paper is sent. Friday 2026-10-02, 14:17 to 15:05 EDT
(America/New_York).

Baseline: `paper/ns-dividing-plane/main.tex` (297 lines) and `main.pdf` (12 pages, SHA-256
`406e6dc08daf1406df3ab95a6efbe4db4a1e35a9dd611e723c43b05d1f8882cf`) as committed at `3ab19fe`
(2026-10-02 14:15 EDT). The later commits up to `902b484` (15:03 EDT) leave main.tex, main.pdf and
the rest of the paper's directory unchanged, except that `902b484` committed an earlier draft of this
file; this file as it now stands is the review. Locations are main.tex line
numbers ("l.") and printed PDF pages ("p."). Finding IDs OF-1 to OF-18 are this review's: OF-1 is the
one MAJOR item, OF-2 to OF-18 are MINOR, numbered in the order they appear. This file proposes edits
and changes nothing.

Read for this review: the paper (all 12 pages as text, pp. 1, 6, 7, 9 and 11 also rendered and
inspected); the earlier reviews and their dispositions (`reviews/claude/REPORT.md` and `DISPOSITION.md`
with its consistency pass; `docs/research/2026-10-01-ns-open-map/reviews/astra/` REVIEW, DISPOSITION,
PROMPT and RESPONSE; `reviews/astra-2026-10-02/` REVIEW and DISPOSITION; the chat session's review
`docs/outreach/2026-10-02/opus-chat-handoff/02-OPUS-PAPER-REVIEW-2026-10-01.md` and its adjudication
`docs/outreach/2026-10-02/CHAT-COMMENTS-2026-10-02.md`); `paper/common/README.md`; the paper's README;
and, for the provenance claims, `docs/research/2026-09-30-navier-stokes-blowup/EXPLANATION-B.md`, the
lane README, `docs/research/2026-10-01-ns-open-map/OPEN-MAP.md` and the lane's registration
`docs/DESIGN-BLOWUP-PULLBACK.md`. Items those reviews settled are not repeated; everything below was
checked against the paper as it stands.

Tools: Python 3.12.10, sympy 1.14.0, mpmath 1.3.0, numpy 2.2.6, scipy 1.16.3, pytest 9.0.3,
PyMuPDF 1.27.2.3, pdftotext 4.00. The independent scripts written for this review (symbolic
identities, a re-integration of (17), a scan for unquoted source text) are scratch files, not part
of the record; their outputs are quoted where used.

**Summary.** 0 BLOCKING, 1 MAJOR, 17 MINOR. Every numbered statement (Lemma 3.1, Theorem 3.2(1) to
(4), Proposition 4.1, Lemma 4.2, Proposition 4.3) is correct under its stated hypotheses, and so is
every formula added on 2026-10-02. The MAJOR item is provenance, not mathematics: the harness's own
explanation of Appendix B, written the day before the paper, already sketched the barrier for
reflection-symmetric profiles, while the attribution block and Section 6 describe that explanation
as having only asked a question (OF-1). One sentence of Remark 3.6 has source and sink reversed
(OF-3). The paper should go out after the five edits listed in F.

## A. Statements against proofs.

| Statement | Verdict | What was checked |
|:--|:--|:--|
| Lemma 3.1 (l. 133-150, p. 6) | CORRECT | Vanishing of the leading azimuthal residual is pointwise the balance `(1/L){W D_X H + H_c H_eta + h(1 - 2 eta U) H} = (2/X) D_X(D_X - 1) H`: (4.14) (p. 27) for the material derivative, and `r (d_rr + d_r/r - 1/r^2)(q^{-h} H/r) = q^{-h-1} (2/X) D_X(D_X - 1) H` (rederived; sympy). With `H = 2X phi/C` this is (4.13)_1 exactly. At eta = 0: L = d = 1; `H_c(X,0) = U(X,0) = 0`; `W(X,0) = 1 - w` (the term `2 D eta A_X(U)` dies through eta, as the proof says); `1 - 2 eta U = 1`; `H_eta` enters only multiplied by `H_c`. No parity is used. |
| Theorem 3.2(1) (l. 155, 173; pp. 6-7) | CORRECT | `H' = D_X H` solves (16) with source `(hX/2) H >= 0`, and `H' = (2X/C)(phi + X phi_X) > 0` near the axis. At a first zero X_1 (including X_1 = X_a, by the one-sided derivative) `D_X H'(X_1) <= 0` contradicts `(h X_1/2) H(X_1) > 0` when h > 0. When h = 0, `dH'/dX = c(X) H'/X` with c continuous, and uniqueness on intervals bounded away from 0 forces `H' == 0` on (0, X_1]. Hence `a = 2 - 2H'/H < 2`. Only continuity of w is used. |
| Theorem 3.2(2) | CORRECT | `U(X,0) = 0` on the closed core gives `D_X U(X,0) = 0`, so `b_s = 0` where E > 0 and `v_s = a` where a > 0. |
| Theorem 3.2(3) (l. 157-160, 177-181; pp. 6-7) | CORRECT | The Riccati form `D_X l = l(1 - l - (X/2)(w - 1)) + hX/2` and (17) rederived from (14). (17) is the first equation of (B.25) (p. 151) at eta = 0 with `p_1 = a`, where `S_q = -(1 - w) l - h`. Frozen-supremum argument: on the maximal interval (X_0, X_1] with a > a_*, either X_0 > 0 with a(X_0) = a_*, or X_0 = 0 and then a_* = 0 because a(0+) = 0; there 0 < a < 2. Braces: if B > 1 + h, `(w - 1)(1 - a/2) < (B - 1)(1 - a_*/2) = h` (for w >= 1 both factors are dominated, the second strictly; for w < 1 the left side is negative); if 1 <= B <= 1 + h, `<= B - 1 <= h`; if B < 1, negative. With `-(1 - a/2) a < 0` this gives `D_X a < 0`, so `a(X_1) < a_*`. The case split is complete. The closing parenthetical is imprecise: OF-2. |
| Theorem 3.2(4) (l. 161-164, 183) | CORRECT | Theorem 4.6(i) gives smoothness and phi > 0, (ii) gives (4.13) on [0, X_a] (p. 33). If a(X_a,0) <= 0, the lower bound on a in (iii) and `a(X_a, eta) > 0` of Proposition 4.10(ii) (p. 37) fail; if a(X_a,0) > 0, `v_s = a < 2` breaks the bound on `v_s - 2` and `v_s(X_a, eta) > 2 + c_ex`. From the definitions above (7.1) on p. 74 (`lambda_0^2 = -2 F_0 N_theta (2 F_0 N_theta + abs(g_0))`, `N = g_0/abs(g_0)`, `g_0 = F_0(-a, b_s)`), sympy gives `lambda_0^2 = 2 a F_0^2 (1 - 2/v_s)`, hence `2 F_0^2 (a - 2)` at b_s = 0, and (15) gives `<= -4 h F_0^2/(B - 1)`. |
| Remark 3.3 | CORRECT | For phi = 1, U = (1 + h) eta: `W = 1 - (1 + h) L` and `S_q = -W - h(1 - 2(1 + h) eta^2) = 0` (sympy), so (4.13)_1 holds with both sides zero and a == 0; B = 1 + h, and (15) gives a <= 0, met with equality. |
| Remark 3.4 | CORRECT | If U is odd and phi, Pi are even, then W and S_q are even and H_c and S_n odd, so the class is consistent with (4.13) and (4.7) order by order; the remark calls this formal. (B.3) (p. 145) defines phi^* for every j_0 (the regularization sigma_* keeps it finite). j_0 > 0 enters through `Z_*(eta_0) >= c j_0 P_*^2 > 0` (Section B.1, p. 144), which fixes delta_* and sigma_* in (B.2) and so the two alternatives behind (B.19) (pp. 149-150). The hedge "we have not checked the existence argument at j_0 = 0" is the right size. |
| Remark 3.5, including the sentences added on 2026-10-02 | CORRECT | At h = 0, w = 4, (14) reads `D_X H' = (1 - 3X/2) H'`, so `H' = c X e^{-3X/2}` and `H = c'(1 - e^{-3X/2})` (sympy: solves (14)); `2 - a = 2 D_X H/H = 3X/(e^{3X/2} - 1)` (sympy: identity), positive for X > 0 and decreasing, so the supremum of a over (0, 20] is at X = 20, where `60/(e^30 - 1) = 5.6145738e-12` (mpmath, 40 digits): the remark's `(and $3\cdot20/(e^{30}-1)$ is the $5.6\cdot10^{-12}$ above)` is right. The bound at the axis strain 4 is 2h/3 < 1/150. The suprema 1.99310 and 1.93103 are reproduced in D. |
| Remark 3.6 | WRONG in one sentence; otherwise CORRECT | The advection-diffusion sentence reverses source and sink: OF-3. The Rayleigh and Ludwieg reading is credited to Duraiswami, pp. 21-22, with his `d log Gamma/d log X = 1 - a/2` (which is l; checked). Two precisions: OF-4. |
| Remark 3.7 | CORRECT | Scope matches the theorem. |
| Proposition 4.1 (l. 210-220, p. 9) | CORRECT | Theorem 4.6(v) asserts S(inf, eta) = 0, and "All assertions hold for every η ∈ [−1, 1]." (p. 32); U = V_0 = 0 on [X_v, inf); `E = c_inf X^{-A} H(2d/X)` with H(0) = 1 and 2A = 1 + 2h > 1, so both integrals converge; E > 0 for X > 0 is Theorem 4.6(i) (p. 33). |
| The two paragraphs after it (l. 222, 224; p. 9), including the factors added on 2026-10-02 | CORRECT | Flux: at fixed (z, t), q and eta are fixed and `X = r^2/(2q)` gives `r dr = q dX` (sympy); with `u_z = q^{-A} U` and `p = q^{-2A} Pi`, `int (u_z^2 + p) r dr = q^{1-2A} int (U^2 + Pi) dX = q^{-2h} S(inf, eta)`. The integration by parts and `X Pi -> 0` hold for the canonical pressure (4.25), where `Pi ~ -c_inf^2 X^{-2A}/(4A)`. The manuscript has the same identity in the proof of Lemma A.8 (p. 141): "∫ r(u_z^2 + p) dr = q^{1−2A} ∫ (U^2 − E^2/2) dX = 0" (layout simplified). Tail: `T_{0,z} = F X N_s/(LE) = X N_s/(L sqrt(2X))`, and `r T_z = sqrt(2qX) q^{-A-1/2} T_{0,z} = q^{-A} X N_s/L` (sympy). Locator: OF-12. |
| Lemma 4.2 (l. 226-239, p. 9), including the parenthetical added on 2026-10-02 | CORRECT | The N_s line of (4.16) (p. 28; eta factors read on the rendered page) holds for general U, E, Pi: sympy confirms `d_X(X N_s) = S_n` given `S_X = U^2 - E^2/2` and `Pi_X = E^2/(2X)`, not only on the checker's single test profile. `Z_{-2A} Pi = 0` is `4A eta Pi - d Pi_eta = -2 eta X Pi_X = -eta E^2`. The parenthetical: for `E^2 = c^2 X^{-2A} G(2d/X)` with arbitrary G, the substitution u = 2d/x turns `(1/2) int_X^inf E^2 dx` into `R = (1/2) c^2 (2d)^{-2h} int_0^{2d/X} u^{2A-2} G(u) du` (sympy, integrand identity; the integral converges at u = 0 because 2A - 2 = 2h - 1 > -1), and differentiating in eta gives `4 h eta R/d` from the prefactor and `-eta X E^2/d` from the upper limit, so `4 h eta R - d R_eta = eta X E^2` for every G (sympy). With the manuscript's heat factor H of (4.29), h = 0.1, eta = 0.4, X = 3, the two forms of R agree to 3e-8 and the identity's residual is 2e-8, both at the quadrature tolerance. |
| Proposition 4.3 (l. 241-251, p. 10) | CORRECT | In the exterior `V_0 = -(2 D eta M_inf + d M_inf')/L`, whose kernel `c(1 - eta^2)^D` is even; K == 0 is `sqrt(X) T_{0,z} -> 0`; `d S' = 4 h eta S` has solutions `c(1 - eta^2)^{-2h}`; S_inf is bounded. The last step's wording: OF-5. Observation, no change needed: since C^1 regularity at eta = +-1 alone forces M_inf == 0 (the proof's own parenthetical), the conclusion S(inf, eta) = 0 holds for every smooth profile with this exterior and no r^{-1} axial tail, symmetric or not; oddness is needed only for the contradiction at eta = 0. So the abstract's "alone forces the identity" is accurate. |
| Remark 4.4 | CORRECT | At h = 0, H == 1 in (4.29), so `E^2 = c_inf^2/X` and S_inf diverges for compactly supported U. |
| Remark 4.5 | CORRECT | Constantin, Ignatova and Vicol's Remark 2.6 assumes `u_z(0, t_0) != 0`, and their footnote 9 gives `u_z(0, t) = j_0 (-t)^{-1/2-h}` for this construction (p. 11), that is `j_0 tau^{-A}`. Proposition 4.1 gives axial velocity somewhere on each slice, not at the axis point. Liu's unbiased families are conditional examples of exactly that (OF-11). |

### OF-2 (MINOR, optional). The closing parenthetical of the proof of (3).

- Location: l. 181, p. 7.
- Claim: `(The strict barrier at $a=2$ is the case $B=\infty$ of the same computation: at $a=2$ the braces are exactly $-h$.)`
- Evidence: with a_* = 2 the frozen-interval computation does not apply: on an interval where a > 2 the
  factor 1 - a/2 is negative, `-(1 - a/2) a > 0`, and the braces have no sign. What works is a
  first-crossing argument at the level a = 2 itself, where (17) gives `D_X a = -hX`, negative for h > 0.
  At h = 0 this is zero (a == 2 solves (17) when h = 0), and strictness then comes only from the
  uniqueness argument of (1).
- Fix: `(For $h>0$ the strict barrier at $a=2$ can also be read off \eqref{eq:R}: at $a=2$ the braces are exactly $-h$, so $\DX a=-hX<0$ there; at $h=0$ strictness rests on the uniqueness argument of (1).)`

### OF-3 (MINOR, before sending). Remark 3.6 calls an absorption a source.

- Location: l. 199, p. 8.
- Claim: `A one-dimensional advection--diffusion profile with $H(0)=0$, no interior sink and a nonnegative source has no interior maximum, so the circulation rises monotonically outward.`
- Evidence: in the usual sign convention (steady balance diffusion - advection + source = 0) a
  nonnegative source permits an interior maximum: `H'' = -1` on (0, 2) with H(0) = 0 gives
  `H = x - x^2/2`, maximal at x = 1. In (14), written as `(2/X) D_X(D_X - 1) H - (1 - w) D_X H - h H = 0`,
  the h-term enters as `-hH`, a linear absorption: it is the similarity-frame image of the growth
  q^{-h} of the physical angular momentum q^{-h} H, which diffusion must resupply at every point. That
  sign is what forbids an interior maximum: at a critical point (14) gives `2 X H_XX = h H > 0`. The
  contrast is the mechanism of the manuscript's own biased core, where the transport term makes S_q a
  large positive source (`S_q >= 2.5 + .95 Lambda L chi`, (B.17), p. 148) and a can pass 2. "Source" is
  the right word only for the gradient equation (16), as the proof of (1) uses it. Read literally, as a
  fluid dynamicist will read it, the sentence states a false principle.
- Fix: replace the sentence with `In this balance the term $hH$ acts as a linear absorption, not a source: diffusion must supply $hH\ge0$ at every point to keep pace with the growth $q^{-h}$ of the physical angular momentum, and it cannot do so at an interior maximum (a nonnegative source would allow one). With $H(0)=0$ the circulation therefore rises monotonically outward.`

### OF-4 (MINOR, optional). Two precisions in Remark 3.6.

- Location: l. 199, p. 8.
- (a) Claim: `The steady Burgers vortex \cite{Burgers}, whose circulation $\Gamma=\Gamma_\infty(1-e^{-\alpha r^2/2\nu})$ is monotone, is the $h=0$, constant-strain instance.`
  Evidence: alpha is not defined, and the formula holds for the strain `u_r = -alpha r`, `u_z = 2 alpha z`.
  The h = 0, constant-strain solution of (14) is `H = c(1 - e^{-(w-1)X/2})` (for w = 4 the H of
  Remark 3.5), which in `r = sqrt(2qX)` has the Burgers shape with `alpha = (w - 1)/(2q)` and nu = 1: a
  collapsing flow with the Burgers profile at each instant, not the steady vortex itself.
  Fix: `The circulation of the steady Burgers vortex \cite{Burgers} in the strain $u_r=-\alpha r$, $u_z=2\alpha z$, $\Gamma=\Gamma_\infty(1-e^{-\alpha r^2/2\nu})$, is monotone, and it is the shape of the $h=0$, constant-strain solution $H=c(1-e^{-(w-1)X/2})$, with $\alpha=(w-1)/(2q)$ and $\nu=1$.`
- (b) Claim: `the transport term $-\Hc(\log E)_\eta$ of $\Sq$ is the one Proposition~B.3 of the manuscript makes of size $\Lambda L$`.
  Evidence: (B.21), p. 149, reads `−H_c(log φ)_η ≥ ΛLχ − Cχ − C_{σ*}√χ − C/Λ ≥ .95ΛLχ − C_{σ*}/Λ`
  (layout simplified), with `χ = H_*^2/(H_*^2 + σ_*^2)` from (B.2); at eta = 0, χ = j_0^2/(j_0^2 + σ_*^2),
  a fixed factor below 1.
  Fix: `of size $\Lambda L$, up to the fixed factor $\chi\le1$ of its (B.2)`.

### OF-5 (MINOR, recommended). Proposition 4.1 is invoked outside its hypothesis.

- Location: l. 250, p. 10.
- Claim: `Hence $S_\infty\equiv0$, and Proposition~\ref{prop:flux} applies.`
- Evidence: Proposition 4.1 assumes that "the leading profile satisfy Theorem 4.6(v)", which also asks
  for M(inf) = J(inf) = 0 and the subtracted angular identity of (4.28). The proof of Proposition 4.3
  establishes M_inf == 0 and S_inf == 0 only. The proof of Proposition 4.1 uses nothing but
  S(inf, eta) = 0 and the convergence of the two integrals, both available here, so the conclusion stands.
- Fix: `Hence $S_\infty\equiv0$, and the proof of Proposition~\ref{prop:flux}, which uses only $S(\infty,\eta)=0$, applies.`

## B. Abstract and introduction against the statements.

Quotations from the paper in this table render its mathematics in plain text.

| Claim | Where | Verdict | Against |
|:--|:--|:--|:--|
| The piecewise margin: "2 - a >= 2h/(B - 1) whenever the running supremum B ... exceeds 1 + h ... and with a <= 0 otherwise" | abstract (l. 23, p. 1); introduction (l. 40, p. 3), "and with a <= 0 when B <= 1 + h" | CORRECT | Theorem 3.2(3) and (15), both branches nonstrict as there. |
| "the explicit lower bound on the margin, where B > 1 + h, is linear in h", and nothing stronger | abstract (l. 23); introduction (l. 42): "the explicit lower bound on the margin ... is linear in h. The second fact is a loss of uniformity of the bound as h → 0; the theorem asserts nothing about the limit of the actual margin"; Remark 3.5 (l. 195) | CORRECT | A grep of main.tex for "proportional", "vanish" and "tends" finds no stronger claim, and Remark 3.5 displays the positive h = 0 margin `3X/(e^{3X/2} - 1)`. The paper's README still makes the stronger claim: OF-18. |
| The squared growth rate | introduction (l. 40): "the pulses' squared growth rate λ0² = 2aF0²(1 − 2/vs)" and "the squared growth rate is 2F0²(a − 2) < 0"; Section 2.2 (l. 106); Theorem 3.2(4) | CORRECT | p. 74: "take λ0 > 0" and "λ0² = 2aF0²(1 − 2/vs)" (layout simplified); the negative value is assigned to the square, never to the rate. |
| h >= 0 concerns the scalar equation | abstract: "The sign holds for every h >= 0 in the equation"; introduction: "for every h >= 0 in the dividing-plane equation"; Remark 3.5's last sentence | CORRECT | Theorem 3.2's "for any h >= 0 in (14)"; Remark 3.5 separates the equation from the leading-order approximation, whose neglect of axial viscosity needs the factor q^{2h} (p. 26). |
| The relaxed form's hypothesis | abstract: "for h > 0, the vanishing of the coefficient of the r^{-1} axial stress tail alone forces the identity" | CORRECT | Proposition 4.3's `sqrt(X) T_{0,z} -> 0`, the coefficient K, not the unweighted limit, which l. 224 says is not a hypothesis. "Alone" is accurate (see the observation under Proposition 4.3). |
| Scope | abstract's last sentence; introduction (l. 44); Remark 3.7 | CORRECT | Leading profile, one hypothesis, Theorem 4.6 as imposed; nothing about other flows, the summed background, or the unforced problem; "the sign of Rayleigh's criterion" is not a stability theorem. |
| The remaining abstract sentences | l. 23 | CORRECT | "strictly increasing" (Theorem 3.2(1)); "the sign of Rayleigh's centrifugal criterion that forbids growth, with Ludwieg's axial-shear term inactive" (a < 2, b_s = 0); "no energy source at the dividing-plane point of the inner edge ... clause (iii) ... fails at that point" (Theorem 3.2(4)); the moment obstruction credited to Duraiswami, p. 20. |

### OF-6 (MINOR, recommended). "The flow is an axisymmetric vortex."

- Location: l. 32, p. 2.
- Claim: `The flow is an axisymmetric vortex that collapses onto the origin in anisotropic similarity variables`
- Evidence: only the leading flow is axisymmetric. The manuscript, p. 3: "The leading flow u(0) is
  axisymmetric: its components depend on r, z, t, but not on θ." The pulses that complete the flow are
  not: "Their cylindrical velocity components have zero angular average" (p. 6), and "Angular periodicity
  requires kp to be an integer" (p. 74). Constantin, Ignatova and Vicol's analyticity argument turns on
  this distinction ("the solution is exactly axisymmetric in a collapsing core region", their abstract).
- Fix: `Its leading-order flow is an axisymmetric vortex that collapses onto the origin in anisotropic similarity variables`

### OF-7 (MINOR, recommended). A source sentence used without quotation marks.

- Location: l. 34, p. 2.
- Claim: `The pulses grow by extracting energy from the background shear, and near the plane $z=0$ that shear has to come from somewhere.`
- Evidence: the manuscript's p. 6 has "The pulses grow by extracting energy from the background shear."
  word for word. A scan of every seven-word run of main.tex against the OpenAI manuscript and the four
  cited preprints found no other unquoted verbatim run of prose (the other hits are the bibliography,
  the block quotation and transcribed formulas).
- Fix: ``` ``The pulses grow by extracting energy from the background shear'' \cite[p.~6]{OpenAINS}, and near the plane $z=0$ that shear has to come from somewhere. ```

### OF-8 (MINOR, optional). "this transport" has no antecedent in the abstract.

- Location: l. 23, p. 1.
- Claim: ``` because under exact reflection symmetry ``this transport would vanish at $z=0$'' ```
- Evidence: in the source the antecedent is the preceding sentence, "Away from the middle plane, axial
  flow carries angular momentum from more rapidly rotating layers, ..." (p. 5), which the abstract does
  not quote; a reader of the abstract alone cannot tell which transport is meant.
- Fix: ``` because under exact reflection symmetry the transport of angular momentum by the axial flow ``would vanish at $z=0$'' ``` (the quoted words stay verbatim).

### OF-9 (MINOR, optional). An unexplained comparison.

- Location: l. 42, p. 3.
- Claim: `And the role of the anisotropy exponent $h$ is the opposite of its role elsewhere in the construction:`
- Evidence: the paper never says what the role of h elsewhere is, and what follows the colon says only
  that the sign does not need h and that the bound is linear in h.
- Fix: `And the anisotropy exponent $h$ plays no part in the sign:`

### OF-10 (MINOR, optional). "it is verified by a program".

- Location: l. 40, p. 3.
- Claim: `The theorem uses only the manuscript's displayed formulas, and it is verified by a program that rederives those formulas from the manuscript's Lemma~4.1 and solves the full stress-free system as an exact power series with symmetric axis data.`
- Evidence: the program checks the derivation symbolically and tests the conclusion on fifteen sampled
  strains and on a 12-term series (Section 5); "verified" can be read as a check of the theorem itself,
  which Section 5's last paragraph rightly disclaims.
- Fix: `The theorem uses only the manuscript's displayed formulas, and its derivation is checked by a program that rederives those formulas from the manuscript's Lemma~4.1, tests the conclusion on fifteen strain profiles, and solves the full stress-free system as an exact power series with symmetric axis data.`

## C. Sources.

**Copies.** The OpenAI manuscript at the scratchpad path has SHA-256
`0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`, the bibliography's value; re-fetched
from the bibliography's URL at about 14:42 EDT it returned HTTP 200, 2,959,204 bytes, the same SHA-256 and 166
pages, printed page = PDF page. Fetched from arxiv.org at 14:25 EDT and saved under the reviewer's
scratch directory: Duraiswami 2609.17642v1 (31 pp., SHA-256 `a38af23a...ba166fe95`), Lei and Ren
2609.35406v2 (245 pp., `8396b998...e64e8d`), Constantin, Ignatova and Vicol 2609.20803v2 (34 pp.,
`5454d7c0...8dda`), Liu 2609.14292v1 (32 pp., `cd569ce5...314f31`). Their abstract pages give the
bibliography's titles, authors and versions (Lei and Ren's listing title has "Part I:", their PDF title
page "Part I."; the bibliography follows the listing); v1 is the only version of Duraiswami and of Liu,
v2 the latest of the other two. Spot-checked folios equal PDF pages.

**Quotations**, compared word for word on the cited page, with symbols, case and punctuation by eye
(the first column renders mathematics in plain text):

| Quotation in the paper | Source | Result |
|:--|:--|:--|
| The abstract's four fragments; the block quotation (l. 36) | OpenAI p. 5 | verbatim |
| "angular velocity decreases sufficiently rapidly with radius" (Remark 3.6) | OpenAI p. 6 ("If angular velocity decreases sufficiently rapidly with radius, this outward motion increases the surplus ...") | verbatim |
| Theorem 4.6(ii) and (iii) | OpenAI p. 33 | verbatim |
| (v): "for some fixed X_v in (X_a, X_b), U = V_0 = 0 throughout [X_v, inf)" | OpenAI p. 33 (continues ", including the outer collar [Xv, Xb].") | verbatim |
| Proposition 4.10(ii): "a(X_a, eta) > 0 and v_s(X_a, eta) > 2 + c_ex for a constant c_ex > 0" | OpenAI p. 37, after "At its inner endpoint," | verbatim |
| "required by the viscous waves" | OpenAI p. 31 ("The additional inequality is required by the viscous waves.") | verbatim |
| "a profile with U odd in eta has U(X,0)=0, so S(inf,0) = -int_0^inf E(X,0)^2/2 dX" and "The leading profile of the OpenAI 2026 construction therefore carries axial velocity on the dividing plane: the core is an axial through-flow" | Duraiswami p. 20 | verbatim |
| "The positive shift j separates the zero of H_0 from the pressure symmetry point Z = 0, so that axial shear can supply the missing contribution there" | Lei and Ren p. 108 | verbatim |
| "If the shift were zero, the zero of H_0 would be Z = 0, where evenness of P_0 would give g(0) = 0; the two shear mechanisms would then weaken at the same point" | Lei and Ren p. 109 | verbatim; their "no uniform limit as j ↓ 0 is asserted" (p. 108) is paraphrased, correctly, not quoted |

Lei and Ren call their own paper "a readable and accessible version of the profile-construction part"
of the manuscript (their abstract), so "their readable account" (l. 38) is their description.

**Locators.** In the OpenAI manuscript: (4.1), p. 24; D_X, Lemma 4.1 and (4.2), (4.3)-(4.4) and (4.6),
p. 25; phi > 0, (4.7), (4.8), (4.9)-(4.10), the q^{2h} viscosity comparison and `l = 1 + X F_X/F`, p. 26;
(4.11), Proposition 4.2, (4.13), (4.14), p. 27; (4.15), Lemma 4.3, (4.16) and the integration by parts,
p. 28; the r^{-2} and r^{-1} tails and (4.20), p. 30; (4.21) and the viscous-waves sentence, p. 31;
Theorem 4.6, pp. 32-34, with (i), (ii), (iii), (v), (4.25), (4.28)-(4.29) on p. 33; Proposition 4.10(ii),
p. 37; the display above (7.1), p. 74; (B.1) and Section B.1, p. 144; (B.3), p. 145; Proposition B.2,
p. 146; Proposition B.3, p. 148, with (B.19) and (B.21), p. 149; (B.25), p. 151; the scalings, p. 4
(inside the cited pp. 4-5); Section 5, "Correcting the base flow to every order". All resolve and say
what the paper uses them for, except Lemma A.8 (OF-12). In Duraiswami: p. 6 (characteristics "emanate
from the curve Dη + dU = 0 near the dividing plane η = 0", and "The sign of the axial profile U(X, 0) on
the dividing plane decides which way information leaves it"); p. 20 (the moment argument); p. 21 (the
cone "fails on every matched profile" and the Rayleigh and Ludwieg reading with
`d log Γ/d log X = 1 − a/2`); p. 22 (the rate "real exactly where a > 0 and vs > 2, so the Ludwieg
condition of the cone is the condition that the pulses can grow at all"). His p. 21 also discusses the
dividing plane at the outer edge X_b; the paper's theorem concerns the inner edge and the stress-free
core and does not need that passage (the manuscript's own construction has `2 + h < a <= 2 + 2h` on
`e^{1/2} X_tail <= X < X_b`, Lemma 4.9, p. 36), so no citation is recommended. In Lei and Ren: (8.9)-(8.10)
and the zero-shift sentence, p. 108; the second quotation, p. 109. Constantin, Ignatova and Vicol: Remark
2.6 and footnote 9, p. 11.

**Classical references.** Crossref records: Rayleigh, "On the dynamics of revolving fluids", Proc. R.
Soc. Lond. A 93 (648), 148-154, 1917 (DOI 10.1098/rspa.1917.0010, author J. W. Strutt); Leibovich and
Stewartson, "A sufficient condition for the instability of columnar vortices", J. Fluid Mech. 126,
335-356, 1983 (DOI 10.1017/S0022112083000191); Burgers, "A Mathematical Model Illustrating the Theory
of Turbulence", Advances in Applied Mechanics 1, 171-199, 1948 (DOI 10.1016/S0065-2156(08)70100-5). All
match the bibliography. Ludwieg has no DOI: the 1961 entry is confirmed by the reference list Cambridge
deposited for Leibovich and Stewartson (Ludwieg 1961, "Ergänzung zu der Arbeit: 'Stabilität der Strömung
in einem zylindrischen Ringraum'", Z. Flugwiss. 9, 359-361; the deposited string has its umlauts
damaged), and the 1960 entry by the reference list of Billant and Gallaire, "A unified criterion for the
centrifugal instabilities of vortices and swirling jets", J. Fluid Mech., on Cambridge Core (Ludwieg 1960,
"Stabilität der strömung in einem zylindrischen ringraum", Z. Flugwiss. 8, 135-140). The paper's short
"Ergänzung" for the 1961 title is identifiable; German titles are source titles.

**What could not be reached.** The original texts of Rayleigh 1917, Ludwieg 1960 and 1961, Leibovich and
Stewartson 1983 and Burgers 1948 (bibliographic records only; publisher full texts not attempted). The
arXiv API's id_list query once returned an empty body; the abstract pages were used instead. No captcha
was met.

**Anything new since the earlier receipts.** The arXiv API query `all:"Navier-Stokes" AND all:OpenAI`,
newest first (14:45 EDT), lists nothing after Lei and Ren's v1 of 2026-09-28; one web search
(dividing plane, symmetric core, axial bias, October 2026) returned only the cited works.

### OF-11 (MINOR, recommended). Liu's families include axis data without bias.

- Location: l. 283, p. 12.
- Claim: `Liu's conditional families \cite{Liu} do not touch the symmetric case.`
- Evidence: true of reflection symmetry, but it leaves out the item of that paper closest to the
  hypothesis (13). Liu's Theorem 3.1(ii), p. 6: "There are a fixed nonzero tilt γ > 0 and j∗ > 0 such
  that one canonical axis pressure trace Πγ = Πref + γη supports every Gj = 4η + j, |j| ≤ j∗."; (iii),
  p. 6: realizations "with G = mη", "At fixed h and nonzero pressure tilt"; at j = 0 "the origin is an
  exact stationary material particle" (p. 8); and "An auxiliary core at γ = 0 is used only for this
  parity estimate, not as a completed exit." (p. 19). Here G(η) = U(0, η) and Πref is even (Liu's (68),
  p. 16). So Liu (conditionally on his completion input) has cores without bias at the axis whose
  symmetry is broken by the pressure tilt. By (8)_2 at X = 0, eta = 0, with U(0,0) = 0 and
  Pi_eta(0,0) = gamma, `-2 U_X(0,0) = S_n(0,0) = -gamma`, so `U_X(0,0) = gamma/2 != 0` and (13) fails; the
  checker's own series solver, given U^* = 4 eta and the tilted datum, returns U_1(0) = 1/20 for
  gamma = 1/10 (D). These families are consistent with Theorem 3.2 and Proposition 4.1, and they show
  that what the theorem forces is axial velocity on the dividing plane of the core, not the upward bias
  at the axis point.
- Fix: ``` Liu's conditional families include axis data without bias, $G=4\eta+j$ at $j=0$ and $G=m\eta$, realized with a nonzero tilt $\gamma\eta$ of the axis pressure \cite[Theorem~3.1(ii)--(iii), p.~6]{Liu}; by \eqref{eq:413}$_2$ at the axis the tilt gives $\partial_XU(0,0)=\gamma/2\ne0$, so \eqref{eq:hyp} fails for them, and his zero-tilt core is used ``only for this parity estimate, not as a completed exit'' \cite[p.~19]{Liu}; what Theorem~\ref{thm:barrier} forces is axial velocity on the dividing plane of the core, not the bias at the axis point. ``` Optionally, Remark 4.5 can name Liu's j = 0 member \cite[p.~8]{Liu} as a conditional example of a dividing plane with no axial velocity at the axis point.

### OF-12 (MINOR, recommended). Lemma A.8 is stated on p. 140.

- Location: l. 224, p. 9.
- Claim: `\cite[p.~30 and Lemma~A.8, p.~141]{OpenAINS}`
- Evidence: the statement of Lemma A.8 ("Suppose the leading axisymmetric field is smooth at the axis,
  ...") is at the foot of p. 140; the removal of the tails and the flux identity are in its proof on
  p. 141.
- Fix: `\cite[p.~30 and Lemma~A.8, pp.~140--141]{OpenAINS}`

## D. The checker.

- Run: `python docs/research/2026-10-01-ns-open-map/checks/midplane_barrier.py --json <scratch path>`
  (Windows, Python 3.12.10), 14:29 EDT. Exit 0; 53 Boolean leaves in the receipt, all true (9 in part A,
  2 for each of the 15 cases of B1, 7 in B2, 6 in C, and `all_checks_pass`); 1.47 CPU seconds. Compared
  leaf by leaf with the committed receipt `checks/midplane_barrier.json`: identical except
  `generated_utc`, `cpu_seconds` and `B2.series_cpu_s`. Among them: radius estimate 0.28836,
  `X_max` 0.14418, sup of the series a 0.26602, series against the integrated (14) 3.90e-12,
  `phi_1(0) = -299/400`, `w = 4 + (351/40) X + ...`, biased datum `U_0(0) = 1/20`, `U_1(0) = 451/4000`
  (hand check: `U_1(0) = (A + 4) j_0/2 = 4.51/40`), as Section 5 reports.
- Arena: the five tests are `tests/test_ns_midplane_barrier.py` at the repository root (there is no
  `tests/` under `docs/research/2026-10-01-ns-open-map/`):
  `python -m pytest tests/test_ns_midplane_barrier.py -q -p no:cacheprovider` gives 5 passed in 1.65 s.
  Neither run changed a tracked file.
- Re-integration of (17) at w = 4, written for this review: u = log l with l = 1 - a/2, in y = log X
  from X = 1e-8 with `l = 1 + (1 - w + h) X/4` (the axis expansion of the Riccati form), scipy Radau,
  rtol 1e-12, 20001 points to X = 20; cross-checked by mpmath `odefun` at 40 digits.

  | h | sup of a over X <= 20 | paper | bound 2 - 2h/3 |
  |:--|:--|:--|:--|
  | 0.01 | 1.993095 (at X = 20) | 1.99310 | 1.993333 |
  | 0.1 | 1.931031 (at X = 20) | 1.93103 | 1.933333 |
  | 0 | 2 - 5.6145738e-12 (mpmath margin at X = 20; equals 60/(e^30 - 1)) | 2 - 5.6e-12 | 2 |

  At h = 0.01 the margin 2 - a at X = 1, 5, 10, 15, 20 is 0.866, 0.0162, 0.00719, 0.00699, 0.00690,
  falling toward the bound 2h/3 = 0.00667 from above, as Figure 1's caption says.
- With the checker's series solver and the unbiased axial datum `U^* = 4 eta`, adding a tilt
  `gamma eta` to the even pressure datum (gamma = 1/10) gives `U_n(0) = 0, 1/20, 151/16000, ...` for
  n = 0, 1, 2: a pressure tilt alone breaks (13) (used in OF-11). With gamma = 0 every U_n(0) is 0.
- What the checker does not cover is stated correctly in Section 5. The exterior cancellation of
  Lemma 4.2, which it does not test, is checked under A for arbitrary G, and (4.16) for general profiles.
  Outside the paper: the docstrings of the checker and the arena still state the shorthand
  `a <= max(0, 2 - 2h/(sup w - 1))` that the 2026-10-01 cross-vendor review retired (it is wrong for
  B < 1); the code itself is piecewise.

### OF-13 (MINOR, optional). "nine identities" names eight.

- Location: l. 266, p. 10.
- Claim: `\emph{Symbolic (sympy), nine identities.}` followed by a list of eight.
- Evidence: part A has nine flags; the one not named is `A5_source_at_a_equals_2_is_minus_h`.
- Fix: before `; and the integration by parts behind $S$` insert `; at $a=2$ the dividing-plane source is $-h$`.

## E. The attribution block against paper/common/README.md.

Checked and correct: the title block is the house's (writer Claude Fable 5.1, Anthropic; at the
direction of David Ross; Hypnos Math; date); the first sentence of the block and the division of labor
follow pattern item 1; the question's origin in the lane is stated (but see OF-1); the self-review's
clause matches its report (0 BLOCKING, 3 MAJOR as listed, 17 MINOR); the cross-vendor clause matches
Astra's review of 2026-10-01 (barrier correct; moment obstruction already Duraiswami's; tail hypothesis
corrected; the four repairs); the 2026-10-02 clause matches Astra's verdict (every numbered statement
correct; two MINOR items, both applied); "No human mathematician has reviewed this paper." is verbatim;
no paper is called the first; the place in the set ("the only manuscript so far from the harness's
second problem lane, written two days after the three manuscripts of 2026-09-28/29") is accurate, and the
open-question map did rank the question first (`OPEN-MAP.md` l. 112: "EXB.Q3 (27)"). US English: a scan
of main.tex finds no British spelling; "gray" in the caption is US. Em dashes: main.tex is pure ASCII
with no `---`, and the PDF's text has no U+2014 (its 31 dashes are en dashes). The Clay alternatives are
never stated (grep for Clay, Millennium, alternative, "(A)", "(B)"), and nothing is claimed about the
Navier-Stokes problem itself.

### OF-1 (MAJOR, before sending). The harness had already sketched the barrier; the block and Section 6 say it only asked.

- Location: attribution block, l. 27, pp. 1-2: `the explanation of its Appendix~B asked whether the midplane bias is forced` and `and without reading any treatment of the symmetric core beyond the sources cited`; Section 6, l. 283, p. 12: `the explanation of Appendix~B asked, as its third open question, whether the midplane bias is forced and whether higher-order terms or an inner stress could evade it`.
- Evidence: `docs/research/2026-09-30-navier-stokes-blowup/EXPLANATION-B.md`, committed in `1656b76` on
  2026-09-30 at 16:41 EDT, the day before the paper and unchanged since, l. 17: "Our reading sharpens
  this: a stress-free profile obeys DXa = XSq/L − (1 − a/2)a [pp. 26, 27, 149, 151]. At a = 2 the term
  −Wl, the order-one part of the angular source Sq, vanishes, leaving −Hc(log E)η − h(1 − 2ηU). Symmetry
  makes Hc = 0 at η = 0, so there Sq = −h < 0 whenever a = 2: a never reaches 2, bs = 0, and the edge
  inequality fails." Its question 3 (l. 62) opens: "Our reading gives a < 2 on the midplane for symmetric
  stress-free profiles at leading order; could higher-order terms or an inner stress evade this?" That
  is the first-crossing form of Theorem 3.2(1), (2) and (4) for h > 0 under reflection symmetry, in the
  harness's record before the paper was written; the paper's own parenthetical at l. 181 is the same
  argument. The open-question map, which the block names as where the question was ranked, lists the
  explanation's reading among the question's sources ("EXB (our reading)", `OPEN-MAP.md` l. 59), and
  the research attempt the paper was written from cites the explanation's question 3
  (`docs/research/2026-10-01-ns-open-map/attempts/midplane-obstructions.md` l. 7). The house pattern
  (`paper/common/README.md`, item 2) asks the block to say "whether the mathematics is the session's or
  the harness's"; as it stands the block credits the harness with the question and the writing session
  with all of the mathematics, and its last sentence says the paper was written without reading any
  treatment of the symmetric core beyond the sources cited, which the explanation is. What remains the
  paper's is substantial: the hypothesis (13) in place of symmetry, the monotonicity of H for every
  h >= 0 including h = 0, the margin (15) with the running supremum, the case split and growth-rate
  consequences of Theorem 3.2(4), Remark 3.4's formal series, and Section 4's relaxed form.
- Severity: MAJOR. It is the provenance of the main result; no statement or proof changes.
- Fix, three replacements:
  1. l. 27: `the explanation of its Appendix~B asked whether the midplane bias is forced, and the open-question map of 2026-10-01 ranked that question first.` becomes `the explanation of its Appendix~B sketched why a reflection-symmetric stress-free core cannot reach the threshold $a=2$ on the dividing plane (there the angular source is $-h<0$ wherever $a=2$) and asked whether the midplane bias is forced, and the open-question map of 2026-10-01 ranked that question first; the paper proves that sketch under a weaker hypothesis and for every $h\ge0$, and adds the margin.`
  2. l. 27, last sentence: `and without reading any treatment of the symmetric core beyond the sources cited.` becomes `and without reading any treatment of the symmetric core beyond the sources cited and the harness's own explanation of Appendix~B.`
  3. l. 283: `the explanation of Appendix~B asked, as its third open question, whether the midplane bias is forced and whether higher-order terms or an inner stress could evade it.` becomes `the explanation of Appendix~B had already sketched the barrier for reflection-symmetric profiles (on the dividing plane the source of the equation for $a$ is $-h<0$ wherever $a=2$, so $a$ never reaches $2$, $\bs=0$, and the inner-edge inequality fails) and asked, as its third open question, whether the midplane bias is forced and whether higher-order terms or an inner stress could evade it; what this paper adds is the hypothesis \eqref{eq:hyp} in place of symmetry, the case $h=0$, the monotonicity of $H$, the margin \eqref{eq:margin}, and the consequences in Theorem~\ref{thm:barrier}(4).`

### OF-14 (MINOR, before sending). "an autonomous research harness" against the lane's registration.

- Location: l. 283, p. 11.
- Claim: `The questions behind this paper were produced inside Hypnos, an autonomous research harness, in its second problem lane.`
- Evidence: the lane's registration, `docs/DESIGN-BLOWUP-PULLBACK.md` l. 381-383, on the explanations:
  "Ungraded, assisted research, reported as such (paper ledger C's rule); never counted as autonomous
  production."; the lane README, l. 35: "assisted research, ungraded, never autonomous production." The
  block does say that David Ross set the task and ran the process, but this sentence reads as autonomous
  production of the questions. It sits beside the third replacement of OF-1 and costs one clause.
- Fix: `The questions behind this paper were produced inside Hypnos, an autonomous research harness, in its second problem lane, whose outputs are registered as assisted research, not autonomous production.`

### OF-15 (MINOR, before sending). The chat session's comments carry no vendor and no verdict.

- Location: l. 27, p. 2.
- Claim: `applied the same day together with the comments of a Claude Opus 5.5 chat session of 2026-10-01.`
- Evidence: pattern item 3: "The reviews, named by model and vendor, with their verdicts in one clause
  each". The session's text (`02-OPUS-PAPER-REVIEW-2026-10-01.md`) opens its section on this paper with
  "It checks out."; it re-derived the main identities, reproduced the three suprema of Remark 3.5,
  extended Lemma 4.2's cancellation to every exterior of the same similarity form, and corrected the
  introduction's "both facts" sentence (dispositions in `reviews/astra-2026-10-02/DISPOSITION.md`,
  section B). The other papers' blocks omit the same clause.
- Fix: `applied the same day together with the comments of a Claude Opus 5.5 chat session of 2026-10-01 (an Anthropic model), which found no mathematical error, reproduced the suprema of Remark~\ref{rem:h}, extended the cancellation in the proof of Lemma~\ref{lem:Ns} to every exterior of the same similarity form, and corrected the introduction's sentence on the loss of uniformity.`

### OF-16 (MINOR, recommended). The consistency pass is not named.

- Location: l. 27, p. 2.
- Claim: the block names the self-review, the two reviews by GPT-6 Astra and the chat session, and no
  other review.
- Evidence: a fresh Claude Opus 5.5 agent checked the abstract, every quotation and every locator against
  the sources (62 checks, ledger appended to `reviews/claude/DISPOSITION.md`), and fifteen corrections were
  applied in `7c3931b` (2026-10-01 23:27 EDT), among them "squared growth rate", "from above", five
  repairs that made quotations verbatim and three page locators. Every other review is named in the block.
  Outside the paper: that ledger's heading reads "Consistency pass, 2026-10-02" although its commit is
  2026-10-01 23:27 EDT; the parallel heading in the unfolded-zeros ledger was corrected to the Eastern date
  in `65a7b20`, and the package's file name for this ledger,
  `self-review-by-Claude-DISPOSITION-applied-and-2026-10-02-pass.md`, carries the same date.
- Fix: after the sentence on the 2026-10-01 cross-vendor review add `A consistency pass on 2026-10-01 by a fresh Claude Opus 5.5 agent checked the abstract, every quotation and every page locator against the sources and found fifteen corrections, all applied.`; date the ledger heading 2026-10-01.

### OF-17 (MINOR, recommended). "both reviewers" and "either reviewer's" now undercount.

- Location: l. 269, p. 11: `were checked against the manuscript by both reviewers`; l. 279, p. 11: `(both reviewers did)`; l. 283, p. 12: `Neither the writer's search nor either reviewer's found`.
- Evidence: three reviews before this one read the manuscript and checked Lemma 4.2 against it (the
  self-review; Astra on 2026-10-01; Astra on 2026-10-02, whose Section D also ran a literature search),
  and this review did the same.
- Fix: `by every reviewer`; `(every reviewer did)`; `Neither the writer's search nor any reviewer's found`.

### OF-18 (MINOR, before sending). The paper's README ships in the package and still says what NS-1 removed from the paper.

- Location: `paper/ns-dividing-plane/README.md` l. 26-27 and l. 52-79; `paper/common/package_set.py`
  copies this README into the reader's package as the paper folder's README.md.
- Claim (l. 26-27): `The sign holds for every h >= 0 in the equation; where B > 1 + h the margin is proportional to h (for 1 < B < 1 + h the formula 2h/(B - 1) exceeds 2 and is not a bound; a <= 0 is).`
- Evidence: Remark 3.5 now says "the theorem asserts neither that the actual margin tends to zero nor any
  spectral stability" and displays the positive h = 0 margin. The README's Reviews section (l. 52-79)
  still describes two reviews ("both are applied, and both ledgers accompany the source"), omits the
  2026-10-02 review, the consistency pass, the chat-session comments and this review, and points to
  `reviews/claude/REVIEW-astra.md`, which is not in this directory (it is
  `docs/research/2026-10-01-ns-open-map/reviews/claude/REVIEW-astra.md`) and is not packaged.
- Fix: l. 26-27 becomes `The sign holds for every h >= 0 in the equation; where B > 1 + h the explicit lower bound 2h/(B - 1) on the margin is linear in h (the theorem says nothing about the limit of the margin itself: at h = 0 and w = 4 the margin is 3X/(e^{3X/2} - 1) > 0); for 1 < B < 1 + h the formula 2h/(B - 1) exceeds 2 and is not a bound; a <= 0 is.` In the Reviews section, add one bullet each for `reviews/astra-2026-10-02/` (every numbered statement correct, two MINOR items, applied), the consistency pass in `reviews/claude/DISPOSITION.md`, the chat-session comments (adjudicated in `reviews/astra-2026-10-02/DISPOSITION.md`, section B) and `reviews/opus-final-2026-10-02/`, and give REVIEW-astra.md its full path.

## F. Verdict.

**BLOCKING: 0.** No statement is false and no proof has a gap.

**MAJOR: 1.**
- OF-1: the harness's explanation of Appendix B already sketched the barrier for symmetric profiles; the
  attribution block and Section 6 credit it with a question only, and the block's independence sentence
  is not accurate.

**MINOR: 17.**
- OF-2: the "B = infinity" parenthetical in the proof of (3) is a first-crossing remark valid for h > 0 only.
- OF-3: Remark 3.6 calls the absorption term hH a source; a nonnegative source would permit a maximum.
- OF-4: Remark 3.6 leaves the Burgers strain alpha undefined, and "of size Lambda L" omits the factor chi.
- OF-5: Proposition 4.3's proof invokes Proposition 4.1 outside its hypothesis; its proof applies.
- OF-6: "The flow is an axisymmetric vortex": only the leading flow is.
- OF-7: a p. 6 sentence of the manuscript is used verbatim without quotation marks.
- OF-8: "this transport" in the abstract has no antecedent.
- OF-9: "the opposite of its role elsewhere in the construction" is never explained.
- OF-10: "it is verified by a program" overstates what the program does.
- OF-11: Liu's families include unbiased axis data whose pressure tilt breaks (13); the clause omits it.
- OF-12: Lemma A.8 is stated on p. 140, not p. 141.
- OF-13: "nine identities" lists eight.
- OF-14: "an autonomous research harness" against the lane's registration as assisted research.
- OF-15: the chat session's comments lack a vendor and a verdict clause.
- OF-16: the consistency pass of 2026-10-01 is not named (and its ledger heading carries the UTC date).
- OF-17: "both reviewers" and "either reviewer's" undercount the reviews.
- OF-18: the packaged README still says the margin is proportional to h and lists only two reviews.

**Should it go to Duraiswami and to Lei and Ren as it stands?** Not quite. The mathematics can go as it
stands, but the smallest set of edits before sending is: OF-1 (the three replacements), OF-3 (one sentence
of Remark 3.6), OF-14 (one clause, beside OF-1's third replacement), OF-15 (one clause) and OF-18 (two
places in the README, which ships in the package), with a rebuild and one more clause in the attribution
block naming this review. A clause in the house form, to be adjusted to the disposition: `A final review on 2026-10-02 by Claude Opus 5.5, an Anthropic model, fresh to the paper, found every numbered statement correct, one major item (the harness's explanation of Appendix~B had already sketched the barrier for reflection-symmetric profiles, which the provenance did not say) and seventeen minor ones.` If an
optional item is left unapplied, "Every finding was applied" in the block needs the matching change.
Recommended in the same pass, because these readers will notice them: OF-5, OF-6, OF-7, OF-11, OF-12,
OF-16 and OF-17. Optional: OF-2, OF-4, OF-8, OF-9, OF-10 and OF-13.

**Mechanics and page budget.** Every original quoted in a "Claim" line above occurs exactly once in
main.tex at `3ab19fe`, so each replacement applies mechanically. A scratch copy with every proposed edit
applied builds with tectonic with only the two TeX warnings the committed version already has (the
0.37 pt overfull box at l. 141 and the underfull box at l. 288-289). The paper is full, though: the
before-sending set alone, including the clause naming this review, moves the last bibliography entries
onto a 13th page, and so did every shorter wording tried (the shortest kept each edit to about one
added line), with or without a narrower figure. Either accept 13 pages, which means changing "12-page
note" in `docs/outreach/2026-10-02/emails.md` (l. 26, 120 and 141) and the page count in `paper/STATUS.md`
(l. 16), or trim about seven lines elsewhere in the same pass.

**Confirmations (checked and found correct).**
- Lemma 3.1 and the balance behind it, rederived from (4.14) and the radial viscous identity (12).
- Theorem 3.2(1) for h > 0 and for h = 0, including the closed endpoint X_a; (2); (3) with the Riccati form,
  (17), its agreement with (B.25), and all three cases of B; (4) with the case split and the growth-rate
  algebra from the p. 74 definitions.
- Remarks 3.3, 3.4, 3.5 (all three suprema, the h = 0 solution, `60/(e^30 - 1) = 5.6146e-12`), 3.7, 4.4
  and 4.5; the Rayleigh and Ludwieg credit in Remark 3.6.
- Proposition 4.1; the flux factor `q^{-2h}` and the tail factor `r T_z = q^{-A} X N_s/L`; Lemma 4.2 with
  (4.16) for general profiles and the cancellation for every similarity exterior; Proposition 4.3, whose
  conclusion does not even need oddness.
- The abstract and introduction, claim by claim (B), including the piecewise margin, the wording
  "explicit lower bound ... linear in h", the squared growth rate, h >= 0 for the scalar equation, the
  relaxed form's hypothesis and the scope.
- Every quotation verbatim (C); every locator except Lemma A.8's page; all bibliographic data; the pinned
  OpenAI hash, still served at its URL.
- The checker (53 of 53 flags, numbers identical to the receipt), the arena (5 of 5) and an independent
  re-integration of (17).
- The house format: the title block, the human-review sentence, no "first", US English, no em dash, no
  Clay alternatives, nothing claimed about the Navier-Stokes problem itself.
