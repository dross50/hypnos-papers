# Final review of "The unfolded zeros of the Riemann zeta function do not form a Riesz basis of exponentials"

Reviewer: Claude Opus 5.5 (Anthropic), a fresh agent launched by the Claude Fable 5.1 outreach
session as the last review before the paper goes to its first human reader. Written on Friday
2026-10-02, finished at 14:55 EDT.

Baseline: `main.tex` blob `d27e81d`, as committed in `3ab19fe` (2026-10-02 14:15 EDT) and
unchanged at `HEAD` `7af8e1f` (14:23 EDT); `main.pdf`, 17 pages, SHA-256
`49a3e68e2336bb8c7d1b7bb8a75d962d2162f612e5bcd1e8451590a5cf576cd8`, also unchanged since
`3ab19fe`. "Line" means a line of `main.tex`; "p." means the printed page of `main.pdf` (equal to
the PDF page index).

Read before reviewing: `reviews/claude/REPORT.md`; `reviews/astra/REVIEW.md` and
`reviews/astra/DISPOSITION.md`, including the consistency-pass ledger of 2026-10-01/02 (46 rows);
`reviews/astra-2026-10-02/REVIEW.md` and `DISPOSITION.md`; the chat session's package under
`docs/outreach/2026-10-02/opus-chat-handoff/` and `CHAT-COMMENTS-2026-10-02.md`. Items settled
there are not repeated unless the current text reopens them; the paper was judged as it stands.

What was run:

- A scratch rebuild with tectonic (a copy of the source and `paper/common/`, nothing in the
  repository touched): "Output written on main.xdv (17 pages, 134216 bytes)", only the two known
  benign warnings (the `../common/hypnos-paper` package-name request; inputenc ignored under a
  UTF-8 engine), no undefined reference, no overfull or underfull box, and the extracted text of
  all 17 pages identical to the committed `main.pdf`.
- The first 1000 ordinates recomputed with `mpmath.zetazero` at 25 digits, independently of the
  repository's table; they agree with `artifacts/zeros/dps200` to `5.0e-19`. The 10^5 statistics
  were recomputed from that certified table with my own code. Unfolding by `mpmath.siegeltheta`
  at 30 digits; Gram eigenvalues by `numpy.linalg.eigvalsh` in double precision (the 50- and
  60-digit residual certificates of jobs 260 and 263 were not repeated). The checker is
  `check_numbers.py`, output `check_numbers.json`, in the scratchpad of the session that ran this
  review (`.../9ba14bc4-.../scratchpad/agents/unfolded/`).
- Sources fetched and read at the locators given in section C. Third-party texts are reported by
  exact locator, with formulas and numbers transcribed exactly and their prose paraphrased; one
  short verbatim quotation is used (Conrey). Quotations of the manuscript and of the project's own
  files are verbatim.

## Findings at a glance

| ID | Severity | Location | Finding |
|---|---|---|---|
| OF-1 | MAJOR | `README.md` of the paper (ships beside the PDF) | Says the unconditional lower bound of Theorem 6.1 is "NOT available"; three other superseded statements |
| OF-2 | MINOR | line 267, pp. 10-11 | "raises the proportion to two thirds" skips the published record (0.4075, Pratt, Robles, Zaharescu and Zeindler); "has not been peer reviewed" is not something the preprint states |
| OF-3 | MINOR | line 360, p. 15 | "every statement is proved from the classical results cited in Section 2": Conrey's theorem, used in Theorem 6.1(a), is cited only in Section 6 |
| OF-4 | MINOR | line 257, p. 10 | Section 6.1's opening still says the set's density is bounded only from above |
| OF-5 | MINOR | line 26, p. 1; `reviews/astra-2026-10-02/DISPOSITION.md`, section B, fourth row | "a fresh instance of the same model line" for a review by a different model; the ledger records the chat session's objection as already resolved, which it is not |
| OF-6 | MINOR | line 26, p. 2 | No verdict clause for the chat session; this review must be named once applied |
| OF-7 | MINOR | line 354, p. 14 | The jitter control is matched in maximal displacement only, not in "displacement size" |
| OF-8 | MINOR | line 99, p. 5 | "strictly increasing across simple zeros" fails for an off-line pair of simple zeros |
| OF-9 | MINOR | line 360, p. 15 | "it does at block length log^2 T" without "below height T", credited to Theorem 4.1 |
| OF-10 | MINOR | line 140, p. 6 | The title "Kadec and Avdonin fail at every height scale" can be read against Corollary 4.2 |
| N1-N8 | NIT | listed in F | wording, rounding, a script comment, dates |

No BLOCKING item. No proof is wrong; every printed number reproduces.

## A. Statements against proofs

