# Adversarial review of Approximate Antiunitary Symmetry as a Matching Problem

OpenAI review completed September 28, 2026 EDT. Fixed baseline: `9820d1ed1e61381cb22185740377f7d2ee99a6f1`.

## Candid verdict

**The main theorem survives.** Its proof is correct for precisely the stated nonnegative symmetric costs, zero diagonal, unitary competitors, and linear penalty on the squared Frobenius defect. The substantive corollaries also survive: commuting-observable covariance, rigidity under the stated hypotheses, stability, both parity statements, the hard negative-square formula, matching duality, the ordered-spectrum recurrence, and the perturbation estimate. I found no false stated mathematical theorem and no missing hypothesis that invalidates one.

**The main weakness is positioning, not correctness.** The supplied literature search misses directly relevant work by José J. Gil and older work on prescribed-singular-value congruence orbits. The weighted soft-penalty identity was not found in the primary sources examined, but priority remains unresolved. The normal forms, parity facts, matching machinery, and most algorithmic consequences are classical or routine once the key reduction is recognized.

**The strongest follow-on result is a specific density-matrix extremum.** The matching lemma removes the aligned-orientation restriction in Gil's 2026 coherence theorem when the skew singular values remain free. A separate elementary projection argument gives a stronger, attained spectral majorization bound, hence a common maximum-purity and minimum-entropy state at fixed entrywise real part. This is a proved answer to a precisely identified question, not a claim to solve every orientation or fixed-singular-value problem mentioned in that literature.

**Some tempting extensions fail.** The matching-polytope point need not come from one matrix. A four-level fixed-defect problem has a strict relaxation gap. Negative costs and nonlinear defect penalties also defeat unchanged matching formulas. These failures do not contradict the original theorem, whose boundaries are stated correctly.

The work supports retaining the original theorem and adding a focused extension note. It does not support a physical time-reversal classification, an infinite-dimensional claim, or promotional novelty language.

## What was reviewed and how independence was protected

All original source and supplied verification code were retrieved from the fixed Git object without changing the checkout. The supplied rendered PDF was accessible and its bytes are identical to the baseline `main.pdf`. Mathematical review used the authoritative LaTeX source; the PDF was not separately visually audited. The baseline source SHA-256 is `75abc10db1a933ecc4c0534edcab31f15d4fe792bc1383633d6cf7e04c2166f5`.

The central proof was reconstructed before consulting the original `PROOF-AUDIT.md`. Three bounded internal OpenAI tasks independently handled proof review, primary literature, and experiments; their arguments and evidence are preserved here. They were not used as a vote on correctness.

**Reviewer separation was maintained. No accidental exposure to the other reviewer's work occurred.** The Claude review directory, its reports, drafts, experiments, task history, outbox notes, and review-related commits or diffs were not inspected. No message was sent to the other reviewer. Operational memory files were read only after checking that their modification times preceded the fixed baseline; repository history inspection was anchored at that baseline. Unfiltered conversation-history retrieval was deliberately omitted because it could expose concurrent review material. No prior OpenAI review directory existed when this investigation began.

All canonical new research is under `paper/antiunitary-matching/reviews/openai/`. The running Hypnos service, database, configuration, recorded verdicts, original manuscript, and shared verification files were not changed. No publication, submission, or external contact was made. Delivery copies are exports of this directory, not a second research workstream.

## 1. Correctness assessment

The [claim audit](claim-audit.md) gives baseline line numbers and complete arguments for each substantive claim. The central chain is:

1. For U unitary, K=(U-U^T)/2 is a complex skew-symmetric contraction. The transpose of a unitary is unitary; no real-matrix assumption is used.
2. Every odd principal submatrix of K is singular and remains a contraction. Its Frobenius squared norm is at most its rank, giving the full odd-set inequalities with the correct factor of two.
3. Edmonds' theorem puts x_ij=|K_ij|² in the matching polytope. It is convex-hull membership, not a realizability assertion for arbitrary fractional matchings.
4. The exact residual identity is U bar(U)+I=(U+U^T)bar(U). The exact energy decomposition has a nonnegative symmetric-part remainder because the costs are nonnegative.
5. A minimizing matching has a feasible signed-swap unitary witness with diagonal symmetric part. Therefore the lower bound is attained. This closes the relaxation; the polytope inclusion alone would not.

