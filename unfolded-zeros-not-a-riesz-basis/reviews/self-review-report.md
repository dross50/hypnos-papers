# Adversarial self-review (Claude side) of "The unfolded zeros of the Riemann zeta function do not form a Riesz basis of exponentials"

Reviewer: a fresh Claude Opus agent, dispatched by the authoring session (Claude Fable 5.1) on
2026-09-29 at about 00:24 EDT, with instructions to read only `paper/unfolded-zeros/main.tex`
(no other draft or review directory) and to check every proof and citation. Baseline reviewed:
the text as of commit 7f0cfb6 with the small edits that followed within the hour. Duration 38
minutes, 34 tool calls, numeric checks with mpmath. The report below is the reviewer's text as
delivered. Every MAJOR and MINOR item was applied in commit d8e4ce4 (see the last section).

---

I found no BLOCKING error. The core argument of Theorem 5.1 holds. Five issues are MAJOR, and the most serious one changes what the headline theorem actually says.

## MAJOR

1. **The unfolding constant 3/2 makes Λ a perturbation of Z\{0} (line 127, eq. (1.1), Theorem 5.1, Section 4).**
   - What: With x_n = θ(γ_n)/π + 3/2 we get x_n ≈ n. The computed value is x_1 = 0.94975, so the gap at the origin is 1.90. The counting deviation is f(x) = n_Λ(0) − ½sgn(x) + sgn(x)S(t(|x|)).
   - Why it matters: The unperturbed model E(Z\{0}) is incomplete (deficiency 1). Even if |S| were below 1/4, Λ would still not be a Riesz basis, because Λ ∪ {0} would satisfy Kadec and removing a point from a Riesz basis leaves an incomplete system.
   - False sentence: Line 127 says any other unfolding constant is "harmless for basis questions". For the symmetric set that is wrong. Changing the constant moves the two halves in opposite directions, which is not a translation. The discarded constant 1 gives {±(θ(γ_n)/π+1)} ≈ Z+½, which is the natural candidate.
   - Kadec/Avdonin framing: Any Z-enumeration of Λ has displacement about d_n+1 on one side and −d_n on the other. So both conditions fail for Λ for a reason unrelated to S.
   - Fix: Delete "harmless". State Theorem 5.1 for Λ_a = {±(θ(γ_n)/π+a)} for every real a, plus any finite modification. The proof covers these word for word: condition (ii) ignores bounded changes of n_Λ, and n_{Λ_a}(x) − x = S(t(x+3/2−a)) + const. Use Λ_1 (or Λ∪{0}) for the Kadec discussion.
   - Numerics: Say which constant job 260 used for the symmetric sections. Finite sections of Z\{0} and of Z+½ are both orthonormal, so the numerical record cannot detect this.

2. **Remark 5.4 (and line 57) is false as stated.**
   - What: The index set n ≠ 0 leaves out λ_0. The counting deviation is −c log|x| − ½sgn(x) + const + sawtooth.
   - Why: The log term is fine: its extension −c log|x+iy| equals ũ with u = c·arg(x+iy), which is bounded. The −½sgn term is exactly the Z\{0} obstruction (the weight behaves like (1+x²)^{-1}, which is not A_2). So (iii) fails for every c, and c = 0 is literally Z\{0}.
   - Also wrong: "Every real c" fails where two points coincide (c = −1/log 2 gives λ_1 = λ_2). And v is the Poisson extension of the sawtooth, which is small for large y but not 0.
   - Fix: Use {0} ∪ {n + c log|n|}, for all c at which the points are distinct (every c except a countable set, and every |c| < 1/log 2).

3. **Beurling densities (line 199, Theorem 5.2, line 109).**
   - What: "n_Λ = x + O(log x), so lower and upper Beurling density are 1" does not follow. Beurling densities take the sup or inf over all windows, and the O(log x) is not uniform.
   - Contradiction with the paper itself: Question 6.5 says unit-window counts are conjecturally unbounded, which makes D⁺ = ∞. Unbounded normalized gaps would make D⁻ = 0.
   - Theorem 5.1 survives: n_Λ(x)/x → 1 gives D⁻ ≤ 1 ≤ D⁺, and Landau then forces |I| = 2π.
   - Theorem 5.2 does not: Its hypothesis "uniform Beurling density" is unknown for ζ, so as stated it covers neither the paper's own example nor Corollary 5.3.
   - Fix: Replace it with "(n_Λ(x) − n_Λ(0))/x → d as x → +∞".

4. **Corollary 5.3 is missing hypotheses.**
   - (a) The proof needs the variance of S_F over [T,2T] to diverge, not just its second moment. A smooth drift (θ_F off by a multiple of log t) makes the mean square diverge while staying in BMO. Fix: assume ∫_0^T S_F = o(T). Note that "O(T^{1−ε}) follows from o(T)" is false, and it is not needed.
   - (b) The Landau step needs S_F(t) = O(log t). Fix: add it as a hypothesis.
   - (c) Selberg 1992 announced the Selberg-class results without proofs. Fix: cite them as announced or conditional.

5. **Multiplicity.**
   - What: Λ is defined as a set, but Lemma 3.3 counts zeros with multiplicity. If ζ has a multiple zero, Lemma 3.3 is false for the set. The sequence version then has a repeated vector, so it is trivially not a Riesz basis.
   - Fix: Define Λ as a sequence with multiplicity. The distinct-frequency version is proved only if all but finitely many zeros are simple.
   - Question 6.3: Use inf, not liminf (a single multiple zero already breaks separation).

## MINOR

