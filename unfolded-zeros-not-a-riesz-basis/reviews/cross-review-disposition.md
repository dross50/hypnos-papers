# Disposition of Astra's referee report on paper/unfolded-zeros

Review: `reviews/astra/REVIEW.md` (OpenAI Codex, gpt-6-astra, launched by Claude through the
Codex CLI on 2026-09-29 13:12 EDT with the prompt in `reviews/astra/PROMPT.md`; committed at
23c0132, 13:40 EDT). Reviewed manuscript: `main.tex` blob 448de51 (the d8e4ce4 text, after the
Opus self-review was applied). Applied by Claude (Fable 5.1) on 2026-09-29, 14:00 to 14:30 EDT,
the same way d8e4ce4 applied the Opus review: every finding read against the text, every fix
made in place, nothing of the mathematics changed except where the review showed a gap.

Legend: APPLIED = the fix in the review was made; APPLIED (variant) = the same defect fixed by
a different edit, stated; DECLINED = not changed, with the reason.

## 1. BLOCKING, check (f): Theorem 6.1 applied a multiplicity-sensitive density to a multiplicity-insensitive span

APPLIED. The theorem is restated for the set of distinct points `Lambda'*`. Part (a),
unconditional: the multiset's Beurling-Malliavin density is 1 and the set's completeness
radius is at most pi (support counts are bounded by multiplicity counts). Part (b), under the
hypothesis that all but finitely many ordinates are simple: the set has finitely many repeated
points (ordinate multiplicity plus the finitely many cross-half coincidences
`theta(gamma_n) + theta(gamma_m) = -2 pi a`), its density is 1, and the radius is exactly pi.
A paragraph after the theorem says plainly that the unconditional lower bound is not available
and why. The subsection opens with the distinction the review drew: completeness depends only
on the set; the multiplicity form of Beurling-Malliavin concerns the exponential polynomials
`t^j e^{i lambda t}` (Seip and Ulanovskii, Proc. AMS 125 (1997), p. 1745, cited for the
convention), a different system. Abstract, introduction and README now carry the conditional
statement. The hypothesis is phrased on ordinates, not zeros, per finding 2 (two simple zeros
off the line share an ordinate); under RH it reads "all but finitely many zeros are simple".

## 2. MAJOR, check (c): Lemma 3.3 false on its stated domain for negative `a`; the finite-modification paragraph wrong

APPLIED, both parts. The cutoff is now `X_a > max(1, x_a(7), -x_a(gamma_1))`, chosen not to
be a point of `Lambda_a`, so every reflected negative frequency lies below it; the lemma is
stated for `x >= X_a`, the proof counts the points of `[X_a, x)` and the constant absorbs
`n(X_a) - N(t_a(X_a))`; the proof of Theorem 5.1 starts its windows at `T >= t_a(X_a)`. The
paragraph before that proof was rewritten as the review specified: a Riesz basis has no repeated
element, so the theorem holds for every sequence as stated; repetitions come from ordinates of
multiplicity at least 2 and from the finitely many cross-half coincidences; finitely many can be
removed by a finite modification (bounded change of the counting function), infinitely many
cannot; for the set of distinct points the theorem is proved when all but finitely many
ordinates are simple, and says nothing otherwise. The CORRECT verdict on the analytic
obstruction (Kozma-Lev transcription, the Landau step `d <= D^- <= 1 <= D^+ <= d`, the
Jacobian, the `1/(8 pi^2)` coefficient, John-Nirenberg's direction, finite modifications,
Theorem 5.2) needed no change.

## 3. MAJOR, check (d): Remark 5.4's verification of condition (iii) was incomplete

APPLIED, with the review's direct HNP repair written out: the counting normalization
`n_Z(u) = ceil(u)`, the decomposition `f = q + 1/2 + g + R` with `g = -(c/2) log(1 + x^2)` (the
nonsingular model) and `R` bounded, Lipschitz and `O(log|x|/|x|)`, hence in `L^2`; the gap
integrals of `q` are `O((1+|n|)^{-2})` after subtracting `T'(n)`, so `q` has a bounded primitive
`Q` and `||P_y * q||_inf <= (2/(pi y)) ||Q||_inf < 1/4` for large `y`; `P_y * g = -c log|x + i(1+y)|`
has bounded conjugate; `R~` is bounded (Lipschitz cancellation plus Cauchy-Schwarz) and
`P_y * R = u_2~` with `u_2 = -P_y * R~` in `L^inf` since `R~~ = -R` on `L^2`. The false claim that
the remainder is smooth is gone, as is the sentence about larger `|c|`. The Lyubarskii-Seip
parenthetical no longer asserts the weight bounds; it names the criterion as another route not
carried out. The remark is still labeled a sketch.