The commuting change of basis is U=VWV^T. All constants use unnormalized Frobenius norms. Zero costs, repeated joint eigenvalues, ties, tau=0, n=1, and odd dimension are covered as stated. The gap estimates require a positive matching gap, and their second-best notation only makes sense for n>=2.

No substantive repair is needed. Two presentation changes are justified: call the computation a weighted matching problem on a polynomial-size graph, since the displayed odd-set LP has exponentially many inequalities; and fix the missing LaTeX backslash on `max` at baseline line 352.

Historical Hypnos provenance is not a mathematical premise. This review did not query the live database or independently authenticate the origin of its recorded observations.

## 2. Stronger optimizer conclusions proved here

The original positivity assumption in its exact rigidity proposition is stronger than necessary. **A unique optimal matching alone implies the complete phase-decorated matching form of every optimizer.** Equality forces x to be that matching vector. Matched rows saturate. Between two unmatched vertices, uniqueness forces c_ij>4 tau, so the remaining symmetric block is diagonal.

With no uniqueness assumption, the exact equality test is:

    U minimizes iff x belongs to the optimal matching face
    and S_ij=0 on every positive-cost edge.

This includes ties and arbitrary zero-cost patterns and is accompanied by a full primal-dual slack identity in the audit. It does not assert that all points on the optimal face are realizable.

A stronger matrix-distance estimate is also available. Let Q_M be the phase-decorated optimizer family of a unique matching, Delta its gap, and epsilon the energy excess. For n>=2,

    dist_F(U,Q_M)² <= 4n epsilon/Delta.

This needs no global positive minimum edge cost. If the unique matching is perfect, 2n replaces 4n. The audit proves these estimates and gives a more detailed coefficient depending on the number of unmatched vertices. The original perturbation constant 2 is sharp even for one two-dimensional observable.

These are useful refinements of the original theorem. Their proofs are supplied, but this review does not certify separate publication priority for each inequality.

## 3. Closest prior work and the consequential application

Gil's [Entropy paper](https://doi.org/10.3390/e28080877), Section 3.4, Theorem 2, maximizes the imaginary antisymmetric part of a density matrix in an aligned class. Its hypotheses are

    rho=A+iN>=0,
    A=diag(a_1,...,a_n), a_1>=...>=a_n>=0, sum a_i=1,
    N real and N^T=-N.

The fixed real structure is essential: A is the entrywise real part, not the Hermitian part. Gil's result allows the pairing and skew singular values to vary within the aligned class and explicitly leaves arbitrary orientations separate. The support-aware factorization N=A^(1/2) K A^(1/2), with K a real skew contraction, was already present in his earlier work and is not a new contribution of this review.

The baseline matching lemma immediately proves the unrestricted result:

    max_{N: A+iN>=0} ||N||_F²
      = 2 sum_{j=1}^{floor(n/2)} a_(2j-1) a_(2j).

Zero populations force zero rows in N by positive semidefinite 2-by-2 minors, so singular A causes no gap. The maximizing state has saturated adjacent 2-by-2 blocks.

The stronger result is that every feasible rho has

    lambda(rho) majorized by
    q=(a_1+a_2, a_3+a_4, ..., [a_n if n is odd], 0,...,0).

The same paired state attains q. A complete proof takes a top-k complex spectral subspace, includes it in the real span of its real and imaginary parts, and applies the classical maximum-trace principle to a real projection of rank at most 2k. Positivity is essential. This yields exact maximum purity, minimum von Neumann entropy, minimum Rényi entropies, and minimum rank ceil(rank(A)/2). No sufficiency assertion for every intermediate spectrum is made.

