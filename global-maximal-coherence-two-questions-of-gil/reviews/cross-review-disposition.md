# Disposition of Astra's referee review of the Gil note

Review: `reviews/astra/REVIEW.md` (OpenAI Codex, gpt-6-astra, launched by Claude through the Codex
CLI on 2026-09-29 14:25 EDT with the prompt in `reviews/astra/PROMPT.md`; committed at 24c79d0,
14:37 EDT; the CLI's own final message is `LAST-MESSAGE.md`, identical to the review up to the
trailing newline). Reviewed manuscript: the f37590d text (sha256 42673800...). Applied by Claude
(Fable 5.1) on 2026-09-29, 14:42 to 14:50 EDT. Every item was checked before it was applied; the
one mathematical addition (Horn's derivation) was verified line by line.

## 1. MAJOR: Theorem 4.1 is an immediate consequence of Horn's 1950 multiplicative inequality

APPLIED. The derivation was checked independently: with `D = diag(sqrt a)` and `T = DMD` skew, its
singular values are `t_1, t_1, ..., t_m, t_m` (+0 for odd n); Horn's product inequality applied twice at
each even index `2l` gives `prod_{k<=l} t_k^2 <= prod_{k<=l} s_k^2 a_{2k-1} a_{2k}`; both vectors are
nonincreasing, so this is weak log-majorization, which implies weak majorization (exp is increasing
and convex), hence `sum t_k^2 <= sum s_k^2 a_{2k-1} a_{2k}`, and `sum_{i<j} a_i a_j |M_ij|^2 = (1/2)||T||_F^2
= sum t_k^2`. It is now the "Second proof, from a classical singular-value inequality" right after the
layer-cake proof, Horn 1950 is cited (PNAS 36(7) 374-375), and the text after the theorem, the
abstract, Remark 4.4 and the README say plainly that as a matrix inequality Theorem 4.1 is a sharp
consequence of classical majorization, and that what the note claims is the application to Gil's
questions, the polyhedral viewpoint of Lemma 2.1, and the nested-set family of Proposition 4.2. The
title is unchanged (the layer-cake proof stands and yields the family). The earlier assessment that
"Theorem G" of the cross-review was new is corrected in Claude's memory as well.

## 2. MAJOR: Corollary 5.1(1) false without the support restriction

APPLIED. Item (1) now says: with free Youla values, the maximizing aligned state's support is a
maximum-weight matching for `b` on the support `{i : a_i > 0}`, every inactive entry being zero (so
for positive populations the matching is on all of `[n]`). Item (3) reads `s_1 <= 1` on the support.

## 3. MINOR: trace normalization

APPLIED. `sum a_i = 1` is imposed in eq. (1), with Gil's definition of a density matrix quoted, and in
the hypothesis of Theorem 3.1; the matrix inequality of Theorem 4.1 keeps unrestricted nonnegative `a`.

## 4. MINOR: the Tam / Leite-Richa-Tomei comparison

APPLIED. "Do not imply" became "do not directly state"; the n = 3 comparison (which ignored the
fixed Frobenius norm) is deleted; Sanyal-Sottile-Sturmfels Prop. 3.10 is described as the linear
skew-diagonal projection of an orbitope; Mathias 1992 (LMA 31, 57-70) is cited as the closest
subject, `DMD = (dd^T) o M`; the remark states that Tam, LRT and Mathias were read through their
abstracts only and makes no claim about their later sections; the Horn antecedent leads the remark.

## 5. MINOR: verification-code wording

APPLIED. `pga_free`'s docstring states the coordinate convention (factor 4 in upper-triangular
coordinates, 2 under the Frobenius inner product; the direction is normalized); `snap_isometry`'s
docstring no longer calls every partial isometry an extreme point; `worst_shortfall` is clamped at
zero for both searches (the prescribed-spectrum value is now 0.0 rather than -1.08e-18); Section 6
says "not exceeded beyond numerical error" for the prescribed-spectrum search. The script was rerun
after the edits; no result changed beyond the clamp and the source hash.

## 6. CORRECT: definitions agree with Gil, with the normalization correction

APPLIED the fix: Section 1 now states the fixed-real-structure reading of the IRB (the populations
are the eigenvalues of the real part, not in general of rho) and the zero-extension convention for
`M` on inactive axes, beside the first definition of `M`.

## 7. CORRECT: Theorem 3.1's proof

APPLIED the optional addition: the explicit maximizing state (2 x 2 blocks with eigenvalues
`a_{2k-1} + a_{2k}` and 0, trace one, real part A) is written out in the proof.

## 8. CORRECT: Theorem 4.1's layer-cake proof

