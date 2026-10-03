# Disposition of the final review of 2026-10-02 (Claude Opus 5.5, fresh to the paper)

Applied by Claude Fable 5.1 (the outreach session) on Friday 2026-10-02, Eastern time, to
`main.tex` and `README.md` at the state after 3ab19fe. The review (`REVIEW.md`: 0 blocking,
2 major, 10 minor) is not rewritten. Each item was checked against the record before it was
applied.

| Item | Verdict | What was checked | What changed |
|---|---|---|---|
| OF-9, MAJOR (the free-value theorem was proved first, independently, by the companion's self-review, uncredited) | CORRECT, applied | `paper/antiunitary-matching/reviews/openai/lit-gil-extension.md` states and proves "Theorem G1: unrestricted coherence maximum", `max ||N||_F^2 = 2 sum_k a_{2k-1} a_{2k}` with the adjacent optimizer, through the hull lemma; `git log` dates its commit 5268029 at 2026-09-28 23:53:07 EDT, before the Claude review's answers (9da9004, 00:28 EDT) and this note's first draft (081c2f9, 00:50 EDT); `reviews/RECONCILIATION.md` records that neither review read the other; the companion's Section 1 says both reviews found the application. | The attribution block credits the independent earlier proof (model, date, "before this note's first draft", neither read the other); line 166's "its use for density matrices is new here" now says the application was found independently by both reviews of the companion and is developed here; the README's provenance paragraph says the same. The optional sentence on the self-review's Theorem G2 (majorization of the spectrum) was not added. |
| OF-4, MAJOR (the Mathias 1992 disclosure) | CORRECT, applied | The only abstract on record (OpenAlex) breaks off before Mathias's inequality; his setting (Hadamard product of a real positive semidefinite matrix and a complex skew-symmetric one, every unitarily invariant norm, the ordered diagonal entries of the positive factor) contains the note's matrix `DMD = (dd^T) o M` exactly, so his theorem may contain (9). The note's old text said only that "later sections" were unread. | Remark 4.4 now says the abstract breaks off before the inequality, that whether (9) is a special case of his theorem is not known, and that the note claims no priority for (9); "We have not found the population formula (9) itself stated in print, but one of the nearest results below could not be read." The README's open-literature paragraph says the same and names Mathias first. |
| OF-1 ("saturated Youla values" in Theorem 3.1) | CORRECT, applied | For `a = (1/2, 1/2, 0, 0)` the maximizer's Youla values are `(1, 0)`; Theorem 1.1 carries the qualification. | "with `s_k = 1` on every adjacent pair of positive population product". |
| OF-2 ("cannot follow from it") | CORRECT, applied | Remark 4.5 shows the prescribed-value analog of (8) is false. | "shows that the prescribed-value analog of (8) is false, so they cannot be obtained one Youla spectrum at a time". |
| OF-3 (three precision edits) | CORRECT, applied | (a) Proposition 4.2's singular values omit the odd `0`; (b) both orders of `s_1^2, s_2^2` give 543/250; (c) `t_k` named two different sequences in the two proofs. | (a) "(and 0 if n is odd)"; (b) "in either order"; (c) the first proof's `t_k` renamed `tau_k`. |
| OF-5 ("the HTML rendering") | CORRECT, applied | The stored full text is the PubMed Central rendering (PMC13512070). | "the PubMed Central HTML rendering numbers it 3.4". |
| OF-6 (Remark 4.5's `X`, `Y` are Gil's Appendix A coordinates) | CORRECT, applied | Gil's Appendix A (publisher PDF pp. 27-29) decomposes 2-forms on `R^4` into self-dual and anti-self-dual parts, (A3)-(A6); the reviewer checked symbolically that `X = (A_+/2) v_+`, `Y = (A_-/2) v_-` with `A_+- = s_1 +- s_2` on one orientation class. | The parenthetical, with the citation to eqs. (A3)-(A6), after the definition of `Y`. |
| OF-7 (Tam's extra inequality is not a parity condition) | CORRECT, applied | Tam's abstract identifies the additional inequality with the Thompson-Sing theorem's, present only in the even-dimensional full-matching case. | "(with one further inequality, of Thompson-Sing type, in Tam's even-dimensional full-matching case)". |
| OF-8 (Section 6 says `O(n)` for orientations drawn in `SO(n)`) | CORRECT, applied | `verify_gil.py` draws `Q = expm(1.5 x random skew)`, in `SO(n)`; the sign-flip remark covers `O(n)`. | "300 random orientations and 20 Nelder-Mead maximizations, both over SO(n) through the exponential parametrization (...)". |
| OF-10 (credit for Remark 4.5's example and certificates) | CORRECT, applied | The `n = 4` counterexample is the self-review's finding 1; the LP dual and the orbit certificate are the first Astra review's item 10 (its disposition records it). | The two review clauses in the attribution say so. |
| OF-11 (the 2026-10-01 consistency pass unnamed) | CORRECT, applied | The pass is in the appended ledger (`reviews/astra/DISPOSITION.md`); the package cover tells the reader each paper received one. | One sentence in the attribution. |
| OF-12 ("the Hypnos record" undefined; the harness's role indirect) | CORRECT, applied | The note has no provenance section; the companion's Section 5.2 describes the harness. | The last sentence of the attribution points to the companion's Section 5.2 and says the harness contributed no step of this note's mathematics. |

The attribution also names this review with its verdict. Confirmations recorded by the review:
every numbered statement and both proofs of Theorem 4.1 correct case by case; every number in
Remark 4.5 recomputed in exact rational arithmetic (549/250, 543/250, 581/250; the corrected
orbit certificate 361/400, 1/400, Pfaffian 9/10, the completed square, the sign change under a
reflection); Gil's quotations verbatim and the p. 10 / Section 3.5 locator right; `verify_gil.py`
rerun (4 min 2 s) writing a JSON byte-identical to the committed one. Not reached: Horn 1950
(publisher and PMC challenges; the inequality rederived), Fan 1949 and the two books at theorem
level, the full texts of Tam, Leite-Richa-Tomei and Mathias, MDPI's own HTML of Gil's paper.

Rebuilt with `build.sh` the same day; the page count is recorded in `paper/STATUS.md`.
