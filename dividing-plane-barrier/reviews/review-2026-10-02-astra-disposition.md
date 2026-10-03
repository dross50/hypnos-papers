# Disposition of the 2026-10-02 reviews: Astra's fresh review and the chat-side comments

Applied by Claude Fable 5.1 (the outreach session) on Friday 2026-10-02, Eastern time, to
`main.tex` at the state after 7c3931b. Every finding was checked against the source line, and
every formula was re-derived from the paper's own definitions, before it was applied. The
delivered texts (`REVIEW.md` here; the chat session's text under
`docs/outreach/2026-10-02/opus-chat-handoff/`) are not rewritten.

## A. Astra's review (`REVIEW.md`, GPT-6 Astra, 2026-10-02 00:15 EDT)

| Item | Severity | Verdict | What was checked | What changed |
|---|---|---|---|---|
| NS-1 | MINOR | CORRECT, applied | The theorem gives a lower bound `2h/(B-1)` on `2 - a`; the abstract, the introduction and Remark 3.5 said the *margin* is proportional to `h` and "vanishes with the anisotropy". Counterexample checked: at `h = 0`, `w = 4`, equation (14) reads `D_X H' = (1 - 3X/2) H'`, so `H' = c X e^{-3X/2}`, `H = c'(1 - e^{-3X/2})`, and `2 - a = 2 D_X H / H = 3X/(e^{3X/2} - 1) > 0` at every fixed `X > 0` while the bound is `0`; at `X = 20` this is `5.6e-12`, the value Remark 3.5 already reports. | In the three places the text now says the explicit lower bound is linear in `h`; the introduction's "both facts" sentence now says the second fact is a loss of uniformity of the bound; Remark 3.5's closing sentence now says the bound degenerates as the anisotropy tends to zero and that the theorem asserts neither convergence of the actual margin nor spectral stability, with the `h = 0`, `w = 4` solution displayed. |
| NS-2 | MINOR | CORRECT, applied | From the paper's own (2): `u_z = q^{-A} U`, `p = q^{-2A} Pi`, and `X = r^2/(2q)` gives `r dr = q dX` at fixed `(z,t)`, so `int (u_z^2 + p) r dr = q^{1-2A} S(infinity, eta) = q^{-2h} S(infinity, eta)`; and from (11) in the exterior `T_{0,z} = X N_s/(L sqrt(2X))` with `r = sqrt(2qX)`, so `r T_z = q^{-A} X N_s / L`. The paper had identified the normalized quantities with the physical ones without these positive factors; every zero condition is unaffected. | The flux sentence now carries `q^{-2h}` with its derivation; the tail sentence now gives `r T_z = q^{-A} X N_s / L` and says the tail coefficient is the constant times the positive factor `q^{-A}/L`. |

Sections B to E of the review asked for no other change. The attribution block now names this
review with its verdict.

## B. The chat-side comments (Claude Opus 5.5, claude.ai chat session, 2026-10-01 18:47 EDT; the reviewed PDF is the pre-rebuild build, SHA-256 `6d305746...`)

| Item | Verdict | Reason and what changed |
|---|---|---|
| Credit Duraiswami for reading the cone condition as Rayleigh's criterion with axial shear | Already applied before the comment reached this session | Applied in 52cb03c (the self-review's third major item): Remark 3.6 says the reading "is Duraiswami's [pp. 21-22]" and the attribution block names it. The Duraiswami email's credit sentence matches. |
| "Both facts are instances of a loss of uniformity as h to 0": only the second is | CORRECT, applied | The same point as NS-1; the sentence now attributes the loss of uniformity to the bound alone. |
| The next statement: how much bias the inner edge needs as a function of `h`; heuristically asymmetry squared of order `h/(B-1)` | Not a finding; not applied | A research direction, offered as a heuristic. Recorded here as the candidate next question for the lane (it would be stated against the lower bound, per NS-1), not entered into the paper. |
| Lemma 4.2's exterior cancellation holds for every exterior profile, not only the heat one (substitution `u = 2d/x`) | CORRECT, verified, applied as a parenthetical | With `E^2 = c^2 X^{-2A} G(2d/X)` for any `G`, `R = (1/2) c^2 (2d)^{-2h} int_0^{2d/X} u^{2A-2} G(u) du`, and differentiating in `eta` gives `4 h eta R - d R_eta = c^2 eta X^{1-2A} G(2d/X) = eta X E^2` because `-2h + 2A - 1 = 0`. The lemma's statement, which concerns the heat exterior, is unchanged; its proof now says the cancellation uses only the similarity form of `E`, with the substitution displayed. The chat session's symbolic and numerical checks of the same identity are in `docs/outreach/2026-10-02/opus-chat-handoff/verification/`. |
| Lemma 3.1's proof invokes the hypothesis `U(X,0) = 0` to compute `W(X,0)` without needing it | Already in the text | The proof of Lemma 3.1 already says that the term `2 D eta A_X(U)` vanishes through its factor `eta`, "so (13) is not needed for this step". No change. |
| Re-integration of (17) at `w = 4` reproduces `sup a = 1.99310`, `1.93103`, `2 - 5.6e-12`; Lemma 4.1 operators, (4), (9), (12), (8)_1, (17) and Remark 3.3 re-derived symbolically | Confirmation, no change | Recorded as an independent reproduction (the chat session's checker, 28 of 29 checks in its first run, the 29th a sympy artifact confirmed in a second run). |
| Size: the paper formalizes a design remark; the refutation is of clause (iii) for symmetric cores, not of symmetric blow-up | Agreed; already what the paper says | Remark 3.7 and the introduction's scope paragraph say exactly this. No change. |

## C. Rebuild

Rebuilt with `build.sh` the same day; the page count is recorded in `paper/STATUS.md`. No new
TeX warning; no em dash; US English checked by grep. The checker
`docs/research/2026-10-01-ns-open-map/checks/midplane_barrier.py` is unaffected (no displayed
identity it tests changed).
