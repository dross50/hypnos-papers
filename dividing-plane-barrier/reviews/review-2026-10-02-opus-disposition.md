# Disposition of the final review of 2026-10-02 (Claude Opus 5.5, fresh to the paper)

Applied by Claude Fable 5.1 (the outreach session) on Friday 2026-10-02, Eastern time, to
`main.tex` and `README.md` at the state after 3ab19fe. The review (`REVIEW.md`: 0 blocking,
1 major, 17 minor) is not rewritten. Each item was checked against the record or the source it
cites before it was applied.

| Item | Verdict | What was checked | What changed |
|---|---|---|---|
| OF-1, MAJOR (the harness had already sketched the barrier; the block and Section 6 say it only asked) | CORRECT, applied | `docs/research/2026-09-30-navier-stokes-blowup/EXPLANATION-B.md` line 17 (committed 1656b76, 2026-09-30 16:41 EDT): "Symmetry makes Hc = 0 at eta = 0, so there Sq = -h < 0 whenever a = 2: a never reaches 2, bs = 0, and the edge inequality fails"; its question 3 opens "Our reading gives a < 2 on the midplane for symmetric stress-free profiles at leading order". That is the first-crossing form of Theorem 3.2(1), (2) and (4) for h > 0 under symmetry, in the record before the paper. | The attribution block says the explanation sketched why a symmetric stress-free core cannot reach a = 2 and asked the question, and that the paper proves the sketch under a weaker hypothesis, for every h >= 0, with the margin; its last sentence names the explanation among what was read; Section 6 states the sketch and what the paper adds (the hypothesis (13), the case h = 0, the monotonicity of H, the margin, the consequences in Theorem 3.2(4)). The README says the same. |
| OF-3 (Remark 3.6 calls the absorption a source) | CORRECT, applied | In (14) the h-term enters as -hH, a linear absorption; a nonnegative source would allow an interior maximum (H'' = -1 on (0,2) with H(0) = 0 has one). | The sentence now says hH acts as a linear absorption, what diffusion must supply, and why an interior maximum is impossible. |
| OF-5 (Proposition 4.1 invoked outside its hypothesis) | CORRECT, applied | Proposition 4.1 assumes Theorem 4.6(v) in full; the proof of Proposition 4.3 establishes M_infinity = 0 and S_infinity = 0 only; the proof of Proposition 4.1 uses only S(infinity, eta) = 0. | "the proof of Proposition 4.1, which uses only S(infinity, eta) = 0, applies". |
| OF-6 ("The flow is an axisymmetric vortex") | CORRECT, applied | The manuscript, p. 3: only the leading flow is axisymmetric; the pulses have zero angular average (p. 6) and angular periodicity (p. 74). | "Its leading-order flow is an axisymmetric vortex". |
| OF-7 (a p. 6 sentence used verbatim without quotation marks) | CORRECT, applied | The pinned manuscript's text contains "The pulses grow by extracting energy from the background shear." word for word (checked here by grep). | The sentence is now quoted and cited to p. 6. |
| OF-11 (Liu's families include axis data without bias) | CORRECT, applied | Liu, arXiv 2609.14292v1, p. 6, Theorem 3.1(ii): "There are a fixed nonzero tilt gamma > 0 and j* > 0 such that one canonical axis pressure trace Pi_gamma = Pi_ref + gamma eta supports every G_j = 4 eta + j, |j| <= j*"; (iii) realizations with G = m eta at nonzero tilt; p. 19: "An auxiliary core at gamma = 0 is used only for this parity estimate, not as a completed exit" (both pages checked here). By (8)_2 at the axis the tilt gives U_X(0,0) = gamma/2, so (13) fails for them. | The sentence on Liu now says which of his families lack the axis bias, why they fall outside hypothesis (13), and that what the theorem forces is axial velocity on the dividing plane, not the bias at the axis point. |
| OF-12 (Lemma A.8 is on p. 140) | CORRECT, applied | `pdftotext -f 140 -l 140` of the pinned PDF shows the statement of Lemma A.8 on p. 140; its proof continues on p. 141. | "Lemma A.8, pp. 140-141". |
| OF-14 ("an autonomous research harness" against the lane's registration) | CORRECT, applied | `docs/DESIGN-BLOWUP-PULLBACK.md` registers the lane's outputs as assisted research, never autonomous production. | The sentence adds "whose outputs are registered as assisted research, not autonomous production". |
| OF-15 (the chat session's comments carry no vendor and no verdict) | CORRECT, applied | House pattern item 3; the chat session's text opens "It checks out." and its four contributions are in the 2026-10-02 ledger. | The clause names the vendor and the four things the session found or did. |
| OF-16 (the consistency pass unnamed; its ledger heading carried the UTC date) | CORRECT, applied | `reviews/claude/DISPOSITION.md` holds the pass (62 checks, 15 corrections, commit 7c3931b at 23:27 EDT on 2026-10-01); its heading said 2026-10-02. | One sentence in the attribution; the ledger heading now says 2026-10-01 and records the correction. |
| OF-17 ("both reviewers", "either reviewer's" undercount) | CORRECT, applied | Four reviews have read the manuscript against the sources. | "every reviewer", "every reviewer did", "any reviewer's". |
| OF-18 (the README still says the margin is proportional to h and lists two reviews) | CORRECT, applied | The README ships in the package (`package_set.py`); its margin sentence was the one NS-1 removed from the paper; its review list stopped at two and pointed to a file under a wrong path. | The README rewritten: the margin sentence as the paper has it, the five review entries with their paths, the explanation's sketch in the provenance line, the public status from the release. |
| OF-2, OF-4, OF-8, OF-9, OF-10, OF-13 (optional) | CORRECT, not applied | A first-crossing parenthetical valid for h > 0; the undefined Burgers strain and the factor chi; the abstract's "this transport"; the unexplained "opposite of its role"; "verified by a program"; "nine identities" naming eight. | None today; recorded for the next revision. |

The attribution also names this review with its verdict and the count applied. Confirmations
recorded by the review: every numbered statement and formula correct, including today's
additions (the h = 0, w = 4 solution and 60/(e^30 - 1) = 5.6e-12; the factors q^{-2h} and
r T_z = q^{-A} X N_s / L, checked symbolically; Lemma 4.2's cancellation for every G, and the
manuscript's (4.16) for general profiles); the checker's 53 flags with numbers identical to the
committed receipt; the five tests at `tests/test_ns_midplane_barrier.py`; the reviewer's own
re-integration of (17) (sup a = 1.993095 and 1.931031; the h = 0 margin 5.6146e-12). Not
obtained: the original texts of the four classical references (bibliographic data confirmed
through Crossref and publisher reference lists). The reviewer disclosed that one Crossref
request carried the owner's email address in its header.

Rebuilt with `build.sh` the same day; the page count (13, up from 12, with the provenance
sentences) is recorded in `paper/STATUS.md` and in the emails.
