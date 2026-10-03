# Final review before sending: "Approximate Antiunitary Symmetry as a Matching Problem"

Reviewer: Claude Opus 5.5 (Anthropic), a fresh agent launched by the outreach session for the last
review before the paper goes to Jose Jorge Gil as the second attachment of the Gil-note email.
Friday 2026-10-02, begun about 14:17 EDT, completed 14:47 EDT (America/New_York).

Baseline: commit `3ab19fe` (2026-10-02 14:15:59 EDT). `main.tex` SHA-256 `93a94030c2baf16a7385c09e246da087d9639c394032e83b1d21b34f4c2db039`;
`main.pdf` SHA-256 `19dfa8817b53c9cf4b40082a43a21b2840c95f5d357bc1a161bf945f8681e14c`, 10 pages.
Locations: "line" is a `main.tex` line at this commit; "p." is a page of this `main.pdf`.

What was done: `main.tex` read in full; all ten pages of `main.pdf` rendered to images and read
(overbars, the figure, the table, the line breaks); every proof reconstructed by hand; an
independent numerical battery written from the statements (not from `verify.py`) and run; both
verification programs rerun under the pinned versions and compared field by field with the
committed JSON; Looi, Edmonds, Loring, Higham and Kramers fetched; Crossref records for Edmonds,
Wigner, Mirsky, Gil and Loring; Gil read from the stored PDF; the provenance snapshot read for
the five nodes of Section 5.2. Earlier reviews and ledgers were read as instructed (this review
is not blinded); items they settled are cited, not repeated, and every finding below is new.

Receipts (downloads, scripts, outputs): [a working directory of the reviewing session, withheld from the public copy]
(file list and hashes in C.8 and D).

Quotation policy: sources are quoted verbatim only where they are public domain (Edmonds 1965, a
US government work; Kramers 1930) or CC BY (Gil 2026); Looi is paraphrased with exact locators,
with one short quotation. Quotations of `main.tex` are byte-exact.

## Summary

- Every numbered statement is CORRECT as stated, with the conjugate where it must be. No proof
  has a gap that affects a statement.