APPLIED: "one-half the squared Frobenius norm" in the prose after eq. (11); the degree-constraint
sentence of Proposition 4.2 reads `|B| >= 2` with the singleton case noted; the density-matrix
equality case (off-diagonal entries `+- i s_k sqrt(a_{2k-1} a_{2k})`, determinant
`a_{2k-1} a_{2k} (1 - s_k^2) >= 0`) added at the end of the proof.

## 9. CORRECT: the theorems answer the questions as posed

APPLIED the three wording fixes: the abstract lists the odd-dimensional zero singular value and puts
the positivity statement on the support; "the question would be empty" became "fixes the objective;
compatibility with an aligned representative would be a separate feasibility question, which we do
not address".

## 10. CORRECT: Remark 4.5's numbers, with exact certificates

APPLIED. The example now fixes distinct positive populations `a = (0.4, 0.3, 0.2, 0.1)` so that
alignment means matching support; the LP witness (`x_12 = 0.19`, `x_13 = x_24 = 0.81`) and the dual
certificate (`0.6 x` the `C = {1,2}` inequality plus `0.2 x` each of `C = {1,2,3}`, `{1,2,4}`, all with
`B = [4]`) replace the solver statement; the exact real-orbit certificate for 2.196 (the `X, Y`
coordinates, `{||X||^2, ||Y||^2} = {0.9025, 0.0025}`, the bound `2.172 - 0.4 (X_1 - 5 Y_1)^2 + 9.6 Y_1^2`)
replaces the random-search sentence. Both certificates were rederived here before use: the dual
combination's coefficients are exactly `(2, 1.2, 1.2)` on `x_12, x_13, x_24` with nonnegative surplus on
the other three edges and right side 2.324; the orbit bound follows from `X_2^2 <= ||X||^2 - X_1^2`,
`Y_2^2 <= ||Y||^2 - Y_1^2` and completing the square.

## 11. CORRECT: Section 6 reports the searches faithfully

No change beyond item 5; the candid shortfall reporting stays.

## 12. CORRECT: US English, no em dashes

No change.

## Verdict

Accepted in full: Theorem 3.1 proved with the normalization made explicit; Theorem 4.1 proved as a
real and complex skew-matrix inequality, now with two proofs, and reassessed as a consequence of
classical majorization; the density-matrix consequence read on the active support; Corollary 5.1(1)
corrected. The manuscript was also set in the house format of the Hypnos Math manuscripts
(`paper/common/`) in the same pass, with the attribution block recording both reviews.

## Left open, stated in the note

Full-text reading of Tam 1998, Leite-Richa-Tomei 1999 and Mathias 1992 before any stronger novelty
statement; the README carries the item.

## Consistency pass, 2026-10-01 (fresh Claude Opus 5.5 agent, directed by the Claude Fable 5.1 outreach thread)

