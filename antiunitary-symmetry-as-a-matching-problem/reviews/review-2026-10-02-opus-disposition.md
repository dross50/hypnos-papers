# Disposition of the final review of 2026-10-02 (Claude Opus 5.5, fresh to the paper)

Applied by Claude Fable 5.1 (the outreach session) on Friday 2026-10-02, Eastern time, to
`main.tex` at the state after 3ab19fe. The review (`REVIEW.md`, 0 blocking, 0 major, 12 minor)
is not rewritten. Each item was checked against the source line and, where a source is cited,
against the source, before it was applied.

| Item | Verdict | What was checked | What changed |
|---|---|---|---|
| F1 (abstract: which `lambda_i`) | CORRECT, applied | Corollary 3.1 lists the joint eigenvalue vectors "repeated with joint multiplicity"; read with distinct vectors the formula fails (`H = 0` in dimension 2: formula `8 tau`, true value `0`). | The abstract now reads "If `lambda_1, ..., lambda_n` are the joint eigenvalue vectors, repeated with multiplicity, and `tau >= 0`". |
| F2 (Section 1: the contribution without "commuting") | CORRECT, applied | The exact reduction holds for commuting tuples only (Corollary 3.1; Section 5.3); the Pauli triple's value `8 min{3, tau+1}` is in `reviews/openai/REPORT.md` section 4, against `min(8 tau, 24)` for the commuting triple with the same separate spectra. | "the exact reduction of (1) for commuting tuples"; "hence commuting tuples of two or more observables". |
| F3 (Section 5.1: "independently peer reviewed") | CORRECT, applied | The sentence is the first version's; Section 5.3 reports two independent reviews one page later. | "formalized in a proof assistant or reviewed by a human mathematician." |
| F4 (the source-access sentence changed earlier today) | CORRECT, applied | `LITERATURE.md`, "Primary sources examined", lists Edmonds, Loring and Higham at full text and Wigner at bibliographic level; Kramers, Mirsky and Gil entered with the reviews (af7f1b2) and Looi on 2026-10-01 (00782dd). Kramers 1930 is served openly by the KNAW digital library (PU00015981.pdf, printed pp. 959-972; the reviewer's copy is in its scratch directory, the theorem stated on p. 965). | The paragraph now says which texts the original search examined, and ends: Kramers and Mirsky were cited after the reviews; the full texts of Wigner and Mirsky were not obtained by the search or by any review; that of Kramers was obtained in the fourth review. The KNAW URL is added to the Kramers entry. |
| F5 (Section 5.3: what the congruence-orbit literature contains) | CORRECT, applied | Neither review says that literature contains the single-observable ingredients (which are Wigner, Kramers, Mirsky); the OpenAI review calls Tam's theorem a statement about selected entries of one orbit, the Claude review calls it linear Cartan-projection statements about one entry per block. The clause entered with reconciliation edit 6 without a review sentence behind it. | "which concerns selected entries of a single orbit rather than the squared-entry hull or the weighted identity." |
| F6 (Loring is published) | CORRECT, applied | Crossref 10.1016/j.exmath.2025.125737: "Transforming antiunitary symmetries to a normal form", Expositiones Mathematicae 44(2), article 125737, issued April 2026 (checked from this session). | The bibliography entry now cites the journal article and says the text was cited from arXiv:2508.13004v2. |
| F7 (the attribution's disposition sentence and the fourth review) | CORRECT, applied | README item 3: every review named by model and vendor with its verdict, and the dispositions sentence after the last review. | The block names the fourth review with its verdict and the count applied, and ends with the dispositions sentence. |
| O3 (proof of (12): which matrix is block diagonal) | CORRECT, applied | Under the congruence `U = V W V^T` of Corollary 3.1 the block-diagonal matrix is `W = V^* U conj(V)`; `||U conj(U) + I||_F = ||W conj(W) + I||_F`. | The sentence now says so. |
| O4 (Gil's term) | CORRECT, applied | Gil's populations are intrinsic populations; the companion note's title uses the term. | "prescribed intrinsic populations" at both places. |
| O5 (Proposition 4.1: the pair `{1,2}` case) | CORRECT, applied | The trivial case was unstated. | "If it is paired with 2, delete 1,2 and continue." |
| O1 (Looi's own date, August 29, 2026) | CORRECT, not applied | The paper says Looi's paper was posted after this one was written, which is exact; it does not say when it was conceived. Astra's review of 2026-10-02 read it the same way. | None. |
| O2 (two tolerances printed as ceilings; 280 trivial singleton checks among 1,270) | CORRECT, not applied | The printed `1.8e-13` and `1.5e-6` are upper bounds on the recorded `1.7e-13` and `1.4e-6` ("below" is true of a ceiling); the singleton checks are counted as the program counts them. | None. |

Confirmations recorded by the review: every numbered statement correct; `sigma_y` sampled over
400,000 Haar unitaries per `tau` never below `min(8 tau, 8)`, and the theorem false without the
conjugate; the `(0,2,3,5)` curve exact; Looi's description accurate in every constant and
hypothesis; `verify_exact.py` reproduces its record byte for byte and `verify.py` every count
under the pinned versions. Not reached: the full texts of Wigner 1960 and Mirsky 1960 (publisher
human-verification pages; not attempted).

Rebuilt with `build.sh` the same day: 10 pages, no overfull or underfull box, no em dash.