- Findings: 0 BLOCKING, 0 MAJOR, 12 MINOR. Seven are recommended before sending (F1 to F7: the
  abstract's index set, the commuting hypothesis in Section 1's contribution sentence, a stale
  "independently peer reviewed", two inexact sentences in the related-work paragraph, the
  published version of Loring, and the attribution's disposition sentence). Five are optional
  (O1 to O5).
- The verification record reproduces under the pinned versions: every count, every pass, the
  96/120 and 80/120 optimizer figures, and the gradient-check number identical; four
  roundoff-level maxima differ in the last digits (platform).
- Recommendation: apply F1 to F7 (text only, no statement or proof changes), rebuild, send. If
  a rebuild is not possible this afternoon, the paper as it stands contains no mathematical
  error and can go.

## A. Statements against proofs

### A.1 Verdict per statement

| Statement | Lines, page | Verdict | Independent reason; boundary cases |
|---|---|---|---|
| Theorem 2.1 and decomposition (7) | 131-143 p. 3; proof 191-217 p. 4 | CORRECT | `S=(U+U^T)/2`, `K=(U-U^T)/2` are Frobenius-orthogonal (symmetric against skew), so `||S||^2+||K||^2=n`; `K` is an average of two unitaries, hence a contraction. `U^T conj(U)=(U^*U)^T=I` gives `U conj(U)+I=(U+U^T)conj(U)`, so `||U conj(U)+I||^2=4||S||^2`. Per pair, `U_ij=S_ij+K_ij`, `U_ji=S_ij-K_ij` give `|U_ij|^2+|U_ji|^2=2|S_ij|^2+2|K_ij|^2`. With `||S||^2=n-2 sum_{i<j} x_ij` (`K_ii=0`): `E=4 tau n+2 sum_{i<j}(c_ij-4 tau)x_ij+2 sum_{i<j}c_ij|S_ij|^2`, the factors 2 and 4 exactly as printed. The discarded term is nonnegative because `c_ij>=0`; that is the only use of the sign hypothesis (`tau>=0` is not used in this proof, so the identity also holds for `tau<0`, as Astra noted). Lemma 2.2 puts `x` in `P_n`; an affine function on a polytope attains its minimum at a vertex `1_M`, with value `4 tau n+2 sum_M(c_ij-4 tau)=2 sum_M c_ij+4 tau(n-2|M|)`. The signed-swap witness has `S` = identity on unmatched vertices and 0 on pairs, `x=1_M`, last term 0, `U conj(U)+I` equal to 2 on unmatched diagonal entries: the lower bound is attained. |
| Lemma 2.2 | 161-184 p. 3 | CORRECT | Row sums: `sum_j |K_ij|^2=(KK^*)_ii<=1`. Odd principal block: `det K_A=det K_A^T=det(-K_A)=-det K_A` over the complex field (no reality or normality used), so `rank K_A<=|A|-1`; compression keeps singular values `<=1`, so `||K_A||_F^2<=rank K_A`, and `||K_A||_F^2=2 sum_{E(A)}|K_ij|^2`. Converse by signed-swap partial isometries. The sentence after the proof (the hull, not the image, is `P_n`) is correct and needed (the four-vertex non-realizable point in `reviews/openai/REPORT.md` section 5). |
| Corollary 3.1 | 229-249 p. 4 | CORRECT | `V^T conj(V)=conj(V^*V)=I` and `conj(H_r)=conj(V) D_r V^T` (real `D_r`) give both displayed identities; `U -> V^* U conj(V)` is a bijection of `U(n)`, so `W` ranges over `U(n)`. `c_ij=sum_r(lambda_i^(r)-lambda_j^(r))^2` is symmetric, zero on the diagonal, nonnegative. Joint multiplicity is retained. The remark after it (matched joint eigenvectors exchanged with opposite signs, unmatched coordinates conjugated) is right for the stated optimizer: `T v_i=-v_j`, `T v_j=v_i`, `T v_k=v_k`. |
| Proposition 3.2 | 256-294 pp. 4-5 | CORRECT | Uniqueness makes the minimizing face of `P_n` the single vertex `1_{M*}`; at a minimizer both nonnegative excesses in (7) vanish. Matched pair: `|K_ij|=1` and `2|S_ij|^2+2<=2` force `S_ij=0`, unit entries, and zero elsewhere in rows and columns `i,j`, so the block is `K_ij [[0,1],[-1,0]]`, a unit scalar times the signed swap. Unmatched pair: `c_ij>4 tau>=0` by uniqueness (this is where `tau>=0` is used), so `S_ij=0`, and `K_ij=0` since `x_ij=0`. Conversely every phase-decorated matrix attains the minimum. Quantitative part: in a convex decomposition the non-optimal weight is at most `epsilon/Delta`, and `|M sym-diff M*|<=|M|+|M*|<=n`; the second estimate needs only `c_min>0` (`2 sum_{i<j} c_ij|S_ij|^2>=c_min||S-diag S||_F^2`). `n>=2` makes `Delta` meaningful. The tie remark (`n=3`, `c=0`, `tau=1`) checks: the 90-degree rotation about `(1,1,1)/sqrt 3` has energy 4, the minimum, and is not a signed swap. |
| Corollary 3.3 | 304-331 p. 5 | CORRECT | (10) is Theorem 2.1 with `c=0`, `tau=1`. (11): `ker K` is nonzero in odd dimension, `Kv=0` gives `Sv=Uv`, so `||S||_op>=1`, and `<=1` as an average of unitaries; (6) gives `||U conj(U)+I||_op=2||S conj(U)||_op=2` for every `U`. (12): exact commutation makes `W=V^*U conj(V)` commute with every `D_r`, hence block diagonal on joint eigenspaces; blocks are independent. Wording nit O3. The two sentences after it (minimum 1 for `||(U+U^T)/2||_F`, minimum 2 for `||U conj(U)+I||_F`; `2 sin(pi/(2n))` is the determinant-only floor, which is what node 2698 derived) check. |
| Corollary 3.4 | 340-357 p. 5 | CORRECT | `U conj(U)=-I` iff `conj(U)=-U^*` iff `U^T=-U`; then `S=0`, the objective is linear in `x`, every degree constraint is tight (unit rows, zero diagonal), so every matching in a convex decomposition is perfect; any signs of `c` are allowed (and even the zero-diagonal hypothesis is unnecessary, since `U_ii=0`). Even `n` is needed for feasibility. |
| Proposition 3.5 | 361-384 p. 6 | CORRECT | Stacked residuals with `sqrt(tau)` on the square term; the square residual cancels in the difference; `||XU-U conj(X)||_F<=2||X||_F`; reverse triangle inequality pointwise, then minima in both directions. Commutativity is used only to evaluate `Phi_tau(A)` by (8); the positive part in the lower bound is present. |
| Section 4.1: (15), dual (16), envelope | 390-424 p. 6 | CORRECT | (15) is (3) rewritten with `b_ij=8 tau-2c_ij`. (16) and `B` are Edmonds' (5)-(7) with `r=(|A|-1)/2`; weak duality uses only `x>=0`, so negative benefits are harmless; strong duality (existence of exact certificates) follows from Edmonds' theorem and LP duality, and rational data give rational dual vertices. Three-vertex certificate: `z_123=8>=b=8` on each edge, `B=8`, energy `>=12-8=4`. Envelope: slopes `4(n-2|M|)>=0`, so continuous, nondecreasing, concave, piecewise affine; for `tau1<tau2` with optimal `M1`, `M2`, adding the two optimality inequalities gives `(tau2-tau1)(|M1|-|M2|)<=0`, so cardinality cannot decrease. |
| Proposition 4.1 and (17), (18) | 428-460 p. 7 | CORRECT | Exchange identities: `(c-a)^2+(d-b)^2-(b-a)^2-(d-c)^2=2(c-b)(d-a)>=0` and `(d-a)^2+(c-b)^2-(b-a)^2-(d-c)^2=2(d-b)(c-a)>=0`; cardinality is preserved; after deletions the remaining indices stay contiguous, so adjacency is not distorted; repeated values only create ties; exchanges preserve perfectness, and the only perfect adjacent matching is `{1,2},{3,4},...`. `F_0=0`, `F_1=4 tau`, `O(n)` after sorting. Nit O5. |
| Example (19) and Figure 1 | 462-478 pp. 7-8 | CORRECT | Recomputed in exact rationals over all matchings of `(0,2,3,5)`: best cost by cardinality 0, 2 (pair 2-3), 16 (pairs 0-2 and 3-5); the crossing and nested perfect matchings cost 36 and 52. `Phi_tau=min{16 tau, 2+8 tau, 16}`; `16 tau=2+8 tau` at `tau=1/4`, `2+8 tau=16` at `tau=7/4`; at `1/4` the empty matching ties with {2,3}, at `7/4` {2,3} ties with {0,2},{3,5}. The figure on p. 8 shows exactly these three lines, the envelope and both breakpoints; legend and caption match. |

### A.2 The conjugate in the commutation error, and sigma_y

The antiunitary `T=UC` commutes with `H` iff `HUC=UCH=U conj(H) C`, that is iff
`HU=U conj(H)`. The conjugate is load-bearing:

- Without it the theorem is false for complex tuples. For `H=sigma_y`, `U=sigma_y` gives
  `||sigma_y sigma_y-sigma_y sigma_y||^2+tau||sigma_y conj(sigma_y)+I||^2=0+tau||-I+I||^2=0` for
  every `tau` (computed: 0.0 at `tau=0.5, 1, 2`), while the formula gives `min(8 tau, 8)>0`.
- With it, `U=sigma_y` (the standard spin time reversal up to a phase, under which `sigma_y` is
  odd) gives commutation error `2I` and square residual 0, objective 8 (computed: 8.000000000000002).
- Haar sampling, 400,000 unitaries of `U(2)` per value (script `mychecks.py`, section 1):

| tau | formula `min(8 tau, 8)` | Haar sample minimum | samples below formula | BFGS, 30 starts | constructed optimizer `V W V^T` |
|---|---|---|---|---|---|
| 0.5 | 4 | 4.000002409717973 | 0 | 3.999999999999998 | 3.9999999999999982 (empty matching) |
| 1 | 8 | 8.000000000001757 | 0 | 7.999999999999988 | 7.9999999999999964 (tie) |
| 2 | 8 | 8.006093583057794 | 0 | 7.999999999999996 | 7.9999999999999964 (the pair) |

- Every occurrence of the commutation error in `main.tex` carries the conjugate: lines 23
  (abstract), 48, 56 (eq. (1)), 243, 318 (eq. (12)), 381. On the page images the overbar is
  visible on p. 1 (abstract, zoomed at 4x), p. 2 (paragraph 1 and eq. (1)), p. 4, p. 5 and p. 6.
  Text extraction drops it, so any machine summary of the paper must be checked against the PDF.

### A.3 Boundary cases

- `tau=0`: value `min_M 2 sum_M c=0` (empty matching), attained by `W=I`, that is `U=V V^T`
  in physical coordinates: the eigenbasis conjugation of Section 5.3, square `+I`. Proposition
  3.2 at `tau=0`: uniqueness holds iff all `c_ij>0`, and its proof's `c_ij>4 tau` is then `c_ij>0`.
- `n=1`: both sides of (3) equal `4 tau` (`U=e^{i theta}`, `U conj(U)=1`); Lemma 2.2 is vacuous;
  the quantitative part of Proposition 3.2 is excluded by `n>=2`; (11) holds; `F_1=4 tau`.
- Repeated joint eigenvalue vectors: zero-cost edges, matched at zero cost when `tau>0`; ties
  allowed; (12) counts odd multiplicities. My battery deliberately repeated joint vectors.
- Odd `n`: at least one unmatched vertex; with `c=0`, value `4 tau`; (11) for every `U`.
- Complex tuples: complex `V` throughout Corollary 3.1, complex Haar unitaries in Theorem 2.1;
  nothing assumes reality. The real orthogonal optimizer is a conclusion, not an assumption.

### A.4 Independent numerical battery (`mychecks.py`, seed 20261002; output `mychecks.json`)

| Check | Result |
|---|---|
| Corollary 3.1 on 144 random complex commuting tuples (`n=1..6`, `d=1..3`, repeated joint vectors, `tau` in {0, 0.3, 1, 2.5}): witness, 2,000 Haar samples each, BFGS for `n<=4` | witness error `<=2.1e-14`; min(Haar minus formula) `-8.9e-15`; min(BFGS minus formula) `-5.3e-15`; covariance identities to `1e-10` |
| Decomposition (7), complex Haar `U`, `n=1..9`, 450 cases | max error `4.3e-14` |
| Lemma 2.2, 360 complex skew contractions (from Haar `U`; random complex skew scaled to operator norm exactly 1; saturated `Q J Q^T`), every odd subset, `n<=9` | max constraint excess `1.8e-15` |
| (11) on 1,000 odd-dimensional Haar `U`; BFGS minima of `||U conj(U)+I||^2` for `n=1..5`; (12) with multiplicities (1,2,3) | error `1.3e-15`; minima 4, 0, 4, 0, 4; block minima 4, 0, 4, total 8 = `4 #odd` |
| Corollary 3.4, 18,000 skew unitaries, signed costs | min(value minus formula) `-2.0e-14` |
| Proposition 3.2, 360 near-optimal `U` with a unique optimum | `max(||x-1_M||_1 - n eps/Delta)=-1.2e-7`; `max(||S-diag S||^2 - eps/c_min)=-1.0e-9`; phase-decorated optimizers exact to `7.1e-15` |
| Proposition 3.5, 32 noncommuting cases | `max(|sqrt Phi(H)-sqrt p|-2 eta)=-0.47` |
| Proposition 4.1, 1,800 cells in exact rationals (DP, brute force, best adjacent matching; even-`n` hard value) | 0 mismatches |
| Matching LP duality over all odd sets, 60 random instances | dual optimum minus maximum benefit: 0.0 |
| Cardinality monotonicity, 120 instances by 41 values of `tau` | 0 violations |

### A.5 Optional nits in proofs

**O3, MINOR (optional): Corollary 3.3, proof of (12).** Lines 328-330, p. 5. Claim:
"Finally, exact simultaneous commutation makes $U$ block diagonal on the joint eigenspaces in a
joint eigenbasis." Evidence: under the paper's own congruence (Corollary 3.1, and the warning at
line 251 that similarity is the wrong rule), the matrix that is block diagonal is
`W=V^* U conj(V)`, not `V^* U V`; the sentence is right only if "in a joint eigenbasis" is read
with the antiunitary transformation rule. Fix: replace the sentence with
"Finally, under the congruence of Corollary~\ref{cor:tuple}, exact simultaneous commutation
makes $W=V^*U\overline V$ block diagonal on the joint eigenspaces, and
$\|U\overline U+I\|_\F=\|W\overline W+I\|_\F$."