| Statement (line, page) | Verdict | What was checked |
|---|---|---|
| Section 2.1 conventions and facts (46-63, pp. 3-4) | CORRECT | (2.1) with means at ordinates; `theta'(t) = (1/2)log(t/2pi) - 1/(48t^2) + ...` vanishes near `t = 6.29` and is positive on `[7, oo)`; S strictly decreasing between ordinates there; jump `+m`. (S1) is Goldston's Theorem 8, (10.6), at `k = 1`, differenced between `2T` and `T` (the extra term `(T/pi^2)(log log 2T - log log T)` is `O(T/log T)`); (S2)-(S4) at the Titchmarsh locators of section C; (S3) as recorded by Tsang (1.2). |
| Theorem 2.1, Kadec (68-70, p. 4) | CORRECT (imported) | Strict `< 1/4`, sharpness; agrees with Alemany and Nitzan, p. 2. |
| Theorem 2.2, Avdonin, and the note after it (72-82, p. 4) | CORRECT | Alemany and Nitzan, p. 2, state it with uniform discreteness, `sup abs(lambda_n - n) < oo` and `sup_m abs(N^{-1} sum_{n=mN}^{(m+1)N-1} (lambda_n - n)) < 1/4`, for `e^{2 pi i lambda t}` on `L^2[0,1]`: no centering constant, blocks `mN <= n <= (m+1)N - 1`. Re-indexing `lambda'_n = lambda_{n+1}` turns that partition into the paper's and shifts every displacement by 1, which `c` absorbs; a common frequency shift is a modulation. The note is right. |
| Theorem 2.3, HNP, and the facts of line 95 (86-95, pp. 4-5) | CORRECT | Kozma and Lev, Theorem 5.1, p. 14, in their normalization `e^{2 pi i lambda t}` on `(0, a)` with `f = n_Lambda(x) - ax`; `a = 1` corresponds to `e^{i lambda t}` on `(-pi, pi)`; their counting function is the paper's (p. 13). John-Nirenberg direction right. Landau directions right (a Riesz basis is separated, so the uniform discreteness that Landau assumes holds). Beurling-Malliavin with `R = pi D` (Seip and Ulanovskii, p. 1745, use the same normalization; their "substantial" systems of intervals are the paper's "long" families). |
| Line 99, p. 5 (monotonicity of `x_n`, value of `x_1`) | WRONG in one phrase (OF-8) | `x_1 = 0.94975` recomputed. |
| Theorem 3.1 (101-111, p. 5) | CORRECT | `N(gamma) = n - j + m/2` under the mean convention; algebra re-derived. Wording: N2. |
| Paragraph after Theorem 3.1 (113, p. 5) | CORRECT | `Lambda_1 = {+-(n - 1/2 + d_n)}`; `Lambda_{3/2}` perturbs `Z \ {0}`. |
| Proposition 3.2 (115-128, p. 5) | CORRECT | `F' = 0` between ordinates; the jump `(S^+ - S^-)(S^+ + S^-)/2 = m S(gamma)`; the corrections `(m+1)/2 - j` sum to 0 over a cluster. |
| Lemma 3.3 (130-138, p. 6) | CORRECT | Every reflected point is at most `-x_a(gamma_1) < X_a`; `t_a(X_a)` is not an ordinate because `X_a` is not in `Lambda_a`; the constant `c_0`; a finite modification is bounded and eventually constant. |
| Theorem 4.1 (142-158, p. 6) | CORRECT | Both block choices lie within `2N` indices of `N(t_0)`; `d_n <= N(t_0) - n + 1/2 - A` for `n <= N(t_0)` by monotonicity alone; averages `N/2 - A` (sliding) and at most `2N - 1/2 - A` (partition); the mirror case at a negative excursion; (S3) gives both signs; moving to a non-ordinate on the correct side uses `S(gamma^+-) = S(gamma) +- m/2`. |
| Paragraph after Theorem 4.1 (160, p. 7) | CORRECT | Thresholds `N/2 + 1/4`, `r + N/2 + 1/4` with `r = N(t_0) mod N`, the shift by `c`, and `A - N/2` for the following window: all re-derived. |
| Corollary 4.2 (162-172, p. 7) | CORRECT | Integration by parts; boundary terms `O(log^2 b)`; `int theta'' S_1 = O(log b log(b/a))`; a cut cluster costs `O(log^2 b)` at each end; the RH form from Titchmarsh Theorem 14.13 and `m <= 2 sup abs(S)`. |
| Paragraph after Corollary 4.2 (174, p. 7), rewritten today | CORRECT | A.2 below. |
| Theorem 5.1 and the paragraph before its proof (178-208, pp. 7-8) | CORRECT | The Landau squeeze `len(I)/2pi <= D^- <= 1 <= D^+ <= len(I)/2pi`; Jacobian bounds and their ratio; `abs(u+w)^2 >= abs(u)^2/2 - abs(w)^2`; the factor `1/4` from a Jacobian ratio of at least `1/2`; minimizing over `c'` subtracts the squared mean; coefficient `1/(8 pi^2)`, and `1/(4 pi^2)` when `b = 0` (valid, not sharp); the one-sided system; repetitions and finite modifications. |
| Theorem 5.2 (212-222, p. 9) | CORRECT | `n_{d Lambda}(x) = n_Lambda(x/d)`; `E(Lambda)` on `I` corresponds to `E(d Lambda)` on `I/d`; mean-square oscillation is dilation invariant. |
| Corollary 5.3 and line 236 (224-236, p. 9) | CORRECT (conditional, as stated) | Jacobian ratio at most `K` gives `1/(2K)`; `int_0^T S_F = O(T)` bounds the dyadic mean; line 236 claims no family. |
| Remark 5.4 (238-248, pp. 9-10) | CORRECT (labeled a sketch) | Gaps within `1 +- log(3/2)`; `n_Z(u) = ceil(u)` counts `Z` on `[a, b)`; `f = q + 1/2 + g + R` checked; the gap integral is `O((1+abs(n))^{-2})`; the `L^1` norm of `P_y'` is `2/(pi y)`; `-c log abs(z + i(1+y))` has a bounded conjugate; `P_y * R = H(-P_y * H R)` because `H H R = -R`. |
| Remark 5.5 (250-252, p. 10) | CORRECT (cited scope) | Bufetov's abstract (one point removed: uniqueness set; two: zero set); Ghosh's abstract (completeness in `L^2[-pi, pi]`); number variance `pi^{-2} log L + O(1)` at density one. |
| Section 6.1 opening (257, p. 10) | CORRECT, last sentence stale (OF-4) | |
| Theorem 6.1(a) (262, p. 10; proof 269-286, p. 11) | CORRECT | A.1 below. |
| Theorem 6.1(b) (263, p. 10; proof at the end of 286, p. 11) | CORRECT | Finitely many repeated points give `#(Lambda'* cap I) = n(I) + O(1)`; cross-half coincidences need `theta(gamma_n) + theta(gamma_m) = -2 pi a`, finitely many pairs. |
| Paragraph after Theorem 6.1 (267, pp. 10-11) | CORRECT in its mathematics; literature wording (OF-2) | A.3 below. |
| Proposition 6.2 and line 307 (296-307, p. 12) | CORRECT | Interlacing; trace; the closest pair's eigenvalues `2 pi (1 +- abs(sinc s_N))`; `1 - sinc(s) <= pi^2 s^2/6`; GUE minimal gap `N^{-1/3}` gives `A_N <~ N^{-2/3}`; `inf s_N = 0` is open (Inoue proves `mu < 0.50895` on RH; `mu = 0` is not known). |
| Questions 6.3-6.5 (312-322, p. 12) | CORRECT as stated | A unit unfolded window counts `1 + S(t') - S(t) + O(1)` zeros with `t' - t ~ 2 pi/log(t/2pi)`; Tsang's Theorem 3 range checked (section C). |
| Section 8, first paragraph (358, pp. 14-15) | CORRECT | A.4 below. |
| Section 8, second paragraph (360, p. 15) | Two MINOR items (OF-3, OF-9) | |
| Section 4 title (140, p. 6) | MINOR (OF-10) | |

### A.1 Theorem 6.1(a), the unconditional lower bound added today

1. Conrey's theorem gives `N*(t) >= q N(t)` for every `q < 2/5` and all large `t`. Conrey defines
   (printed p. 3, (11) and (12)) `N_0*(T)` as the number of zeros with `0 < gamma < T`,
   `beta = 1/2` and `zeta'(rho) != 0`, and `kappa* = liminf_{T -> oo} N_0*(T)/N(T)`; Theorem 1
   (printed p. 4) gives `kappa >= 0.4077` and `kappa* >= 0.401` and concludes that "at least 2/5
   of the zeros ... are simple and on the critical line". So `kappa*` is exactly what the proof
   needs: a liminf of the proportion of zeros (counted with multiplicity in `N`) that are simple and
   on the line. Since `kappa* >= 0.401 > 2/5`, every `q < 2/5` (indeed every `q < 0.401`) works.
   Conrey counts `gamma < T` where the paper counts `gamma <= t`, and the paper's `N(t)` takes
   means at ordinates; both differences are `O(log t)` and vanish in the margin `0.401 - q`.
2. Two simple zeros on the line have different ordinates: `1/2 + i gamma` and `1/2 + i gamma'`
   with `gamma = gamma'` are the same point. The injection into distinct ordinates survives
   off-line zeros at the same height (such an ordinate is not simple, but it is still one point).
3. The two-sided bound for `A(x)`. Lower: the untouched simple on-line zeros with
   `t_a(X_a) <= gamma < t_a(x)` map injectively (`x_a` is strictly increasing on `[7, oo)`) into
   `Lambda'* cap [X_a, x)`; the losses (zeros below `t_a(X_a)`, the finitely many touched by the
   modification, at most one at `gamma = t_a(x)`) are `O(1)`. With (2.1),
   `N(t) = x - a + 1 + S(t)`, and (S4), `q N(t) - O(1) = q x - O(log x)`. Upper:
   `A(x) <= n([X_a, x)) = x + O(log x)` by Lemma 3.3 and (S4); the printed `+ O(1)` is harmless.
