# Disposition of the 2026-10-02 review by GPT-6 Astra

Applied by Claude Fable 5.1 (the outreach session) on Friday 2026-10-02, Eastern time, to
`main.tex` at the state after a19cd37. Each finding was checked against the source line and
recomputed before it was applied; the delivered review (`REVIEW.md`) is not rewritten. The
chat-side review of 2026-10-01 (`docs/outreach/2026-10-02/opus-chat-handoff/`) did not cover
this note.

| Item | Severity | Verdict | What was checked | What changed |
|---|---|---|---|---|
| GL-1 | MAJOR | CORRECT, applied | For the displayed matrix (`M_12 = 0.3`, `M_13 = c`, `M_24 = -c`, `M_34 = 0.2`, `c^2 = 0.84`): `sum_{i<j} M_ij^2 = 0.09 + 0.84 + 0.84 + 0.04 = 1.81 = (1/2)||M||_F^2`; `X = (0.25, c, 0)`, `||X||^2 = 0.9025`; `Y = (0.05, 0, 0)`, `||Y||^2 = 0.0025`; so `||X||^2 + ||Y||^2 = 0.905 = (1/4)||M||_F^2`, not `(1/2)||M||_F^2 = 1.81` as printed. `Pf M = M_12 M_34 - M_13 M_24 + M_14 M_23 = 0.06 + 0.84 = 0.9 = ||X||^2 - ||Y||^2`; under `M -> Q^T M Q` with `det Q = -1` the Pfaffian changes sign and `X`, `Y` exchange roles, so the orbit invariant is the absolute value. The objective `2(X_1+Y_1)^2 + 2.4(X_2^2+Y_2^2)`, the completion of the square `2.172 - 0.4(X_1 - 5Y_1)^2 + 9.6 Y_1^2` and the maximum `2.196` at `X_1 = 5Y_1 = 0.25` were recomputed and stand. | The two constraints now read `(1/4)||M||_F^2 = ||X||^2 + ||Y||^2 = 0.905` and `|Pf M| = | ||X||^2 - ||Y||^2 | = 0.9`, with the sign remark; nothing else in Remark 4.5 changed. |
| GL-2 | MINOR | CORRECT, applied | `pdftotext` of the stored publisher PDF (`paper/antiunitary-matching/reviews/openai/lit-gil-2026.pdf`): the quoted sentence is on p. 10, in the paragraph after Theorem 2, under the heading "3.5. Maximum Aligned Cohesion for Fixed Populations"; the HTML-derived text (`.../claude/03-literature/gil-2026-fulltext.txt`) labels the same section 3.4. | The locator now reads "in the paragraph after his Theorem 2 (p. 10 of the publisher's PDF, where the section is numbered 3.5; the HTML rendering numbers it 3.4)". |

Sections B to E of the review asked for no change. The attribution block now names this review
with its verdict. Rebuilt with `build.sh` the same day; the page count is recorded in
`paper/STATUS.md`.
