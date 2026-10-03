# Reconciliation of the two reviews of "Approximate Antiunitary Symmetry as a Matching Problem"

Applied 2026-09-29 (about 13:20 EDT) by Claude (Fable 5.1) on the owner's instruction ("go ahead
and handle the edits"), against baseline 9820d1e (the manuscript as Astra wrote it). The two
reviews were produced independently and neither reviewer read the other; this file is the first
place they meet. Astra's authorship of the manuscript is unchanged; every edit below is a
review-driven change of exposition or hypothesis, not new mathematics, and the two reviews'
own new results stay in their directories (`reviews/openai/extensions.md`,
`reviews/claude/04-new-results.md`, `reviews/claude/extension-note.pdf`, and the Gil note).

## Where the two reviews agree

| Finding | OpenAI (`reviews/openai/REPORT.md`, `claim-audit.md`) | Claude (`reviews/claude/REPORT.md`, `06-claim-audit.md`) |
|---|---|---|
| Main theorem, hull lemma, every corollary | correct, no substantive repair | correct, no false statement |
| `max` outside math mode, eq. (benefits) | fix the missing backslash | typo (#23) |
| Rigidity proposition needs only a unique optimal matching | "a unique optimal matching alone implies the complete phase-decorated form" | `c_ij > 0` redundant (#13, Prop F) |
| Hard-constraint corollary needs no sign condition on `c` | (implicit in its audit) | #21 |
| Gil, Entropy 28(8):877 (2026) is directly relevant and was not cited | the main weakness is positioning | #32 |
| Single-observable case is classical | (not stated) | Wigner + Kramers + Mirsky (Prop D), #32 |
| The computation is a polynomial-size matching problem; the odd-set LP is exponential | presentation change | (agrees implicitly) |

No finding of either review contradicts the other.

## Edits made to `main.tex`

1. **Typo (both).** Eq. (benefits): `-max_{M}` became `-\max_{M}`.
2. **Polynomial-size wording (OpenAI).** Section 4.1: the matrix problem is stated as a
   maximum-weight matching problem on a polynomial-size graph, solvable by Edmonds' algorithm;
   the odd-set description is described as exponential and used only for proofs and certificates.
3. **Rigidity hypothesis (both).** Proposition 3.2: the hypothesis `c_ij > 0` was dropped from
   the exact-structure statement; uniqueness of the optimal matching suffices. The proof was
   completed accordingly: on a matched pair `|K_ij| = 1` forces `S_ij = 0` and unit entries
   through `|U_ij|^2 + |U_ji|^2 = 2|S_ij|^2 + 2 <= 2`; two unmatched vertices have `c_ij > 4 tau`
   by uniqueness, hence `S_ij = 0`. The second stability estimate keeps its own hypothesis
   `c_min > 0`, stated inline. The tie example `n = 3, c = 0, tau = 1` (rotations by ninety
   degrees about any axis are minimizers) is named as the reason uniqueness is needed.
4. **Hard constraint (both).** Corollary 3.5 now states that no sign condition on the off-diagonal
   costs is needed, with the one-line reason (`S = 0` under `U^T = -U`, the objective is linear).
5. **Framing (Claude, consistent with OpenAI's "positioning").** Section 1: a paragraph states
   that the single-observable case follows from Wigner's normal form, Kramers' theorem and
   Mirsky's inequality and reduces to the sorted-spectrum recurrence, that the substantive
   content is the general cost array (tuples of two or more observables) carried by the hull
   lemma, and that the lemma bears on Gil's coherence maximization, an application both reviews
   found independently and which is developed separately.
6. **Related work (both).** Section 5.3: the related-work paragraph records that two independent
   reviews also failed to find the identity or the hull lemma in print, found Gil (2026), and
   found older work on congruence orbits with prescribed singular values containing the
   single-observable ingredients.
7. **Caveat (Claude #31).** Section 5.3: for a single observable the value depends on consecutive
   spectral gaps alone, so it certifies spectral pairing, not the symmetry of a prescribed
   antiunitary.
8. **Bibliography.** Added Kramers (1930), Mirsky (1960), Gil (2026).

Not changed: the abstract's "certified alternative to continuous symmetry searches on finite
spectral data" (Claude #33 accepts it with the caveat now stated in Section 5.3); the numerical
section (both reviews reproduced its counts; OpenAI's rerun gave 82 optimizer success flags
against the recorded 80 with the same 96 accurate outcomes, a dependency-version effect noted in
its report, so the recorded numbers stand as the record of the authoring run); the provenance
and attribution paragraphs (Astra's).

## Left open, deliberately

- Priority: both reviews searched and found nothing; neither claims an exhaustive search.
- Whether the four-level fixed-defect problem's exact value can be found (OpenAI, "strict
  relaxation gap").
- The Gil application is Paper 3 (written at `reviews/claude/gil-note/`, moved to `paper/gil-note/`
  on 2026-10-01), under its own reviews.

Rebuilt after the edits: 9 pages, no warnings, no em dashes; verification scripts untouched
because no numerical claim changed.

## Addendum, 2026-10-01 (Claude Fable 5.1): the Looi paragraph

The outreach plan's datedness check of 2026-10-01 (`docs/outreach/2026-10-02/PLAN.md`, section 2)
found one paper adjacent to this manuscript and posted after both reviews: S. Looi, "Stability
of isometries of quantum states", arXiv 2609.37133, posted 2026-09-29 (41 pages, math.FA). It
was read in full on 2026-10-01 from the arXiv PDF before anything was written. What it proves:
dimension-independent Hyers-Ulam stability for surjective approximate isometries of the positive
trace-class cone in the Bures metric (within 2 sqrt(2) epsilon of a Wigner symmetry, Theorem 1.2)
and the trace metric (within 9 epsilon / 2, or 3 epsilon when zero is fixed, Theorem 1.3 and
Corollary 1.4), with no linearity, affinity or continuity assumed on the maps; on the state space,
instability in infinite dimension (Theorem 1.5) and a modulus in each finite dimension that
cannot be chosen uniformly in the dimension (Corollary 1.6). Its subject is a map on states and
how close it is to one conjugation by a unitary or antiunitary (the Molnar-Timmermann
classification made quantitative). This manuscript's subject is a fixed tuple of observables and
the least error over all antiunitaries in commutation together with the square relation, given
exactly by a matching. No observable, commutation error or square relation appears in Looi's
theorems; no distance between states or approximate isometry appears here; the shared ancestor is
Wigner's theorem. No priority claim is made in either direction.

Edits (three, no change to any statement or proof): one paragraph at the end of Section 1 that
cites and distinguishes the paper as above; one sentence at the end of Section 5.3 recording the
2026-10-01 search and its one adjacent find; the bibliography entry `looi`. The attribution block
records the 2026-10-01 addition in one clause. `LITERATURE.md` carries a dated line. Rebuilt with
tectonic; page count recorded in `paper/STATUS.md` (the refresh of 2026-10-01/02).

## Consistency pass, 2026-10-01 (fresh Claude Opus 5.5 agent, directed by the Claude Fable 5.1 outreach thread)

A bounded pass, begun 2026-10-01 at 23:09 EDT, checking the abstract and Section 1 against the theorems, the Looi paragraph and sentence against Looi's text, quotations and source citations, the attribution block against `paper/common/README.md`, and the house language rules; it is not a third review of the mathematics.

| # | check (1-6) | item checked | source and page | command or method | finding | verdict | what was done |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Abstract, sentence 1: a commuting tuple of Hermitian matrices; least combined error in commutation and `T^2=-I` | `main.tex` Cor. 3.1 (hypothesis), eq. (1) | read side by side | hypothesis and quantity match | NO FINDING | none |
| 2 | 1 | Abstract formula: the objective over `U(n)` equals the minimum over all matchings of `2 sum dist(lambda_i, lambda_j)^2 + 4 tau (n - 2 #M)`, with Euclidean `dist` | Thm. 2.1 eq. (3); Cor. 3.1 eq. (8) with `c_ij = dist(lambda_i, lambda_j)^2` | term-by-term comparison | factor 2, `4 tau`, `n - 2 #M`, empty matching included, minimum attained; `tau >= 0` is implicit in the abstract's "combined error" and stated at (1) | NO FINDING | none |
| 3 | 1 | Abstract optimizer: signed swaps on matched pairs, scalar phases on unmatched states | Thm. 2.1 (block `[[0,1],[-1,0]]` per pair, entry 1 per unmatched vertex, "an optimizer"); Prop. 3.2 (unit scalars) | read | existential claim; entry 1 is a phase, and Prop. 3.2 allows every phase | NO FINDING | none |
| 4 | 1 | Abstract: squared entries of a skew-symmetric contraction give a point of Edmonds' polytope | Lemma 2.2 | read | matches (`K^T=-K`, operator norm at most 1) | NO FINDING | none |
| 5 | 1 | Abstract: odd-set inequalities supply the parity obstruction missing from a degree-only relaxation | Remark 2.3 (`n=3, c=0, tau=1`) | read | matches | NO FINDING | none |
| 6 | 1 | Abstract: "generic optimizer rigidity" | Prop. 3.2 after the 2026-09-29 reconciliation: the only hypothesis is a unique optimal matching (`c_ij > 0` dropped) | read | a tie between two matchings is one of finitely many hyperplanes in `(c, tau)`, so uniqueness is generic; the abstract adds no positivity or simple-spectrum hypothesis | NO FINDING | none |
| 7 | 1 | Abstract: "stability estimates" | Prop. 3.2 eq. (9): first estimate under uniqueness and `n >= 2`, second also under `c_min > 0`; Prop. 3.5 eq. (14) | read | plural matches; the abstract states no hypothesis that contradicts either | NO FINDING | none |
| 8 | 1 | Abstract: "exact dual certificates" | Sec. 4.1: dual (16), bound `B`, exact rational check, three-vertex certificate (`z=8`, `B=8`, energy 4) | read; three-vertex arithmetic redone | matches | NO FINDING | none |
| 9 | 1 | Abstract: "linear-time recurrence for one sorted spectrum" | Prop. 4.1 eq. (17), `O(n)` once sorted | read | matches | NO FINDING | none |
| 10 | 1 | Abstract: classical odd-dimensional defect bounds and Kramers pairing as boundary cases | Cor. 3.3 eqs. (10) to (12); Cor. 3.4 eq. (13) | read | matches | NO FINDING | none |
| 11 | 1 | Abstract: "certified alternative to continuous symmetry searches on finite spectral data" | Sec. 4.1 (no continuous unitary search); Sec. 5.1 (BFGS exact in 96 of 120 attempts, a local optimizer is not a certificate); Sec. 5.3 caveats | read | matches; kept as accepted on 2026-09-29 (Claude #33) | NO FINDING | none |
| 12 | 1 | Sec. 1 para. 1: `T = U C`, `T^2 = U Ubar`, error `HU - U Hbar`; exact commutation with `T^2=-I` forces even multiplicities | Cor. 3.3 eq. (12) | direct computation; read | the value is 0 exactly when no multiplicity is odd | NO FINDING | none |
| 13 | 1 | Sec. 1 para. 2: definition (1) with `tau >= 0`, unnormalized Frobenius norms, no scalar-square assumption | Thm. 2.1 (`tau >= 0`); Prop. 3.5 (same `tau >= 0`) | read | matches | NO FINDING | none |
| 14 | 1 | Sec. 1 para. 3: run-18 observations (odd-dimensional Frobenius defect 2, negative square as skew symmetry, eigenbasis conjugations) | Sec. 5.2 nodes 2649, 2676, 2677; Cor. 3.3 (the unsquared Frobenius residual has minimum 2 in odd dimension) | read | matches | NO FINDING | none |
| 15 | 1 | Sec. 1 para. 4: contribution; single-observable case classical, hard or soft, reducing to Prop. 4.1; substance of Thm. 2.1 is the general cost array carried by Lemma 2.2 | Prop. 4.1 eqs. (17) (soft) and (18) (hard, even `n`); Cor. 3.4 | read | matches; "the value of (1)" under the hard constraint reads as the constrained problem of Cor. 3.4 and eq. (18) | NO FINDING | none |
| 16 | 1 | Sec. 1 para. 4: Gil maximizes coherence at prescribed populations over a restricted class of antisymmetric parts, and the hull lemma removes the restriction | Gil, Entropy 28(8):877, Sec. 3.4 (maximum over the aligned class; global optimality over arbitrary Youla orientations left open there); `reviews/claude/03-literature/gil-2026-fulltext.txt` lines 199 to 231 | `grep -n -i` for `aligned`, `Youla` | matches; the aligned class is the restriction | NO FINDING | none |
| 17 | 1 | Sec. 1, Looi paragraph: "the data are a fixed tuple of observables, ... which Theorem 2.1 gives exactly as a matching value" | Cor. 3.1 (commuting hypothesis); Sec. 5.3 (the exact spectral formula requires a finite commuting Hermitian tuple) | read side by side | the commuting hypothesis was missing; for a noncommuting tuple only the bounds of Prop. 3.5 hold | CORRECT, applied | "commuting" inserted: "a fixed commuting tuple of observables" |
| 18 | 2 | Posting date: Sec. 1 (September 29, 2026, after this manuscript was written on September 28); Sec. 5.3 (posted after the reviews); attribution (posted 2026-09-29) | Looi p. 1 stamp `arXiv:2609.37133v1 [math.FA] 29 Sep 2026`; arxiv.org/abs/2609.37133 history: v1 Tue, 29 Sep 2026 09:36:14 UTC | `pdftotext -enc UTF-8 -layout -f 1 -l 1`; `curl -sSL https://arxiv.org/abs/2609.37133` | v1 is 05:36 EDT on 09-29, after the 23:20 EDT 09-28 snapshot and after both review reports (file times 09-28 23:52 and 09-29 00:40 EDT) | NO FINDING | none |
| 19 | 2 | Bures constant `2 sqrt(2) epsilon` for a surjective cone map, zero not fixed | Looi Thm. 1.2, eq. (1.4), p. 5 | `pdftotext -enc UTF-8 -layout -f 5 -l 7` | matches | NO FINDING | none |
| 20 | 2 | Trace constants `9 epsilon/2`, and `3 epsilon` when zero is fixed | Looi Thm. 1.3, eq. (1.6) and the sentence after it, p. 5; Cor. 1.4, eq. (1.8), p. 5 (also under delta-surjectivity) | same | matches | NO FINDING | none |
| 21 | 2 | Hypothesis and conclusion: a surjective map of the positive trace-class cone preserving the Bures or trace distance up to additive error epsilon lies uniformly near a conjugation `A -> UAU*`, U unitary or antiunitary | Looi eq. (1.3) and the stability problem, p. 4; Thms. 1.2 and 1.3, p. 5; Wigner symmetry defined on p. 3 | full `pdftotext -enc UTF-8 -layout` read | matches | NO FINDING | none |
| 22 | 2 | "with no linearity or continuity assumed" | Looi p. 4 (no linearity, affinity or continuity assumption anywhere in the paper) | `grep -ci affinity` (1 hit, p. 4) | accurate paraphrase, not in quotation marks; dropping "affinity" only weakens the claim | NO FINDING | none |
| 23 | 2 | "constants independent of the dimension" for the cone | Looi abstract, p. 1 (dimension-independent stability); p. 4 (cone bounds with constants independent of dimension) | read | matches | NO FINDING | none |
| 24 | 2 | State space: no modulus uniform in the dimension | Looi Thm. 1.5, eqs. (1.9) and (1.10), p. 5 (infinite dimension); Cor. 1.6, p. 6 (a modulus in each finite dimension); p. 4 and the abstract (none uniform in the dimension) | read | matches | NO FINDING | none |
| 25 | 2 | Exact classification attributed to Molnar and Timmermann: bijective isometries of the cone and the state space, Bures and trace, are Wigner symmetries; Looi's results are its quantitative form | Looi Thm. 1.1 (Molnar-Timmermann), p. 3, citing their Theorems 1 to 4; p. 4 (quantitative versions of Thm. 1.1) | read | matches | NO FINDING | none |
| 26 | 2 | "no observable, commutation error or square relation enters Looi's theorems" | all 41 pages; the statements of Thms. 1.1 to 1.5 and 4.1, Cors. 1.4 and 1.6, Lemmas 3.1 to 3.5, 4.2, 4.3, 5.1 to 5.4 | `pdftotext -enc UTF-8 -layout`, then `grep -ci` with page numbers: `observ` 2, `commut` 5, `square` 12, `matching` 0, `time.revers` 0, `Kramers` 0 | `observ`: one motivating sentence of the Introduction (p. 1) and "observe" (p. 37); `commut`: inside proofs (pp. 19, 25, 36) and a reference title (p. 41); `square`: square roots and squared quantities; none in a statement | NO FINDING | none |
| 27 | 2 | "what the two share is Wigner's theorem behind the unitary-or-antiunitary dichotomy" | Looi pp. 1 and 3 (the conclusion is a Wigner symmetry, a unitary or antiunitary conjugation; Wigner's theorem is not named) | `grep -ci wigner` (5 hits) | interpretive sentence about shared background, consistent with Looi's definitions | NO FINDING | none |
| 28 | 2 | Sec. 5.3 sentence: a search on 2026-10-01 for work posted after the reviews found one adjacent paper and nothing stating the identity | `docs/outreach/2026-10-02/PLAN.md` section 2 (receipts 2026-10-01 20:38 to 22:00 EDT); `LITERATURE.md` addendum (Liu et al., arXiv 2610.01555, judged not adjacent) | read | matches | NO FINDING | none |
| 29 | 2 | Bibliography entry `looi`: S. Looi, Stability of isometries of quantum states, arXiv:2609.37133, 2026 | Looi p. 1; title of the abs page | read; `grep -o '<title>'` | matches | NO FINDING | none |
| 30 | 2 | Attribution clause: "on 2026-10-02 added one paragraph in Section 1 and one sentence in Section 5" | file times: Looi PDF saved 2026-10-01 22:46 EDT, `main.tex` last written 2026-10-01 23:04 EDT before this pass (02:46 and 03:04 UTC on 10-02); clock at the start of this pass Thu Oct 1 23:09 EDT | `ls -la`; `date`; `TZ=America/New_York date` | the addition was made on 2026-10-01 in Eastern time; 2026-10-02 is its UTC date and the ship-target date; the house convention is Eastern | CORRECT, not applied (the same date stands in the 2026-10-02 addendum above, which this pass may not rewrite, in `LITERATURE.md`, and in the heading set for this section; changing the paper alone would split one record into two dates) | reported to the directing thread, which owns every copy of the date |
| 31 | 3 | Quotations attributed to a source | `main.tex` | grep for paired backticks, paired single quotes and the double-quote character | no quotation marks in the file; nothing is quoted from a source | NO FINDING | none |
| 32 | 4 | Page, section, theorem or equation numbers of sources cited in the text | all eight cited works at every `\cite` site | read; `grep -n cite` | no source is cited by page, section, theorem or equation (Gil and Looi are cited without numbers; Looi's theorem numbers appear only in this ledger) | NO FINDING | none |
| 33 | 4 | Edmonds entry (J. Res. NBS Sec. B 69B(1-2):125-130, 1965, title) and the attributions of eq. (4), the dual (16) and Edmonds' algorithm | NIST PDF: Vol. 69B Nos. 1 and 2, January-June 1965, printed pp. 125 to 130 (6 pages); odd-set inequality (3) over sets of 2r+1 nodes, Theorem (P), and the dual with node variables y and odd-set variables z on p. 126; weighted matching algorithm in the abstract, p. 125 | `curl -sSL` the NIST URL; `pdftotext`; `grep -n` | matches | NO FINDING | none |
| 34 | 4 | Higham entry: Gover and Barnett, eds., Applications of Matrix Theory, pages 1-27, Oxford University Press, 1989 | reprint footnote on p. 1 of the PDF at the bibliography URL | `curl -sSL`; `pdftotext` | matches | NO FINDING | none |
| 35 | 4 | Gil entry: Entropy 28(8):877, 2026, doi 10.3390/e28080877, title | header of `gil-2026-fulltext.txt` (PMC13512070, published 2026 Aug 4) | `head` | matches | NO FINDING | none |
| 36 | 4 | Loring entry and "a recent constructive treatment" | Loring PDF p. 1 (arXiv:2508.13004v2, 20 Aug 2025; the abstract calls Wigner's method constructive and gives two algorithms) | `pdftotext -f 1 -l 1` | matches | NO FINDING | none |
| 37 | 4 | Wigner 1960, Kramers 1930, Mirsky 1960 entries | not fetched | per the brief: no quotation or in-text page citation depends on them, and none was found | bibliographic data not verified against the sources | NO FINDING | none |
| 38 | 5 | Both reviews named, each verdict in one clause | `reviews/openai/REPORT.md` (no substantive repair, two presentation changes); `reviews/claude/REPORT.md` Verdict (everything proved is correct, two hypotheses stronger than needed, one typo, single-observable case classical); README pattern items 3 and 4 | read | matches | NO FINDING | none |
| 39 | 5 | "applied in full", "eight edits, no new mathematics", 2026-09-29 | this file, sections above (applied 2026-09-29 about 13:20 EDT; eight edits) | read | matches | NO FINDING | none |
| 40 | 5 | "No human mathematician has reviewed this paper." | `paper/common/README.md` pattern item 4 | grep | present verbatim | NO FINDING | none |
| 41 | 5 | Place in the set; no paper called "the first" | `paper/common/README.md` item 5 and the set table; sibling blocks in `paper/unfolded-zeros/main.tex` (after Astra's paper) and `paper/gil-note/main.tex` (the last of the three) | `grep -n -i first` (4 hits: a proof step, an estimate, a recurrence, "first version"); read | "one of three manuscripts ... the earliest of the three" agrees with both siblings | NO FINDING | none |
| 42 | 5 | Last clause: the others "were written without reading it while it was being written" | `paper/gil-note/main.tex` attribution (it found Gil's questions while reviewing this paper and reuses its hull lemma); README item 5 (a paper states that it was written without reading the others) | read | read naturally, false for the Gil note and vacuous under the other parse; README item 5 not stated | CORRECT, applied | clause now reads "came after it, and it was written without reading them" |
| 43 | 6 | US English | `main.tex` | Python scan for the British -our, -re, -ise and -yse families, doubled-l inflections and about twenty British-only words; non-ASCII scan | no hit; the file is pure ASCII | NO FINDING | none |
| 44 | 6 | No em dash | `main.tex`; rendered `main.pdf` | grep for U+2014 and for three hyphens in the source; `pdftotext -enc UTF-8 main.pdf -` with `grep -c` for U+2014 | none in the source, 0 in the rendered text; `--` only in ranges and paired names (Hyers--Ulam, Molnar--Timmermann, population--coherence) | NO FINDING | none |
| 45 | 6 | No claim on the Riemann hypothesis, zeta zeros or infinite-dimensional operators beyond Sec. 5.3 | `main.tex` | `grep -n -i` for `riemann`, `zeta`, `infinite` | hits: the Sec. 5.3 disclaimer and the attribution's name of the Riesz-basis paper; the Looi paragraph reports Looi's dimension-free cone bounds as Looi's and claims nothing for this paper | NO FINDING | none |
| 46 | 6 | No Clay Mathematics Institute (A)/(B) statement | `main.tex` | `grep -n -i` for `clay`, `millennium` | no hit | NO FINDING | none |

Build after the two edits: `bash build.sh` (tectonic) wrote main.pdf, and the log reads "Output written on main.xdv (10 pages, 64916 bytes)"; `pdftotext main.pdf - | grep -c $'\f'` gives 10; the warnings are the two of the previous build (the `../common/hypnos-paper` package-name notice and the inputenc notice), with no Overfull or Underfull box.