**O5, MINOR (optional): Proposition 4.1, proof.** Line 446, p. 7. Claim: "If it is unmatched,
delete it and continue. Otherwise suppose it is paired with $j>2$." Evidence: the case "paired
with 2" is not stated (it is the trivial case). Fix: insert before "Otherwise": "If it is paired
with $2$, delete $1,2$ and continue."

## B. Abstract and introduction against the statements

### B.1 Case by case

| Claim (location) | Against | Verdict |
|---|---|---|
| Commuting tuple; "we determine exactly the least combined error" (abstract, lines 20-21, p. 1) | Corollary 3.1 | CORRECT |
| "$\tau\ge0$" (line 22, added today) | (1), Theorem 2.1 | CORRECT; applied as AN-1 asked |
| "$\lambda_i\in\mathbb R^d$ are the joint eigenvalue vectors" (line 22) | Corollary 3.1, "repeated with joint multiplicity" | Index set and multiplicity unstated: F1 |
| The formula: factor 2, `4 tau`, `n-2|M|`, all matchings, Euclidean norm (lines 23-27) | (8) | CORRECT |
| "An optimizer consists of signed swaps on matched pairs and scalar phases on unmatched states" (lines 28-29) | Theorem 2.1 (phase 1), Proposition 3.2 (all phases); every phase is optimal even without uniqueness | CORRECT (existential) |
| Hull and parity obstruction (lines 29-32) | Lemma 2.2, Remark 2.3 | CORRECT |
| "generic optimizer rigidity, stability estimates, exact dual certificates, and a linear-time recurrence" (lines 32-34) | Prop. 3.2 (uniqueness fails only on finitely many hyperplanes in `(c, tau)`), (9), (14), Section 4.1, Prop. 4.1 | CORRECT |
| "Classical odd-dimensional defect bounds and Kramers pairing appear as boundary cases" (lines 34-35) | Corollaries 3.3, 3.4 | CORRECT |
| "certified alternative to continuous symmetry searches" (lines 35-36) | Sections 4.1, 5.1, 5.3 | Within what is proved; settled 2026-09-29 (Claude #33) |
| Section 1, paragraphs 1-3 (lines 45-71, p. 2) | Kramers; (1); nodes 2649, 2676, 2677 | CORRECT |
| Single-observable case classical, hard or soft, via Wigner, Kramers, Mirsky (lines 81-85) | `reviews/claude/04-new-results.md` Proposition D(a), re-derived here: with `H~=(H+THT^{-1})/2`, `||H-THT^{-1}||^2=4||H-H~||^2`; `H~` has even multiplicities on the `-1` eigenspace of `T^2` (Kramers) and on each `E_theta+E_{-theta}`; Mirsky gives at least `P` consecutive pairs at cost `2(lambda_j-lambda_i)^2` each; the penalty is at least `4 tau m_+=4 tau(n-2P)` | CORRECT |
| "Our contribution is the exact reduction of (1) ... to matching"; "hence tuples of two or more observables" (lines 77-79, 86-87) | Corollary 3.1 needs commuting; Section 5.3 | Commuting hypothesis missing: F2 |
| Gil paragraph (lines 88-93) | Gil Theorem 2 (Section 3.5, pp. 9-10), p. 10, Section 8.2 p. 27 (C.5) | CORRECT; wording O4 |
| Looi paragraph (lines 95-118, pp. 2-3) | Looi pp. 1-6 (C.1) | CORRECT; fairness O1 |
| Section 5.1 numbers and table (lines 484-529, pp. 7-8) | `verification.json`, `verification-exact.json`, my rerun (D) | CORRECT (nit O2) |
| "it has not been formalized in a proof assistant or independently peer reviewed" (line 533, p. 8) | Section 5.3 line 585-586, attribution line 40 | Inconsistent: F3 |
| Section 5.2, provenance (lines 537-554, pp. 8-9) | `hypnos-provenance.json`: `captured_utc` 2026-09-29T03:20:40Z = 23:20 EDT on 9/28; node 2649 (f = 2.0 at n = 3, 5, unsquared Frobenius), 2676 ("whether they are comparable up to constants on U(n) is open"), 2677 (eigenbasis construction, machine-level residuals), 2698 (floor `2 sin(pi/(2n))`, `delta(3)>=1`), 2707 (symmetrization residual exactly 1 at n = 3, 5) | CORRECT |
| Section 5.3, limits (lines 558-575, p. 9) | Corollary 3.1; Proposition 3.5; Proposition 4.1 | CORRECT; the RH sentence is a disclaimer only |
| Section 5.3, source-access sentence (lines 577-582, changed today) | `LITERATURE.md`; the reviews' access records; KNAW | Inexact: F4 |
| Section 5.3, "older work on congruence orbits ... which contains the single-observable ingredients" (lines 590-592) | `reviews/openai/literature.md`, `reviews/claude/07-literature-comparison.md` | Unsupported: F5 |
| Section 5.3, Looi sentence (lines 592-595) | `LITERATURE.md` addendum; RECONCILIATION addendum | CORRECT |

### B.2 Findings

**F1, MINOR (recommended): the abstract does not say which `lambda_i` it matches.**
Location: line 22, p. 1. Claim: "If $\lambda_i\in\mathbb R^d$ are the joint eigenvalue vectors and
$\tau\ge0$, the minimum of [...] equals the minimum, over all matchings $M$, of
$2\sum_{\{i,j\}\in M}\|\lambda_i-\lambda_j\|^2+4\tau(n-2|M|)$." Evidence: the formula is true only
when `i` runs over `1..n` with joint multiplicity, as Corollary 3.1 states ("repeated with joint
multiplicity", lines 231-232); read with the distinct joint eigenvalue vectors it is false. Example:
`H=0` in dimension 2 has one distinct joint eigenvalue, the formula then gives `8 tau`, and the true
value is 0 (take `U` skew unitary). The abstract is the statement most readers check; AN-1 was the
same kind of repair. Fix (line 22):
`If $\lambda_1,\ldots,\lambda_n\in\mathbb R^d$ are the joint eigenvalue vectors, repeated with multiplicity, and $\tau\ge0$, the minimum of`

**F2, MINOR (recommended): Section 1 states the contribution without the commuting hypothesis.**
Location: lines 77-79 and 86-87, p. 2. Claims: "Our contribution is the exact reduction of
\eqref{eq:physical}, including its soft square penalty, to matching, together with the resulting
certificates and stability statements." and "The substantive content of Theorem~\ref{thm:main} is
the general cost array, hence tuples of two or more observables". Evidence: (1) is defined for every
Hermitian tuple (line 53), and Section 1 never states the commuting hypothesis before the Looi
paragraph; the exact reduction holds for commuting tuples only (Corollary 3.1; Section 5.3, line 558,
"The exact spectral formula requires a finite commuting Hermitian tuple"). For a noncommuting tuple
(1) is not a matching value of spectra: the Pauli triple `(sigma_x, sigma_y, sigma_z)` has
`Phi_tau=8 min{3, tau+1}` (`reviews/openai/REPORT.md` section 4; my multistart, 40 starts: 8, 12,
16, 24 at `tau=0, 0.5, 1, 3`), while the commuting triple `(sigma_z, sigma_z, sigma_z)`, with the
same separate spectra, has its matching value `min(8 tau, 24)`: 0, 4, 8, 24. The 2026-10-01
consistency pass inserted "commuting" in the Looi paragraph for this reason (RECONCILIATION item
17); the contribution sentence, in the preceding paragraph, was not changed. Fix: line 78, after
`\eqref{eq:physical}` insert ` for commuting tuples`; line 86, `hence tuples of two` becomes
`hence commuting tuples of two`.

**F3, MINOR (recommended): Section 5.1 says the theorem has not been "independently peer
reviewed", one page before Section 5.3 reports "Two independent reviews".**
Location: line 533, p. 8. Claim: "it has not been formalized in a proof assistant or independently
peer reviewed." Evidence: the sentence is the first version's (commit `9820d1e`); since then the
attribution (line 40, p. 1) reports a cross-vendor review and a fresh review, and Section 5.3 (lines
585-586, p. 9) reads "Two independent reviews of the manuscript, conducted after this search". The
intended meaning, no human review, is the house sentence. Fix (line 533):
`formalized in a proof assistant or reviewed by a human mathematician.`
(The paper's `README.md`, lines 5-6, carries the same stale sentence, "There is no independent referee
report or proof-assistant certificate"; it is not the paper and is not sent.)

**F4, MINOR (recommended): the source-access sentence changed today is inexact on two counts.**
Location: lines 577-582, p. 9. Claim: "The related-work search examined the accessible primary texts
and the bibliographic records of the sources cited below (the full texts of Wigner, Kramers and
Mirsky were not obtained, and the reviews record which originals they reached)". Evidence:
(a) "the related-work search" is the search made when the manuscript was written: the next sentences
call it "this search" and date the reviews after it. Its record, `LITERATURE.md` section "Primary
sources examined", lists four sources: Edmonds, Loring and Higham at full text and Wigner at
bibliographic level. Kramers, Mirsky and Gil entered the bibliography from the reviews on 2026-09-29
(commit `af7f1b2`), Looi on 2026-10-01 (commit `00782dd`); so that search did not examine four of
the eight "sources cited below". (b) Kramers 1930 is openly accessible: the KNAW digital library
serves it without login or challenge (https://dwc.knaw.nl/DL/publications/PU00015981.pdf, 14 pages,
printed pp. 959-972), and this review obtained it (C.6). Pairing "examined the accessible primary
texts" with "Kramers ... not obtained" implies an access barrier that does not exist, and after
this review "not obtained" is no longer true of the record. For Wigner and Mirsky the statement
stands (C.6). Fix, two edits in the paragraph:
lines 577-580 become
```
The related-work search made when the manuscript was written examined
the primary texts of Edmonds, Loring and Higham and the bibliographic
record of Wigner, and
```
and after the paragraph's last sentence ("...and nothing stating the identity.", line 595) add
```
Kramers and Mirsky were cited after the reviews. The full texts of
Wigner and Mirsky were not obtained by the search or by any review;
that of Kramers was obtained in the fourth review; the reviews record
which originals they reached.
```
("The fourth review" assumes F7's wording, which names this review as the fourth; without F7, write
"in the review by Claude Opus 5.5 of 2026-10-02".)
Optional with this fix: add `\url{https://dwc.knaw.nl/DL/publications/PU00015981.pdf}.` to the
`kramers` entry (line 629).

**F5, MINOR (recommended): Section 5.3 attributes to the congruence-orbit literature content the
reviews do not report.**
Location: lines 590-592, p. 9. Claim: "both found [...] older work on congruence orbits with
prescribed singular values, which contains the single-observable ingredients but not the weighted
identity." Evidence: both reviews found that literature (Tam 1998, SIAM J. Matrix Anal. Appl.
19:737-754, and relatives), but neither says it contains the single-observable ingredients. The
OpenAI review: it is "relevant to any extension from a contraction ball to one fixed singular-value
orbit" and characterizes "selected unsquared entries" of one orbit (`reviews/openai/literature.md`
lines 9, 24, 48). The Claude review: "all of these are linear (Cartan-projection) statements about
ONE entry per 2x2 block", relevant to prescribed singular values (`reviews/claude/07-literature-comparison.md`
lines 51-65). The single-observable ingredients, in the paper's own Section 1 (lines 81-85) and in the
Claude review's Proposition D(a), are Wigner's normal form, Kramers' theorem and Mirsky's inequality.
The clause entered with reconciliation edit 6 (`reviews/RECONCILIATION.md` lines 47-49), which cites no
review sentence for it. Fix (lines 590-592): replace "which contains the single-observable
ingredients but not the weighted identity." with
```
which concerns selected entries of a single orbit rather than the
squared-entry hull or the weighted identity.
```

