# Gil note: final adversarial review before the first reader

- Reviewer: Claude Opus 5.5 (Anthropic), a fresh agent launched by the outreach session. I read the
  earlier reviews and dispositions (as instructed, so as not to repeat settled items), but every
  verdict below rests on my own derivations, computations and source checks.
- Completed: Friday 2026-10-02, about 14:55 EDT.
- Baseline: `paper/gil-note/main.tex` and `main.pdf` as committed in `3ab19fe` (2026-10-02 14:15:59
  EDT). HEAD moved to `7af8e1f` (14:23 EDT) during the review; that commit touches no file under
  `paper/gil-note/`. SHA-256: `main.tex` 4c265a9a...0756, `main.pdf` 66066b90...c903. I rebuilt the
  PDF from HEAD's `main.tex` with tectonic in scratch; its extracted text is identical to the
  committed PDF's, so the PDF is current. The LaTeX log has no overfull or underfull box and no
  undefined reference.
- Read in full: `main.tex`, `main.pdf` (all nine pages; page 7 also rendered at 170 to 300 dpi to
  check the Remark 4.5 display), the companion `paper/antiunitary-matching/main.tex` and
  `main.pdf`, `self-review/REPORT.md` and `DISPOSITION.md`, `reviews/astra/` (REVIEW, DISPOSITION
  with the appended 2026-10-01 consistency-pass ledger, LAST-MESSAGE), `reviews/astra-2026-10-02/`
  (REVIEW, DISPOSITION), `paper/common/README.md`. Read for provenance: the companion's
  `reviews/RECONCILIATION.md`, `reviews/openai/REPORT.md`, `reviews/openai/lit-gil-extension.md`,
  `reviews/claude/REPORT.md` and `04-new-results.md`, and the git history of these files.
- Locations: "l." is a `main.tex` line; "p." is a page of the 9-page `main.pdf`. Page numbers of
  the companion refer to its PDF as committed in `3ab19fe`. Its source was being edited by another
  session while this review ran (uncommitted changes to its abstract, attribution and a few
  sentences); every companion passage cited below is unchanged in that working copy.
- Severity: BLOCKING (false mathematics, or a false claim that must not reach the reader); MAJOR
  (fix before sending); MINOR (exactness or polish, a phrase or one sentence each).
- Scratch files (downloads, scripts, renders) are in the session scratchpad under `agents/gil/`;
  nothing in the repository other than this file was written.

## Summary

The mathematics is right. Every numbered statement is correct, both proofs of Theorem 4.1 are
complete, and every number in Remark 4.5, including the exact-orbit certificate as corrected today,
checks in exact rational arithmetic. The verification program reproduces its JSON byte for byte.
The two items that should be fixed before the note goes to Gil are both about honesty of
provenance, which is what this set is built on:

1. **OF-9 (MAJOR).** Theorem 3.1 (the free-value answer) was found and proved independently, through
   the same hull lemma and about an hour before this note's first draft, by the companion
   manuscript's own adversarial self-review (GPT-6 Astra, committed 2026-09-28 23:53 EDT). The
   companion, which travels with the note, says two reviews found the application; the note
   credits neither the other review nor the earlier proof, and l. 166 calls the use for density
   matrices "new here".
2. **OF-4 (MAJOR).** The disclosure about Mathias 1992 is not exact. The only accessible abstract
   breaks off before its inequality, and that unread inequality concerns exactly the matrix
   `DMD = (dd^T) o M` of the second proof, in every unitarily invariant norm. The note's "we do not
   claim that their later sections contain no equivalent formulation" understates this: for
   Mathias the main theorem itself is unread, and it may contain (9) as its Frobenius-norm,
   rank-one case.

Ten MINOR items follow, each a phrase or one sentence. Recommendation: apply OF-4 and OF-9 (written
out below) and then send; apply the MINOR items in the same pass if time allows.

## A. Statements against proofs