## 4. MAJOR, checks (e) and (h): Corollary 5.3's applications not adequately sourced

APPLIED (variant). The corollary is kept exactly in terms of its analytic hypotheses. Its proof
now notes the two changes the review asked for: the finite-prefix cutoff of Lemma 3.3, and a
Jacobian only comparable to `log t`, so the ratio of its bounds is a constant `K` and the factor
`1/4` becomes `1/(2K)`. The sentence asserting the Dirichlet and Selberg-class applications was
replaced by a paragraph stating that no family is verified in the paper: for a fixed Dirichlet
`L`-function the height-aspect mean square is the subject of Selberg's method (Selberg 1946b),
the Selberg-class results were announced (Selberg 1992), and a statement of exactly the
displayed form for a fixed function has not been confirmed from either source. The review's
alternative, precise fixed-function theorem and page references, was not available to either
reviewer or to us without the original 1946 Dirichlet paper; the honest fix is the conditional
statement, which is what stands.

## 5. MAJOR, check (g): a false sample/error pairing and overstated reproducibility

APPLIED, every sub-item.
- Block residual: `7.3e-34` over the 40-window run, `3.2e-34` over the 12-window run, both stated.
- Height versus index: the `|S| <= 1.63` bound is now stated over the harness's table, whose last
  ordinate lies at height `7.49e4`; "for `t <= 10^5`" is gone.
- Bober-Hiary: cited as a literature measurement (`S ~ 3.3455` just after a zero near
  `7.7573e27`, their Table 2); "largest ever" and "no computation has seen" replaced by "the
  largest in the published record known to us" and "larger than any value of `S` we know to have
  been computed".
- Job 313: the paper now says the job recorded the raw one-sided residual, whose magnitude runs
  from `1.3e-7` to `1.5e-6` across the table, the size of `eps theta'/pi` from bottom to top; not a
  separately reported error after subtracting that term.
- Fit ranges: `-1.03` over `M = 4096, ..., 65536` (job 110) and `-0.94` on job 67's coarser scan;
  "the decay is `D(M) ~ M^{-1}`" became "over the tested range the decay is consistent with
  `M^{-1}`; a finite fit does not establish the asymptotic order". Same change in Section 4's
  closing sentence.
- `D(8) = 0.216` added beside `D(6) = 0.330`; "among the block lengths tested" was already there.
- Eigenpair residuals: `8.4e-31` in the job's primary normalization and `1.4e-30` for
  sup-norm-normalized eigenvectors, both stated; "below `10^{-30}`" is gone.
- Reproducibility language: the numerics introduction now says which quantities were
  recomputed with independent code (identity residuals, Kadec and Avdonin statistics, closest
  pairs) and which are quoted from the job records (finite-section constants, confirmed in double
  precision only; the jitter ensemble as recorded). The two limits of the verification scripts
  (algebraic block check, finite phase steps) are stated, with the note that neither bears on the
  proofs.
- Historical jobs: jobs 100 and 166 now have their artifact files vendored under
  `data/hypnos-jobs/`; the artifact directories of jobs 25 and 48 were not retained on the
  execution host, so their execution records with every check value were copied from the
  harness's database to `job-25/db-record.json` and `job-48/db-record.json`. The Provenance and
  Data-and-code sections say so.
- `scripts/make_figures.py`: reads `../data/hypnos-jobs` and writes `../figures` by default;
  rerun, figures regenerated.

## 6. MAJOR, check (i): the broad novelty claim missed a directly relevant preprint