## C. Sources

### C.1 Looi, arXiv 2609.37133 (fetched in full, 41 pages)

Receipts: `looi.pdf` (SHA-256 `3e025aed...1148d`), `looi-abs.html`. The arXiv record: "Stability of
isometries of quantum states", Sam Looi, v1 Tue 29 Sep 2026 09:36:14 UTC (05:36 EDT); the PDF's page 1
carries the date line August 29, 2026.

| Paper's claim (lines 95-118, pp. 2-3) | Looi | Verdict |
|---|---|---|
| Posted September 29, 2026, after this manuscript was written on September 28 | arXiv v1 05:36 EDT 9/29; this manuscript committed `9820d1e` 2026-09-28 23:30:47 EDT | CORRECT (see O1) |
| Hyers-Ulam stability on the state side | abstract, p. 1; the stability problem, p. 4 | CORRECT |
| Surjective map of the positive trace-class cone preserving Bures or trace distance up to additive `epsilon` | Definition (1.3), p. 4: `|d(S(A),S(B))-d(A,B)|<=epsilon`; Theorems 1.2, 1.3 assume surjectivity | CORRECT |
| "with no linearity or continuity assumed" | p. 4: "no linearity, affinity or continuity assumptions whatsoever on the approximate isometries are assumed" | CORRECT |
| Uniformly within `2 sqrt 2 epsilon` (Bures) | Theorem 1.2, (1.4), p. 5, every `A` in the cone, zero not assumed fixed | CORRECT |
| `9 epsilon/2` (trace), `3 epsilon` when zero is fixed | Theorem 1.3, (1.6) and the sentence after it, p. 5; also Corollary 1.4, (1.8), under delta-surjectivity | CORRECT |
| Of some conjugation `A -> UAU^*`, `U` unitary or antiunitary | Theorems 1.2, 1.3; "Wigner symmetry" defined p. 3 | CORRECT |
| Constants independent of the dimension | p. 4 (cone results) and abstract | CORRECT |
| On the state space no modulus uniform in the dimension | Theorem 1.5, (1.9)-(1.10), p. 5 (infinite dimension); Corollary 1.6, p. 6 (each fixed dimension); p. 4 | CORRECT |
| Quantitative form of the Molnar-Timmermann classification of bijective isometries as Wigner symmetries | Theorem 1.1, p. 3; "We study quantitative versions of Theorem 1.1", p. 4 | CORRECT |
| No observable, commutation error or square relation enters Looi's theorems | statements of Theorems 1.1-1.5 and Corollaries 1.4, 1.6 read; term counts in the full text: `observ` 2, `commut` 5, `Kramers` 0, `matching` 0, `Wigner` 5 (pp. 1, 3 only) | CORRECT |