The [standalone density-matrix note](lit-gil-extension.md) gives both proofs and this exact synthetic example:

    A=diag(16,9,4,1)/30,
    N_12=12/30, N_34=2/30, N_ji=-N_ij, other entries zero.

Then rho has spectrum (5/6,1/6,0,0), imaginary-part squared norm 74/225, purity 13/18, and globally minimum entropy equal to the binary entropy of 1/6. A nonaligned competitor with the same saturated skew singular values is computed exactly and has strictly smaller coherence and purity.

This application is relevant to fixed-real-part density-matrix completion and resource-theory questions about imaginarity. It is invariant under the real orthogonal coordinate changes appropriate to that fixed real structure. It is not invariant under changing the reference conjugation arbitrarily, and it does not establish the presence of a physical time-reversal symmetry. Under a prescribed full nonsaturated skew singular spectrum, the attaining saturated witness may be inadmissible; that different orientation problem remains open here.

The [literature comparison](literature.md) records actual source access, theorem locations, backward and forward leads, and search limits. Edmonds and Ky Fan supply classical machinery. Tam's 1998 selected-entry congruence theorem is a relevant warning about prescribed singular values. Some full texts, including Wigner, Tam, and Gil's EPJ Plus paper, were not accessible; their contents were not assumed absent. Unsuccessful searches are not proof of novelty.

## 4. Further completed investigations

Complete proofs are in [extensions.md](extensions.md).

**Nearest common Kramers symmetry.** For a commuting tuple in even dimension, the squared distance to any Hermitian tuple admitting a common antiunitary T with T²=-I is one half the minimum perfect-matching sum of squared joint spectral distances. The target tuple need not be commuting, yet a commuting optimum exists: replace each matched joint pair by its midpoint. This turns the original hard constraint into a concrete simultaneous data-correction problem. For a prescribed T, orthogonal projection already solves the correction problem without matching.

**An exact noncommuting qubit formula.** Write H_r=alpha_r I+h_r dot sigma and G=sum_r h_r h_r^T. Then, without a commutativity assumption,

    Phi_tau(H)=8 min{tr(G), tau+lambda_min(G)}.

The proof reduces the unitary problem to a quadratic form on a real four-dimensional unit sphere. For the Pauli triple it gives 8 min{3,tau+1}. Three commuting copies of sigma_z have the same separate spectra but minimum zero at tau=0, whereas the Pauli triple has minimum 8. Thus separate spectra cannot determine a general noncommuting extension.

**Restricted skew contractions.** With an allowed-edge graph and rank(K)<=2k, the squared-entry convex hull is exactly the hull of graph matchings of size at most k. A proof uses the fact that adjacent matching vertices differ in cardinality by at most one. This yields exact rank- and support-constrained coherence maxima. Arbitrary fixed nonzero singular values are not covered.

**Constructive commuting approximants.** For two Hermitian matrices, spectral bins of width h, bin means, and pinching produce commuting A,B with

    ||X-A||_F²+||Y-B||_F² <= n h²/12
       + ||[X,Y]||_F ||Y-(tr Y/n)I||_F/h.

