# Referee report on the Gil note (independent hostile review)

Saved verbatim by the dispatching session (Claude Fable 5.1, 2026-09-29 ~14:30 EDT) because the
reviewing agent could not write into the repository. Reviewer: a fresh Claude Opus agent,
independent of the authoring thread's own audit files and of the OpenAI review directory
(neither was opened). NOT YET APPLIED to gil-note/main.tex at the time of saving.

- Manuscript: `reviews/claude/gil-note/main.tex`, "Global Maximal Coherence for Prescribed Intrinsic Populations: Two Open Questions of Gil Answered by a Matching Polytope" (dated September 29, 2026), with `README.md`, `verify_gil.py`, `verification-gil.json` and `verify_gil.stdout.txt`.
- Referee: Claude (Opus 5.5), independent review, 2026-09-29, about 13:45 EDT.
- Files not opened: `../REPORT.md`, `04-new-results.md`, `05-application.md`, `06-claim-audit.md`, `07-literature-comparison.md`, `00-CHECKPOINT.md`, `extension-note.tex`, anything under `reviews/openai/`; in `03-literature/`, the two summaries written by the authoring thread (`agent-literature-report.md`, `gil-key-formulas.md`).
- Sources read: Gil's paper (full text in `03-literature/`, plus the PMC HTML with its MathML); the companion `paper/antiunitary-matching/main.tex` for its hull lemma; Tam's 1998 abstract (OpenAlex); Sanyal, Sottile and Sturmfels, arXiv:0911.5436v4; Gil's Zenodo metaspin preprint (contains no global maximum).
- Numbering: equation numbers are those of the compiled PDF, (1) to (13). Line numbers refer to `main.tex`.

## Bottom line

Theorems 3.1 and 4.1 are correct and their proofs are complete. Every step was rechecked by hand and numerically, and the equality case was constructed independently. Together they answer Gil's problems (i) and (iii) as posed.

There is no BLOCKING item. Three MAJOR items must be fixed before submission, and none touches the proofs:
1. The abstract claims aligned-class extremality for every nonnegative-weight functional in a sentence that reads as covering prescribed Youla values. There it is false; an explicit counterexample is given in finding 1.
2. The manuscript asserts that Tam 1998 does not contain (9), but nobody in this chain has read Tam's full text.
3. Section 6 says the free-value maximizations attained the bound. That is false for 15 of 30 instances.

## Status by check item

| # | Check | Status | Findings |
|---|---|---|---|
| 1 | Definitions against Gil | CORRECT in substance; MINOR wording | 4, 5, 6, C1 |
| 2 | Proof of Theorem 3.1 (hull lemma, positivity, validity of the maximizer) | CORRECT; MINOR gaps | 7, 8, 9, C2 |
| 3 | Proof of Theorem 4.1 (layer cake, Ky Fan, interlacing, equality case) | CORRECT; MINOR precision | 10 to 14, C3 |
| 4 | Do the theorems answer Gil's (i) and (iii)? | CORRECT for both; MAJOR overclaim in the abstract | 1, 6, C4 |
| 5 | Bibliography and novelty | MAJOR (unchecked Tam claim); citation data otherwise accurate | 2, 16 |
| 6 | `verify_gil.py` reproduction and my own checks | Reproduces byte for byte; MAJOR misstatement in Section 6 | 3, 15, C5 |
| 7 | US English and typography (no em dashes) | CORRECT; MINOR layout | 17 |

## Findings, most severe first

### 1. MAJOR (item 4): the abstract's aligned-extremality claim is false with prescribed Youla values

Location: Abstract, lines 48 to 50 ("Consequently every pairwise coherence functional with nonnegative weights is extremized in the aligned class"), right after the prescribed-spectrum inequality. Related text: "What is not settled", lines 358 to 362.

What is wrong: the claim is true with free Youla values (Theorem 3.1, eq. (8); Corollary 5.1(1)). Read where it stands, it asserts the prescribed-spectrum version, which is false.

Counterexample: n = 4, s = (1, 0.9), weights b_12 = 2, b_13 = b_24 = 1.2, all other b_ij = 0, and c = sqrt(0.84) = 0.9165:

```
M = [[ 0.0,  0.3,   c,   0.0],
     [-0.3,  0.0,  0.0,  -c ],
     [ -c,   0.0,  0.0,  0.2],
     [ 0.0,   c,  -0.2,  0.0]]
```

- M has the prescribed spectrum: M is real skew, s_1^2 + s_2^2 = (1/2)||M||_F^2 = 1.81 and s_1 s_2 = |Pf M| = 0.06 + 0.84 = 0.9, so its singular values are (1, 1, 0.9, 0.9) and M = Q Sigma_s Q^T for an orthogonal Q (computed from the real Schur form; reconstruction error 7e-16).
- Value of M: sum b_ij M_ij^2 = 0.18 + 1.008 + 1.008 = 2.196.
- Best aligned value: 2.172, from the matching {13, 24} with s_1^2, s_2^2 in order. The matching {12, 34} gives 2.0 and {14, 23} gives 0.
- Global check: 300 Riemannian ascents over O(4) find 2.196 as the maximum, so the maximizer is not aligned.
- The LP over (13) is not tight here either: it gives 2.324.
- Random survey: over 120 instances (n = 4, 5, 6), the orbit maximum beat the aligned maximum in 1, and the (13) LP was not tight in 11 (gap up to 0.046). Rare in random data, but they exist.

Why it matters: the abstract is where a reader learns the scope. The example also shows that the product form of the weights (a_i a_j) is essential in Theorem 4.1, which is worth stating.

Fix: rewrite the sentence as "With free Youla values, every pairwise coherence functional with nonnegative weights is maximized in the aligned class", placed before the prescribed-spectrum sentence; add the example as a remark after Theorem 4.1; replace the second clause of "What is not settled" with: for general nonnegative weights with prescribed Youla values, the maximum need not be aligned and the LP over (13) is not tight (example); the value of that maximum remains open.

### 2. MAJOR (item 5): the claim about Tam 1998 has not been checked

Location: Remark 4.4, lines 323 to 325; README's "Before submission" paragraph.

What is wrong: the manuscript states as fact that [sss, Prop. 3.10] and [tam] do not contain (9). Only Tam's abstract was available to the author; the referee could not get the full text either (SIAM page behind a bot challenge, not bypassed; OpenAlex lists it as closed access with no repository copy; Tam's publication list has no PDF).