Judgment. The description is accurate: every constant, quantifier and hypothesis matches. It is fair:
no priority is claimed either way and the two questions are kept apart. The distinction is right:
Looi's unknown is a map on states, his hypothesis is metric, and his conclusion is one approximating
Wigner symmetry; this paper's data are a fixed commuting tuple of observables, its quantity is the
least algebraic residual over all antiunitaries, and its answer is an exact matching value. Neither
result implies the other. "What the two share is Wigner's theorem behind the unitary-or-antiunitary
dichotomy" (lines 116-117) is interpretive and acceptable: Looi's conclusion is the dichotomy; this
paper works on the antiunitary half.

**O1, MINOR (optional, fairness): Looi's own date.** Location: lines 95-96, p. 2 (also the
attribution, line 40, p. 1). Claim: "A paper posted to arXiv on September 29, 2026, after this
manuscript was written on September 28". Evidence: true as written, and carefully "posted"; but the
first page of Looi's PDF is dated August 29, 2026, a month before this manuscript was written, and a
reader comparing a writing date with a posting date may infer an order of the work that the record
does not support. Fix (lines 95-96):
`A paper posted to arXiv on September 29, 2026 (its first page is dated August 29, 2026), after this manuscript was written on September 28, is adjacent and should be distinguished.`

### C.2 Edmonds 1965 (fetched, NIST PDF, 6 pages)

Receipt: `edmonds.pdf` (SHA-256 `6617f7d5...09c0`). Printed pp. 125-130, "Vol. 69B, Nos. 1 and 2,
January-June 1965"; Crossref (DOI 10.6028/jres.069B.013) agrees: title, author, volume 69B, issue
"1 and 2", first page 125, 1965. Page 125: the abstract promises the polyhedron whose extreme points
are the matchings and "an efficient algorithm" for maximum weight-sum matching (supports Section 4.1's
"solvable in polynomial time by Edmonds' algorithm"). Page 126: constraints (1) `x>=0`, (2) degree
at most 1, (3) "for every subset S of 2r+1 nodes in G where r is a strictly positive integer",
then "THEOREM (P): P is the set of vertices (extreme points) of polyhedron C." Since C is bounded,
C is the convex hull of the matching vectors: exactly (4) of the paper (whose singleton odd sets are
redundant, as the paper says). Section 3 on p. 126 gives the dual: (5) `U=sum y+sum r z`, (6)
`y, z>=0`, (7) `y_1+y_2+sum z>=c` per edge, and `W<=U`: exactly (16) and `B`. Entry and use: CORRECT.