6. **Avdonin's theorem (Theorem 2.2 / Theorem 4.1).** Alemany–Nitzan state Avdonin's condition over a fixed partition into blocks [mN,(m+1)N), with no centering constant. The paper's sliding-window version is a stronger hypothesis, so showing it fails proves less than showing Avdonin's condition fails. Fix: State the partition form. In the proof, take the last full block ending at or before N(t_0); then d_n ≤ 2N − A and the argument goes through.

7. **Theorem 6.1, converse direction.** The error term is O(log(2+|I_k|+dist(0,I_k))), not O(log|I_k|). The proof drops the distance term. Fix: If |I_k| ≤ M log(2+dist) eventually, then the series is at most C_M∫log(2+|x|)/(1+x²)dx < ∞. So a long family must contain intervals with log(2+dist)/|I_k| → 0. Also make the dyadic intervals half-open so they are disjoint.

8. **Line 70.**
   - Titchmarsh §9.3 uses S(T+0) at ordinates, not the mean. Drop the attribution. (I checked this only through secondary sources.)
   - "S is strictly decreasing between ordinates" is false on (0, 6.29), where θ′ < 0.
   - Line 79: the O(log t/log log t) bound under RH is Littlewood's (1924). Goldston–Gonek gave the constant ½.

9. **Line 281 and Question 6.5.**
   - Inoue's bound μ < 0.50895 assumes RH; say so.
   - "A_N → 0 ⇔ s_N → 0": only the ⇐ direction is proved.
   - The N^{-1/3} minimal gap, and unbounded counts in a unit window, are GUE predictions. The pair-correlation conjecture alone does not give them.

10. **Numerical slips.**
    - 1 − sinc(0.1376) = 0.03086, not 0.0311 (line 328; 0.0311 is π²s²/6).
    - Proposition 6.2: equality A_N = 1 holds when all pairwise differences are nonzero integers, not only for "a section of integers".
    - x_1 = 0.94975, not 0.4497 (line 113).
    - Line 302: in the paper's convention the job 313 residual is ½ − εθ′/π. I computed 0.49999974 at n = 5. The stated −εθ′/π holds only for the old θ/π+1 unfolding.

11. **Line 188.**
    - The proof as written needs S(t_0) > N − ¼, not N + ¼. Exact averaging gives N/2 + ¼.
    - The cited S = 3.345 (positive) beats this threshold for N = 3, so "every N ≥ 3" should be N ≥ 4.
    - "Locate the Avdonin condition precisely" and "M grows like log²T" (line 306) overclaim. Corollary 4.2 is only an upper bound; the lower bound is M ≥ 2 max S − ½.
    - "First holds at M = 8": only powers of two were tested.

12. **Small proof and wording points.**
    - Corollary 4.2 omits the boundary terms θ′S₁; they are O(log² b), so this is harmless.
    - Proposition 3.2 does not need the simplicity assumption: the corrections (m+1)/2 − j sum to 0 over a multiplicity cluster.
    - Theorem 5.2 is just the contrapositive of HNP (ii) combined with John–Nirenberg.
    - "Dilating by 1/d" should be "by d".
    - Remark 5.5: sine-process realizations are almost surely not separated, so failure to be a basis follows from condition (i) or from Landau directly. The "out of BMO almost surely" claim needs an ergodic argument.

13. **Editorial.** arXiv and most journals do not accept an AI system as an author.

## Checked and correct

- Theorem 3.1: the algebra is right.
- Proposition 3.2: the jump of S²/2 at a zero of multiplicity m is mS(γ), correct.
- Theorem 4.1: block choice, multiplicity counting and inequalities are correct. The (S3) input "S unbounded above and below" is correct.
- Corollary 4.2: correct.
- Theorem 5.1 core argument:
  - The HNP statement matches Kozma–Lev Theorem 5.1 word for word, including p. 240, the counting function n_Λ(b) − n_Λ(a) = #(Λ∩[a,b)), and the 1/4. Their e^{2πiλs} on (0,1) with a = 1 corresponds to e^{iλt} on (−π,π), so the translation is right.
  - The Jacobian bounds, the variance inequality, the (S1)/(S2) error terms and the direction of John–Nirenberg are all correct.
- Proposition 6.2: interlacing, the 2×2 pair bound and the sinc inequality are correct.
- Numbers that check out: first |d_n| ≥ ¼ is at n = 9 (d_9 = 0.2708); the bound 7.9·10⁻⁴; the fitted slope −0.79.
- Citations that check out: Tsang's (h log T)^{1/3} excursions; Ghosh; Bufetov; S = 3.345 near 7.7573·10²⁷.
- Typography: no em dashes and no British spellings.

## Verdict

The main theorem is proved for Λ as a sequence with multiplicity, for every bounded interval. The only repair it needs is the one-line Beurling-density fix. However, the chosen symmetrization is modeled on Z\{0}, so the theorem should be restated for every unfolding constant and every finite modification; the proof already covers those. Remark 5.4 is false and must be corrected. Theorem 5.2 and Corollary 5.3 need their hypotheses changed before they apply to ζ or to L-functions.

---

## Disposition (authoring session, 2026-09-29 01:03 EDT, commit d8e4ce4)

Applied in full: items 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. Item 2 was applied in the form the
paper already had by the time the review landed (the index set is all of Z with log(2+|n|) and
|c| <= 1, so the points are distinct and separated); the sketch of condition (iii) was rewritten
with the log-drift harmonic extension and the O(1/y) Poisson bound the reviewer describes, and
the Lyubarskii-Seip weight reading was added. Item 13 is the owner's call and is untouched (the
build is the named sharing version, as for the settled methods paper). The reviewer's remark on
item 11 about N >= 3 was superseded by the exact threshold N/2 + 1/4, under which the recorded
excursion 3.345 defeats every N <= 6. Rebuilt at 12 pages with no warnings.
