# Disposition of the final review of 2026-10-02 (Claude Opus 5.5, fresh to the paper)

Applied by Claude Fable 5.1 (the outreach session) on Friday 2026-10-02, Eastern time, to
`main.tex` and `README.md` at the state after 3ab19fe. The review (`REVIEW.md`: 0 blocking,
1 major, 9 minor, 8 nits) is not rewritten. Each item was checked against the source line
before it was applied.

| Item | Verdict | What was checked | What changed |
|---|---|---|---|
| OF-1, MAJOR (the README denies Theorem 6.1(a) and carries three superseded statements) | CORRECT, applied | `README.md` said the unconditional lower bound is not available, "15 pages, amsart", "Neither contains Theorem 5.1", two reviews; `package_set.py` ships the README and the cover tells the reader to read it. | The README now states Theorem 6.1(a) as the paper does (`2/5 <= D_BM <= 1`, `2 pi/5 <= R <= pi`, with Conrey's theorem and the date of the change), the height quantifier on Corollary 4.2, 17 pages in the house format, the Mikulik sentence as the paper has it, the two reviews of 2026-10-02 and the consistency pass, and a note that the second script does not compute the finite-section constants or the jitter control. The package cover note is corrected in the same pass. |
| OF-2 (the sentence after Theorem 6.1 on the preprint) | CORRECT, applied | "raises the proportion" read as 2/5 to 2/3, while the published record after Conrey is higher (the review cites Pratt, Robles, Zaharescu and Zeindler 2020, kappa* >= 0.407511, which this session did not independently verify and does not add); the preprint does not itself say it is unreviewed. | "which carries no journal reference as of this writing, states a proportion of two thirds". The optional PRZZ citation was not added. |
| OF-3 (Section 8: the inputs the statements rest on) | CORRECT, applied | Theorem 6.1(a) now rests on Conrey, cited in Section 6 only. | The sentence names Conrey's theorem for the lower bound in Theorem 6.1(a). |
| OF-4 (Section 6.1's opening describes only an upper bound) | CORRECT, applied | Theorem 6.1(a) now has a lower bound from a non-counting input. | "a lower bound for the set needs an input about distinct ordinates, which Conrey's theorem supplies" appended. |
| OF-5 ("a fresh instance of the same model line"; the shipped ledger said the objection was resolved) | CORRECT, applied | `grep "model line" main.tex` found the clause at line 26; the ledger row of this morning was wrong about that phrase (right about "first/second author"). | The clause now reads "an adversarial same-vendor review by Claude Opus 5.5, an Anthropic model other than the writer, in a fresh context (2026-09-29)"; the morning ledger row carries a dated correction; the Gil note's identical clause was corrected the same way. |
| OF-6 (verdict clauses for the chat session and for this review) | CORRECT, applied | House pattern item 3. | The chat session's verdict is stated in one clause; this review is named with its verdict. |
| OF-7 (the jitter control is matched in its largest displacement only) | CORRECT, applied | The control's `u_n` is uniform on `[-max|d_n|, max|d_n|]`; its root-mean-square displacement at `N = 500` is `0.6642/sqrt(3) = 0.38` against the zeros' `0.25` (the reviewer's recomputation; the arithmetic of the uniform case checked here). | The sentence added this morning now says what is matched and what is not, with the two numbers, and that the control's points are independent. |
| OF-8 ("strictly increasing across simple zeros") | CORRECT, applied | The paper's own distinction at line 54: two simple zeros can share an ordinate. | "strictly increasing across distinct ordinates (`x_n < x_{n+1}` exactly when `gamma_n < gamma_{n+1}`)". |
| OF-9 (Section 8 drops the height quantifier and credits Corollary 4.2 to Theorem 4.1) | CORRECT, applied | Corollary 4.2 is a finite-height statement; the abstract and introduction carry "below height T". | "(it does not, for any fixed block length; below height T it does at block lengths of order log^2 T, Corollary 4.2)". |
| OF-10 (Section 4's title) | CORRECT, applied | The title read against Corollary 4.2. | "Kadec and Avdonin fail for every block length". |
| Nits (eight; among them `3.2e-34` as a round-up of `3.142e-34`) | Recorded, not applied | Ceilings stated as "to" a value are true of the recorded residuals. | None. |

Confirmations recorded by the review: the new proof paragraph "Lower bound for the set"
correct in every step and constant (Conrey's `kappa*` is a liminf of the proportion of zeros
that are simple and on the line; distinct such zeros have distinct ordinates; the two-sided
bound on `A(x)`; the long family); the rewritten paragraph after Corollary 4.2 matches the proof
of Theorem 4.1; the abstract and introduction agree with the theorems case by case; every
printed number reproduced from the first 1000 zeros (recomputed with mpmath and agreeing with
the certified table to `5e-19`) and the table for `10^5`; a scratch rebuild gives 17 pages and
text identical to the committed PDF; no em dash, no UK spelling, no Clay wording. Not reached:
the originals of Selberg 1946 and 1992, Avdonin, Kadec, Pavlov, HNP p. 240, Koosis and several
full texts (metadata checked through reference lists); Tsang read from the copy fetched on
2026-10-01 (the journal's server answered with a bot check).

Rebuilt with `build.sh` the same day; the page count is recorded in `paper/STATUS.md`.
