# Disposition of the self-review of the Gil note

Review: `self-review/REPORT.md` (fresh Claude Opus agent, 2026-09-29 ~13:45 EDT, independent of
the authoring thread's audit files and of the OpenAI review directory). Applied by Claude
(Fable 5.1) on 2026-09-29, 14:20 to 14:50 EDT, to `main.tex`, `verify_gil.py` and `README.md`.
Theorems 3.1 and 4.1 were found proved; nothing in the mathematics changed. Item numbers are the
report's. Remark numbers in "Now" refer to the rebuilt manuscript, in which the new Remark 4.5
(the counterexample) follows the old Remarks 4.3 and 4.4, whose numbers are unchanged.

## MAJOR

1. **Abstract's aligned-extremality claim false with prescribed Youla values.** APPLIED. The
   sentence now reads "with free Youla values, every pairwise coherence functional with
   nonnegative weights is maximized in the aligned class" and stands before the prescribed-value
   sentence; the abstract ends by saying the product form of the weights is essential and that
   an n = 4 example shows a non-aligned maximum. The example (s = (1, 0.9), b_12 = 2,
   b_13 = b_24 = 1.2, M with entries 0.3, sqrt(0.84), -sqrt(0.84), 0.2) is Remark 4.5, with its
   singular values (1, 1, 0.9, 0.9), value 2.196, best aligned value 2.172 (matching {13, 24}),
   LP value 2.324, and a random search over O(4) finding nothing above 2.196; every number was
   recomputed independently before it went in. "What is not settled" now says the maximizer need
   not be aligned and the LP need not be tight for general weights, value open.
2. **Tam 1998 claim made without the full text.** APPLIED as the report specified: Remark 4.4 now
   says the skew-symmetric Schur-Horn theorem (Leite, Richa and Tomei 1999; Sanyal, Sottile and
   Sturmfels Prop. 3.10) and Tam's main theorem describe the entries on one fixed matching (weak
   majorization of the skew-diagonal moduli by the Youla values, with Tam's parity inequality)
   and do not imply (9), with the n = 3 comparison, and that no earlier statement of (9) was
   found; it states that Tam's paper was available only through its abstract. Leite, Richa and
   Tomei added to the bibliography with DOI. README's "before submission" item kept and sharpened.
3. **Section 6 misreported check A.** APPLIED. `verify_gil.py` check A now uses projected
   gradient ascent over the contraction ball (Euclidean projection = singular values clipped at
   1, 20 starts x 4000 normalized steps, a final snap of the singular values to 1) and records
   the maximum AND the minimum over instances of (best - bound), the worst shortfall, and the
   counts of instances within 1e-6 and 1e-4; check B records its minimum too. The run of
   2026-09-29 14:18 EDT: check A never exceeded the bound (5.6e-16), came within 1e-6 in 19 of
   30 instances and within 1e-4 in all 30, worst shortfall 7.2e-5 at n = 7; check B reached its
   value within 1e-6 in all 30. Section 6 quotes those recorded values and no longer says the
   bound was attained where it was not.

## MINOR

4. "cohesion" vs "squared cohesion": APPLIED throughout (abstract, Section 1, both theorems'
   proofs, Corollary 5.1(3), Section 6); Section 1 says Gil calls ||N||_F the cohesion and cites
   his eqs. (20) and (33) for the formula.
5. Aligned class per Gil's Definition 1: APPLIED ("in some admissible IRB representative").
6. Problem numbering and "affirmatively": APPLIED ("unnumbered there, and we number them (i) to
   (iii)"; "we determine the maximum asked for in (i) and answer (iii) affirmatively"; the
   reading of "suitable spectral constraints" as Youla-value constraints stated, with the
   tr rho^2 reason).
7. Eq. (8) and the hull claim with zero populations: APPLIED (Theorem 3.1 states (8) and the hull
   claim for positive populations, and on the support of A otherwise; the proof carries the
   a = (1/2, 1/2, 0, 0), b_12 = 1, b_34 = 10 example; Corollary 5.1(2) says "for positive
   populations").
8. Symbol clash M: APPLIED (matchings are mu, incidence vectors 1_mu; the reservation of M for
   the metaspin tensor stated).
9. Exchange argument: APPLIED (complete to a matching of maximal size; for odd n move the unpaired
   vertex to n; each uncrossing lowers sum |i - j| by 2(k - j) > 0, so the process stops at the
   adjacent pairing, the only perfect matching of {1, ..., 2m} without a crossing or nested pair).
10. Density-matrix reading of Theorem 4.1: APPLIED (s_1 <= 1 in the statement; the support
    condition, at most floor(r/2) positive s_k when r populations are positive; positive
    populations realize every orientation with s_1 <= 1).
11. "Theorem 3.1 is the special case s = 1": APPLIED (Theorem 4.1 recovers (7) through
    monotonicity of the right side in every s_k; it does not recover (8) or the hull statement,
    and Remark 4.5 shows it cannot).
12. Remark 4.3's units and inference: APPLIED with the script's own numbers rather than the
    referee's scratch runs. The remark quotes the excess of the C = B linear program in both
    units (the LP's own and ||N||_F^2), says that the degree constraints added to C = B still
    fail in the recorded instances, and states the prefix result (the n(n+1)/2 prefix
    inequalities alone reproduce the value); `verify_gil.py` check C now computes all four
    families (full, C = B, C = B plus degree, prefix) and `verification-gil.json` carries them:
    full and prefix agree with the theorem to 5.6e-17; C = B alone exceeds by up to 0.0097 in
    the LP's units (0.019 in ||N||_F^2); C = B plus degree still exceeds in 4 of 30 instances,
    by up to 2.2e-4 (4.4e-4 in ||N||_F^2). The random instances differ from the first run's
    because the ascent consumes the seeded stream differently, which is why the C = B excess is
    no longer the 0.0126 of the original JSON.
13. Corollary 5.1(3) equality condition: APPLIED (||M_{[p],[q]}||_F^2 = R(p, q) for every p <= q
    with a_p > a_{p+1} and a_q > a_{q+1}, a_{n+1} = 0; whether this forces alignment not examined).
14. "Since s is sorted decreasingly" misplaced: APPLIED (moved to the interlacing step, t_k <= s_k).
15. Script wording, SO(n) vs O(n), theorem numbering in the docstring: APPLIED (docstring uses
    3.1 / 4.1 / 4.2 / Lemma 2.1; Section 6 says "floating-point checks" for the odd-set
    inequalities and that the SO(n) search covers O(n) up to a coordinate sign flip, which
    preserves squared entries).
16. Bibliography: APPLIED (DOIs and issue numbers for Youla, Fan, Sanyal-Sottile-Sturmfels, Tam,
    Horn-Johnson Topics; Horn and Johnson, Matrix Analysis, 2nd ed., cited for the real normal
    form under orthogonal congruence beside Youla; Leite-Richa-Tomei added).
17. Typography: APPLIED (the two exchange inequalities set in align*, no overfull box in the
    rebuilt log; `Pl\"ucker`).
18. Title: APPLIED ("... Answered by a Matching Polytope and a Layer-Cake Inequality").

## CORRECT items C1 to C5

No change required. C5's byte-identical reproduction refers to the previous script; the script
is now a new file with a new `source_sha256`, and its `verification-gil.json` and
`verify_gil.stdout.txt` were regenerated by one run on the laptop (Python 3.12.10, numpy 2.2.6,
scipy 1.16.3).

## Not changed

- Authorship, the research attribution paragraph, the location of the note inside
  `reviews/claude/` (the owner's call), and the date line.
