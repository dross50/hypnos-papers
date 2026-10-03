# Fresh adversarial review: Approximate Antiunitary Symmetry as a Matching Problem

Reviewer: GPT-6 Astra (OpenAI). Review completed: 2026-10-01 23:52 EDT (America/New_York), for the October 2 review set. Baseline: `5202569`, incorporating `7399037` and the `00782dd` consistency/Looi changes. Locations below refer to this baseline's `main.tex` and 10-page `main.pdf`.

I read the entire source and extracted PDF text, visually inspected PDF p. 2, reconstructed every proof, read both delivered reviews and the reconciliation ledger including tonight's pass, and fetched Looi's complete 41-page PDF. This is a fresh assessment with the earlier reviews available, as requested, not a blinded review. No manuscript or verification artifact was changed. No numerical rerun or proof-assistant verification is claimed.

## A. Statements against proofs.

All eight theorem/lemma/proposition/corollary statements are CORRECT. There is no missing hypothesis affecting a proof.

| Statement and location | Verdict | Independent reason and boundary checks |
|---|---|---|
| Theorem 2.1, source lines 131-143, PDF p. 3; proof p. 4 | CORRECT | For `S=(U+U^T)/2` and `K=(U-U^T)/2`, right multiplication by `conj(U)` preserves Frobenius norm and gives `||U conj(U)+I||_F^2=4||S||_F^2`. Pairwise cancellation gives (7), including factors 2 and 4. Its discarded term is nonnegative exactly because the off-diagonal costs are nonnegative. Lemma 2.2 gives a lower bound and the signed-swap witness attains it. Zero costs, `tau=0`, `n=1`, repeated costs, and odd dimensions cause no exception. |
| Lemma 2.2, lines 161-184, PDF p. 3 | CORRECT | Principal compression preserves the contraction bound. An odd complex skew matrix is singular under transpose, without any reality or normality assumption. Thus its squared Frobenius norm is at most its rank, giving every odd-set constraint. Matching vertices are themselves realized, so convex-hull equality follows. The warning that the squared-entry map need not be onto is necessary and correct. |
| Corollary 3.1, lines 229-249, PDF p. 4 | CORRECT | Simultaneous unitary diagonalization is available for a commuting Hermitian tuple. The change of variables is congruence `U=VWV^T`, not similarity. Both displayed covariance identities hold, including conjugation on the original observables. Joint multiplicities are retained. |
| Proposition 3.2, lines 256-294, PDF pp. 4-5 | CORRECT | Equality forces the matching-polytope point to the unique minimizing vertex. A unit-modulus skew entry saturates both associated unitary rows. Two unmatched vertices must have `c_ij>4 tau`; otherwise adding their edge contradicts uniqueness. This proves the remaining diagonal form without global positive costs. In a convex decomposition, nonoptimal matching mass is at most `epsilon/Delta`; the symmetric difference has at most `n` edges. The second estimate separately needs `c_min>0`, as stated. The quantitative assertion is restricted to `n>=2`, so a nonexistent second matching when `n=1` is not used. |
| Corollary 3.3, lines 304-334, PDF p. 5 | CORRECT | Maximum matching cardinality gives the Frobenius floor. In odd dimension a vector in `ker K` gives `||S||_op>=1`, while the triangle inequality gives the reverse bound. Exact commutation decomposes into the joint eigenspaces, and each odd block contributes 4 units of squared Frobenius defect. |
| Corollary 3.4, lines 344-365, PDF p. 5 | CORRECT | The hard square relation is equivalent to skew unitarity. All vertex sums equal 1; consequently every matching in any convex decomposition with positive weight is perfect. The remaining objective is linear and its coefficients may have either sign. Even dimension is stated. |
| Proposition 3.5, lines 369-391, PDF p. 6 | CORRECT | For fixed `U`, the norm difference of the stacked residual vectors is bounded by `2 eta`; the square component cancels. Taking infima in both directions proves the square-root Lipschitz bound. Squaring the lower bound requires its positive part, which is present. No commutativity is used until the supplied approximant is evaluated by matching. |
| Proposition 4.1, lines 440-475, PDF p. 7 | CORRECT | Exchange at the first remaining vertex preserves matching cardinality and does not increase squared-distance cost. Both crossing and nested pair configurations reduce to adjacent pairs. Removing an unmatched initial vertex cannot create an edge across an earlier removed vertex. Repeated spectral values merely allow ties. The recurrence, its initial values, the even-dimensional hard value, and the linear operation count after sorting follow. |