What is confirmed:
- Sanyal, Sottile and Sturmfels, Prop. 3.10 is the skew-symmetric Schur-Horn theorem (credited to Leite, Richa and Tomei): the moduli of the skew-diagonal entries are weakly majorized by the Youla values. The note describes it accurately, and it does not contain (9). The numbering is from arXiv v4, matching Mathematika 57(2):275-314.
- Tam's main theorem, per the abstract, covers the entries (i, n+i), i <= p, of U^T A U over U in U(m), characterized by weak majorization of their moduli by s plus a Thompson-Sing parity inequality when m = 2n and p = n. It constrains one fixed matching at a time while (9) couples all pairs; at n = 3 per-matching information gives only sum a_i a_j M_ij^2 <= s_1^2 (a_1 a_2 + a_1 a_3 + a_2 a_3), while the true bound is s_1^2 a_1 a_2. The applications section of Tam's paper is still unread.
- Targeted searches (skew-symmetric matrices with prescribed singular values and weighted squared entries; imaginarity or coherence with a fixed real part or fixed populations; follow-ups to Gil; Gil's Zenodo preprint) found no earlier statement of (9) or of Theorem 3.1. Closest: Chen and Fei, arXiv:2404.16279, which fixes the mixedness, not the real part.

Fix: get Tam's full text through a library. Until then write: "The skew-symmetric Schur-Horn theorem [LRT; sss, Prop. 3.10] and the main theorem of [tam] describe the entries on one fixed matching and do not imply (9); we have found no earlier statement of (9)." Cite Leite, Richa and Tomei, Linear Algebra Appl. 286 (1999) 149-173.

### 3. MAJOR (item 6): Section 6 misreports the free-value maximizations

Location: Section 6, lines 370 to 373, and check A in `verify_gil.py`.

What is wrong: Section 6 says the maximizations over the contraction ball attained (7). A replay of `verify_gil.py` with the same seed and call order (reproducing every committed number exactly) shows: check A (free values), the best of 20 Nelder-Mead runs fell short in 15 of 30 instances (every instance with n = 5, 6 or 7; worst shortfall 0.0281 at n = 7 where the bound is 0.1760, 16 percent short; only n <= 4 attained). Check B (prescribed values): all 30 attained within 2e-16. The JSON records only the maximum over instances of (best minus bound), 1.7e-16, which shows "never exceeded", not "attained".

Fix: record the minimum over instances as well; replace Nelder-Mead in check A with projected gradient ascent (within 9.3e-6 of the bound in all 15 instances in the referee's runs) or ascent on the maximal-rank skew partial isometries; or say "never exceeded it, and attained it for n <= 4".

### 4. MINOR (item 1): Gil's "cohesion" is ||N||_F, not its square
Abstract line 34; line 76 with eq. (5); Theorems 3.1 and 4.1. Gil (Sec. 2.4) writes "The cohesion of the antisymmetric block, ||N||_F"; his Theorem 3 calls ||N||_F^2 the "cohesion squared". Use "squared cohesion" throughout. Citing Gil's eq. (33) for (5) is acceptable; his eq. (20) is the more direct source.

### 5. MINOR (item 1): the aligned class is misstated
Lines 83 to 85. Gil's Definition 1 allows any admissible IRB representative, including the leftover orthogonal freedom inside degenerate eigenspaces of A; the note drops this. Nothing depends on it (the maximizers are aligned in the strict sense). Add "in some admissible IRB representative (Gil, Definition 1)".

### 6. MINOR (items 1 and 4): numbering of the problems and "affirmatively"
Lines 35 to 37 and 93 to 104. Gil does not number his three problems; (i) to (iii) are the note's labels. Problem (i) asks for a maximum to be determined, so "answer ... affirmatively" does not fit it. Reading "suitable spectral constraints" in (iii) as constraints on the Youla values is the note's interpretation, a sound one (with the spectrum of rho and the populations both fixed, tr rho^2 = sum a_i^2 + ||N||_F^2 already fixes ||N||_F, which would make the problem trivial); say so. Write "(numbered here (i) to (iii))" and "we determine the maximum asked for in (i) and answer (iii) affirmatively".

### 7. MINOR (item 2): eq. (8) and the hull claim fail when a population is zero
Theorem 3.1, lines 189 to 192, and Corollary 5.1(2). Take a = (1/2, 1/2, 0, 0), b_12 = 1, b_34 = 10: the maximum over states is 1, the maximum matching weight is 11. Corollary 5.1(2) also divides by a_i a_j. Assume positive populations, or restrict matchings and the polytope to the support of A.

### 8. MINOR (item 2): M means two things
Section 2 and eq. (8): M is both the metaspin tensor and a matching, and eq. (8) uses both. Use mu for matchings.

### 9. MINOR (item 2): the exchange argument skips two steps
Lines 176 to 185. The exchange identities are correct, but two steps are missing: completing a partial matching first (harmless, nonnegative weights), and a reason the uncrossing stops (for example, sum |i - j| strictly decreases). Add both, or cite Gil's (24) with the completion remark.

### 10. MINOR (item 3): the density-matrix reading of Theorem 4.1 needs hypotheses
Lines 211 to 214. s_1 <= 1 is needed (otherwise no state exists); with zero populations at most floor(r/2) Youla values can be positive, r the size of the support (for example a = (1/2, 1/2, 0, 0) with s = (1, 1) admits no state). State both.

### 11. MINOR (item 3): "Theorem 3.1 is the special case s = (1, ..., 1)" is imprecise
Lines 284 to 285. Eq. (7) follows from Theorem 4.1 applied to each contraction with its own s plus monotonicity of the right side in every s_k, not from setting s = 1. Eq. (8) and the hull claim do not follow from Theorem 4.1 (finding 1 shows they cannot). Rephrase.

### 12. MINOR (item 3): Remark 4.3's units and inference are off
Lines 305 to 313. Units: "up to 0.013" is in units of ||N||_F^2; in the LP's own units the excess is 0.0063. Inference: showing that the C = B family alone fails does not prove "therefore essential" (that family lacks even the degree constraints); the conclusion is nevertheless true: degree plus C = B still fails in 2 of 136 instances (n = 7, excess 2.1e-4), where the prefix inequality with C = {1,2,3}, B = [7] is violated by 0.137. Understatement: the proof shows the n(n+1)/2 prefix inequalities alone give the exact value (exact in all 136 instances). Correct the units, replace the inference with this evidence, state the prefix result.

### 13. MINOR (item 3): Corollary 5.1(3) is vague
Lines 343 to 347. Equality forces ||M_{[p],[q]}||_F^2 = R(p, q) for every p <= q with a_p > a_{p+1} and a_q > a_{q+1}, where a_{n+1} = 0. State that; either say whether it forces alignment or drop "concentrated as in the aligned adjacent configuration".

### 14. MINOR (item 3): a reason is attached to the wrong step
Line 250. "Since s is sorted decreasingly" does not justify (12), which is pure counting; the sorting is used later, in t_k <= s_k. Move the phrase.

### 15. MINOR (item 6): wording in the script and in Section 6
Line 380 says "Exact odd-set inequalities" but these are floating-point checks; the script's docstring numbers the results Theorem 1, Theorem 2 and Proposition 3 while the manuscript uses 3.1, 4.1 and 4.2; Section 6 says "over O(n)" but the script searches only SO(n) (results unaffected: flipping the sign of one coordinate preserves squared entries; say so).

### 16. MINOR (item 5): bibliography
Every entry checks out against Crossref, OpenAlex and arXiv (Gil, Edmonds, Youla, Fan, Sanyal-Sottile-Sturmfels, Tam 19(3) 737-754); the companion paper's title and lemma match. Add issue numbers and DOIs (Tam: 10.1137/S0895479896312559); Youla treats complex matrices under unitary congruence, so for the real normal form of a real skew matrix also cite Horn and Johnson, Matrix Analysis; add Leite, Richa and Tomei.

### 17. MINOR (item 7): typography
No em dashes (U+2014 and "---" both checked); en dashes used correctly; US English throughout. One overfull box (0.97 pt) at source line 181: split that display. Line 100 has a raw u-umlaut; `Pl\"ucker` would match the file's `R\'enyi` style.

### 18. MINOR (title)
"Answered by a Matching Polytope" describes only question (iii); question (i) is answered by the layer-cake and Ky Fan argument. For example "... by Matching Polytopes and a Layer-Cake Inequality".

### C1. CORRECT (item 1): definitions and quotations match Gil
The representation rho = A + iN (his eq. (3)), the metaspin tensor M (eq. (7)), rho = A^{1/2}(I + iM)A^{1/2} with the positivity statement (eq. (8)), the Youla values (eq. (9)); Gil's Theorem 2 is restated faithfully as Theorem 1.1; the two quotations from Gil's Sections 3.4 and 8.2 are verbatim; the paraphrase of problem (i) matches.

### C2. CORRECT (item 2): Lemma 2.1 and Theorem 3.1
The hull lemma holds for real and complex matrices (degree constraints from row norms; odd-set constraints because an odd-order skew block is singular; the hull equals Edmonds' polytope via the signed-swap matrices). Positivity of rho is handled exactly: for positive populations rho >= 0 exactly when ||M||_op <= 1. The maximizer rho* = A^{1/2}(I + iJ)A^{1/2}, J pairing adjacent indices with +-1, is a valid density matrix (PSD, trace 1, real part A, ||N||_F^2 = 2 sum a_{2k-1} a_{2k}); checked numerically with the intrinsic basis recomputed from scratch. The non-convexity remark is true (the mixture t 1_{12,34} + (1-t) 1_{13}, 0 < t < 1, forces s_1 > 1).

### C3. CORRECT (item 3): Theorem 4.1
The layer-cake identity (10); level sets are prefixes; 2 Psi = ||M_{C,B}||_F^2; h = R/2 with the floor and ceiling counts; Ky Fan's maximum principle; interlacing (t_k <= s_k); the three cases are exhaustive; equality at Q = I. The aligned matrix attains every prefix inequality at once; the argument covers complex skew matrices; Proposition 4.2 and Remark 4.4 are correct.

### C4. CORRECT (item 4): the theorems answer (i) and (iii) as posed
For positive populations every orientation with s_1 <= 1 is realized by some state, so Theorem 4.1 answers (i) exactly; Theorem 3.1 answers (iii) under positivity alone and Theorem 4.1 also when the Youla spectrum is prescribed; (ii) is correctly left open.

### C5. CORRECT (item 6): reproduction
The script's SHA-256 matches the JSON; a byte-identical copy run from the scratchpad with the working directory set to gil-note produced a byte-identical JSON and matching printed output (Windows line endings aside); 176 s with Python 3.12.10, numpy 2.2.6, scipy 1.16.3.

## Verdict

Theorems 3.1 and 4.1 are proved. Theorem 3.1 rests on a correct hull lemma and the exact equivalence between positivity and ||M||_op <= 1, with an explicit valid maximizer. Theorem 4.1's proof is short, complete and sharp (layer cake to prefix sets, Ky Fan, interlacing) and holds for complex matrices, odd n, and repeated or zero Youla values. Hypotheses to add: positive populations for eq. (8), the hull claim and Corollary 5.1(2); s_1 <= 1 and the support condition for the density-matrix reading of Theorem 4.1. With those stated, the note settles Gil's problem (i) and answers problem (iii) affirmatively. What is not ready is the framing: the abstract's overclaim (false for prescribed spectra with general weights), the novelty claim against Tam 1998 made without the full text, and the misreported free-value optimizations in Section 6. Fix the three MAJOR and the MINOR items; the note is then ready for author review.

## Numerical checks run (scripts in the reviewing session's scratchpad, not the repository)

1. Rerun of verify_gil.py: JSON byte-identical, printed output matching apart from line endings, 176 s.
2. Instrumented replay (same seed and call order): check A attained the bound in 15 of 30 instances (worst shortfall 0.0281 at n = 7); check B 30 of 30; the coarse LP exceeded the theorem value in 11 of 30 (up to 0.0126 in cohesion units); the full LP matched to 5.6e-17.
3. Theorem 4.1 random sampling: 16,000 orthogonal and 16,000 unitary samples, n = 2 to 9, populations including zeros and ties, spectra including repeats and zeros; largest LHS minus RHS 2.2e-16; largest ratio 1 + 1.8e-15.
4. Each proof step separately (Ky Fan, interlacing, the bound R) on every pair C subset of B at n = 4, 5, 6: 282,300 tests, largest excess 4.0e-15.
5. Layer-cake identity: 200 cases, largest error 2.8e-17.
6. Equality case at Q = I (n = 4 to 7): valid state (smallest eigenvalue >= -2.8e-17, trace 1), populations recovered to 5.6e-17, Youla values to 2.2e-16, ||N||_F^2 equal to the formula to 1.0e-17.
7. Gradient ascent on O(n): 100 instances with 30 random starts each (15 at n = 7); bound never exceeded (largest excess 2.5e-16), reached in every instance to within 3e-7.
8. Joint search over Q, a and s (n = 4, 5, 6): no positive gap.
9. Near-global search at n = 4 (SO(4) = SO(3) x SO(3)), 60 instances: largest gap 0.0, smallest gap -4.6e-8.
10. Hull lemma on complex skew contractions (n = 3 to 9): largest violation 3.6e-15.
11. Non-convexity witness: smallest achievable operator norm over all phases 1.044 to 1.151, always above 1.
12. Edmonds sanity check: LP over the polytope agrees with maximum-weight matching to 1.8e-15.
13. Theorem 3.1 on 6000 random physical states: largest excess 8.9e-16; squared entries always in the polytope.
14. Projected gradient ascent for Theorem 3.1: never exceeded the bound, within 9.3e-6 in every instance.
15. Zero-population counterexample to eq. (8): maximum over states 1, maximum matching weight 11.
16. LP subfamilies (136 instances): C = B alone fails in 33; degree plus C = B fails in 2; prefix-only and full families exact.
17. General weights with prescribed Youla values: explicit witness 2.196 against aligned 2.172 with LP bound 2.324; in a 120-instance survey the orbit maximum beat the aligned maximum once and the LP was not tight in 11.
18. Scans for em and en dashes, non-ASCII characters and British spellings, plus the LaTeX log: only the issues in finding 17.