### C.3 Loring, arXiv 2508.13004 (fetched)

Receipt: `loring.pdf` (SHA-256 `21e44916...8543`), v2 of 20 Aug 2025 (v1 18 Aug 2025). Page 1: title
and author as cited; the abstract presents Wigner's method as constructive with two algorithms, so "a
recent constructive treatment" (line 74) is accurate.

**F6, MINOR (recommended): the bibliography cites only the preprint of a published paper.**
Location: lines 611-615, p. 9. Claim: "T.~A.~Loring. Transforming antiunitary symmetries to a normal
form. arXiv:2508.13004, 2025." Evidence: Crossref record 10.1016/j.exmath.2025.125737: same title,
author Terry A. Loring, Expositiones Mathematicae 44(2), article 125737, issued April 2026 (DOI
registered 2025-11-20), five months before this manuscript; the Claude review's agent saw a
ScienceDirect listing (pii S0723086925000921) but did not verify the journal. Only the arXiv text has
been read by any pass. Fix (lines 611-615):
```
\bibitem{loring}
T.~A.~Loring.
Transforming antiunitary symmetries to a normal form.
\emph{Expositiones Mathematicae}, 44(2):125737, 2026.
\href{https://doi.org/10.1016/j.exmath.2025.125737}{doi:10.1016/j.exmath.2025.125737}.
Cited from arXiv:2508.13004v2, \url{https://arxiv.org/abs/2508.13004}.
```

### C.4 Higham 1989 (fetched, author's reprint, 23 PDF pages)

Receipt: `higham.pdf` (SHA-256 `181ac821...7818`). The footnote on PDF p. 1 gives Gover and Barnett,
editors, Applications of Matrix Theory, pages 1-27, Oxford University Press, 1989: identical to the
entry. The survey supports "Matrix nearness is a classical optimization framework". CORRECT.

### C.5 Gil 2026 (stored PDF `reviews/openai/lit-gil-2026.pdf`, SHA-256 `57160b4b...a87e`, 30 pages)

Crossref (10.3390/e28080877): Entropy 28(8), 877, published 2026-08-04, Jose J. Gil, title as cited.
Section 3.5, p. 9, "Maximum Aligned Cohesion for Fixed Populations": Theorem 2 gives the maximum of
`||N||_F^2` over the aligned class, `2 sum a_{2k-1} a_{2k}`, with populations fixed and both the
aligned pairing and the Youla values free. Page 10 (CC BY 4.0): "Whether the same maximum is globally
optimal over arbitrary Youla orientations is a separate optimization problem and is not assumed here."
Section 8.2, p. 27, lists that question among three open problems. So "Gil maximizes the coherence of
a density matrix with prescribed populations over a restricted class of antisymmetric parts, and the
hull lemma removes that restriction" (lines 89-91) is accurate (Gil himself calls it "the
fixed-population coherence problem restricted to aligned supports", p. 10), and the hull lemma does
remove the restriction in Theorem 2's free-Youla-value setting (with positive populations,
`A+iN>=0` iff the metaspin tensor is a real skew contraction; zero populations force zero rows of
`N`, as the Gil note handles). "Found independently by two reviews" checks against both reports. The
section numbering differs between the PDF (3.5) and the HTML (3.4); the paper cites no section.

**O4, MINOR (optional, consistency with the companion note in the same email): Gil's term.**
Location: line 90, p. 2, and lines 588-589, p. 9. Claim: "prescribed populations". Evidence: Gil's
populations are intrinsic populations, the eigenvalues of `Re rho` in his intrinsic reference basis
(abstract and Section 3.5); the Gil note's title is "Global Maximal Coherence for Prescribed Intrinsic
Populations". Fix: "prescribed populations" becomes "prescribed intrinsic populations" at both places.

### C.6 Wigner 1960, Kramers 1930, Mirsky 1960

| Entry | Bibliographic record | Full text | Verdict on the entry |
|---|---|---|---|
| Wigner, Normal form of antiunitary operators, J. Math. Phys. 1(5):409-413, 1960, doi 10.1063/1.1703672 | Crossref: title, Eugene P. Wigner, volume 1, issue 5, pages 409-413, issued 1960-09-01 | Not reached: the DOI resolves to pubs.aip.org, which returns HTTP 403 with a human-verification page ("Just a moment..."); not pursued | CORRECT |
| Kramers, Theorie generale de la rotation paramagnetique dans les cristaux, Proc. ... 33:959-972, 1930 | Leiden Lorentz Institute list of Kramers' publications: Proceedings Koninklijke Akademie van Wetenschappen 33: 959-972 (1930); the KNAW scan: "Communicated at the meeting of November 29, 1930", pages numbered 960-972 after an unnumbered first page | Obtained: KNAW digital library PU00015981.pdf, 14 pages, `kramers1930.pdf` (SHA-256 `ce2f5c50...fa59a`). Section 2 (p. 962) proves the general theorem; p. 965 states it: "les états stationnaires d'un système atomique sont toujours dégénérés quand le système contient un nombre impair d'électrons, le degré de dégénération étant un nombre pair." The argument is the conjugation-with-spin-reversal relation `a* a = (-1)^n` (p. 965), the `T^2=-1` mechanism | CORRECT; the venue name is the modern English rendering (in 1930: Koninklijke Akademie van Wetenschappen te Amsterdam), acceptable |
| Mirsky, Symmetric gauge functions and unitarily invariant norms, Q. J. Math. 11(1):50-59, 1960, doi 10.1093/qmath/11.1.50 | Crossref: title, L. Mirsky, volume 11, issue 1, pages 50-59, 1960 | Not reached: academic.oup.com returns HTTP 403 with a human-verification page; not pursued. The Mirsky PDF in `reviews/openai/literature.md` is a different paper ("Maximum Principles in Matrix Theory") | CORRECT |

