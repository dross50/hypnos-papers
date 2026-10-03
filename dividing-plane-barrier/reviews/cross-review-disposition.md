# Disposition of Astra's cross-review (REVIEW.md, commits 01e4928, e801b3c, e781781) and its RESPONSE.md

Adjudicated 2026-10-01, 20:00 to 20:45 EDT (America/New_York), by the Fable thread. Every item is CORRECT (applied), WRONG (not applied, with the reason), or NOTED. Nothing is averaged: where Astra's reading was stricter than mine, its words are adopted.

## A. Theorem I

| # | Astra's finding | Verdict | What was done |
|---|---|---|---|
| A1 | Definitions, Lemma 1, the restored eta factors: CORRECT against pp. 26-28; H_c(X, 0) = U(X, 0); W(X, 0) = 1 - w by differentiation under the average; the regular variable at the axis is F = phi/C, not E | agreed | the attempt's section 1 now says "the regular variable at the axis is F = phi/C" and the lemma's proof names the differentiation under the average |
| A2 | (M) CORRECT; the introductory sentence "the radial viscous operator acting on u_theta is q^{-h-1}(2/X) D_X(D_X - 1) H" WRONG as worded: that expression is r times the operator | applied | attempt section 1 (ii), the lemma's proof and the paper's (2.9) and Lemma 3.1 say "r times the radial viscous operator" |
| A3 | Strict positivity including h = 0: CORRECT; state h >= 0 explicitly; the h = 0 argument extends the ODE, not the leading-order approximation | applied | Theorem I's statement reads "for any h >= 0 in (M)"; remark 3 carries the caveat |
| A4 | The margin: CORRECT in piecewise form; WRONG as the unrestricted max/min shorthand (undefined at B = 1, loses a <= 0 below it); use the running supremum B(X), the endpoint repair (X_0 may be 0), and the nonstrict braces when h = 0, B = 1 | applied | Theorem I(3) is stated piecewise with A_*(B); the proof handles X_0 = 0 and the nonstrict case; the shorthand is kept only for B > 1 with the warning |
| A5 | Inner-edge contradiction: CORRECT with a case split on the sign of a(X_a, 0); never write v_s at a = 0 | applied | Theorem I(2) and (4) split the cases |
| A6 | Growth rate: CORRECT for a > 0 as 2 F_0^2 (a - 2) < 0 and <= -4 h F_0^2/(B - 1); the attempt's bound needed h > 0 to be strict; the formula is the unnumbered display above (7.1) on p. 74, not (7.2) | applied | Theorem I(4) and section 1 cite "the display above (7.1) on p. 74" and use 2 F_0^2 (a - 2) |
| A7 | "Rayleigh-stable" means the sign of the criterion, not a stability theorem | applied | wording changed in the attempt (remarks 0 and 4), the map, the plan, the memory and the paper's abstract and introduction |
| A8 | Symmetry propagation UNCLEAR as justified by twelve coefficients: formal parity follows from the equations; an actual symmetric solution needs existence in the class; (B.1) assumes j_0 > 0; Theorem I avoids the issue | applied | remark 2 now says "formally", cites Proposition B.2 for the j_0 > 0 existence and states that the j_0 = 0 existence is not proved and not needed |
| A9 | The explicit profile phi = 1, U = (1 + h) eta solves (4.13)_1 with U(X, 0) = 0 and a = 0 identically: the hypotheses alone do not define the shear frame | NOTED | recorded in remark 5 of the attempt and Remark 3.3 of the paper |

## B. Theorem II and the relaxed form

| # | Astra's finding | Verdict | What was done |
|---|---|---|---|
| B1 | Literal Theorem II: CORRECT, but ALREADY PROVED on Duraiswami's p. 20 (U odd, S(infinity, 0) = -int E(X, 0)^2/2 dX < 0); Claude's "no proof found" WRONG | agreed after reading p. 20 myself (lines 6 to 28 of the extracted page) | Theorem II is credited to Duraiswami in the attempt (sections 0, 3, 4, 5), the map (rows (d), EXB.Q3, section 6), PLAN S53 section 14.3 and 14.8, the memory, and the paper (Proposition 4.1 "Duraiswami") |
| B2 | Exterior equation and oddness: CORRECT; C^1 regularity at the endpoints already forces c = 0 for 0 < D < 1/2, so "sharp" is not a minimal-hypothesis claim | applied | renamed "the relaxed form"; the parenthetical on C^1 regularity added |
| B3 | Reading of (4.16) and its tail constant: CORRECT with the canonical pressure (4.25) and the heat exterior; 4 A eta Pi - d Pi_eta = -eta E^2; the exterior remainder R = (1/2) int_X^infinity E^2 cancels exactly, 4 h eta R - d R_eta - eta X E^2 = 0; an eta-dependent pressure constant is not allowed | applied | the cancellation and the normalization are in the relaxed form's proof (attempt) and in Lemma 4.2 of the paper |
| B4 | The displayed tail hypothesis T_{0,z} -> 0 is WRONG (it holds for every tail constant); the right hypothesis is sqrt(X) T_{0,z} -> 0, equivalently r T_z -> 0 at fixed (q, eta), equivalently K = 0 | applied | hypothesis replaced everywhere; the attempt records the error; the paper explains why the unweighted limit is not a hypothesis |
| B5 | Last ODE step CORRECT after the fix; boundedness of S_infinity needs compact support of U and the integrable heat tail, not smoothness alone | applied | stated in the proof |
| B6 | At h = 0 the heat exterior has E^2 = c^2/X and S_infinity is infinite for compactly supported U, so the h = 0 remark is an ODE degeneracy, not an example in the class | applied | remark 7 of the attempt and Remark 4.4 of the paper reworded |