4. The family `I_k = [C^k, C^{k+1})` is disjoint and long:
   `|I_k|^2/(1 + C^{2k}) -> (C - 1)^2 > 0`, so every tail diverges; it lies on one side of 0, so it
   is also "substantial" in Seip and Ulanovskii's sense. For `C^k >= X_a`,
   `#(Lambda'* cap I_k) = A(C^{k+1}) - A(C^k)` (the printed "`>=`" is an equality)
   `>= q C^{k+1} - C^k - O(k) = (qC - 1) C^k - O(k)`, which exceeds `d |I_k| = d (C-1) C^k` for
   large `k` because `(qC - 1)/(C - 1) > d`. Such `C` exists: `(qC - 1)/(C - 1)` increases to `q`
   as `C -> oo` (it is below `q` for every finite `C`, since `q < 1`).
5. Finite modifications: removals touch finitely many heights; additions only enlarge `Lambda'*`;
   the reflected half never enters `[X_a, oo)`.
6. Directions and constants: `D_BM(Lambda'*) >= d` for every `d < q < 2/5` gives
   `D_BM >= 2/5` and `R = pi D_BM >= 2 pi/5`; "complete for every `b < 2pi/5`" follows from
   `R >= 2pi/5` and monotonicity of completeness in `b`; "incomplete for every `b > pi`" from
   `R <= pi`. Both strict inequalities in (a) are the right ones.

Verdict: CORRECT. The same theorem gives `0.401` in place of `2/5`, and the published record gives
`0.4075` (OF-2); `2/5` is a valid weakening.

### A.2 The paragraph after Corollary 4.2 (UZ-1 repair)

Checked against the proof of Theorem 4.1. The window of the `N` ordinates preceding a non-ordinate
`t_0` is the block `k = N(t_0) - N`, which exists exactly when `N(t_0) >= N` (the paragraph's "with
at least N ordinates below it"), lies below `t_0 <= T`, and has mean at most `N/2 - A`. That mean
is at most `-1/4` exactly when `N <= 2A - 1/2`, so the window is defeated unless `N > 2A - 1/2`
(the boundary case `N = 2A - 1/2` gives a mean of at most `-1/4`, which already violates a bound
`d < 1/4`, so counting it as defeated is right). Negative excursions are correctly left out. The
numerical consequences hold: the largest `|S|` over the table is `1.6287` (one-sided limits; it is
`max |d_n| + 1/2`, since `S` is monotone between ordinates), below `1.75 = 3/2 + 1/4`, so no
`N >= 3` is bitten; `3.3455 >= 3.25 = 6/2 + 1/4` defeats every `N <= 6` (`2A - 1/2 = 6.19`) and not
`N = 7` (`3.75`); `N = 8` needs `4.25`. Verdict: CORRECT.

### A.3 The sentence after Theorem 6.1

The mathematics (Conrey's proportion, distinct ordinates, the conditional `2 pi/3`) is right; the
description of the literature is less exact than its sources (OF-2, in section C).

### A.4 Section 8's first sentence

"This paper proves a conjecture that a machine made (Theorem~\ref{thm:kadec}) and answers a
question that it asked (Theorem~\ref{thm:main})." This agrees with Section 8's own account (nodes
1296, 1637, 1638 conjectured that the Kadec failure is unconditional and shift-invariant; nodes 1687
and 2181 asked whether the Riesz property degrades). Checkable here only through the job records,
which carry node ids that match Section 8's groupings: job 100 (node 1296), job 166 (node 1637, a
"shift-invariant displacement radius"), job 260 (node 1687), job 263 (node 2181), job 202 (node
537), job 25 (node 831), job 313 (node 2371), jobs 67, 48 and 110 (nodes 1032, 1034 and 1115). The
node texts themselves are not in this repository (the `hypnos.db` here is a 26-node copy of
2026-08-22). The sentence does not overstate depth: Section 4 already says the proof uses only
monotonicity and the unboundedness of `S`. Verdict: CORRECT as far as checkable.

### A.5 Findings in statements

**OF-3 (MINOR). Section 8 says every statement rests on Section 2's inputs; Theorem 6.1(a) now also rests on Conrey's theorem.**
- Location: line 360, p. 15.
- Claim: "No part of the mathematical content depends on the harness: every statement is proved from the classical results cited in Section~\ref{sec:inputs}, and the numerical record is reported as record, not as evidence."
- Evidence: line 286, p. 11: "By Conrey's theorem \cite[Theorem~1]{Conrey89}, for every fixed $q<\frac25$ we have $N^\ast(t)\ge qN(t)$ for all large $t$." `\cite{Conrey89}` occurs only at lines 267 and 286; Section 2 (lines 43-95) does not cite it.
- Fix: "every statement is proved from the classical results cited in Section~\ref{sec:inputs} and, for the lower bound in Theorem~\ref{thm:BM}(a), Conrey's theorem \cite{Conrey89}, and the numerical record is reported as record, not as evidence."

**OF-4 (MINOR). The opening of Section 6.1 still describes only an upper bound for the set.**
- Location: line 257, p. 10.
- Claim: "Our counting estimates count with multiplicity, so what they control unconditionally is the exterior density of the multiset, and that bounds the density of the set from above."
- Evidence: Theorem 6.1(a), line 262, now states `\frac25\le D_{BM}(\Lam'^\ast)`, proved from an input that is not a counting estimate (line 286).
- Fix: append "; a lower bound for the set needs an input about distinct ordinates, which Conrey's theorem supplies (Theorem~\ref{thm:BM}(a))." before the final period.

**OF-8 (MINOR). "strictly increasing across simple zeros" contradicts the paper's own distinction.**
- Location: line 99, p. 5.
- Claim: "the sequence $(x_n)$ of \eqref{eq:unfold} is nondecreasing, strictly increasing across simple zeros, and $x_1=0.9497\ldots$."
- Evidence: line 54, p. 3: "a simple zero need not lie on a simple ordinate, since two simple zeros $\beta+i\gamma$ and $1-\beta+i\gamma$ share an ordinate." For such a pair `x_n = x_{n+1}`.
- Fix: "strictly increasing across distinct ordinates ($x_n<x_{n+1}$ exactly when $\gamma_n<\gamma_{n+1}$)".

**OF-9 (MINOR). Section 8 drops the height quantifier that the abstract and introduction carry, and credits Corollary 4.2's content to Theorem 4.1.**
- Location: line 360, p. 15.
- Claim: "Theorem~\ref{thm:kadec} answers the question its nodes 1870 and 2400 asked, namely whether Avdonin's mean condition survives where Kadec's fails (it does not, for any fixed block length, and it does at block length $\log^2T$)".
- Evidence: Corollary 4.2 (line 167) is a statement about blocks "whose ordinates lie below height $b$". The consistency pass added "below height T" to the same claim in the abstract and the introduction (`reviews/astra/DISPOSITION.md`, consistency rows 4 and 15) because without it the clause reads against "fail ... for every block length". The second half is Corollary 4.2, not Theorem 4.1.
- Fix: "(it does not, for any fixed block length; below height $T$ it does at block lengths of order $\log^2T$, Corollary~\ref{cor:growing})".