| Statement | Location | Verdict | What I checked |
|---|---|---|---|
| Theorem 1.1 (Gil's Theorem 2, restated) | l. 99-103, p. 3 | CORRECT | Against the publisher PDF, p. 9: the value 2 sum_k a_{2k-1} a_{2k}, the adjacent pairing, and saturation only on pairs of positive population product all match Gil's statement and eq. (23). |
| Lemma 2.1 (hull lemma) | l. 142-162, p. 3 | CORRECT | Row norms give the degree inequalities; an odd-order skew principal block K_B has det K_B = (-1)^{\|B\|} det K_B = -det K_B, so rank <= \|B\| - 1, and a contraction's squared Frobenius norm is at most its rank; this holds for complex K. Converse: signed-swap blocks. Hull identity: conv(S) is in P_n because P_n is convex, and P_n = conv(1_mu) is in conv(S). Matches the companion's Lemma 2.2 (p. 3 there). The non-convexity remark (l. 167-168) is right: for x = t 1_{12,34} + (1-t) 1_{13}, row 1 has unit norm, so (KK^*)_{14} = 0, but (KK^*)_{14} = -K_13 conj(K_34) != 0 for 0 < t < 1. |
| Theorem 3.1 | l. 173-231, p. 4 | CORRECT (wording item OF-1) | Positive populations: the admissible N are exactly A^{1/2} M A^{1/2} with M a real skew contraction (rho is then Hermitian, PSD, trace one, real part A, and its IRB is the identity). Vertex optimality, completion to maximal size, the odd-n move (weight change a_w(a_v - a_n) >= 0), the two exchange identities (which are Gil's (26) and (27) verbatim), the decrease 2(k - j) of sum \|i - j\| for both crossing and nested pairs, and the claim that the only perfect matching of [2m] with no crossing or nested pair is adjacent (if 1 is matched to j > 2, the pair containing 2 nests or crosses it). The explicit blocks have eigenvalues a_{2k-1} + a_{2k} and 0. Zero populations and the a = (1/2, 1/2, 0, 0), b_12 = 1, b_34 = 10 example (state maximum 1, matching weight 11) check. |
| Theorem 4.1, layer-cake proof | l. 259-327, pp. 5-6 | CORRECT | See A.2. |
| Theorem 4.1, second proof (Horn) | l. 329-349, p. 6 | CORRECT | See A.3. |
| Text after Theorem 4.1 | l. 351-358, p. 6 | CORRECT in substance (wording item OF-2) | Recovering (7): apply (9) to each contraction and use monotonicity in every s_k. |
| Proposition 4.2 | l. 360-376, p. 6 | CORRECT (polish OF-3) | The left side of (13) is \|\|M_{C,B}\|\|_F^2 for any C in B; the bound used only \|C\| and \|B\|. R(1, q) = s_1^2 for q >= 2; R(1, 1) = 0; R(q, q) = 2 sum_{k <= floor(q/2)} s_k^2, which is Edmonds' odd-set bound at s = 1 and odd q. |
| Remark 4.3 | l. 378-393, p. 7 | CORRECT | The numbers match the JSON (Section D). "The proof uses only the n(n+1)/2 prefix inequalities" is a proof fact, not only a numerical one: the layer-cake argument applies verbatim to any x satisfying the prefix inequalities. |
| Remark 4.4 | l. 395-423, p. 7 | Mathematics CORRECT; positioning items OF-4 and OF-7 | tr(AXAX) <= tr(A^2 X^2) by Cauchy-Schwarz in the Hilbert-Schmidt inner product; von Neumann gives sum_i a_i^2 mu_i^2 with both sequences sorted; for X = iM this is sum_k s_k^2 (a_{2k-1}^2 + a_{2k}^2), a bound on \|\|N\|\|_F^2 = 2 x (left side of (9)), weaker than 2 x (right side of (9)) by AM-GM. |
| Remark 4.5 | l. 425-457, pp. 7-8 | CORRECT, every number exact | See A.1; wording items OF-3(b) and OF-6. |
| Corollary 5.1 | l. 461-492, p. 8 | CORRECT | (1) and (2) carry the support and positivity restrictions. (3): for u >= v the pair (C, B) = ([p], [q]) occurs on {u in [a_{p+1}, a_p), v in [a_{q+1}, a_q)} (a triangle when p = q), of positive measure exactly when a_p > a_{p+1} and a_q > a_{q+1}, with a_{n+1} = 0; equality of the integrals forces Psi = h almost everywhere. Necessity only is claimed, as it should be. |

### A.1 Remark 4.5 in exact arithmetic

Computed with SymPy over the rationals and Q(sqrt 21), c = sqrt(21)/5, so c^2 = 21/25 = 0.84.

| Quantity | Exact value | Note's value |
|---|---|---|
| \|\|M\|\|_F^2 | 181/50 = 3.62 | (not printed) |
| (1/2)\|\|M\|\|_F^2 = s_1^2 + s_2^2 | 181/100 = 1.81 | 1.81 |
| (1/4)\|\|M\|\|_F^2 | 181/200 = 0.905 | 0.905 |
| Pf M = M_12 M_34 - M_13 M_24 + M_14 M_23 | 3/50 + 21/25 = 9/10 | 0.9 |
| det M | 81/100 = (Pf M)^2 | |
| Characteristic polynomial of M^T M | (z - 1)^2 (z - 81/100)^2 | singular values 1, 1, 0.9, 0.9 |
| Value 2 x_12 + 1.2 x_13 + 1.2 x_24 at M | 549/250 = 2.196 | 2.196 |
| Matching {12, 34}, both orders | 2 or 81/50; best 2 | 2.0 |
| Matching {13, 24}, both orders | 543/250 = 2.172 in either order | 2.172 |
| Matching {14, 23} | 0 | 0 |
| LP point x_12 = 19/100, x_13 = x_24 = 81/100 | satisfies all 81 nested constraints C in B in [4] (no violation) | feasible |
| Its objective | 581/250 = 2.324 | 2.324 |
| R(2, 4) and R(3, 4) | 2 and 281/100 | 2 and 2.81 |
| Dual combination 0.6 [C = {1,2}] + 0.2 [C = {1,2,3}] + 0.2 [C = {1,2,4}], B = [4] | coefficients 2, 6/5, 6/5, 6/5, 6/5, 2/5 on x_12, x_13, x_14, x_23, x_24, x_34; surplus over the objective (6/5) x_14 + (6/5) x_23 + (2/5) x_34 >= 0; right side 581/250 | 2.324 |
| X = (1/2)(M_12 + M_34, M_13 - M_24, M_14 + M_23) | (1/4, sqrt(21)/5, 0), \|\|X\|\|^2 = 361/400 = 0.9025 | 0.9025 |
| Y = (1/2)(M_12 - M_34, M_13 + M_24, M_14 - M_23) | (1/20, 0, 0), \|\|Y\|\|^2 = 1/400 = 0.0025 | 0.0025 |
| \|\|X\|\|^2 + \|\|Y\|\|^2 and \|\|X\|\|^2 - \|\|Y\|\|^2 | 181/200 = 0.905 and 9/10 = Pf M | 0.905 and 0.9 |

Identities, checked symbolically for a general real 4 x 4 skew M:

- (1/4)\|\|M\|\|_F^2 = \|\|X\|\|^2 + \|\|Y\|\|^2, Pf M = \|\|X\|\|^2 - \|\|Y\|\|^2, det M = (Pf M)^2.
- The inverse map M_12 = X_1 + Y_1, M_34 = X_1 - Y_1, M_13 = X_2 + Y_2, M_24 = Y_2 - X_2,
  M_14 = X_3 + Y_3, M_23 = X_3 - Y_3 is consistent, and the objective equals
  2(X_1 + Y_1)^2 + 2.4(X_2^2 + Y_2^2), which is symmetric under X <-> Y.
- With X_2^2 = 0.9025 - X_1^2 - X_3^2 and Y_2^2 = 0.0025 - Y_1^2 - Y_3^2, the identity
  2(X_1 + Y_1)^2 + 2.4(0.9025 - X_1^2 + 0.0025 - Y_1^2) = 2.172 - 0.4(X_1 - 5Y_1)^2 + 9.6 Y_1^2
  holds exactly, and 2.172 + 9.6 x 0.0025 = 549/250 = 2.196. Dropping X_3^2 and Y_3^2 only
  increases the bound (coefficient 2.4 > 0), and Y_1^2 <= \|\|Y\|\|^2 = 0.0025.
- Equality: Y = (+-1/20, 0, 0), X_1 = 5 Y_1, X_3 = 0, X_2^2 = 0.84; the displayed M
  (X_1 = 1/4, Y_1 = 1/20) attains it.
- Orientation reversal, Q = diag(1, 1, 1, -1): Pf(Q^T M Q) = -Pf M, and the new coordinates are
  X' = (Y_1, Y_2, -Y_3), Y' = (X_1, X_2, -X_3). So the Pfaffian changes sign and X and Y exchange
  roles, exactly as l. 448-450 say; only \|Pf M\| is invariant on the O(4) orbit, and the two
  invariants force {\|\|X\|\|^2, \|\|Y\|\|^2} = {0.9025, 0.0025}.
- The rendered p. 7 sets the absolute value with larger bars than the norms; it reads correctly.

Verdict on Remark 4.5: CORRECT throughout, including today's GL-1 correction. The phrase "with
s_1^2, s_2^2 in that order" (l. 438) is harmless but misleading, since b_13 = b_24 makes the order
immaterial (OF-3(b)).

### A.2 The layer-cake proof, case by case

- Layer cake: a_i a_j = double integral of 1[a_i > u] 1[a_j > v] over [0, inf)^2; averaging with
  the swapped identity gives (10). Same for h. Both integrands are symmetric in (u, v).
- For u >= v, C = {a_i > u} = [p] is contained in B = {a_i > v} = [q] (prefixes because a is sorted).
- 1[a_i > v, a_j > u] = 1[j in C] for i < j: if a_j > u then a_i >= a_j > u >= v. Hence
  2 Psi = 2 x(E(C)) + x(C, B \ C) = \|\|M_{C,B}\|\|_F^2.
- h: 2k - 1 <= p iff k <= ceil(p/2); 2k <= q iff k <= floor(q/2); 2k <= p iff k <= floor(p/2);
  so 2h = R(p, q) as in (12).
- Ky Fan: for the rank-p coordinate projection P, tr(P X X^* P) <= sum_{k <= p} sigma_k(X)^2
  (rederived: weights <P u_k, u_k> in [0, 1] summing to p). Compression: sigma_k(M_B) <= sigma_k(M)
  (rederived: sigma_k(P M Q) <= \|\|P\|\| sigma_k(M) \|\|Q\|\|), so t_k = sigma_{2k}(M_B) <= sigma_{2k}(M) = s_k.
- p even: p/2 <= floor(q/2), both sides 2 sum_{k <= p/2}. Correct.
- p odd, p < q: q >= p + 1, so (p + 1)/2 <= floor(q/2) and sigma_p(M_B) = t_{(p+1)/2} is a genuine
  paired value; both sides 2 sum_{k <= (p-1)/2} + one term. Correct.
- p = q odd: all singular values of M_B, the last one 0; R(q, q) = 2 sum_{k <= (q-1)/2} s_k^2. Correct.
- The three cases exhaust 0 <= p <= q (p = 0 gives 0 <= 0). Equality at Q = I; the density-matrix
  blocks have determinant a_{2k-1} a_{2k}(1 - s_k^2) >= 0. Correct.

### A.3 The second proof

- T = DMD is skew-symmetric (real or complex), so its singular values pair: t_1, t_1, ..., t_m, t_m
  (+ 0), and sum_{i<j} a_i a_j \|M_ij\|^2 = (1/2)\|\|T\|\|_F^2 = sum_k t_k^2. Correct.
- Horn's inequality prod_{j <= r} sigma_j(XY) <= prod_{j <= r} sigma_j(X) sigma_j(Y): Horn's pages
  were not reachable (Section C), so I rederived it: prod_{j <= r} sigma_j(Z) = \|\|Lambda^r Z\|\|_op and
  Lambda^r(XY) = Lambda^r X Lambda^r Y.
- At r = 2l, with sigma_j(D) = sqrt(a_j) in decreasing order: prod_{k <= l} t_k^2 <=
  prod_{k <= l} s_k^2 a_{2k-1} a_{2k}. Both sequences are nonincreasing (s_k and a_{2k-1} a_{2k}
  both are). Correct.
- Weak log-majorization implies weak majorization for nonnegative vectors. Zero cases: if the right
  side has a zero at index k_0 (zeros sit at the tail), the product inequality at l = k_0 forces
  t_{k_0} = 0, so the left side vanishes from k_0 on; on the strictly positive part exp of the logs
  applies, and further zeros on the left only help. "Zeros are handled by continuity" (l. 346)
  is a fair one-line summary of this. Correct.
- Numerically (20,000 random cases, n = 2 to 8, real and complex M, zero populations included): the
  even-index product inequalities and the partial-sum inequalities never failed beyond rounding
  (largest partial-sum excess 5.3e-15).

### Findings in A

**OF-1, MINOR: "saturated Youla values" in Theorem 3.1 is too strong when a population vanishes.**
- Location: l. 180-181, p. 4.
- Claim: the maximum is "attained inside the aligned class by the adjacent pairing with saturated
  Youla values".
- Evidence: for a = (1/2, 1/2, 0, 0) the maximizer has M_12 = +-1 and M_34 = 0 (zero extension, l.
  71-74), so its Youla values are (1, 0), not saturated; s = (1, 1) admits no state (the note says
  so itself at l. 254-256). Gil's own statement, restated faithfully at l. 102, has the
  qualification "on every pair of positive population product".
- Fix: replace "with saturated Youla values." by "with $s_k=1$ on every adjacent pair of positive
  population product."

**OF-2, MINOR: "cannot follow from it" is logically loose.**
- Location: l. 357-358, p. 6.
- Claim: "Remark 4.5 shows that they cannot follow from it."
- Evidence: (8) and the hull statement are true, so in the strict sense they "follow" from
  anything. What Remark 4.5 shows is that the prescribed-spectrum analog of (8) is false (2.196 >
  2.172), so (8) cannot be obtained one Youla spectrum at a time, the way (7) is obtained.
- Fix: replace the sentence by "Remark~\ref{rem:nonproduct} shows that the prescribed-value analog
  of \eqref{eq:weights} is false, so they cannot be obtained one Youla spectrum at a time."

**OF-3, MINOR: three one-phrase precision edits in Section 4.**
- (a) l. 361, p. 6. Proposition 4.2 lists the singular values as s_1, s_1, ..., s_m, s_m, which is
  n - 1 values when n is odd; Theorem 4.1 (l. 243) adds "(and 0 if n is odd)". Fix: "Let $M$ be
  skew-symmetric with singular values $s_1,s_1,\dots,s_m,s_m$ (and $0$ if $n$ is odd), and".
- (b) l. 438, p. 7. "with $s_1^2,s_2^2$ in that order" suggests the other order differs; it does
  not (b_13 = b_24, both orders give 543/250). Fix: "in either order".
- (c) l. 301-317 and 331-347, pp. 5-6. t_k denotes the singular values of M_B in the first proof and
  of T = DMD in the second proof of the same theorem. Fix: rename the first proof's t_k to
  $\tau_k$ (l. 301, 308, 313, 315, 317).

## B. Abstract and introduction against the statements

| Claim (location) | Statement it rests on | Verdict |
|---|---|---|
| rho = A + iN with A = diag(a_1 >= ... >= a_n >= 0), N real antisymmetric (l. 20-22, p. 1) | eq. (1); Gil eq. (3) | CORRECT |
| Gil showed the aligned-class maximum is attained by adjacent pairing (l. 22-25) | Theorem 1.1; Gil Theorem 2 | CORRECT |
| Gil asked whether this remains true over all orientations with free Youla values, and the maximum over all orientations with prescribed Youla values (l. 25-27) | Gil p. 10 (the sentence after Theorem 2) and Section 8.2, problem (i); the note's Section 1 maps them the same way | CORRECT (a fair reading: Gil's p. 10 sentence states the free-value question as open rather than asking it, and the note quotes it) |
| Free values: squared entries of any real antisymmetric contraction lie in Edmonds' polytope because odd-order principal blocks are singular (l. 28-31) | Lemma 2.1 (proved for real and complex) | CORRECT |
| "positivity of rho is exactly the contraction condition on the support of the populations" (l. 31-32) | eqs. (3)-(4); Gil Section 2.3 (rows and columns on inactive axes vanish) | CORRECT; the support restriction is stated |
| With free values, every nonnegative-weight pairwise functional is maximized in the aligned class (l. 33-35) | Corollary 5.1(1), valid for every population vector (matching on the support); the abstract claims neither the value (8) nor the hull, which need positive populations | CORRECT |
| Gil's adjacent-pairing value is the global maximum (l. 35-36) | Theorem 3.1, eq. (7) | CORRECT |
| The inequality with \|M_ij\|^2, for every skew-symmetric M with singular values s_1, s_1, ..., s_m, s_m and 0 for odd n (l. 36-39) | Theorem 4.1, real and complex M, a sorted and nonnegative, no normalization, no bound on s | CORRECT; the modulus covers complex M; the odd-dimensional zero is present |
| "the sharp inequality" (l. 36) | equality at Q = I for every a and s | CORRECT |
| "a direct consequence of Horn's 1950 multiplicative inequality ..., as we show" (l. 39-40) | the second proof | CORRECT |
| "another proof, by a layer-cake decomposition combined with Ky Fan's maximum principle and interlacing" (l. 41-42) | the first proof; "interlacing" is the one-sided compression bound sigma_k(M_B) <= sigma_k(M), which is half of interlacing | CORRECT |
| The family "contains the degree and odd-set constraints as its two extreme members" (l. 43-44) | Proposition 4.2: \|C\| = 1 gives the spectral degree bound s_1^2; C = B gives the set bound, Edmonds' at s = 1 | CORRECT |
| With prescribed values and general weights the maximum need not be aligned, explicit n = 4 example (l. 45-47) | Remark 4.5, now with an exact certificate | CORRECT |
| Section 1: a_i are eigenvalues of the real part, not of rho (l. 63-66) | Gil Section 2.1 | CORRECT |
| Section 1: iM has eigenvalues +-s_k and 0 for odd n; positivity iff s_1 <= 1 (l. 78-84) | Gil Section 2.3 and eq. (8) | CORRECT (for positive populations; with zeros, on the support, as l. 71-74 set up) |
| Section 1: cohesion is \|\|N\|\|_F, its square is (5) (l. 85-89) | Gil p. 7, where the cohesion of the antisymmetric block is \|\|N\|\|_F, and the derivation before eq. (33) | CORRECT |
| Section 1: Youla normal form display (l. 93-94) | Gil eq. (9), p. 6, rendered and checked: the same block orientation [[0, s_k], [-s_k, 0]] | CORRECT |
| Section 1: aligned per Gil's Definition 1, in some admissible IRB representative (l. 95-97) | Gil Definition 1, p. 7 | CORRECT |
| Section 1: "We determine the maximum asked for in (i) (Theorem 4.1) and answer (iii) affirmatively (Theorem 3.1); (ii) is not addressed", with the stated reading of "suitable spectral constraints" and the tr rho^2 remark (l. 117-124) | Theorems 3.1 and 4.1; tr rho^2 = sum a_i^2 + \|\|N\|\|_F^2 (Gil eq. (17)) | CORRECT |

No finding in B.

## C. Sources

### C.1 Gil, Entropy 28(8):877 (2026)

Checked against the stored publisher PDF (`paper/antiunitary-matching/reviews/openai/lit-gil-2026.pdf`,
30 pages, extracted with pdftotext and the relevant displays rendered as images) and against the
HTML-derived text (`paper/antiunitary-matching/reviews/claude/03-literature/gil-2026-fulltext.txt`)
and the stored PMC HTML.

- **Quotation at l. 105-107** (the sentence after Theorem 2): verbatim in the PDF, p. 10, last
  sentence of the paragraph that follows the proof of Theorem 2; the note ends it with a comma
  inside the closing quotation marks (US punctuation), otherwise word for word. CORRECT.
- **Locator at l. 105**: in the PDF, Section 3.5 (maximum aligned cohesion for fixed populations)
  starts on p. 9, Theorem 2 is on p. 9, the quoted paragraph on p. 10. The PDF numbers the proof of
  Theorem 1 as its own Section 3.3; the PMC HTML sets that proof under an unnumbered run-in
  heading, which is why the HTML numbers the same section 3.4. The new locator is CORRECT for the PDF and for the
  PMC HTML; see OF-5 for the word "HTML".
- **Quotation at l. 107-109** (the reason Gil gives for leaving the problems open): verbatim, PDF
  p. 27, in Section 8.2 (which starts on p. 26). CORRECT. The phrase quoted at l. 119 is verbatim
  from the same paragraph. CORRECT.
- **Problems (i) to (iii)** (l. 110-115): unnumbered in Gil (introduced as one problem, another,
  and a third); (i) matches Gil's wording up to notation; (ii) fairly paraphrases Gil's problem of
  characterizing the image of the map (a, Q_M) to G(a, Q_M) under the Plucker constraints; (iii)
  says "decide" where Gil's verb is "identify". Section 8.3 (Open Questions, p. 27) lists three
  different directions; the note correctly draws its problems from 8.2 and does not cite 8.3.
  CORRECT.
- **Equation and section map**, PDF pages: (3) p. 4, the IRB form with N^T = -N (Section 2.1, p. 4,
  also the definition of a density matrix as Hermitian, PSD, trace-normalized); (7) p. 5, the
  metaspin tensor, with the zero extension on inactive axes stated in Section 2.3 (p. 5); (8) p. 5,
  rho_O = A^{1/2}(I + iM)A^{1/2} on the support; (9) p. 6, the Youla form, block [[0, s_k],
  [-s_k, 0]] as in the note; Definition 1 p. 7 (existential over IRB representatives, residual
  freedom included); (20) p. 8, \|\|N\|\|_F^2 = 2 sum_{i<j} N_ij^2 = 2 sum_k a_{i_k} a_{j_k} s_k^2 on
  the aligned class; Theorem 2 and (23)-(26) p. 9; (27) p. 10; (33) p. 11, whose preceding sentence
  and first form give (5) for every state. Every citation in the note resolves to the content it
  is cited for. Equation numbers agree between the PDF and the PMC rendering. CORRECT.
- Gil's Appendix A (pp. 27-30) treats exactly the n = 4 self-dual and anti-self-dual decomposition
  that Remark 4.5 uses; see OF-6.

### C.2 Other sources

| Source | What I reached | Verdict |
|---|---|---|
| Edmonds 1965 | NIST PDF (`jresv69Bn1-2p125_A1b.pdf`, printed pp. 125-130): inequalities (1) x >= 0, (2) degree <= 1, (3) at most r inside every set of 2r + 1 nodes, r >= 1; Theorem (P): the matching vectors are the vertices. | CORRECT. Eq. (6) adds the singleton odd sets, which read 0 <= 0; the polytope is bounded, so vertices = hull. |
| Youla 1961 | Cambridge PDF, 11 pages, printed 694-704: eq. (2) on p. 694 gives U'CU = E_1 + ... + E_k + 0 for complex skew C under unitary congruence. | CORRECT as cited ("for the complex case under unitary congruence"); the real orthogonal form is cited to Horn and Johnson, as it should be. |
| Horn 1950 | Not reached: PNAS PDF answered 403; PMC answered a proof-of-work bot challenge (not attempted); Europe PMC answered 403 and 500. Crossref confirms title, PNAS 36(7) 374-375, July 1950. | Inequality rederived (A.3); attribution of the product inequality to this paper is standard and is what the first Astra review reports from the original pages. |
| Fan 1949 | Not attempted beyond Crossref (same hosts as Horn). Crossref confirms PNAS 35(11) 652-655. | Maximum principle rederived (A.2). |
| Bhatia 1997, Ch. III; Horn-Johnson Topics Thm. 3.1.2, Cor. 3.1.3; Horn-Johnson Matrix Analysis 2nd ed. Sec. 2.5 | Not reached (no open copies). Crossref confirms Topics (1991). | Locators not verified at the theorem-number level; the facts used are rederived in A.2. |
| Sanyal-Sottile-Sturmfels | arXiv 0911.5436v4 (8 Mar 2011), whose journal reference is the cited Mathematika 57(2) 275-314 article: Proposition 3.10, p. 14, the skew-symmetric Schur-Horn theorem, credited to their reference [22]: \|SD(N)\| is weakly majorized by the Youla values; [22] is Leite-Richa-Tomei, LAA 286 (1999) 149-173. | CORRECT as described at l. 408-413. |
| Tam 1998 | Abstract (OpenAlex, complete). The sets D_p(A) are the entries (i, n + i), i <= p, of U^T A U over the unitary group; weak majorization by the s_k describes all cases except m = 2n, p = n, which adds one inequality that the abstract identifies with the Thompson-Sing theorem. Full text: SIAM, closed; not reached. | Description CORRECT except the word "parity" (OF-7). |
| Leite-Richa-Tomei 1999 | Bibliographic record (Crossref). Abstract not reached: OpenAlex has none, Semantic Scholar elides it, ScienceDirect answered 403. Attribution of the skew-symmetric Schur-Horn theorem confirmed through Sanyal-Sottile-Sturmfels' citation [22]. | Record CORRECT. |
| Mathias 1992 | Bibliographic record (Crossref: LMA 31(1-4) 57-70, June 1992). Abstract: OpenAlex holds a truncated text; Semantic Scholar elides it; Taylor and Francis answered 403; a web copy of Mathias's later Handbook of Linear Algebra chapter, which might have restated the result, answered 404. | Record CORRECT; disclosure not exact (OF-4). |

Bibliographic data of all twelve external entries (Gil, Edmonds, Youla, Fan, Horn, Bhatia, both
Horn-Johnson books, Leite-Richa-Tomei, Mathias, Sanyal-Sottile-Sturmfels, Tam) match Crossref or
the publisher record (titles, volumes, issues, pages, years, DOIs). The companion entry is in
Section E.

### Findings in C

**OF-4, MAJOR: the disclosure about Mathias 1992 is not exact, and his unread theorem may contain (9).**
- Location: l. 405-419, p. 7 (Remark 4.4); the README's "Open literature item" repeats it.
- Claim: "We have found no earlier statement of the population formula (9) itself in print"; Mathias
  "treats the singular values of the Hadamard product of a positive semidefinite matrix and a
  skew-symmetric one, which is exactly the matrix DMD = (dd^T) o M ... and is the closest subject
  we know of"; "Tam, Leite-Richa-Tomei and Mathias were available to us only through their
  abstracts ..., so we do not claim that their later sections contain no equivalent formulation."
- Evidence: the only abstract on record (OpenAlex) defines the ordered singular values and the
  ordered main diagonal entries of a matrix, takes B complex skew-symmetric and any unitarily
  invariant norm, and then stops in mid-statement right after introducing an arbitrary real
  positive semidefinite n x n matrix A; no inequality follows. Semantic Scholar marks the abstract
  as elided by the publisher; the publisher page answered 403. So the result of the paper, not
  merely its later sections, is unread. Its setting contains the note's matrix exactly: A = dd^T is real positive semidefinite
  with diagonal a, and A o M = DMD. The natural sharp statement in that setting is the paired
  bound sigma(A o B) weakly majorized by (sqrt(alpha_1 alpha_2) sigma_1(B), sqrt(alpha_1 alpha_2)
  sigma_2(B), sqrt(alpha_3 alpha_4) sigma_3(B), ...), whose Frobenius-norm case at A = dd^T is
  exactly 2 x (9). As a heuristic only (not evidence of what Mathias proved), that general paired
  bound held in 4,000 random cases at each n = 3 to 7 (real PSD A of every rank, complex skew B).
  The note already concedes that (9) is "not new in substance"; the defect is that the one paper
  most likely to state it is described as merely "the closest subject", with a disclosure that
  says less than the truth about what was read.
- Severity: MAJOR. This is the one remaining priority-flavored sentence about (9), and an
  abstracts-only disclosure protects the note only if it says exactly what was and was not read.
- Fix (smallest): in l. 405-407 replace "We have found no earlier statement of the population
  formula \eqref{eq:prescribed} itself in print, and the nearest results we know are these." by
  "We have not found the population formula \eqref{eq:prescribed} itself stated in print, but one
  of the nearest results below could not be read." Replace l. 413-419 from "Mathias~\cite{mathias}"
  through "equivalent formulation." by:

  > Mathias~\cite{mathias} studies the singular values of the Hadamard product of a real positive
  > semidefinite matrix and a complex skew-symmetric one, in every unitarily invariant norm and in
  > terms of the ordered diagonal entries of the positive semidefinite factor; with that factor
  > equal to $dd^T$, $d_i=\sqrt{a_i}$, the product is exactly the matrix $DMD=(dd^T)\circ M$ of the
  > second proof. The abstract available to us breaks off before Mathias's inequality, so we cannot
  > say whether \eqref{eq:prescribed} is a special case of his theorem, and we claim no priority for
  > it. Tam and Leite--Richa--Tomei were available to us only through their abstracts
  > (Sanyal--Sottile--Sturmfels in full), and we do not claim that their papers contain no
  > equivalent formulation.

  Before any release beyond Gil, obtain Mathias's paper (library or interlibrary loan); if it
  contains (9), cite it as the first statement and say so in Remark 4.4 and the README.

**OF-5, MINOR: "the HTML rendering" should name which HTML.**
- Location: l. 105, p. 3.
- Claim: "(p. 10 of the publisher's PDF, where the section is numbered 3.5; the HTML rendering
  numbers it 3.4)".