APPLIED. Mikulik, "Unfolded Gaussian Gram stability for zeta zeros" (ResearchGate preprint,
April 2026; verified 2026-09-29 through the ResearchGate page, abstract only, no file
available) and Burnol, JTNB 16 (2004) 65-94 (verified through the journal's page) are cited in
the Provenance section and distinguished from Theorem 5.1 in the terms the review gave; the
harness's "absence in print" sentence is kept as a report of what the sweep found, and the
paper's own claim is now the narrow one: no earlier proof of the exact Selberg-variance/Pavlov
obstruction for the theta unfolding was found, a bounded search and not a certification of
priority. README updated the same way.

## 7. MINOR group, checks (b), (f), (g), (h)

- Threshold after Theorem 4.1: APPLIED. The paragraph now names the windows an excursion
  defeats (the preceding uncentered sliding window at `A > N/2 + 1/4`; the last complete
  partition block at `A > r + N/2 + 1/4` with `r = N(t_0) mod N`; centered thresholds shifted by
  `c`; the following window at a negative excursion at `A > N/2 + 1/4 + c`) and says an excursion
  defeats those windows, not every window. The bracketing paragraph is restricted to the
  uncentered sliding-window form and to windows below the height in question, and says that a
  finite-height bound does not assert Avdonin's global hypotheses.
- Corollary 4.2: APPLIED. Endpoint corrections for a block cutting a repeated ordinate
  (`m = O(log b)` displacements of size `O(log b)`, absorbed into the constant), the strict
  inequality `M > 4C log^2 b`, and "with a larger absolute constant".
- Long-family calculation: APPLIED inside the new proof of Theorem 6.1: the upper direction
  derives `L <= C_d log(2 + r)` from `(d-1)L <= K log(2 + r + L)` by absorbing `log(1 + L)`, and
  the "never long" argument groups intervals by `dist(0, I)` in shells `2^j <= r < 2^{j+1}` (which
  handles intervals crossing dyadic boundaries) with the near-origin family bounded separately.
- Tsang's range: APPLIED, `1/log t <= h <= 1/log log t`, with the theorem number.
- Interpretation of numerical bounds: APPLIED. "Explains the decay ... driven by the closest
  pair" became "an upper bound; the observed decay is consistent with it" (two places); the
  upper-constant sentence now names the Bessel half of the frame question and what else a frame
  needs; the `-7e-6` mean is attributed to Proposition 3.2 with (S2) and (S4), not to Theorem 3.1.
- Separation for every `a`: APPLIED. Question 6.3 asks about the positive half, with the
  finitely many cross-half coincidences named (`a = -theta(gamma_1)/pi` puts `0` twice).

## 8. CORRECT, check (a): algebra of Theorem 3.1 and Proposition 3.2

APPLIED the one fix: "multiplicity of an ordinate" is defined in Section 2 as the total jump of
`N`, "simple ordinate" replaces "simple zero" wherever the scalar identity is asserted (abstract,
Theorem 3.1, the paragraph after it), and the text notes that a simple zero need not lie on a
simple ordinate off the line, with the two notions coinciding under RH.

## 9. CORRECT, check (b): Theorem 4.1's proof

No change to the proof; the explanatory threshold claim fixed under item 7.

## 10. CORRECT with exceptions, check (h): citations

- Titchmarsh for (S2): APPLIED, now `Theorem 9.9(A)`; verified against the scanned second
  edition (Theorem 9.9 is Littlewood's formula for `S_1`, Theorem 9.9 (A) is `S_1(T) = O(log T)`).
- Bober-Hiary: cited as their Table 2 (item 5).
- Tsang: theorem number and range (item 7).
- Kadec, Avdonin, Pavlov/HNP via Kozma-Lev, Landau, Beurling-Malliavin, Selberg 1946 (both
  results), Ghosh, Bufetov, Inoue: no change needed, per the review.
- Selberg 1946b and 1992: handled under item 4.

## 11. CORRECT, checks (f), (g): Proposition 6.2

APPLIED: `N >= 2` for the closest-pair assertions, `sinc(0) = 1`, the equality condition for
`A_N = 1`, and the causal reading removed (item 7).

## Verdict and recomputed numbers

The review's verdict (Theorem 5.1 proved in substance, no missing number-theoretic input;
revision required for Theorem 6.1, Remark 5.4, Corollary 5.3's applications, novelty and
numerical reporting) is accepted in full and every named item is addressed above. The
recomputed numbers in the review agree with the committed records at every printed digit; the
2,000- and 20,000-zero runs it requested have their own extrema, as it notes, and the 100,000-zero
supplement matches the published record exactly.

## Not changed

- The authorship, title, and the framing of Section 8 (the harness's provenance): outside the
  review's scope.
- The date line: kept at September 29, 2026 (the day of every review and edit).

## Consistency pass, 2026-10-01 (fresh Claude Opus 5.5 agent, directed by the Claude Fable 5.1 outreach thread)

Scope: five bounded checks and nothing else (the abstract and Section 1 against the statements they summarize, every quotation against its source text, every page, table and theorem citation, the attribution block against `paper/common/README.md`, and US English and the house rules); the mathematics was not re-reviewed.

| # | check | item checked | source and page | command or method | finding | verdict | what was done |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Abstract: "the set Lambda_{3/2} cup {0} is modeled on Z" | main.tex eq. (1.1) ("sequences counted with multiplicity"); the paragraph before the proof of Theorem 5.1 | read both, compare | "set" clashes with the body's sequences counted with multiplicity and reads the main result onto the set of distinct points, which Theorem 5.1 covers only when all but finitely many ordinates are simple | CORRECT, applied | "the set" became "the sequence" |
| 2 | 1 | Abstract: "at every simple ordinate ... x_n - n = -S(gamma_n) with S(t) = pi^{-1} arg zeta(1/2 + it)" | Theorem 3.1; Section 2.1 (S at an ordinate is the mean of the one-sided limits) | compare | "simple ordinate" matches; the identity is exact only under the mean-value convention at an ordinate (under the right-limit convention it is off by 1/2), and the abstract did not state it | CORRECT, applied | added "(at an ordinate, the mean of its one-sided limits)" |
| 3 | 1 | Abstract: Kadec and Avdonin "fail unconditionally for every centering constant and every block length" | Theorem 4.1 (every N >= 1 and c, partition and sliding forms; (S3) is unconditional) | compare | matches | NO FINDING | none |
| 4 | 1 | Abstract: "the block condition does hold at block lengths of order log^2 T" | Corollary 4.2 (blocks whose ordinates lie below height b, M > 4C log^2 b) | compare | the corollary is a statement below a given height; the abstract dropped that quantifier and had not yet defined T, so the clause read as contradicting "fail ... for every block length" | CORRECT, applied | "although below height T the block condition does hold ..." |
| 5 | 1 | Abstract: main result for every a, every finite modification, every bounded interval | Theorem 5.1 | compare | matches (the theorem also covers translates and the one-sided system) | NO FINDING | none |
| 6 | 1 | Abstract: the mean square of S over [T,2T] "grows like (2 pi^2)^{-1} log log T" | (S1) | divide (S1) by T | (2 pi^2)^{-1} log log T + O((log log T)^{1/2}); matches | NO FINDING | none |
| 7 | 1 | Abstract: "applies to any L-function whose argument has a Selberg-type mean square" | Corollary 5.3 (displayed hypotheses: the mean square of S_F over [T,2T] tends to infinity AND the integral of S_F over [0,T] is O(T)) | compare | the bounded-mean hypothesis was dropped; without it a smooth drift gives a divergent mean square inside BMO (self-review item 4(a)); the setting hypotheses (theta_F' comparable to log t, S_F = O(log t)) stay with the word "L-function" | CORRECT, applied | "... a Selberg-type mean square and a bounded mean" |
| 8 | 1 | Abstract: distinct points incomplete for every b > pi, complete for every b < pi if all but finitely many ordinates are simple | Theorem 6.1(a), (b) | compare strictness and hypothesis | matches | NO FINDING | none |
| 9 | 1 | Abstract: "the separation of Lambda_a remain open" | Question 6.3 (asks about the positive half; names the cross-half coincidences, 0 twice at a = -theta(gamma_1)/pi) | compare | for the countably many a with a cross-half coincidence Lambda_a is not separated, so only the positive half is open; Astra item 7 fixed the question, not the abstract | CORRECT, applied | "the separation of the positive half of Lambda_a" |
| 10 | 1 | Abstract: provenance sentence | Section 8 | compare | matches | NO FINDING | none |
| 11 | 1 | Introduction: x_n approx n; Lambda_{3/2} cup {0} and Lambda_1 perturb Z and Z + 1/2; density one | Theorem 3.1 and the paragraph after it | compare | matches | NO FINDING | none |
| 12 | 1 | Introduction: "the displacement from the lattice is the argument of zeta, x_n - n = -S(gamma_n)" | Theorem 3.1 (general form -S(gamma) + (m+1)/2 - j; the scalar form only at simple ordinates) | compare | stated for every n; Astra item 8 put "simple ordinate" into the abstract, Theorem 3.1 and the paragraph after it, not into this sentence | CORRECT, applied | added "at every simple ordinate" |
| 13 | 1 | Introduction: block sums "governed by the integral of theta' S and by jumps of S^2/2" | Proposition 3.2 and its proof | compare | matches | NO FINDING | none |
| 14 | 1 | Introduction: Kadec and Avdonin fail "for every centering and every fixed block length", unconditionally, from the unboundedness of S | Theorem 4.1 and its proof ((S3) in both directions) | compare | matches | NO FINDING | none |
| 15 | 1 | Introduction: "the averaged condition holds once the block length is of order log^2 T" | Corollary 4.2 | compare | the same missing height quantifier as row 4 | CORRECT, applied | "below height T the averaged condition holds once ..." |
| 16 | 1 | Introduction: main theorem sentence | Theorem 5.1 | compare | matches | NO FINDING | none |
| 17 | 1 | Introduction: HNP makes BMO of n_Lambda(x) - x necessary; Selberg plus Littlewood; "applies to L-functions with a Selberg-type argument variance" | Theorem 2.3(ii), (S1), (S2), Theorem 5.2, Corollary 5.3 and its proof | compare | a divergent variance is what the two displayed hypotheses of Corollary 5.3 give together and what its proof uses | NO FINDING | none |
| 18 | 1 | Introduction: radius of the set of distinct points at most pi, equal to pi if all but finitely many ordinates are simple | Theorem 6.1 | compare | matches | NO FINDING | none |
| 19 | 1 | Introduction: Gram sections obey a pair bound consistent with the observed decay | Proposition 6.2 and the paragraph after it | compare | matches (an upper bound, consistency only) | NO FINDING | none |
| 20 | 1 | Introduction: four items "remain open (Section 6.3)" | Section 6.3 (three questions); the paragraph after Theorem 6.1 | compare | the unconditional radius is discussed after Theorem 6.1, but Question 6.4 (completeness at the critical length) would settle it together with Theorem 6.1(a), so the pointer holds | NO FINDING | none |
| 21 | 1 | Introduction: n + c log(2 + abs(n)) generates a Riesz basis of L^2(-pi,pi) for every abs(c) <= 1 | Remark 5.4 | compare | matches (indexed by Z, abs(c) <= 1, called a sketch in both places) | NO FINDING | none |
| 22 | 1 | Introduction: Selberg's central limit theorem with variance (2 pi^2)^{-1} log log T | (S1) | compare | consistent | NO FINDING | none |
| 23 | 2 | ``1/4 in the mean'' (abstract), the name of Avdonin's condition | Alemany and Nitzan, arXiv:2501.11598 (the source cited for Theorem 2.2); Avdonin 1974 | `grep -n -i "in the mean" alemany-nitzan-2501.11598.txt` | the phrase does not occur in AN; Avdonin 1974 (Vestnik LGU, Russian) is not fetchable | NOT CHECKABLE | left alone; it names the condition and does not quote AN |
| 24 | 2 | ``long'' family of intervals (Section 2, Beurling-Malliavin density) | Beurling and Malliavin, Acta Math. 118 (1967); Koosis, The Logarithmic Integral II | `curl` of the Project Euclid PDF returns a bot-protection page; Koosis II is a paywalled book | not checkable; Seip and Ulanovskii, p. 1745, "Following [3]" (Koosis II), call such a system "substantial", so "long" may not be the cited sources' word; the quotes mark a term defined in the same sentence | NOT CHECKABLE | left alone |
| 25 | 2 | ``centering constant'' (Section 7) | the harness's record, `artifacts/runs/run-13/report.md` | `grep -r -i "centering constant"` over the Hypnos repo | the record says "a pinned centering constant c = 3/2"; it is the harness's own term | NO FINDING | none |
| 26 | 2 | Theorem 2.3, "we quote it as stated by Kozma and Lev [Theorem 5.1], translated" | Kozma and Lev, arXiv:1009.2188v2, Theorem 5.1, p. 14 (printed = PDF) | `pdftotext -layout -f 14 -l 14 kozmalev-1009.2188.pdf -` | (i) separation, (ii) n_Lambda(x) - ax in BMO, (iii) U_f = c + u~ + v with u, v bounded and the sup norm of v below 1/4, and the counting-function and BMO definitions all match after a = 1 and the change from e^{2 pi i lambda t} on (0,1) to e^{i lambda t} on (-pi,pi) | NO FINDING | none |
| 27 | 3 | [HNP, p. 240] | Hruscev, Nikol'skii and Pavlov, LNM 864 (Springer) | not fetchable; KL p. 13 read with pdftotext | KL introduce the same statement as "the following version of Pavlov's theorem (see [7, p. 240])", the same pinpoint | NOT CHECKABLE | left alone (corroborated by KL's pinpoint) |
| 28 | 3 | [KozmaLev, Theorem 5.1] | arXiv:1009.2188v2, p. 14 | `pdftotext -f 14 -l 14` and grep "Theorem 5.1" | resolves; the cited journal version (JFAA 17) was not fetched and is taken to keep the arXiv v2 numbering | NO FINDING | none |
| 29 | 3 | Theorem 2.2, "see [AlemanyNitzan] for the form used here" | AN, arXiv:2501.11598v1, p. 2 (printed = PDF) | `pdftotext -enc UTF-8 -layout -f 1 -l 2` | AN state uniform discreteness, a finite supremum of the displacements, and block means over mN <= n <= (m+1)N - 1 below 1/4 in absolute value with no centering constant, for L^2[0,1]; the paper's (c) adds a centering constant c and offsets the blocks by one | CORRECT, applied | the sentence after Theorem 2.2 now says that the AN statement has c = 0 and the blocks mN <= n < (m+1)N, both harmless by modulation |
| 30 | 3 | [Titchmarsh, Theorem 9.9(A)] for S_1(T) = O(log T) | Titchmarsh, 2nd ed., 1986 | no copy fetchable or on disk (find over the repo, Downloads and the scratchpads) | not checkable | NOT CHECKABLE | left alone |
| 31 | 3 | [Titchmarsh, Theorem 9.4] for S(t) = O(log t) | the same | the same | not checkable | NOT CHECKABLE | left alone |
| 32 | 3 | [Bober, Table 2]: S approx 3.3455 just after a zero near t = 7.7573e27 | Bober and Hiary, arXiv:1607.00709, Table 2, p. 7 (printed = PDF) | `pdftotext -layout -f 7 -l 7` and grep | first row t = 7757304990367861417150213053.6386, S(t) = 3.3455; the caption says a positive value is attained just after the zero | NO FINDING | none (the journal version, Exp. Math. 27, was not fetched) |
| 33 | 3 | [SeipUlanovskii, p. 1745] for the convention t^j e^{i lambda t} at a point of multiplicity m | Proc. AMS 125 (1997), p. 1745 (PDF p. 1), from ams.org | `pdftotext -layout -f 1 -l 1` | p. 1745 defines E(Lambda) = {t^l e^{i lambda_n t}}, 0 <= l <= p_n - 1, with p_n the multiplicity | NO FINDING | none |
| 34 | 3 | [Tsang86, Theorem 3]: excursions of size (h log t)^{1/3} for 1/log t <= h <= 1/log log t | Acta Arith. 46 (1986), p. 370 (scan `aa4646.pdf` from matwbn.icm.edu.pl; two printed pages per PDF page, p. 370 is the left half of PDF p. 2) | rendered with PyMuPDF and read | Theorem 3, proved "Without assuming the RH": sup over [T,2T] of +/-(S(t+h) - S(t)) >= c (h log T)^{1/3} for h in [(log T)^{-1}, (log log T)^{-1}] | NO FINDING | none |
| 35 | 3 | (S3) credited to Selberg, "see also Tsang" | Tsang, p. 369, eq. (1.2) | the same render | S(t) = Omega_pm((log t)^{1/3} (log log t)^{-7/3}), credited to Selberg ([6], Theorem 9) | NO FINDING | none |
| 36 | 3 | Inoue: under RH infinitely many normalized gaps below 0.509 | arXiv:2604.05733v1, abstract and Theorem 1 | `pdftotext -f 1 -l 2` and grep | "Under the Riemann Hypothesis, we have mu < 0.50895" | NO FINDING | none |
| 37 | 3 | Bufetov: excess one; one point removed leaves a uniqueness set, two leave a zero set | arXiv:1912.13454v1, abstract, p. 1 | `pdftotext -f 1 -l 2` and grep | matches | NO FINDING | none |
| 38 | 4 | Attribution block against `paper/common/README.md`, pattern items 1-5 | README.md; the blocks of the antiunitary paper and the Gil note | read and compare | writer, vendor, director and the division of labor (1); Hypnos and Section 8 (2); both reviews named with model and vendor, dispositions said to accompany the source (3); "No human mathematician has reviewed this paper." verbatim (4); one of the three manuscripts of 2026-09-28/29, after Astra's and before the Gil note, written without reading the other two, no paper called "the first" (5) | NO FINDING (apart from row 39) | none |
| 39 | 4 | Self-review clause "which found five major items" | `reviews/claude/REPORT.md`, opening line and Verdict | read | a count, not a verdict; the review opens "I found no BLOCKING error" | CORRECT, applied | "which found no blocking error and five major items" |
| 40 | 4 | Astra clause "one blocking error (...) and five major items" | `reviews/astra/REVIEW.md` | grep for BLOCKING and MAJOR | one BLOCKING (item 1) and MAJOR items 2-6; matches | NO FINDING | none |
| 41 | 4 | "Two reviews were applied in full" | the disposition in REPORT.md (items 1-12 applied; item 13, that journals do not accept an AI author, left as the owner's call); this file | read | the owner settled item 13 with the house format of 2026-09-29 ("Written by ... at the direction of David Ross"); with row 42 applied no sentence presents the model as an author | NO FINDING | none |
| 42 | 4 | Section 8: "built by the second author", "The theorems are the first author's", "The second author directed the work" | `git show aab6215^:paper/unfolded-zeros/main.tex` (old byline `\author{Claude Fable 5.1}`, `\author{David Ross}`); the README house format | grep for "first author" and "second author" | references to an author list that the house format removed; "built by" David Ross also disagreed with the methods paper's attribution ("The loop it describes, its audits, and this text are the model's work; David Ross directed the program") | CORRECT, applied | "built at the direction of David Ross", "The theorems are the model's", "David Ross directed the work" |
| 43 | 5 | US English | main.tex | Python regex over about seventy British forms (colour, behaviour, centre, normalise, summarise, favour, labelled, modelling, analyse, the -ise verbs, the -our nouns) and a review of every word ending in -ise, -our, -re, -lled or -ence | none found | NO FINDING | none |
| 44 | 5 | Em dashes | main.tex | counts of U+2014, U+2013 and "---"; a non-ASCII scan | 0, 0 and 0; the file is pure ASCII | NO FINDING | none |
| 45 | 5 | The Clay problem alternatives (A)/(B) | main.tex | grep for Clay, Millennium, "(A)", "(B)" | only Titchmarsh's "Theorem 9.9(A)" | NO FINDING | none |
| 46 | 5 | Claims about the Riemann hypothesis | main.tex | grep for "Riemann hypothesis" and RH | five occurrences, all conditional (the improved (S2) and (S4), the conditional form of Corollary 4.2, the reading of Theorem 6.1(b), Inoue's conditional bound); no claim about RH itself | NO FINDING | none |

Build: `bash paper/unfolded-zeros/build.sh` succeeded; rerun with `--keep-logs`, main.log reads "Output written on main.xdv (16 pages, 127420 bytes)", so main.pdf has 16 pages, as before the pass. Its two warnings (the `../common/hypnos-paper` package-name request and inputenc ignored under a UTF-8 engine) also appear in a build of the committed text, so neither is new. The pass changed only `paper/unfolded-zeros/main.tex`, `main.pdf` and this file.