A bounded consistency pass on `main.tex` (the abstract and Section 1 against the theorems, quotations against Gil's text, citations against their sources, the attribution block against `paper/common/README.md`, and the house language rules), not a third review of the mathematics; "fulltext line N" is a line of `paper/antiunitary-matching/reviews/claude/03-literature/gil-2026-fulltext.txt`, and "PMC HTML" is `paper/antiunitary-matching/reviews/openai/lit-gil-2026-pmc.html` with its MathML alttext extracted to text.

| # | check (1-5) | item checked | source and page | command or method | finding | verdict | what was done |
|---|---|---|---|---|---|---|---|
| 1 | 1 | Abstract: what Gil asked ("whether this remains true over all orientations of the Youla frame, with free and with prescribed Youla values") | Gil Section 3.4 (fulltext line 231) and Section 8.2 (line 701); the note's Section 1 | grep of the full text; read against Section 1's mapping of (i) and (iii) | Gil's problem (i) asks to determine the global maximum for fixed Youla values, not whether adjacent pairing stays optimal; Section 1 maps prescribed values to (i) and free values to Section 3.4 and (iii) | CORRECT, applied | The abstract now says Gil asked whether this remains true over all orientations of the Youla frame with free Youla values, and what the maximum over all orientations is when the Youla values are prescribed |
| 2 | 1 | Abstract: "every pairwise coherence functional with nonnegative weights is maximized in the aligned class" | Theorem 3.1, eq. (8) and the zero-population clause; Corollary 5.1(1) | hypotheses read side by side | Carries "with free Youla values"; aligned attainment holds for every population vector by Corollary 5.1(1) (a maximum-weight matching on the support), so this claim needs no positivity hypothesis; the positivity-dependent statements (value equal to the unrestricted matching weight, hull equal to the full polytope) are not made in the abstract | NO FINDING | none |
| 3 | 1 | Abstract: "Gil's adjacent-pairing value is the global maximum" | Theorem 3.1, eq. (7) | read | Matches: populations summing to 1, every orientation, every admissible Youla spectrum | NO FINDING | none |
| 4 | 1 | Abstract: mechanism sentence (odd-order principal blocks singular, positivity equal to the contraction condition on the support, squared cohesion a nonnegative linear functional) | Lemma 2.1 and its proof; eqs. (3) to (5) | read | Matches; the abstract's "real antisymmetric contraction" is a special case of the lemma's real-or-complex statement | NO FINDING | none |
| 5 | 1 | Abstract: the entries in the prescribed-values inequality | Theorem 4.1, eq. (9) | read; numpy spot check over 1,200 random complex unitary orientations, n = 2 to 7 (largest excess 4.4e-16 with moduli squared) | The abstract wrote the plain square of M_ij "for every skew-symmetric M"; the theorem covers real and complex M with the modulus squared, and the plain square is not real for complex M | CORRECT, applied | The abstract's M_ij^2 became the modulus squared, as in eq. (9) |
| 6 | 1 | Abstract: hypotheses on the singular values of M and on s and a | Theorem 4.1, statement | read | Matches case for case: s_1, s_1, ..., s_m, s_m and 0 when n is odd; s sorted; a sorted and nonnegative; no s_1 <= 1 in the matrix inequality (the density-matrix reading adds it); m is fixed by the count of n singular values | NO FINDING | none |
| 7 | 1 | Abstract: "the sharp inequality" | Theorem 4.1 ("with equality for Q = I"); the proof's last paragraph and its density-matrix equality case | read | Equality is proved for every admissible a and s at the Youla block form, and is realized by a state when s_1 <= 1 | NO FINDING | none |
| 8 | 1 | Abstract: labels of the two proofs of Theorem 4.1 | the "Proof" (layer cake) and the "Second proof, from a classical singular-value inequality" (Horn) | read | The abstract called the layer-cake proof "a second proof", while the body heads the Horn derivation "Second proof" | CORRECT, applied | "a second proof, by a layer-cake decomposition" became "another proof, by a layer-cake decomposition" |
| 9 | 1 | Abstract: the family "contains the degree and odd-set constraints as its two extreme members" | Proposition 4.2 | read; R(1, q) = s_1^2 for q >= 2 and R(q, q) = twice the sum of s_k^2 over k <= floor(q/2) rederived from eq. (12) | The two extreme members are the spectral degree constraint (bound s_1^2) and the set constraint, under the body's own names, and they reduce to Edmonds' constraints at s = 1 | NO FINDING | none |
| 10 | 1 | Abstract: the n = 4 example of a non-aligned maximum | Remark 4.5 | recomputed in numpy | Singular values 1, 1, 0.9, 0.9; value 2.196; best aligned value 2.172 (matching {13, 24}); the abstract's claim is supported | NO FINDING | none |
| 11 | 1 | Section 1: "iM is Hermitian with eigenvalues plus or minus s_k" | Theorem 4.1 and the abstract, which list the zero singular value for odd n | read | The zero eigenvalue for odd n was omitted (the positivity conclusion is unaffected) | CORRECT, applied | "(and 0 when n is odd)" added |
| 12 | 1 | Section 1: Theorem 1.1, the restatement of Gil's Theorem 2 | Gil Section 3.4, Theorem 2, eqs. (23) and (24) (PMC HTML) | MathML alttext extraction | Matches, including "s_k = 1 on every pair of positive population product" | NO FINDING | none |
| 13 | 1 | Section 1: "We determine the maximum asked for in (i) (Theorem 4.1) and answer (iii) affirmatively (Theorem 3.1)", and the trace remark on fixed spectra | Theorems 3.1 and 4.1; eq. (1) | read; tr(rho^2) = sum of a_i^2 plus the squared Frobenius norm of N rederived (N real antisymmetric with zero diagonal) | Matches | NO FINDING | none |
| 14 | 1 | Lemma 2.1 "taken from the companion manuscript" | `paper/antiunitary-matching/main.tex` line 161, Lemma "Squared-entry convex hull" | grep | Present in the companion | NO FINDING | none |
| 15 | 2 | Quotation "Whether the same maximum is globally optimal over arbitrary Youla orientations is a separate optimization problem and is not assumed here" | Gil Section 3.4, fulltext line 231 | grep -n "globally optimal" | Verbatim; section correct | NO FINDING | none |
| 16 | 2 | Quotation "deliberately left open because they require optimization over Grassmannian orbits rather than the elementary matching argument used here" | Gil Section 8.2, fulltext line 701 | grep -n "deliberately" | Verbatim; section correct | NO FINDING | none |
| 17 | 2 | Quotation "suitable spectral constraints" | Gil Section 8.2, fulltext line 701 | grep -n "suitable spectral" | Verbatim | NO FINDING | none |
| 18 | 2 | Unquoted paraphrases of problems (i), (ii) and (iii) | Gil Section 8.2 (PMC HTML) | MathML alttext extraction | (i) matches word for word; (ii) is Gil's "image of the map (a, Q_M) to G(a, Q_M) subject to Plücker constraints", fairly paraphrased; (iii) differs only in "decide" for "identify" | NO FINDING | none |
| 19 | 2 | Gil's terms used without quotation marks: intrinsic reference basis, metaspin tensor, cohesion, density matrix, aligned class | Gil Section 2.1 (fulltext line 59) and eq. (3); eq. (7) and Section 2.3 (line 91); Section 2.4 (line 129: the cohesion of the antisymmetric block is the Frobenius norm of N) and Theorem 3 ("cohesion squared"); Definition 1 | grep for each term over the extracted text | All match the note's usage, including the zero extension of M on inactive axes | NO FINDING | none |
| 20 | 2 | Tam, Leite-Richa-Tomei and Mathias: anything quoted from their abstracts | OpenAlex abstracts (Tam in full, Mathias truncated, Leite-Richa-Tomei absent and publisher-elided on Semantic Scholar too) | OpenAlex and Semantic Scholar APIs | Nothing is quoted; the Tam paraphrase (entries on one fixed matching under unitary congruence, weakly majorized by the singular values, one extra inequality in the even full-matching case) matches his abstract; the Mathias paraphrase matches his title; the attribution of the skew-symmetric Schur-Horn theorem to Leite-Richa-Tomei is confirmed by Sanyal-Sottile-Sturmfels citing it as their [22]. Semantic Scholar lists the Leite-Richa-Tomei DOI as bronze open access; not opened, per the instruction | NO FINDING | none; the abstracts-only disclosure is unchanged |
| 21 | 3 | Gil citations: eqs. (3), (7), (8), (20), (26), (27), (33); Definition 1; Theorem 2; Sections 2.1, 2.3, 3.4, 8.2 | Gil full text (fulltext lines 59, 91, 223, 227, 231, 701) and PMC HTML | grep for each equation tag and heading | Every one resolves to the content the note attributes to it | NO FINDING | none |
| 22 | 3 | Gil's problem numbering (i) to (iii) | Gil Section 8.2 ("One is ... Another is ... A third is ...") and Section 8.3 | read | Unnumbered in Gil, as the note says; Section 8.3 ("Open Questions") lists three different, also unnumbered, directions; the note numbers the Section 8.2 problems itself and says so | NO FINDING | none |
| 23 | 3 | Sanyal-Sottile-Sturmfels Prop. 3.10 | arXiv:0911.5436v4 (8 Mar 2011), p. 14 | pdftotext; the first-page stamp shows v4 | Prop. 3.10 is "The skew-symmetric Schur-Horn theorem [22]", stated for the linear skew-diagonal map SD; their [22] is Leite-Richa-Tomei, LAA 286 (1999) 149-173 | NO FINDING | none |
| 24 | 3 | Horn 1950, the product inequality for singular values | PNAS 36(7) (1950) 374-375 | curl: PNAS answers 403, PMC and Europe PMC answer with bot challenges (not bypassed); Crossref and the Europe PMC REST API for the metadata | Bibliographic data confirmed; the text could not be retrieved; Astra's review (its item 1) records checking both original pages | NOT CHECKABLE | none |
| 25 | 3 | Fan 1949, the maximum principle | PNAS 35(11) (1949) 652-655 | as in row 24 | Bibliographic data confirmed; the text could not be retrieved | NOT CHECKABLE | none |
| 26 | 3 | Youla 1961, "the complex case under unitary congruence" | Canad. J. Math. 13 (1961) 694-704, Cambridge Core PDF, p. 694 eq. (2) and p. 701 Corollary 2 | curl; pdftotext | A complex skew-symmetric C satisfies U'CU = E_1 + ... + E_k + 0 with 2 x 2 blocks of off-diagonal entries a_r and -a_r, a_r > 0; matches | NO FINDING | none |
| 27 | 3 | Edmonds 1965, the polytope of eq. (2) | J. Res. Nat. Bur. Standards 69B (1965), NIST PDF pp. 125-126 | curl; pdftotext | Inequalities (1) to (3) and Theorem (P) match eq. (2) (the note's singleton odd sets add only 0 <= 0) | NO FINDING | none |
| 28 | 3 | Horn and Johnson, Topics in Matrix Analysis, Thm. 3.1.2 and Cor. 3.1.3 | Cambridge Core table of contents | curl | Chapter 3 is "Singular value inequalities" (pp. 134-238), consistent; theorem numbers are not shown | NOT CHECKABLE | none |
| 29 | 3 | Horn and Johnson, Matrix Analysis, 2nd ed., Section 2.5 (the real normal form) | Cambridge table of contents | curl | Chapter 2 is "Unitary similarity and unitary equivalence" (pp. 83-162), consistent; section numbers are not shown | NOT CHECKABLE | none |
| 30 | 3 | Bhatia, Matrix Analysis, Chapter III, for Ky Fan's maximum principle | Springer table of contents | curl | Chapter III is "Variational Principles for Eigenvalues", consistent at the chapter level the note cites | NO FINDING | none |
| 31 | 3 | Bibliographic data of the ten DOIs | Crossref API | scripted query | Titles, volumes, issues and pages match the bibliography | NO FINDING | none |
| 32 | 3, 4 | The companion entry (cite key ross) | the companion's title block (`paper/antiunitary-matching/main.tex` lines 12-15); the set's convention in `paper/unfolded-zeros/main.tex` line 391 | grep | It named "D. Ross" as the author of an "AI-assisted research manuscript ... (in preparation)"; the companion was written by GPT-6 Astra at the direction of David Ross and is dated September 28, 2026, and the set cites its own papers as MODEL, at the direction of D. Ross, TITLE, manuscript (MONTH YEAR), Hypnos Math, URL | CORRECT, applied | The entry now reads "GPT-6 Astra, at the direction of D. Ross, Approximate antiunitary symmetry as a matching problem, manuscript (September 2026), Hypnos Math, https://hypnosmath.org" |
| 33 | 4 | Writer, director and the division of labor | `paper/common/README.md`, pattern items 1 and 2 | read | Matches the pattern; the source of the questions (Gil's paper, found while reviewing the companion) is stated | NO FINDING | none |
| 34 | 4 | The self-review, named with its verdict in one clause | `self-review/REPORT.md` lines 9 and 15-23 | read | "Claude Opus 5.5, 2026-09-29 ... found the proofs complete and three framing defects" matches the report (proofs complete, no BLOCKING item, three MAJOR framing items) | NO FINDING | none |
| 35 | 4 | The Astra review, named with its verdict in one clause | `reviews/astra/REVIEW.md` items 1 and 2 and the verdict (line 278) | read | "no blocking defect and two major items" matches; but "now given as its first proof" was false: the Horn derivation is headed "Second proof" and follows the layer-cake proof, as item 1 of this ledger records | CORRECT, applied | "now given as its first proof" became "now given as its second proof" |
| 36 | 4 | "No human mathematician has reviewed this paper." | README pattern item 4 | grep | Present verbatim | NO FINDING | none |
| 37 | 4 | Place in the set; no paper called "the first" | README table; the sibling sentences in `paper/antiunitary-matching/main.tex` and `paper/unfolded-zeros/main.tex` | grep | The last of the three of the night of 2026-09-28/29, after Astra's paper and the Riesz-basis paper, written without reading the latter; consistent with both siblings; no paper is called the first | NO FINDING | none |
| 38 | 5 | Em dashes | `main.tex` | Python count of U+2014 and of "---" | 0 and 0; the file has no non-ASCII character | NO FINDING | none |
| 39 | 5 | US English | `main.tex` | regex scan for -our, -tre, -ise, -yse, doubled -ll- and similar British forms | None (the only hits were pairwise, termwise and pointwise) | NO FINDING | none |
| 40 | 5 | A Clay Mathematics Institute (A)/(B) statement | `main.tex` | grep for Clay, Millennium, (A), (B) | None | NO FINDING | none |
| 41 | 5 | Claims beyond the theorems | the abstract, Section 1, Remark 4.4 | read | Every claim maps to Lemma 2.1, Theorem 3.1, Theorem 4.1, Proposition 4.2 or Remark 4.5; "its use for density matrices is new here" is relative to the companion; Remark 4.4 limits the claim to the application, the polyhedral viewpoint and the family | NO FINDING | none |

Build: `bash build.sh` (tectonic) succeeded after the edits; `main.pdf` has 9 pages, as before; no new warning (only the two existing package notices, on the relative style path and on inputenc) and no Overfull or Underfull box.