- Evidence: the stored HTML and the full-text extraction are the PubMed Central rendering
  (PMC13512070), where "Proof of Theorem 1" is unnumbered; the publisher's own HTML (mdpi.com)
  answered 403 and was not checked, and it may follow the PDF's numbering.
- Fix: "the PubMed Central HTML rendering numbers it 3.4".

**OF-6, MINOR: Remark 4.5's X and Y are Gil's own Appendix A coordinates; say so.**
- Location: l. 444-451, p. 7.
- Claim: X and Y are introduced without attribution and the norms {0.9025, 0.0025} are derived
  from the two invariants.
- Evidence: Gil's Appendix A (PDF pp. 27-29) decomposes 2-forms on R^4 into self-dual and
  anti-self-dual parts with the basis (A1), parametrizes one Youla plane by unit vectors v_+, v_-
  through (A3) and (A4), writes M = s_1 pi^(1) + s_2 pi^(2) (A5) and introduces A_+ = s_1 + s_2,
  A_- = s_1 - s_2 (A6). Substituting (A3)-(A5) into the note's definitions gives, identically
  (checked symbolically), X = (A_+/2) v_+ and Y = (A_-/2) v_-. So on one orientation class
  \|\|X\|\| = (s_1 + s_2)/2 = 0.95 and \|\|Y\|\| = (s_1 - s_2)/2 = 0.05, and the exact-orbit
  certificate is a maximization over (v_+, v_-) in S^2 x S^2 in Gil's own variables. For this
  reader the connection is the most useful sentence the remark could carry.