The unnumbered consequences also check: the dual signs in (16), the 3-vertex certificate with benefit 8, the concave nondecreasing penalty envelope, and the nondecreasing optimal cardinality for strictly increasing penalties (PDF p. 6). For `(0,2,3,5)`, the three branches are `16 tau`, `2+8 tau`, and `16`; their breakpoints are `1/4` and `7/4` (PDF p. 7). These are dimensionless mathematical quantities, not measured physical energies.

## B. Abstract and introduction against the statements.

The abstract has the correct commuting hypothesis, joint eigenvalue vectors, squared Euclidean pair cost, factor 2 per pair, and `4 tau` per unmatched vertex. Its optimizer statement is existential, so it does not incorrectly assert rigidity at ties. The hull, parity, stability, certificate, and sorted recurrence summaries match Sections 2-4. The introduction does not extend the exact formula to noncommuting tuples. The single-observable positioning and prescribed-physical-symmetry caveat are consistent with what is proved.

**AN-1, MINOR: state the penalty domain in the abstract.** Location: `main.tex` lines 22-27, PDF p. 1. The displayed minimum introduces `tau` without saying `tau>=0`, whereas (1) and Theorem 2.1 explicitly work with that domain. Tonight's ledger item 2 treats the sign as implicit in the words describing an error. A mathematical abstract should state the domain. Fix: begin the formula sentence with "For `tau>=0`, if ..." or insert "with `tau>=0`" after the objective. This is a completeness-of-statement repair, not a counterexample: with these nonnegative costs the identity in fact also extends trivially to negative `tau`, when the empty matching and identity matrix minimize it.

The Looi paragraph's constants and quantifiers are accurate: surjectivity, a uniform additive metric error, no linearity or continuity, the distinction between the cone and trace-one state space, and dimension dependence are all preserved. The distances used for the approximation should be read as the respective input metrics. Adding the source theorem numbers would improve traceability, but I do not count that optional improvement as another finding.

## C. Sources.

There are no direct source quotations in this manuscript and no external page/equation citations to resolve. All internal references in the extracted PDF resolve to the intended numbered statements. The bibliography contains eight entries.

