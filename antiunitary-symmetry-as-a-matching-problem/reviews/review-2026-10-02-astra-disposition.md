# Disposition of the 2026-10-02 reviews: Astra's fresh review and the chat-side comments

Applied by Claude Fable 5.1 (the outreach session) on Friday 2026-10-02, Eastern time, to
`main.tex` at the state after 00782dd. Each finding was checked against the source line before
it was applied; the delivered texts (`REVIEW.md` here; the chat session's text under
`docs/outreach/2026-10-02/opus-chat-handoff/`) are not rewritten. The reconciliation ledger
`reviews/RECONCILIATION.md` remains the ledger of the two September reviews; this file is the
ledger of the October 2 items.

## A. Astra's review (`REVIEW.md`, GPT-6 Astra, 2026-10-01 23:52 EDT)

| Item | Severity | Verdict | What was checked | What changed |
|---|---|---|---|---|
| AN-1 | MINOR | CORRECT, applied | The abstract introduced `tau` in the displayed minimum without its domain; (1) and Theorem 2.1 state `tau >= 0`. | "and `tau >= 0`" added to the abstract's sentence. |
| AN-2 | MINOR | CORRECT, applied | `reviews/openai/REPORT.md` line 95: "Some full texts, including Wigner, Tam, and Gil's EPJ Plus paper, were not accessible"; the October 2 review likewise did not obtain Wigner, Kramers or Mirsky at full text. Section 5.3's "checked the primary sources cited below" could be read as full-text inspection of every entry. | The sentence now says the search examined the accessible primary texts and the bibliographic records, names the three unobtained full texts, and refers to the reviews' access records; the conclusion stays limited to the sources examined. |

Sections A, B (otherwise), C, D and E of the review asked for no change. The attribution block
now names this review with its verdict.

## B. The chat-side comments (Claude Opus 5.5, claude.ai chat session, 2026-10-01 18:47 EDT; the reviewed PDF is the pre-rebuild build, SHA-256 `e1b10516...`)

| Item | Verdict | Reason and what changed |
|---|---|---|
| The overbar in `H_r U - U conj(H_r)` is load-bearing; text extraction drops it; make sure the site's HTML keeps it | Checked; nothing to change | The staged library entry (`hypnos-public/content/staged/antiunitary-symmetry-as-a-matching-problem.md`) describes the objective in words and renders no formula; the PDF, which the site serves as bytes pinned by SHA-256, carries the bar (the chat session confirmed this by rendering p. 1). |
| Check the unistochastic literature (the Birkhoff hull of `|U_ij|^2`) before calling Lemma 2.2 new | Referred to the literature pass of 2026-10-02 | The duplicate-literature search of this date (`docs/outreach/2026-10-02/LITERATURE-2026-10-02.md`) was briefed to search the unistochastic and orthostochastic literature for a prior statement of the squared-entry hull of skew-symmetric contractions; its result and any citation it requires are recorded there and applied from there. |
| "Certified alternative to continuous symmetry searches" names no one who runs such searches; the Gil application is probably the stronger case | A judgment on framing; not applied today | The sentence is the paper's own closing claim and is within what is proved; the Gil note is attached to the Gil email as the application. Recorded. |
| Decomposition (7), the hull lemma, the parity corollaries, Proposition 3.2 and the recurrence hold by hand; the `(0,2,3,5)` curve reproduces | Confirmation, no change | Recorded as an independent reproduction. |

## C. Rebuild

Rebuilt with `build.sh` the same day; the page count is recorded in `paper/STATUS.md`. No new
TeX warning; no em dash; US English checked by grep.