Is "the full texts of Wigner, Kramers and Mirsky were not obtained" exact? For the record before
this review, yes: `LITERATURE.md` item 3 (Wigner, "this is not recorded as a full-text inspection");
`reviews/openai/literature.md` line 66 (Wigner not available); the Claude review's agent report
(Wigner at abstract level; Kramers only through Wikipedia's citation); Astra's review C (Wigner and
Kramers not reached, Mirsky publisher record only). After this review it is exact for Wigner and
Mirsky only, and Kramers was never behind a barrier: F4.

### C.7 Other searches; the missing literature file

`reviews/astra-2026-10-02/DISPOSITION.md` refers the unistochastic question to
`docs/outreach/2026-10-02/LITERATURE-2026-10-02.md`; that file is not in the repository at `3ab19fe`.
This review is not a priority search, but three targeted web searches were run (squared entries of a
skew-symmetric contraction with "matching polytope"; Majorana covariance matrices of fermionic
Gaussian states, which are real skew contractions, with odd-subset inequalities; skew-symmetric
orthogonal squared entries with "perfect matching polytope"). None found a statement of Lemma 2.2. The
nearest hit, S. Friedland, arXiv 1102.2542 (haffnians), restates the perfect-matching odd-set
inequalities in matrix form and contains no skew-symmetric squared-entry statement (`skew` does not
occur in its text). The paper's priority wording ("not establishing an exhaustive priority claim")
remains the right one.

### C.8 Receipts

All in the scratchpad directory named above: `looi.pdf`, `looi-abs.html`, `edmonds.pdf`,
`loring.pdf`, `loring-abs.html`, `higham.pdf`, `kramers1930.pdf`, `kramers-lorentz.html`, `a1102.pdf`,
`gil.txt` (text of the stored Gil PDF), `paper-p1.png` to `paper-p10.png` and `abstract-formula.png`
(page images), `mychecks.py` (SHA-256 `39cc53f7...a583`) with `mychecks.json`, `pauli_check.py`,
and `rerun/` (Section D).

## D. The verification record

Both programs were run on copies in `rerun/` (running them in place overwrites `verification.json`
and the figure), in a fresh venv with the pinned versions of `requirements.txt` (numpy 2.5.3, scipy
1.18.1, networkx 3.7, matplotlib 3.11.2) on Python 3.12.10, Windows. The source hashes match the
records: `verify.py` `3cf140d5...0c016` (= `verify_sha256`), `verify_exact.py` `d412fd18...a1642`
(= `source_sha256`). Run times: about 10 s and under 1 s.

| Item | Paper (Section 5.1) | Committed record | Rerun |
|---|---|---|---|
| `verify_exact.py`, every field | 210 objective checks; 1,270 odd-set inequalities; 177 stability cases; 3 ties; 30 one-dimensional | identical | byte-identical JSON apart from line endings |
| Matching vs exhaustive, `n=1..10` | 1,000 | 1,000, 0 failures | identical |
| Witness agreement | `3.6e-15` | `3.552713678800501e-15` | identical |
| Haar unitaries, `n=1..12` | 4,800 | 4,800, 0 failures | identical |
| Min energy minus exact minimum | "beyond roundoff" | `-1.4210854715202004e-14` | identical |
| Decomposition, largest discrepancy | `1.8e-13` | `1.7053025658242404e-13` | `2.2737367544323206e-13` |
| Odd-dimensional operator-norm identity | `1.6e-15` | `1.5543122344752192e-15` | `1.7763568394002505e-15` |
| Odd-set excess (Haar `n<=8`, every odd subset of size at least 3) | checked | `0.0` | identical |
| Independent skew contractions, `n=2..9` | 240 | 240 | identical |
| Scalar recurrence, `n=1..30` | 1,500 | 1,500 | identical |
| BFGS within `1e-7` | 96 of 120 | 96 | 96 |
| BFGS success flag | 80 | 80 | 80 (the OpenAI rerun's 82 came from unpinned versions) |
| Maximum excess | 48 | `48.000000000000014` | identical |
| Gradient check | `1.5e-6` | `1.4437805510484203e-06` | identical |
| Covariance and perturbation, `n=2..8` | 70 | 70, max `7.1e-14` | 70, max `5.7e-14` |
| Exact controls (triangle; rewiring `[0, 2, 16]`, breakpoints 1/4, 7/4) | as in the paper | as in the paper | identical |

The four differing maxima are roundoff of a different platform and library build; no count, pass or
claim changes. One BFGS detail (`details[25]`) differs at `1e-15`.

**O2, MINOR (optional): two reported tolerances are ceilings, stated as values; one count includes
trivial cases.** Location: lines 507 and 520, p. 8; line 525, p. 8. Claims: "The energy
decomposition's largest absolute discrepancy was $1.8\times10^{-13}$" and "with absolute discrepancy
$1.5\times10^{-6}$". Evidence: the record has `1.7053e-13` and `1.4438e-6`; the other two tolerances
(`3.6e-15`, `1.6e-15`) round either way, so the paper rounded up throughout. Also, the 1,270 odd-set
inequalities of `verify_exact.py` include 280 singleton sets, which hold trivially (`0<=0`; the code
loops over sizes from 1); 990 have `|A|>=3`. Fix: `$1.7\times10^{-13}$` at line 507,
`$1.4\times10^{-6}$` at line 520, and optionally "$1{,}270$ odd-set inequalities ($990$ with
$|A|\ge3$)" at line 525.

## E. The attribution block and the house rules

Against `paper/common/README.md`:

| Pattern item | Block (line 40, p. 1) | Verdict |
|---|---|---|
| 1. Writer and director; what each did | "written by GPT-6 Astra, an AI model made by OpenAI and run through its Codex agent, at the direction of David Ross"; chose the problem, derivation, programs, literature, text; Ross set the task, ran the process, takes responsibility | CORRECT |
| 2. Origin of the question; whose mathematics | run 18 of the Hypnos harness, Section 5; Section 1 lines 69-71 says the theorem is the session's, not the running system's | CORRECT |
| 3. Reviews by model and vendor, verdict clause each, applied, dispositions accompany | self-review (GPT-6 Astra by "the same model"): "no substantive repair and two presentation changes" (= `reviews/openai/REPORT.md`); Claude Fable 5.1, Anthropic: "every statement correct, two redundant hypotheses, one typo, and a novelty framing to correct" (= `reviews/claude/REPORT.md` verdict); GPT-6 Astra on 2026-10-02: "every statement correct and two minor items" (= its REVIEW.md, AN-1, AN-2); "eight edits" (= RECONCILIATION edits 1-8, commit `af7f1b2` 2026-09-29 13:26 EDT); Looi addition 2026-10-01 (commit `00782dd` 23:24 EDT) | CORRECT, except the placement of the disposition sentence: F7 |
| 4. "No human mathematician has reviewed this paper." | present verbatim | CORRECT |
| 5. Place in the set; written without reading the others; nobody called "the first" | "one of three manuscripts written from the Hypnos record on the night of 2026-09-28/29, the earliest of the three"; the Gil note "grew out of the review of this paper"; consistent with the Gil note's own block ("the last of the three, after Astra's antiunitary paper") and its use of the hull lemma (its lines 164-166 cite this paper as the companion manuscript) | CORRECT |

House rules: `main.tex` is pure ASCII; no U+2014 and no `---` in the source, no U+2014 in the extracted
PDF text; `--` occurs only in page ranges and paired names (`Hyers--Ulam`, `Moln\'ar--Timmermann`,
`population--coherence`, `Sections 2--4`). US English: a scan for British -our, -ise, -yse, -tre, doubled-l
and similar forms found nothing. No Clay Mathematics Institute (A)/(B) statement (`clay`, `millennium`:
no hit). Riemann hypothesis and zeta: only the Section 5.3 disclaimer (line 574) and the sibling paper's
name in the attribution. Build: `main.log` reports 10 pages, no Overfull or Underfull box, only the
two known notices (package name, inputenc).

**F7, MINOR (recommended; consequential): the disposition sentence precedes the third review, and the
block must name this review if anything from it is applied.** Location: line 40, p. 1. Claim:
"changing no statement or proof; the reviews and the reconciliation ledger accompany the source. A
third review on 2026-10-02 by GPT-6 Astra, fresh to the paper, found every statement correct and two
minor items (the domain of $\tau$ in the abstract; the scope of the source-access sentence in
Section~\ref{sec:provenance}), applied the same day." Evidence: README item 3 asks for the statement
that "the reviews with their per-item dispositions accompany the source"; as placed, it covers the
two September reviews and the reconciliation ledger, not the third review or its
`reviews/astra-2026-10-02/DISPOSITION.md`; the Gil note's block puts "The reviews and the per-item
dispositions accompany the source." after its last review. If any finding here is applied, README
item 3 also requires this review, by model and vendor, with its verdict. Fix (replace the quoted
span; the bracketed part must state what was actually applied):
```
changing no statement or proof. A third review on 2026-10-02 by GPT-6 Astra, fresh to the paper, found every statement correct and two minor items (the domain of $\tau$ in the abstract; the scope of the source-access sentence in Section~\ref{sec:provenance}), applied the same day. A fourth review the same day by Claude Opus 5.5, an Anthropic model, fresh to the paper, found every statement correct and twelve minor items of wording and citation (among them the index set of the abstract's formula, the commuting hypothesis in the statement of the contribution, and the record of which sources were read), [the seven it recommended] applied the same day. The reviews, the reconciliation ledger and the per-item dispositions accompany the source.
```

Date note (no change recommended). Astra's review header says "Review completed: 2026-10-01 23:52
EDT", its source-check paragraph is timestamped October 2, 00:02 EDT, and the file was last committed
2026-10-02 00:03:55 EDT (`c598785`); the block's "on 2026-10-02" and "applied the same day" (commit
`3ab19fe`, 14:15 EDT) are therefore defensible. RECONCILIATION item 30 shows the house dates by Eastern
time; if "the night of 2026-10-01/02" is preferred, it must change in all five blocks at once.