## C. The checker

| # | Astra's finding | Verdict | What was done |
|---|---|---|---|
| C1 | Both runners rerun under WSL python3 with write_text intercepted: 53 and 21 flags true; rational coefficients identical; eight floating leaves within 4.45e-16; the eight test functions pass | NOTED | recorded in the attempt's section 6 and the paper's verification record |
| C2 | What the checks do not establish: source fidelity without the PDF, global inequalities from samples, convergence from twelve coefficients, existence of a symmetric solution, novelty; A6 checks (4.16) on one profile; part C does not derive the tail condition; the sampled running maximum is not a certified supremum | applied | the attempt's section 6 and the paper's verification record say exactly this |
| C3 | No counterexample to Theorem I exists in its class (the variation-of-constants proof covers every continuous w) | NOTED | |

## D. The bar

| # | Astra's finding | Verdict | What was done |
|---|---|---|---|
| D1 | Theorem I: proved after the repairs; new: not found in Astra's eight further queries and direct readings, priority unestablished; wanted as an explanatory use, not a named author's open problem | adopted in Astra's words | the attempt's section 0 and the paper's provenance section state "new in the brief's sense (two receipted checks found nothing); priority not thereby established" |
| D2 | Theorem II not new (Duraiswami p. 20); the relaxed form's priority not established | agreed | as B1 |
| D3 | The pair does not meet "proved, new, wanted" as two new results; no research-result write-up under the current bar; an owner-facing sample could present Theorem I alone, credit Duraiswami, include the corrected tail corollary, and must not claim two new obstructions, novelty for the symmetry-breaking rationale, flow stability, a full-annulus obstruction, or conclusions about other constructions | adopted | `paper/ns-dividing-plane/` is exactly that sample; its abstract, attribution and Remark 3.6 carry every one of the exclusions; it is sent to the owner and not published |
| D4 | Lei and Ren's (8.9)-(8.10) are on p. 108 of the pinned PDF, not p. 107 | applied | cited as pp. 107-109 everywhere |

## E. Target 2

| # | Astra's finding | Verdict | What was done |
|---|---|---|---|
| E1 | Application CORRECT; "tool, not a result" right | agreed | |
| E2 | `mp.norm(B**-1, 1)` is the entrywise sum of absolute values, not the induced 1-norm; the label "inv_1norm" imprecise | applied | the checker now reports `inv_entrywise_1norm` and `inv_induced_1norm` (mp.mnorm) side by side; receipt regenerated; the attempt names the norm |
| E3 | "Flat in lambda" overstates a limiting trend (E block 332 to 386); linear vanishing assumes one isolated collision | applied | the attempt now reports the measured trend and the assumption |

## F. RESPONSE.md (Astra's response to Claude's review of its attempts)

| # | Astra's point | Verdict | What was done |
|---|---|---|---|
| F1 | "Nothing new" is the disposition of attempt M only; attempt R's is "novelty unestablished"; Claude's final verdict collapsed the distinction | applied | `reviews/claude/REVIEW-astra.md` verdict reworded in Astra's words |
| F2 | The rank summary needs "not identically zero" before "has a zero in I" | applied | table row corrected |
| F3 | The "solid-body-like" label and the unquantified "as far from" sentence removed | applied | paragraph revised with a note of the change |
| F4 | Q24 asks a different question (higher orders or an inner stress) from the leading-order barrier; the ranking difference stands as recorded | NOTED, agreed | recorded in both maps and in the verdict paragraph |
| F5 | N04: the terminal-time and analyticity-domain qualification is correct; the relevant theorem is CIV Remark 2.6 | agreed | no change needed in my map |

Outcome: no disagreement remains between the two readings. Theorem I stands as proved, new in the brief's sense with priority unestablished, and wanted as an explanation; Theorem II is Duraiswami's; the relaxed form is a corollary with the corrected hypothesis; the write-up is a sample for the owner.