| Entry | What this review verified and source receipt |
|---|---|
| Edmonds (1965) | Fetched the [NIST PDF](https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p125_A1b.pdf). Printed pp. 125-126 give the weighted problem, degree and odd-set constraints, polyhedron theorem, and dual. The title, journal, volume, page range 125-130, year, and DOI agree. This is the decisive external input to the proof. |
| Wigner (1960) | The [cited DOI](https://doi.org/10.1063/1.1703672) did not yield the original text through this session's browser. Loring's paper cites and reconstructs the normal-form result, but that is not a fresh verification of Wigner's original pages or complete bibliographic metadata. No discrepancy established; original-source check remains open. |
| Loring (2025) | Fetched [arXiv 2508.13004v2](https://arxiv.org/pdf/2508.13004), title/author and abstract on p. 1. The description as constructive normal-form work is accurate. This source concerns exact prescribed antiunitaries; it does not state this paper's soft matching identity. |
| Higham (1989) | Fetched the [author's reprint](https://nhigham.com/wp-content/uploads/2023/10/high89n.pdf). PDF p. 1 footnote gives Gover and Barnett, Oxford University Press, and printed pp. 1-27. The reprint has 23 PDF pages; that does not invalidate the printed page range. Its introduction supports the matrix-nearness attribution. |
| Kramers (1930) | Attempted an original-source search by title, author, year and page range, including the Dutch academy domains. No original scan was retrieved. The entry is not established wrong, but this review cannot certify its original bibliographic metadata or original theorem wording. The parity proof in this manuscript is self-contained. |
| Mirsky (1960) | The [Oxford publisher record](https://academic.oup.com/qjmath/article/11/1/50/1525786) confirms author, title, volume 11, issue 1, printed pp. 50-59, year, and DOI. Full-text access was not obtained; I do not claim to have checked the original inequality on a particular page. |
| Gil (2026) | The repository's fetched [Entropy PDF](https://doi.org/10.3390/e28080877), `reviews/openai/lit-gil-2026.pdf`, p. 1, confirms title, author, year and article number. Theorem 2, PDF pp. 9-10, treats aligned orientations; Section 8.2, p. 27, leaves general orientation questions open. This supports the paragraph on p. 2. Follow-up source check, October 2, 00:02 EDT: the stored PDF numbers the former section 3.5, while the stored HTML-derived text calls it 3.4. The [PubMed record](https://pubmed.ncbi.nlm.nih.gov/42649672/) also confirms issue 8. The manuscript's comparison does not depend on the differing section numbers. |
| Looi (2026) | Fetched and read [all 41 PDF pages](https://arxiv.org/pdf/2609.37133). Definition (1.3), p. 4, fixes additive distortion; Theorems 1.2 and 1.3 and Corollary 1.4, p. 5, give the quoted bounds; Theorem 1.5 and Corollary 1.6, pp. 5-6, distinguish infinite/fixed finite dimension; the construction on pp. 31-39 explains the lack of a uniform modulus. The [arXiv record](https://arxiv.org/abs/2609.37133) confirms the September 29 posting. The manuscript itself is dated August 29 on PDF p. 1: the current comparison carefully says *posted* after this paper, and does not claim Looi conceived his work later. |

The Looi distinction is fair. He approximates maps on an entire metric space by one conjugation; this paper optimizes an algebraic residual for a fixed commuting tuple. His hypotheses and conclusions do not give this matching formula, and this formula does not give his stability bounds. Neither work needs to be described as superseding the other.

**AN-2, MINOR: narrow the source-access claim.** Location: Section 5.3, `main.tex` lines 576-591, PDF p. 9, beginning with the assertion that the search checked the cited primary sources. Reason: the delivered OpenAI review, `reviews/openai/REPORT.md`, Section 3, explicitly records that Wigner's full text and some older congruence-orbit texts were inaccessible. The current sentence can be read as claiming full-text inspection of every entry. Fix: say that the search examined the accessible primary texts and bibliographic records, distinguish the unaccessed originals, and keep the conclusion limited to sources actually examined. Do not turn failed access into evidence of absence. This is an access-disclosure repair, not a newly identified antecedent.

## D. Priority and positioning.

Bounded fresh web-search receipt, 2026-10-01 23:48-23:52 EDT (America/New_York). Queries were submitted as written below. Search results were leads; mathematical conclusions rest on the cited primary texts.

| Query | Returned material and disposition |
|---|---|
| `"skew-symmetric contraction" "matching"` | No returned primary paper stating the squared-entry hull identity. Sparse exact-phrase results are weak evidence and were followed by plain-word searches. |
| `antiunitary commutation soft penalty matching polytope` | General matching/antiunitary material and unrelated optimization hits; no primary statement of (3) identified. |
| `skew symmetric squared entries convex hull matching polytope unitary` | Edmonds-related polytope material; Goldberg and Karzanov's [skew-symmetric flows paper](https://arxiv.org/abs/math/0304290); general Schur-Horn material. The flow paper's abstract concerns graph flows, not squared entries of a matrix contraction. No equivalent result established. |
| `"Stability of isometries of quantum states" Looi` | [Looi's arXiv record](https://arxiv.org/abs/2609.37133), followed by the full PDF read described in C. Adjacent, not an antecedent to the claimed identity. |

I found no source in this bounded check stating or proving the general weighted soft identity. This does not establish priority. The paper's narrow contribution wording is appropriate: the hull observation and the general-cost reduction are the central content; parity, one-observable results, matching algorithms, and routine duality remain classical or consequences. Retain the explicit priority limitation and apply AN-2 so its evidence matches its language.

## E. The attribution block and the house rules.

The title names the writer, vendor and director. The attribution on PDF p. 1 names both reviews, gives their verdicts, records application and the reconciliation ledger, and includes the required human-review sentence verbatim. Its chronological position and statement of independence are consistent with the set record. The Gil note is correctly described as growing out of this paper's review; no false mutual independence remains.

The source/PDF language scan found no prohibited English variants in the manuscript prose and no Unicode or TeX-generated em dash. The scope statements distinguish a freely optimized antiunitary from a prescribed physical symmetry, and finite commuting tuples from the supplied-approximant bound. No theorem is promoted into a broader result.

## F. Verdict.

- **BLOCKING: 0 findings.** No invalid theorem, missing proof case, or fatal source dependence found.
- **MAJOR: 0 findings.** The exact reduction and the Looi positioning survive this review.
- **MINOR: 2 findings.** AN-1: give `tau>=0` in the abstract. AN-2: qualify the source-access claim in Section 5.3.

**First-reader decision: READY as it stands**, with the two small prose edits recommended before refreshing the package. No proof edit is needed. Original full-text checks for Wigner, Kramers and Mirsky remain uncompleted in this review; this verdict does not certify those inaccessible originals or establish priority.