**OF-10 (MINOR). Section 4's title can be read against its own corollary.**
- Location: line 140, p. 6.
- Claim: "\section{Kadec and Avdonin fail at every height scale}".
- Evidence: Corollary 4.2 in the same section: below height `b` the averaged condition holds once `M > 4C log^2 b`. Theorem 4.1 is a statement for every fixed block length, not for every height.
- Fix: "\section{Kadec and Avdonin fail for every block length}".

## B. Abstract and introduction against the statements, case by case

| Claim (line, page) | Body statement | Verdict |
|---|---|---|
| Unfolding to unit density, `Lambda_a`, `Lambda_{3/2} cup {0}` on `Z`, `Lambda_1` on `Z + 1/2` (22, p. 1) | (1.1); line 113 | matches |
| "at every simple ordinate ... $x_n-n=-S(\gamma_n)$ ... (at an ordinate, the mean of its one-sided limits)" (22) | Theorem 3.1 | matches (simple ordinate, mean convention) |
| Kadec and Avdonin "fail unconditionally for every centering constant and every block length" (22) | Theorem 4.1 (every `N >= 1`, every `c`, partition and sliding forms; (S3) unconditional) | matches |
| "below height $T$ the block condition does hold at block lengths of order $\log^2 T$" (22) | Corollary 4.2 (blocks below height `b`, `M > 4C log^2 b`) | matches |
| Main result for every `a`, every finite modification, every bounded `I` (22) | Theorem 5.1 (which also covers translates and the one-sided system) | matches |
| Mean square of `S` over `[T, 2T]` grows like `(2 pi^2)^{-1} log log T` (22) | (S1) divided by `T` | matches |
| HNP forces BMO; Selberg's variance growth is incompatible (22) | Theorem 2.3(ii); proof of Theorem 5.1 | matches |
| "any $L$-function whose argument has a Selberg-type mean square and a bounded mean" (22) | Corollary 5.3 | matches; the setting hypotheses ride on the word "$L$-function" (consistency row 7; I agree) |
| Set of distinct points "incomplete in $L^2(-b,b)$ for every $b>\pi$" (22) | Theorem 6.1(a), strict | matches |
| "complete for every $b<2\pi/5$ unconditionally (by Conrey's theorem ...)" (22) | Theorem 6.1(a), strict; Conrey, Theorem 1 | matches |
| "complete for every $b<\pi$ if all but finitely many ordinates are simple" (22) | Theorem 6.1(b) | matches (hypothesis on ordinates) |
| Open: exact unconditional radius, critical length, frame, separation of the positive half (22) | paragraph after Theorem 6.1; Section 6.3 | matches |
| Provenance sentence (22) | Section 8 | matches |
| Density `(1/2pi) log(t/2pi)`, hence no Riesz basis or frame for the raw ordinates (33, p. 2) | a frame needs bounded unit-window counts | correct |
| Both sequences of density one; `a` is not a translation (37, p. 2) | line 113; Theorem 5.1 for every `a` | matches |
| Section 3 summary (39, p. 2) | Theorem 3.1, Proposition 3.2 | matches |
| Section 4 summary with "below height $T$" (39, p. 2) | Theorem 4.1, Corollary 4.2 | matches |
| "the averaged condition holds at every tested block length from 8 upward" on the first `10^5` (39, p. 2) | job 110 scan `M = 8, 12, 16, 24, ..., 65536`, all `D(M) < 1/4`; recomputed through `M = 4096` (section D) | matches |
| Section 5 summary (39, p. 2) | Theorems 5.1, 5.2, Corollary 5.3 | matches |
| "the completeness radius of the set of distinct points lies between $2\pi/5$ and $\pi$ unconditionally, and equals $\pi$ if all but finitely many ordinates are simple" (39, p. 3) | Theorem 6.1(a), (b) | matches |
| Pair bound "consistent with the observed decay" (39, p. 3) | Proposition 6.2 and line 307 | matches (an upper bound, consistency only) |
| `n + c log(2 + abs(n))`, `abs(c) <= 1` (41, p. 3) | Remark 5.4 | matches |
| Selberg's CLT variance; "together with the counting formula and the bounded mean of $S$" (41, p. 3) | proof of Theorem 5.1 | matches the proof's dependencies |

No finding in B. OF-9 and OF-10 are the same quantifier question in Section 8 and in a section title.

## C. Sources

The manuscript contains no attributed verbatim quotation; the quotation marks around "1/4 in the
mean", "long" and "centering constant" mark labels (settled, consistency rows 23-25). Its
paraphrase of Conrey matches Conrey's Theorem 1 (A.1, item 1).