Enumerating the finitely many grid shifts supplies a deterministic approximant and a measured error to insert into the original perturbation bound. The exponent 1/3 obtained by optimizing h is already part of almost-commuting-matrix literature, including [Bansil and Kachkovskiy](https://arxiv.org/html/2608.31000v1). The contribution here is a complete explicit construction tied to the certified antiunitary workflow, not a claimed new exponent. A single pinching step does not make three or more arbitrary observables mutually commute.

## 5. Decisive negative findings

**The squared-entry map is not onto.** On four vertices, x_12=x_23=x_34=1/2 and other entries zero is the average of two matching vectors. Any realizing skew matrix would make a 2-by-2 principal minor of I-KK* equal -1/4, so it cannot be a contraction. Dimensions at most three do not have this obstruction.

**A fixed defect budget has a gap.** For H=diag(0,2,3,5) and defect ||U bar(U)+I||_F²<=4, the true minimum commutation cost satisfies

    9 < minimum <= 12.

The matching lower convex envelope predicts 9. Equality would require exactly the impossible squared-entry vector above. Compactness makes the inequality strict. The upper bound is attained by two explicitly given rotation blocks. Forty-eight numerical constrained searches were consistent with 12, but no proof of equality to 12 was obtained; the certified interval remains strict above 9 and at most 12.

**Changing hypotheses changes the problem.** An exact cyclic-permutation example defeats arbitrary signed costs. A two-dimensional rotation beats all matching endpoints for a penalty quadratic in the squared defect. These examples establish limitations of generalizations, not defects in the original manuscript.

## 6. Checks actually performed

The [reproducibility record](checks.md) and accompanying scripts and JSON preserve all runs, feasibility checks, tolerances, failed optimizations, versions, and hashes.

| Investigation | Actual scope and outcome |
| --- | --- |
| Frozen supplied numerical verifier | All finite checks passed; 96/120 continuous attempts reached the certified value within 1e-7. The 24 misses were retained. |
| Frozen supplied exact verifier | 210 exact real objective checks, 1,270 odd-set inequalities, 177 unique-gap stability checks passed. |
| Independent exact complex arithmetic | 17,200 objective/decomposition comparisons across 860 cost arrays and 25 rational complex unitaries; 8,110 unique-gap cases passed. Counts reuse matrices and are not independent samples. |
| Qubit extension | 400 tuples, 4,000 identities, 4,000 independent Haar lower-bound checks, and 400 attaining witnesses passed. |
| Density spectral majorization | 1,650 states, 9,900 Ky Fan inequalities, and 1,650 attaining witnesses passed; ten exact symbolic assertions verified the rational example calculations. |
| Shifted-grid approximation | 330 Hermitian pairs at three widths, 6,525 partitions, and 990 bound comparisons passed. |
| Fixed-defect searches | 48/48 final points feasible within tolerance; none below 12 beyond tolerance. This is not a global-optimality certificate. |

The baseline rerun used installed dependency versions different from the pinned authoring versions. It produced 82 optimizer success flags rather than the recorded 80, while retaining the same 96 accurate objective outcomes. That distinction is recorded rather than hidden. Exact comparisons used rational complex arithmetic; floating-point discrepancies were checked against stated tolerances and feasibility residuals.

No finite test count is being used as a proof. The manuscript and the substantial extensions have explicit analytic arguments; no proof assistant formalization or external specialist review was performed.

## Remaining uncertainties and justified next steps

1. Resolve priority for the exact soft penalty identity, the complete squared-entry convex hull, and the specific fixed-real-part spectral extremum. The closest known comparison is now concrete, but inaccessible texts and equivalent formulations remain potential sources of prior results.
2. If developing one follow-on paper, center it on the unrestricted density-matrix extremum and majorization theorem, while identifying the classical machinery and the exact restriction removed from Gil. Keep the antiunitary theorem's optimizer and algorithmic results together rather than treating each routine consequence as a separate discovery.
3. The fixed-defect problem deserves further analysis because scalarization provably loses information. The four-level case is a reproducible benchmark, with a rigorous gap and an unresolved exact value.
4. Prescribed singular values, locality restrictions, and a physically fixed antiunitary require additional arguments. Nothing in this review authorizes replacing those constraints by the contraction ball or a freely fitted symmetry.

**Strongest defensible conclusion.** The manuscript's continuous soft antiunitary optimization is exactly a matching problem under its stated assumptions. Its most consequential demonstrated use is an attained global spectral bound for density matrices with a fixed real part, resolving the free-amplitude orientation maximum separated from Gil's aligned theorem and determining entropy and purity extrema. The proofs establish these statements; broader novelty remains an open bibliographic question.