- Fix: after the definition of Y (l. 446) insert "(in the notation of Gil's Appendix~A,
  $X=\tfrac12A_+\hat v_+$ and $Y=\tfrac12A_-\hat v_-$ with $A_\pm=s_1\pm s_2$ on one orientation
  class \cite[eqs.~(A3)--(A6)]{gil})".

**OF-7, MINOR: Tam's extra inequality is not a parity condition.**
- Location: l. 412, p. 7.
- Claim: "(with a parity inequality in Tam's case)".
- Evidence: Tam's abstract identifies the additional inequality (present only when m = 2n and
  p = n) with the inequalities of the Thompson-Sing theorem on diagonal entries and singular
  values. For complex matrices that inequality (sum of the first n - 1 moduli minus the last is at
  most the same combination of singular values) is not a parity condition; parity conditions
  belong to the real case.
- Fix: replace "(with a parity inequality in Tam's case)" by "(with one further inequality, of
  Thompson--Sing type, in Tam's even-dimensional full-matching case)".

## D. The numerical checks of Section 6

- **Reproduction.** I ran an unmodified copy of `verify_gil.py` (SHA-256 2f476e76...1b57, equal to
  the JSON's `source_sha256`) from the scratchpad with Python 3.12.10, NumPy 2.2.6, SciPy 1.16.3
  (the recorded versions). It took 4 min 2 s. The JSON it wrote is byte-identical to the committed
  `verification-gil.json`, and its stdout equals `verify_gil.stdout.txt` up to line endings.
- **Per-dimension record** (an instrumented copy with the same random-number call order; every
  recorded number identical): check A's worst shortfall 7.18e-5 is at n = 7 (as Section 6 says);
  the other n = 7 instances fall short by 2.8e-6 to 8.0e-6; worst at n = 6 is 4.1e-5, at n = 5
  2.9e-5, at n = 4 1.9e-7; n = 2 and 3 reach the bound. Within 1e-6: 5 + 5 + 5 + 3 + 1 + 0 = 19
  instances; within 1e-4: all 30. Check B: every instance at or above its value (smallest
  1.1e-18), largest excess 1.5e-13 (n = 2).
- **Section 6 against the JSON, sentence by sentence.**

| Section 6 / Remark 4.3 statement | JSON | Verdict |
|---|---|---|
| A: 2 <= n <= 7, five population vectors per n, 30 instances, 300 random contractions each | instances 30; random_samples_per_instance 300; code: n in 2..7, 5 per n; operator norms in [1/1.2, 1] | CORRECT |
| A: PGA, 20 starts, 4000 steps, clipping, final snap | method string and code | CORRECT |
| A: largest excess 5.6e-16 | max_optimized_excess 5.551e-16 | CORRECT |
| A: within 1e-6 in 19, within 1e-4 in all 30, worst shortfall 7.2e-5 at n = 7 | 19; 30; 7.1787e-5; n = 7 from the instrumented run | CORRECT |
| B: five spectra per n including s = 1 | code: trial 0 uses s = 1 | CORRECT |
| B: "300 random orientations Q in O(n)" | code: Q = expm(S) with S skew, so Q in SO(n), not Haar | see OF-8 |
| B: largest excess 1.5e-13; within 1e-6 in all 30 | 1.5005e-13; 30 | CORRECT |
| C: full and prefix LPs agree to 5.6e-17 | 5.551e-17 both | CORRECT |
| Remark 4.3: C = B alone exceeds by up to 0.0097 (0.019 in \|\|N\|\|_F^2 units) | 0.019409 in \|\|N\|\|_F^2 units; half is 0.0097 | CORRECT |
| Remark 4.3: C = B plus degree still exceeds in 4 of 30, up to 2.2e-4 (4.4e-4) | 4; 4.4196e-4 | CORRECT |
| D: 3 <= n <= 8, 8760 checks, largest excess -0.032 | 8760 = 40 samples x (1 + 4 + 11 + 26 + 57 + 120) odd sets; -0.03216 | CORRECT |

- **Independent checks** (my own code, no function of the manuscript's script):
  Theorem 4.1 on 7,680 orbit samples, n = 2 to 7, real and complex orientations, populations
  generic, tied, zero-tailed and rank one, Youla spectra random, all ones, zero-tailed (with s up to
  2 for the algebraic statement) and repeated, plus 192 Riemannian ascents: largest excess
  6.2e-15, best ratio to the bound 1 + 1.4e-14. Proposition 4.2 on every nested pair C in B, n <= 6,
  1,235,200 checks: largest excess 8.9e-15.

**OF-8, MINOR: Section 6 says O(n) for orientations drawn in SO(n).**
- Location: l. 518, p. 8.
- Claim: "$300$ random orientations $Q\in\Orth(n)$".
- Evidence: `verify_gil.py` l. 164 draws Q = expm(1.5 x random skew), which lies in SO(n) and is not
  Haar-distributed; the parenthetical about the sign flip is attached only to the Nelder-Mead
  searches. The result is unaffected (a coordinate sign flip preserves squared entries).
- Fix: "$300$ random orientations and $20$ Nelder--Mead maximizations, both over
  $\mathrm{SO}(n)$ through the exponential parametrization (a coordinate sign flip preserves squared
  entries, so this covers $\Orth(n)$);".

## E. The attribution block and the house rules

Checked against `paper/common/README.md` (pattern items 1 to 5) and the sibling blocks.

| Item | Verdict |
|---|---|
| 1. Writer and director, with the division of labor (l. 51, p. 1) | Present in the house words. See OF-9 and OF-10 for what the model did not do alone. |
| 2. Where the questions came from | Gil's paper, found while reviewing the companion: true of this model, but incomplete (OF-9). The note does not say what Hypnos is or that the harness contributed no step of this note's mathematics (OF-12). |
| 3. Reviews by model and vendor, verdict in one clause each | Self-review (Claude Opus 5.5, 2026-09-29; "proofs complete and three framing defects" matches `self-review/REPORT.md`: no BLOCKING, three MAJOR framing items). First Astra review ("no blocking defect and two major items", Horn as the second proof, Corollary 5.1(1)'s support restriction) matches `reviews/astra/REVIEW.md` items 1 and 2 and its verdict. The 2026-10-02 review by GPT-6 Astra ("found both theorems and the hull lemma correct, one major item ... and one minor item ..., both applied the same day") matches `reviews/astra-2026-10-02/REVIEW.md` section F (0 / 1 / 1) and the disposition. "Two reviews were applied in full" matches both dispositions. The 2026-10-01 consistency pass, which edited six sentences including the abstract, is not named (OF-11). |
| 4. "No human mathematician has reviewed this paper." | Present verbatim. CORRECT. |
| 5. Place in the set | "the last of the three, after Astra's antiunitary paper and the Riesz-basis paper ...; it was written without reading the latter": consistent with the antiunitary block ("the earliest of the three") and the unfolded-zeros block ("before the note on Gil's questions"), and with the package timestamps (23:30, 00:24, 00:50 EDT). No paper is called the first. CORRECT. |
| Companion bibliography entry (l. 568-570) | "GPT-6 Astra, at the direction of D. Ross, Approximate antiunitary symmetry as a matching problem, manuscript (September 2026), Hypnos Math, URL": the set's form; title, model, director, month (the companion is dated September 28, 2026) correct. CORRECT. |
| Em dash | `main.tex` has 0 U+2014, 0 `---`, 0 non-ASCII bytes; its 18 `--` are en dashes in ranges and joined names (Cauchy--Schwarz, Schur--Horn, page ranges). CORRECT. |
| US English | No British form found (scans for -our, -ise/-isation, -yse, -tre, -ogue, doubled -ll-). CORRECT. |
| Clay (A)/(B) statement | None; no Clay, Millennium, Riemann or Navier-Stokes claim. CORRECT. |
| Nothing beyond the theorems | Every claim maps to Lemma 2.1, Theorems 3.1 and 4.1, Proposition 4.2, Remark 4.5 or Corollary 5.1, except "its use for density matrices is new here" (l. 166), which the companion contradicts in substance (OF-9), and the Mathias sentence (OF-4). |

### Findings in E

**OF-9, MAJOR: the free-value theorem was found and proved first, independently, by the companion's self-review, and the note does not say so.**
- Location: l. 51 (attribution, p. 1), l. 164-166 (p. 3); `README.md` "Provenance" repeats it.
- Claim: "The model found the two questions of Gil while reviewing the companion manuscript ...,
  proved the theorems"; and, of the hull lemma, "its use for density matrices is new here."
- Evidence:
  - `paper/antiunitary-matching/reviews/openai/lit-gil-extension.md`, committed in `5268029` at
    2026-09-28 23:53:07 EDT (author "DRoss (Codex)"; this is the companion's "adversarial
    self-review by a fresh Codex thread of the same model", GPT-6 Astra, per the companion's
    attribution), states and proves "Theorem G1: unrestricted coherence maximum", that is
    max over A + iN >= 0 of \|\|N\|\|_F^2 = 2 sum_k a_{2k-1} a_{2k} with the adjacent optimizer, which
    is eq. (7) of Theorem 3.1, "through the original manuscript's matching lemma", and says it
    "answers the free-amplitude arbitrary-orientation question stated after Gil's Theorem 2".
  - The Claude review's first answers to Gil's questions (Theorems C and G of
    `reviews/claude/04-new-results.md`) were committed in `9da9004` at 2026-09-29 00:28:25 EDT;
    this note's first draft in `081c2f9` at 00:50:30 EDT.
  - `reviews/RECONCILIATION.md`: "The two reviews were produced independently and neither reviewer
    read the other".
  - The companion, which is attached to the same email, says in its Section 1 (p. 2): "this
    application, found independently by two reviews of the present manuscript, is developed
    separately", and in Section 5.3 that both reviews found Gil's paper.
  - So "proved the theorems" is true of this model but not exclusive, Theorem 3.1 was proved first
    elsewhere in the same project, and "new here" is true only relative to print. A reader who has
    both papers sees two reviews credited in one and one model credited in the other.
- Severity: MAJOR (provenance in a set whose stated purpose is an honest division of labor, going
  to the author whose question it answers).
- Fix (smallest):
  1. In l. 51, after "takes responsibility for the manuscript." insert: "The answer to the
     free-value question (Theorem~\ref{thm:free}, eq.~\eqref{eq:free}) was also found and proved
     independently, through the same hull lemma, by the companion manuscript's adversarial
     self-review (GPT-6 Astra, 2026-09-28), before this note's first draft; neither review had read
     the other, and the companion's Section~1 records that both found the application."
  2. In l. 166 replace "its use for density matrices is new here." by "its application to density
     matrices was found independently by both reviews of that manuscript (its Section~1 says so)
     and is developed here."
  3. Optional, verified here: the same review (its "Theorem G2") also proves that every feasible
     spectrum is majorized by the adjacent saturated state's spectrum q, which implies (7) through
     tr rho^2 and bears on Gil's spectral-sharpening results. I rechecked its proof (top-k
     eigenvectors, the real span W of their real and imaginary parts, P <= Q_W, tr(Q_W N) = 0,
     rank Q_W <= min(2k, n)); it is correct. One sentence in Section 1 or after Theorem 3.1 could
     mention it, credited the same way.

**OF-10, MINOR: Remark 4.5's example and its exact certificates came from the reviews.**
- Location: l. 51, p. 1; Remark 4.5, l. 425-457, p. 7.
- Claim: the model "proved the theorems, wrote the verification program and the text"; the review
  clauses name the defects found, not the mathematics supplied.
- Evidence: the n = 4 counterexample (weights 2, 1.2, 1.2; M with 0.3, c, -c, 0.2) is the
  self-review's finding 1 (`self-review/REPORT.md`); the LP dual certificate, the X, Y orbit
  certificate and the choice a = (0.4, 0.3, 0.2, 0.1) are the first Astra review's item 10
  (`reviews/astra/REVIEW.md`), as its disposition records.
- Fix: in the self-review clause, "(an overclaimed abstract, refuted by the $n=4$ example it
  supplied, now Remark~\ref{rem:nonproduct}, an unread source ...)"; at the end of the first Astra
  clause, "...needed its support restriction; it also supplied the exact certificates of
  Remark~\ref{rem:nonproduct}."

**OF-11, MINOR: the 2026-10-01 consistency pass is not named.**
- Location: l. 51, p. 2.
- Claim: the block names three reviews.
- Evidence: the ledger appended to `reviews/astra/DISPOSITION.md` records a pass by a fresh Claude
  Opus 5.5 agent that applied six edits to this text (the abstract's statement of Gil's questions,
  \|M_ij\|^2 in the abstract, "another proof", the eigenvalue 0 for odd n, "second proof" in this
  block, the companion entry). `paper/common/PACKAGE-README-2026-10-02.md` tells the outside reader
  that each paper received such a pass; the paper itself does not.
- Fix: after the third-review sentence insert "A consistency pass on 2026-10-01 by a fresh Claude
  Opus 5.5 agent (Anthropic), not a review of the proofs, checked the abstract, the introduction,
  the quotations and this block against their sources and made six edits, none to a proof." The
  sibling blocks omit their passes too; the same sentence pattern fits them.

**OF-12, MINOR: "the Hypnos record" is undefined in this note, and the harness's role is indirect.**
- Location: l. 51 (last sentence), p. 2.
- Claim: "It is one of three manuscripts written from the Hypnos record on the night of
  2026-09-28/29".
- Evidence: the note never says what Hypnos is (its siblings each have a provenance section; this
  one has none). Its questions come from Gil's paper and its mathematics from this model and the
  reviews; the hull lemma was developed in the companion's session, and the companion's Section 5.2
  (p. 8) says the harness records were motivation, not premises.
- Fix: "It is one of three manuscripts that came from the record of Hypnos, the research harness
  described in the companion's Section~5.2, on the night of 2026-09-28/29, this one at one remove
  (the harness contributed no step of its mathematics); it is the last of the three, ..."

### The attribution after this review

House item 3 requires this review to be named once its findings are applied. Suggested clause,
after the third-review sentence (and after OF-11's sentence if applied): "A further review on
2026-10-02 by Claude Opus 5.5 (Anthropic), fresh to the paper, found every numbered statement
correct and every number in Remark~\ref{rem:nonproduct} exact, two major items (the independent
earlier proof of Theorem~\ref{thm:free} in the companion's self-review, which this note did not
credit; the disclosure about Mathias's abstract, which breaks off before its inequality) and ten
minor ones, applied the same day."

## F. Verdict

**BLOCKING: 0.** No false mathematics; nothing false is asserted about Gil's paper.

**MAJOR: 2.**
- OF-9: Theorem 3.1 was proved first, independently, by the companion's self-review (GPT-6 Astra,
  23:53 EDT 2026-09-28); credit it in the attribution and fix "new here" at l. 166.
- OF-4: Mathias's only accessible abstract breaks off before its inequality, whose setting
  contains DMD exactly; make the disclosure exact and claim no priority for (9).

**MINOR: 10.**
- OF-1: Theorem 3.1's "saturated Youla values" needs "on every adjacent pair of positive population
  product".
- OF-2: "cannot follow from it" becomes "cannot be obtained one Youla spectrum at a time".
- OF-3: Proposition 4.2's odd-n zero; "in either order" in Remark 4.5; tau_k for M_B's singular values.
- OF-5: "the PubMed Central HTML rendering".
- OF-6: identify X and Y with Gil's Appendix A coordinates (A_+/2) v_+ and (A_-/2) v_-.
- OF-7: Tam's extra inequality is of Thompson-Sing type, not a parity condition.
- OF-8: Section 6's random orientations are in SO(n), not O(n).
- OF-10: credit Remark 4.5's example (self-review) and certificates (first Astra review).
- OF-11: name the 2026-10-01 consistency pass.
- OF-12: say what Hypnos is and that its role in this note is indirect.

**Should the note go to Gil as it stands?** No, but it is two short edits away. The smallest set of
edits is OF-9 (one sentence in the attribution, one clause at l. 166) and OF-4 (one sentence at
l. 405-407, one paragraph at l. 413-419), all written out above, plus the clause naming this review,
then a rebuild and a check that the PDF still builds without warnings. The MINOR items are each a
phrase or one sentence and can go in the same pass; none is a reason to delay.

**Confirmations** (checked and found correct):
1. All six numbered statements (Theorem 1.1, Lemma 2.1, Theorems 3.1 and 4.1, Proposition 4.2,
   Corollary 5.1) and Remarks 4.3 to 4.5; both proofs of Theorem 4.1, including every parity case
   and the zero cases.
2. Remark 4.5 in exact arithmetic: singular values 1, 1, 0.9, 0.9; value 549/250; aligned values
   2, 543/250, 0; LP point feasible in all 81 nested constraints with objective 581/250; the dual
   combination; \|\|X\|\|^2 = 361/400, \|\|Y\|\|^2 = 1/400, their sum 0.905 = (1/4)\|\|M\|\|_F^2, their
   difference 9/10 = Pf M; the objective in X, Y; the completion of the square; the maximum 2.196
   and its equality case; the sign change of the Pfaffian and the exchange of X and Y under a
   reflection. Today's GL-1 correction is right.
3. Every Gil quotation verbatim; the new locator (p. 10, Section 3.5 in the PDF, 3.4 in the PMC
   HTML) right; equations (3), (7), (8), (9), (20), (23)-(27), (33), Definition 1, Theorem 2,
   Sections 2.1, 2.3 and 8.2 resolve as cited; 8.3 is correctly not used.
4. Edmonds' polytope and Theorem (P); Youla's complex normal form; Sanyal-Sottile-Sturmfels
   Proposition 3.10 on p. 14 of the version carrying the cited journal reference; Tam's abstract as
   paraphrased (apart from OF-7); the bibliographic data of every entry.
5. Horn's product inequality, Ky Fan's maximum principle and the compression bound rederived; the
   log-majorization step and its zero cases.
6. `verify_gil.py` reproduces `verification-gil.json` byte for byte; Section 6 and Remark 4.3 quote
   it correctly, including "at n = 7" and 19 of 30.
7. Abstract and introduction: free versus prescribed values, support restrictions, \|M_ij\|^2,
   the odd-dimensional zero, "another proof", "direct consequence of Horn", the n = 4 claim.
8. Attribution: writer, director, three reviews with verdict clauses that match their reports, the
   house sentence, the place in the set; the companion entry's authorship form; no em dash, no
   non-ASCII byte, US English, no Clay statement; the committed PDF matches the committed source.

**Outside the manuscript** (not counted above; relevant if these files travel with the note):
- `paper/common/PACKAGE-README-2026-10-02.md` l. 27: "the papers were written without reading one
  another" is false for this note, which grew out of the review of the antiunitary paper and reuses
  its lemma (its own attribution says so). Suggested: "...and, apart from the Gil note, which grew
  out of the review of the antiunitary paper, the papers were written without reading one another."
- Same file, "Verification": "the Gil note's ... checks run in seconds" is false; `verify_gil.py`
  ran in 4 min 2 s here (176 s in the self-review's run). Suggested: "the Gil note's checks run in
  about three to four minutes".
- `paper/gil-note/README.md`: the "Provenance" paragraph needs the OF-9 credit and the "Open
  literature item" the OF-4 wording.
- `docs/outreach/2026-10-02/emails.md`, Gil email: consistent with the note (it says the note claims
  only the application and the polyhedral viewpoint, which omits the nested-set family; an
  understatement, harmless).