| Source (bibliography number in the PDF) | The paper's use (line, page) | Checked against | Outcome |
|---|---|---|---|
| Conrey 1989 [8] | 22, 26, 267, 286; pp. 1, 2, 10-11 | the scan provided (printed pp. 3-4: (9)-(12), Theorem 1) | CORRECT (A.1). The journal header (J. reine angew. Math. 399 (1989), pages 1 to 26) and the title agree with the bibliography; Crossref DOI 10.1515/crll.1989.399.1. |
| Alpöge and Furman [2] | 267, pp. 10-11 | arXiv abstract page (v1 13 Aug 2026, v2 19 Aug 2026); PDF v2, pp. 1-2 and Appendix A | The abstract claims, unconditionally, at least two thirds of the zeros (counted with multiplicity) simple and on the critical line, at least five sixths distinct, and results formally verified in Lean 4. Theorem A(i), p. 1: `N_0^s(T, 2T) >= (2/3 - o(1)) N(T, 2T)`; p. 2: the same on `(0, T)` (their Remark 6.1), which is the form the paper's argument needs for `2 pi/3`. The arXiv comments field says the proof was discovered by Claude (Anthropic) and verified and communicated by the listed authors. No journal reference. Title and authors in the bibliography match the arXiv listing. See OF-2. |
| Pratt, Robles, Zaharescu and Zeindler (not cited) | relevant to 267 | arXiv:1802.10521v3, pp. 9 and 56; journal reference Research in the Mathematical Sciences 7 (2020), article 2 | They state `kappa > 0.417293` and `kappa* >= 0.407511`, `kappa*` the proportion of simple zeros on the critical line (p. 56: `0.407511457`). See OF-2. |
| Kozma and Lev [18] | 84-95, pp. 4-5 | arXiv:1009.2188v2, pp. 13-14 | Theorem 5.1 (i)-(iii) and the counting function as quoted; pinpoint "see [7, p. 240]" for HNP. JFAA 17 (2011) 879-898 (Crossref). |
| Alemany and Nitzan [1] | 72-82, p. 4 | arXiv:2501.11598v1, p. 2 | As in A (Theorem 2.2 row). Authors Thibaud Alemany and Shahaf Nitzan; title agrees. Their reference list gives Avdonin (Vestnik Leningrad Univ. Ser. Mat. 13 (1974) 5-12; English transl. Vestnik Leningrad Univ. Math. 7 (1979) 203-211) and Kadec (Dokl. Akad. Nauk SSSR 155 (1964) 1253-1254; Soviet Math. Dokl. 5 (1964) 559-561), both matching the paper's entries. |
| Bober and Hiary [5] | 174, p. 7 | arXiv:1607.00709v1, p. 7, Table 2 and caption | First row `t = 7757304990367861417150213053.6386`, `S(t) = 3.3455`; the caption explains that `t` is a zero's ordinate and a positive value is attained just after it. "near $t=7.7573\cdot10^{27}$" and "just after a zero" are right. Exp. Math. 27, 125-137 (Crossref). |
| Tsang [29] | 60, p. 3; 321, p. 12 | the scan (see below for access), printed pp. 369-370 | (1.2), p. 369: `S(t) = Omega_+-((log t)^{1/3}(log log t)^{-7/3})`, credited to Selberg ([6], Theorem 9). Theorem 3, p. 370, without RH: `sup_{t in [T,2T]} +-(S(t+h) - S(t)) >= c (h log T)^{1/3}` for `h` in `[(log T)^{-1}, (log log T)^{-1}]`. Both as used. Acta Arith. 46 (1986) 369-395 (Crossref). |
| Titchmarsh [28] | 59, 61, 63; pp. 3-4 | the 2nd edition scan (title page: second edition, revised by Heath-Brown) | Theorem 9.4, p. 214: `S(T) = O(log T)`. Theorem 9.9 (A), p. 222: `S_1(T) = O(log T)`. Theorem 14.13, p. 350: on RH, `S(t) = O(log t/log log t)` and `S_1(t) = O(log t/(log log t)^2)`, with a footnote crediting Landau, Cramér, Littlewood and Titchmarsh; the paper's "both due to Littlewood" is the usual attribution. |
| Inoue [14] | 307, p. 12 | arXiv:2604.05733v1, abstract and Theorem 1 | On RH, `mu < 0.50895`, `mu` the liminf of normalized consecutive gaps. "smaller than 0.509" follows. |
| Goldston, math/0412313 (Selberg's moments) | (S1), 58, p. 3 | Theorem 8, (10.6), pp. 21-22 | `int_0^T abs(S)^{2k} = (2k)!/(k!(2pi)^{2k}) T (log log T)^k + O_k(T (log log T)^{k-1/2})`; `k = 1` and differencing give (S1). |
| Seip and Ulanovskii [24] | 257, p. 10 | Proc. AMS 125 (1997), p. 1745 (AMS PDF) | The system `{t^l e^{i lambda_n t}}`, `0 <= l <= p_n - 1`, at multiplicity `p_n`; `R(Lambda) = pi D(Lambda)`. As cited. Pages 1745-1749 (Crossref). |
| Bufetov [6], Ghosh [10] | 251, p. 10 | arXiv:1912.13454v1 abstract; arXiv:1211.2435 abstract | As cited. Ghosh: PTRF 163, 643-665 (Crossref). |
| Bibliographic metadata, by Crossref | bibliography, pp. 16-17 | Crossref records | Beurling-Malliavin (Acta Math. 118, 79-93), Landau (Acta Math. 117, 37-52), Littlewood (Proc. Cambridge 22, 295-318), Dyson-Mehta (J. Math. Phys. 4, 701-712), Goldston-Gonek (BLMS 39, 482-486), Lyubarskii-Seip (Rev. Mat. Iberoam. 13, 361-376), Burnol (JTNB 16, 65-94) all agree. Kozma and Lev's reference list agrees with the HNP entry (LNM 864, 214-335) and the Pavlov entry (Dokl. 247, 37-40; Soviet Math. Dokl. 20, 655-659). |

All internal references resolve (scratch rebuild: no undefined reference).

**OF-2 (MINOR). The sentence after Theorem 6.1 describes the literature less exactly than its sources.**
- Location: line 267, pp. 10-11.
- Claim: "What is available unconditionally is a positive proportion: Conrey \cite{Conrey89} proved that at least two fifths of the zeros are simple and on the critical line, [...] the lower bound in (a) rests on this. A preprint of Alp\"oge and Furman \cite{AlpogeFurman}, which states that its results are formally verified in Lean~4 and which has not been peer reviewed, raises the proportion to two thirds; if it stands, the same argument gives $R(\Lam'^\ast)\ge2\pi/3$."
- Evidence: (a) Read after the Conrey clause, "raises" says the proportion went from 2/5 to 2/3. The published proportion of simple zeros on the critical line was raised after Conrey: Pratt, Robles, Zaharescu and Zeindler (Res. Math. Sci. 7 (2020), article 2; arXiv:1802.10521v3, p. 9) state `kappa* >= 0.407511`. Alpöge and Furman's own Section 1.1 (p. 2) names 5/12 for `N_0^s/N`, citing that paper, as the previous record; PRZZ's text gives 5/12 for zeros on the line (`kappa`) and `0.407511` for simple ones (`kappa*`), so the 5/12 should not be imported for simple zeros. (b) The preprint does not state that it has not been peer reviewed; what the record shows is arXiv:2608.13637v2 (19 August 2026) with no journal reference on the abstract page as fetched 2026-10-02. (c) Everything else in the sentence matches the preprint (section C row).
- Fix (smallest): replace "and which has not been peer reviewed, raises the proportion to two thirds;" with "and which carries no journal reference as of this writing, states a proportion of two thirds;".
  Optional, more informative: after "the lower bound in (a) rests on this" add " (published refinements give slightly more, $0.4075$ in \cite{PRZZ}, hence $R(\Lam'^\ast)\ge0.4075\,\pi$)" with `\bibitem{PRZZ} K.~Pratt, N.~Robles, A.~Zaharescu and D.~Zeindler, More than five-twelfths of the zeros of $\zeta$ are on the critical line, Res. Math. Sci. 7 (2020), Paper No.~2.`

Not reached, or not fetched in this review: the originals of Selberg 1946 (zeta; (S1) and (S3) were checked through Goldston and Tsang), Selberg 1946b and Selberg 1992 (the paper claims nothing from them beyond line 236's disclaimer), Avdonin 1974, Kadec 1964 and Pavlov 1979 (bibliographic data checked through the reference lists above), HNP p. 240 (a book chapter; Kozma and Lev give the same pinpoint), Koosis II, and the full texts of Landau 1967, John and Nirenberg 1961, Littlewood 1924, Dyson and Mehta 1963, Lyubarskii and Seip 1997 and Burnol 2004 (metadata only); Mikulik's ResearchGate page was not attempted. On 2026-10-02 the matwbn.icm.edu.pl server answered the Tsang URL with a bot-check page, which was not attempted; Tsang was read from a copy fetched by an earlier session (`tsang_aa4646.pdf`, 2026-10-01 23:06 EDT, SHA-256 `c6f9404e6e1b29202dd11adbefab220903d2400ef05345922795431f3ee2ad6f`, 14 PDF pages, the Acta Arithmetica XLVI header). The harness's live node records were not reachable (A.4). No priority search was repeated (Astra's review of 2026-10-02, section D, covers it).

## D. The numbers

Recomputed values (independent mpmath zeros for `n <= 1000`; the certified table for `n <= 10^5`):

| Printed (line, page) | Recomputed | Agreement |
|---|---|---|
| `x_1 = 0.9497...` (99, p. 5) | `0.9497471705` | yes |
| First Kadec index `n = 9`, `gamma_9 = 48.005` (330, p. 13) | `n = 9`, `gamma_9 = 48.0051509`, `d_9 = 0.2708185` | yes |
| `max abs(d_n)` over `10^3`: `0.734` | `0.7342535` at `n = 871` (`gamma = 1267.571`), mpmath and table identical | yes |
| over `10^4`: `0.948` | `0.9484713` at `n = 8571` | yes |
| over `10^5`: `1.129` at `n = 94352`, `gamma = 71128.97` | `1.1286944` at `n = 94352`, `gamma = 71128.9708` | yes |
| Optimally centered sup `1.103` | `1.1030398` (center `-0.0256547`) | yes |
| `43 588` with `abs(d_n) >= 1/4`; `43 639` outside the centered ball | `43588`; `43639` (with either `>=` or `>`) | yes |
| Mean `-7e-6` | `-6.989e-6` | yes |
| Largest `abs(S)` over the table "about 1.63"; last ordinate `7.49e4` (174, p. 7) | `1.6286944` (one-sided limits); `74920.83` | yes |
| `D(M)`, `n <= 10^5`: 1.129, 0.795, 0.473, 0.216, 0.103, 0.062, 0.028, 0.015, 0.0077, 0.0019, 0.00049 (Table 1, p. 14) | 1.12869, 0.79511, 0.47259, 0.21616, 0.10263, 0.06161, 0.02797, 0.01501, 0.007695, 0.001939, 0.0004905 | yes, all 11 |
| `D(M)`, `n <= 10^4`: 0.948, 0.674, 0.344, 0.146, 0.103, 0.044, 0.022, 0.012, 0.0060, 0.0015, 0.00032 | 0.94847, 0.67399, 0.34434, 0.14595, 0.10263, 0.04382, 0.02176, 0.01154, 0.006021, 0.001457, 0.0003234 | yes, all 11 |
| `D(6) = 0.330`, `D(8) = 0.216`; first tested `M` with `D(M) < 1/4` is 8 (332, p. 13) | `0.33038`, `0.21616`; `D(3) = 0.6007`, `D(4) = 0.4726`; every tested `M >= 8` below `1/4` (job 110's scan to 65536; recomputed to 4096) | yes |
| Fitted exponents `-1.03` (job 110, `M = 4096..65536`), `-0.94` (job 67) | recorded `-1.02798` and `-0.94374` | yes (records) |
| `s_1000 = 0.1376`; `1 - sinc(0.1376) = 0.0309` (354, p. 14) | `0.1376276` at `n = 922` (`gamma = 1329.04`); `0.0308673` (the quadratic bound would be `0.0312`) | yes |
| Closest pair in `10^5`: `0.02186` at `n = 95248`, `gamma ~ 71732.9`, ordinate gap `0.0147`; `A_{10^5} <= 7.9e-4` | `0.0218605`, `95248`, `71732.901`, `0.0147015`; `7.859e-4` | yes |
| `A_N` at `N = 100, 200, 400, 800, 1000`: 0.1115, 0.0774, 0.0421, 0.0283, 0.0159 | 0.111503, 0.077433, 0.042076, 0.028322, 0.015855 | yes |
| `B_N`: 1.953, 2.062, 2.115, 2.277, 2.278 | 1.953086, 2.062241, 2.115398, 2.277481, 2.277956 | yes |
| Observed exponent `-0.79` (307, p. 12) | least-squares slope of `log A_N` on `log N`: `-0.79457` (job 263 records `-0.79457`) | yes |
| `r(N)` at `N = 50, 200, 500`: 0.1324, 0.0771, 0.0404 | 0.132414, 0.077071, 0.040356 (2N-by-2N symmetric sections) | yes |
| Jitter means 0.0625, 0.0083, `3.1e-5` (job 260) | recorded 0.0624971, 0.0082656, `3.0934e-5`; not rerun; the matched `max abs(d_n)` recomputed as 0.4536, 0.5065, 0.6642, equal to job 260's | yes (records) |
| Eigenpair residuals "below `8.4e-31`" and "below `1.4e-30`" | recorded `8.3808e-31` and `1.3098e-30` | yes (records) |
| Job 313: 1141 samples, `epsilon = 1e-6`, magnitudes `1.3e-7` to `1.5e-6` (328, p. 13) | recorded 1141, `1e-6`, `1.2900e-7` to `1.4938e-6`; `epsilon theta'(gamma)/pi` is `1.29e-7` at `gamma_1` and `1.494e-6` at `gamma_{10^5}` | yes |
| Identity residuals below `1e-19` (12 and 40 samples) | recorded `5.457e-21` and `7.113e-20` | yes |
| Block identity `7.3e-34` (40 windows) and `3.2e-34` (12 windows) | recorded `7.2807e-34` and `3.1420e-34` | the second is a ceiling, not a rounding (N1) |

**OF-7 (MINOR). The jitter control is matched in its largest displacement only.**
- Location: line 354, p. 14.
- Claim: "The jitter ensemble is a comparison at matched displacement size, not the random-matrix model of the zeros; a comparison with sections of the sine process is not carried out here."
- Evidence: the same paragraph defines the control's `u_n` as uniform on `[-max_{n<=N}|d_n|, max_{n<=N}|d_n|]`; job 260's specification reads "100 draws of lambda_n = n + u_n with u_n iid uniform on [-max_{n<=N} |delta_n|, +max_{n<=N} |delta_n|]", symmetrized like the zeta sections. Recomputed: at `N = 500`, `max |d_n| = 0.6642`, the zeros' root-mean-square displacement is `0.248`, the control's is `0.6642/sqrt(3) = 0.383`; at `N = 200`, `0.230` against `0.292`; at `N = 50`, `0.197` against `0.262`. Independent points can also nearly collide, which is what drives a section's lower constant down. Figure 1's caption already says "matched sup-norm jitter control".
- Fix: replace "The jitter ensemble is a comparison at matched displacement size, not the random-matrix model of the zeros;" with "The jitter ensemble matches the largest displacement only (at $N=500$ its root-mean-square displacement is $0.38$, against $0.25$ for the zeros), and its points are independent, so neighbors can nearly collide; it is not the random-matrix model of the zeros, and".

## E. The attribution block against paper/common/README.md

| Pattern item | In the block (line 26, pp. 1-2) | Verdict |
|---|---|---|
| 1. Writer and director, division of labor | "This paper was written by Claude Fable 5.1, an AI model made by Anthropic, at the direction of David Ross." The model chose the problem, proved the theorems, wrote the programs and text; David Ross "set the task, ran the process, and takes responsibility for the manuscript." | present |
| 2. Where the questions came from, and whose mathematics | "the record of Hypnos, the research harness described in Section~\ref{sec:provenance}"; "proved the theorems"; Section 8: "The theorems are the model's." | present |
| 3. Every review by model and vendor, with a verdict clause; findings applied; dispositions accompany | Self-review: model named, vendor implied, counts given (OF-5). Cross-vendor: "GPT-6 Astra, an OpenAI model run through the Codex CLI", one blocking error and five major items. Third review: GPT-6 Astra, "no blocking error, two major items (...) and four minor ones, all applied the same day". Chat session: named, no verdict clause (OF-6). "The reviews and the per-item dispositions accompany the source." | present, with OF-5 and OF-6 |
| 4. "No human mathematician has reviewed this paper." | verbatim | present |
| 5. Place in the set; written without reading the others; nothing called "the first" | "one of three manuscripts written from the Hypnos record on the night of 2026-09-28/29, after Astra's paper on approximate antiunitary symmetry and before the note on Gil's questions; it was written without reading the other two." | present |

House rules: `main.tex` is pure ASCII; no U+2014, no U+2013, no `---`; no British form (a regular-expression sweep over the usual -our, -re, -ise, -yse, doubled-l and -ogue forms finds only "cancellation", which is US usage); no Clay or Millennium wording and no (A)/(B) alternatives (the only "(A)" is Titchmarsh's "Theorem 9.9(A)"); every mention of the Riemann hypothesis is conditional. Nothing in the text claims beyond the theorems apart from OF-3, OF-9 and OF-10. The title block follows the house format (writer, director, Hypnos Math, date).

**OF-5 (MINOR). "a fresh instance of the same model line" for a review by a different model; the shipped ledger says the objection was already resolved.**
- Location: line 26, p. 1; `reviews/astra-2026-10-02/DISPOSITION.md`, section B, fourth row (this ledger ships to the reader as `review-by-Astra-2026-10-02-DISPOSITION-applied.md`).
- Claim: "an adversarial self-review by a fresh instance of the same model line (Claude Opus 5.5, 2026-09-29)".
- Evidence: the writer is Claude Fable 5.1 (lines 15 and 26); the reviewer, by the same clause, is Claude Opus 5.5. The chat review (`docs/outreach/2026-10-02/opus-chat-handoff/02-OPUS-PAPER-REVIEW-2026-10-01.md`) says: "The attribution calls Opus 5.5 "the same model line" as Fable 5.1. They share a vendor, not a model." The ledger row answers: "Already resolved | No match in `main.tex` since 1a420e9 (the consistency pass of 2026-10-01 replaced the old two-author byline)." That holds for "first/second author" only: `grep -n "model line" main.tex` returns line 26, and the phrase is in the text committed by 1a420e9 itself. The Gil note's block (`paper/gil-note/main.tex`, line 51) has the identical clause. Separately, the review's own header (`reviews/claude/REPORT.md`) names the reviewer only as "a fresh Claude Opus agent"; the version 5.5 is not in that record (UNCLEAR: settled by the dispatching session's transcript).
- Fix: replace the clause with "an adversarial same-vendor review by Claude Opus 5.5, an Anthropic model other than the writer, in a fresh context (2026-09-29)" (or "a Claude Opus model" if the version cannot be confirmed), and add one line to the ledger, for example in this review's disposition: "Chat item 'the same model line' (2026-10-02 ledger, section B): the phrase was present at main.tex:26; the 'already resolved' entry applied only to 'first/second author'; now applied." If the house keeps "self-review" as its term for a same-vendor review, the ledger should say so and why, instead of saying the phrase is gone.

**OF-6 (MINOR). The chat session has no verdict clause, and this review will need one.**
- Location: line 26, p. 2.
- Claim: "...all applied the same day, when the comments of a Claude Opus 5.5 chat session of 2026-10-01 were also adjudicated."
- Evidence: `paper/common/README.md`, pattern item 3: "The reviews, named by model and vendor, with their verdicts in one clause each, and the statement that every finding was applied and the reviews with their per-item dispositions accompany the source." The chat review's opening for the set: "All three papers hold up: I found no mathematical error"; for this paper it found the Conrey bound and the Section 8 overclaim (both applied) and judged the control the wrong one (one sentence added; a CUE control deferred). `paper/common/package_set.py` already ships `final-review-by-Claude-Opus-2026-10-02-REVIEW.md` and its disposition with this paper.
- Fix: "...when the comments of a Claude Opus 5.5 chat session of 2026-10-01 were also adjudicated (it found no mathematical error, and found the Conrey bound and an overclaim in the first sentence of Section~\ref{sec:provenance}, both applied)." After this review is applied, add one sentence naming it with its verdict, for example: "A final review by Claude Opus 5.5 (Anthropic) on 2026-10-02 found no blocking error, one major item outside the manuscript (its README) and nine minor ones, all applied the same day."

### Material that ships with the paper

**OF-1 (MAJOR). The paper's README, which the reader is told to read with the PDF, denies today's Theorem 6.1(a) and carries three other superseded statements.**
- Location: `paper/unfolded-zeros/README.md`, "Result" items 2 and 4, "Files" first bullet, "Reviews", last paragraph of "Provenance in the DB". The PDF statement it contradicts: line 262, p. 10.
- Claim (README, verbatim): "The unconditional lower bound is NOT available: the density estimate counts with multiplicity, and completeness depends only on the set (Astra's blocking item, applied 2026-09-29)."
- Evidence: line 262: "(a) Unconditionally, $D_{BM}(\Lam')=1$ for the counting measure with multiplicity, $\frac25\le D_{BM}(\Lam'^\ast)\le1$, and $\frac{2\pi}5\le R(\Lam'^\ast)\le\pi$". The README also says "`main.tex`, `main.pdf` (15 pages, amsart)" (the PDF has 17 pages in the house `article` format); "Neither contains Theorem 5.1" (line 358 now reads "Neither accessible account states Theorem~\ref{thm:main}, and we have not checked Mikulik's full manuscript", after UZ-6); its Corollary 4.2 line, "so Avdonin's `1/4` does hold at block length `~ log^2 T`", lacks the height quantifier; and its "Reviews" section lists two reviews where the attribution names three and the chat session. It ships: `paper/common/package_set.py` describes each folder as "the PDF, the paper's README, and every review report and per-item disposition under reviews/", and the cover `PACKAGE-README-2026-10-02.md` says: "The PDF in each folder is the paper. Its README is the project's own summary of the result and its provenance." The cover's own unfolded-zeros bullet ends at "The consistency pass made nine edits, none to a proof." and mentions neither the 2026-10-02 review nor the change to Theorem 6.1(a).
- Severity: MAJOR. The first reader is pointed to a summary that denies a theorem of the PDF.
- Fix:
  1. "Result" item 4, replace the first two sentences with: "**Theorem 6.1:** for the SET of distinct points, `2/5 <= D_BM <= 1` and `2 pi/5 <= R <= pi` unconditionally, and `R = pi` if all but finitely many ordinates are simple. The upper bound comes from the multiset's Beurling-Malliavin density, which is 1; the lower bound from Conrey 1989, Theorem 1 (at least 2/5 of the zeros are simple and on the critical line, and such zeros have distinct ordinates), added on 2026-10-02 (Astra's UZ-2 and the chat session's comment). Completeness depends only on the set while the density estimate counts with multiplicity (Astra's blocking item of 2026-09-29), so the exact unconditional radius is open."
  2. "Result" item 2: "so below height `T` Avdonin's `1/4` does hold at block lengths of order `log^2 T`".
  3. "Files": "`main.tex`, `main.pdf` (17 pages, the house format of `paper/common/`), `build.sh` (tectonic)."
  4. "Reviews": add `reviews/astra-2026-10-02/` (GPT-6 Astra, fresh to the paper: no blocking error, two major items, four minor, all applied on 2026-10-02; the same ledger adjudicates the Claude Opus 5.5 chat session's comments) and `reviews/opus-final-2026-10-02/` (this review and its disposition).
  5. "Provenance in the DB": "Neither accessible account states Theorem 5.1, and Mikulik's full manuscript was not checked".
  6. In the cover's unfolded-zeros bullet, one sentence: "On October 2 a fresh review by GPT-6 Astra (no blocking error; two major items, four minor) was applied; it added the unconditional bound $2\pi/5 \le R$ to Theorem 6.1(a), with its proof, from Conrey's theorem; a final review by Claude Opus 5.5 followed."

## F. Verdict

- **BLOCKING: 0.** No statement is wrong in substance and no proof has a gap.
- **MAJOR: 1.**
  - OF-1: the README that ships beside the PDF says Theorem 6.1(a)'s new lower bound is "NOT available" and carries three superseded statements.
- **MINOR: 9.**
  - OF-2: "raises the proportion to two thirds" skips the published record (`kappa* >= 0.407511`); "has not been peer reviewed" is not stated by the preprint.
  - OF-3: Section 8 says every statement rests on Section 2's inputs; Theorem 6.1(a) also rests on Conrey's theorem.
  - OF-4: Section 6.1's opening still describes only an upper bound for the set.
  - OF-5: "a fresh instance of the same model line" for a different model, and a shipped ledger row that says the objection was resolved when it was not.
  - OF-6: no verdict clause for the chat session; this review to be named once applied.
  - OF-7: the jitter control is matched in maximal displacement, not in typical displacement.
  - OF-8: "strictly increasing across simple zeros" fails for an off-line pair of simple zeros.
  - OF-9: Section 8's "it does at block length log^2 T" lacks "below height T" and belongs to Corollary 4.2.
  - OF-10: Section 4's title "fail at every height scale" can be read against Corollary 4.2.
- **NIT: 8** (no change needed to send):
  - N1, line 328, p. 13: "to $3.2\cdot10^{-34}$ over a run of $12$ windows" for a recorded `3.1420e-34` (`data/verify_10000.json`, `B_worst_resid`); `3.1` matches the "reproduced to the digits printed" convention. The same sentence's "windows of $1$ to $150$ ordinates" should be checked against `scripts/verify_identity.py:120` (`random.randrange(1, 150)`).
  - N2, line 102, p. 5: "where $N(\gamma^-)$ is the number of ordinates below $\gamma$" reads unambiguously as "where $N(\gamma^-)=\#\{k:\gamma_k<\gamma\}$".
  - N3: `scripts/verify_identity.py` lines 15 and 160 say "centred"; US English applies to code comments: "centered".
  - N4, line 367, p. 15: "the result and artifact files of jobs 67, 100, 110, 166, 202, 260, 263, 313": job 67 has no artifact file and jobs 100 and 166 have no `result.json`; "the retained result and artifact files" is exact.
  - N5, line 63, p. 4 (optional): Goldston and Gonek's constant `1/2` has since been improved to `1/4` (Bober and Hiary, arXiv:1607.00709v1, p. 6, report the improvement).
  - N6, line 26 (optional): "A third review on 2026-10-02": the review's header gives "October 1, 2026, 23:58 EDT"; it was committed at 2026-10-02 00:00 EDT (`fb3967a`). "of the night of 2026-10-01/02" fits both.
  - N7, line 26 (optional): the consistency pass of 2026-10-01/02 (a fresh Claude Opus 5.5 agent, 46 checks, nine edits) is not named in the block; the other papers' blocks do not name theirs either, and the package cover does.
  - N8, line 16 (optional): the date line stays "September 29, 2026" although Theorem 6.1(a) changed on October 2; the earlier ledger's reason for keeping it ("the day of every review and edit", `reviews/astra/DISPOSITION.md`) no longer holds. "September 29, 2026; revised October 2, 2026" would say so.

**Decision.** The manuscript is ready for its first reader as far as its mathematics and numbers go:
every statement checked holds, today's new proof paragraph is correct in every step and constant,
and every printed number reproduces to its digits from independently computed zeros or from the
certified table. The package is not ready as it stands, because the README that ships beside the
PDF, and that the cover tells the reader to read, denies Theorem 6.1(a). The smallest set of edits
that makes it ready:

1. OF-1: correct the README (items 1 to 5 of its fix) and add the one sentence to the cover's
   unfolded-zeros bullet.
2. OF-5: correct the shipped ledger row on "the same model line", and either change the clause or
   record why the house keeps it.
3. OF-6, second half: name this review in the attribution block with its verdict clause (the house
   pattern requires it, and `package_set.py` already ships this file with the paper).

Recommended in the same pass, one phrase each and no proof touched: OF-3, OF-8 and OF-9 (literal
inaccuracies in the manuscript), then OF-2, OF-4, OF-6 (first half), OF-7 and OF-10. Then rebuild
(expect 17 pages and no new warning) and rerun `package_set.py`.

**Confirmations (the audit record).**

- Every theorem, proposition, lemma, corollary and remark: verdicts in the table of section A,
  with the new lower bound of Theorem 6.1(a) checked step by step (A.1: Conrey's `kappa*` is a
  liminf of the proportion of zeros that are simple and on the line; distinct ordinates; both sides
  of `A(x)`; the family `[C^k, C^{k+1})` long and dense enough; finite modifications; directions
  and constants) and the rewritten paragraph after Corollary 4.2 checked against the proof of
  Theorem 4.1 (A.2).
- The abstract and introduction: every inequality, condition, quantifier and strictness matches
  a theorem with the same hypotheses (section B).
- Sources: Conrey (Theorem 1 and (11)-(12)), Alpöge and Furman (abstract, Theorem A, the `(0, T)`
  form, the Lean statement, no journal reference), Kozma and Lev (Theorem 5.1, p. 14), Alemany
  and Nitzan (p. 2: `c = 0`, blocks `mN <= n <= (m+1)N - 1`), Bober and Hiary (Table 2, p. 7),
  Tsang ((1.2) p. 369; Theorem 3 p. 370), Titchmarsh (Theorems 9.4, 9.9 (A), 14.13 at pp. 214,
  222, 350), Inoue (Theorem 1), Goldston (Theorem 8, (10.6)), Seip and Ulanovskii (p. 1745),
  Bufetov and Ghosh (abstracts), and bibliographic metadata for the remaining entries (section C).
- Numbers: every value listed in section D agrees to the printed digits, except that `3.2e-34` is
  a ceiling of the recorded `3.142e-34` (N1); the first 1000 zeros computed independently with
  `mpmath.zetazero` agree with the certified table to `5.0e-19`.
- Build: a scratch rebuild gives 17 pages, no undefined reference, no overfull or underfull box,
  only the two known benign warnings, and text identical to the committed PDF.
- House rules: ASCII only; no em dash, en dash or `---`; US English; no Clay (A)/(B) wording;
  "No human mathematician has reviewed this paper." present verbatim; writer, director and place
  in the set stated as the pattern requires.
- Provenance: the job-to-node ids in `data/hypnos-jobs/` match Section 8's groupings; the job dates
  on record (jobs 25 and 48: 2026-08-19 and 2026-08-23 UTC) fall inside the stated window of
  12 August to 27 September 2026.