## F. Verdict

- **BLOCKING: 0.** No false statement, no missing case, no source on which a proof depends that fails.
- **MAJOR: 0.** The exact reduction, the hull lemma, every corollary and the Looi positioning stand.
- **MINOR: 12.** Recommended before sending:
  - F1: the abstract's `lambda_i` must be indexed `1..n` with multiplicity (line 22).
  - F2: "for commuting tuples" in the contribution sentence and "commuting tuples" at line 86.
  - F3: "or reviewed by a human mathematician" for "or independently peer reviewed" (line 533).
  - F4: the related-work search's actual sources; Kramers obtained; Wigner and Mirsky not (lines 577-580, 595).
  - F5: the congruence-orbit literature concerns selected entries of one orbit (lines 590-592).
  - F6: cite Loring's published version, Expositiones Mathematicae 44(2):125737 (lines 611-615).
  - F7: move the disposition sentence after the last review and name this review (line 40).

  Optional:
  - O1: Looi's first page is dated August 29, 2026 (lines 95-96).
  - O2: two tolerances are ceilings of the record; 280 of the 1,270 odd-set checks are singletons (lines 507, 520, 525).
  - O3: the block-diagonal matrix in (12)'s proof is `W=V^*U conj(V)` (lines 328-330).
  - O4: "prescribed intrinsic populations", Gil's term (lines 90, 588-589).
  - O5: state the "paired with 2" case in Proposition 4.1's proof (line 446).

**Should it go to Gil as it stands?** It can: nothing in it would mislead Gil about the mathematics.
I recommend, before sending, the smallest set F1 to F7: about a dozen lines of text, no statement or
proof touched, then a rebuild (`bash build.sh`), the em-dash and US-English scans, and a disposition
ledger for this review beside it. Of the seven, F3 and F5 are the ones a careful reader is most likely
to notice (a self-contradiction across pages 8 and 9; a mischaracterized literature Gil may know),
and F4 is the sentence edited today to be exact, now stale. If only some can be done, do F2, F3, F4
and F5, then F1.

**Confirmations (checked and found correct):**

- Theorem 2.1: decomposition (7) with factors 2 and 4; the nonnegative discarded term (needs `c>=0`
  only); the lower bound through Lemma 2.2 and Edmonds; the attaining signed swap; `tau=0`, `n=1`,
  repeated joint vectors, odd `n`, complex unitaries.
- Lemma 2.2, including the complex case and the convex-hull (not image) statement.
- Corollary 3.1 with the conjugate and the congruence `V W V^T`; the remark on the optimizer's action.
- Proposition 3.2, both parts, and the tie example.
- Corollary 3.3, (10), (11), (12), and the remarks on residual sizes and the determinant floor.
- Corollary 3.4 with signed costs. Proposition 3.5 in both directions.
- Section 4.1: (15), the dual (16) and `B`, the three-vertex certificate, the envelope properties,
  cardinality monotonicity.
- Proposition 4.1, (17), (18); the `(0,2,3,5)` curve `min{16 tau, 2+8 tau, 16}` with breakpoints 1/4
  and 7/4; Figure 1.
- `sigma_y`: Haar minima never below `min(8 tau, 8)` at `tau=0.5, 1, 2`; the theorem fails without the
  conjugate; every occurrence of the commutation error carries the conjugate, visible in the PDF.
- The single-observable route through Wigner, Kramers and Mirsky (re-derived).
- Looi: every constant, hypothesis and quantifier; the posting date; the distinction drawn.
- Edmonds pp. 125-126 support (4), (16) and the algorithm; the entry matches Crossref and the PDF.
- Higham's entry matches the reprint footnote; Loring's arXiv entry matches page 1 (published version: F6).
- Gil: Theorem 2 on the aligned class (pp. 9-10), the open question (pp. 10, 27), the entry (Crossref).
- Wigner and Mirsky entries match Crossref; Kramers' entry matches the KNAW scan and the Leiden list.
- Section 5.2 provenance: snapshot time and all five nodes.
- The verification record reproduces (D), including the recorded 80 success flags under pinned versions.
- Attribution items 1 to 5 of the house pattern (with F7), the human-review sentence, the place in the
  set and the relation to the Gil note; US English; no em dash; no Clay statement; no claim on the
  Riemann hypothesis beyond the disclaimer; clean build, 10 pages.
