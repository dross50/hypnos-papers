# Adversarial self-review (Claude side) of "A dividing-plane barrier in the OpenAI forced Navier-Stokes blow-up construction"

Reviewer: a fresh Claude Fable 5.1 session (the same model line as the writer), started on
2026-10-01 at 20:28 EDT (America/New_York), report written at 20:48 EDT. Baseline reviewed: the
paper as committed at 5c03173 (repository HEAD 823d27a; `main.tex` 297 lines, `main.pdf` 12 pages).
Read, in this order and nothing else before writing: `paper/ns-dividing-plane/main.tex` and
`main.pdf` (every page rendered and looked at); the OpenAI manuscript at the cited URL, sha256
verified equal to `0e779481...8ae228f`, 166 pages, printed page = PDF page, pp. 4-6, 24-28, 30-37,
74, 126-128, 138, 141, 144-151; Duraiswami arXiv:2609.17642v1 pp. 1-2 and 20-22 (plus a grep of the
whole text for the symmetric core, the dividing plane, Rayleigh and Ludwieg); Lei and Ren
arXiv:2609.35406v2 Section 2.5 (p. 16) and pp. 107-109; Constantin, Ignatova and Vicol
arXiv:2609.20803v2 p. 11; the house pattern `paper/common/README.md` and the precedent
`paper/unfolded-zeros/reviews/claude/REPORT.md`. The research record under
`docs/research/2026-10-01-ns-open-map/` and everything under `reviews/` were NOT read. The checker
and the two pytest arenas were run before this report (53 of 53 Boolean flags true, 5 + 3 tests
pass, 1.1 CPU seconds); the checker's run rewrote the record's `checks/midplane_barrier.json`
timestamp, which I restored with `git checkout` so that the record is untouched. Every displayed
formula in Sections 2 to 4 was rederived by hand from the manuscript's Lemma 4.1, (4.7), (4.8),
(4.9) and (4.16); one abstract-level inequality was tested with an independent integrator (scipy
LSODA on the paper's (17), rtol 1e-12). Duration: about 20 minutes of reading and checking, then
this write-up.

---

I found 0 BLOCKING errors. Lemma 3.1, Theorem 3.2, Proposition 4.1, Lemma 4.2 (on the range its
proof covers) and Proposition 4.3 are correct, and every cited formula and page is what the
manuscript says. Three issues are MAJOR: a false inequality in the abstract, a lemma stated on a
larger radial range than its proof covers, and a missing credit to Duraiswami for the physical
reading the abstract and Remark 3.6 present as the paper's own.

## MAJOR

1. **The abstract states the margin without its case condition, and the unqualified inequality is
   false for 1 < B < 1 + h (abstract; Section 1, paragraph 3).**
   - What: the abstract says "with the quantitative margin 2 - a >= 2h/(B - 1) in terms of the
     anisotropy exponent h and the running supremum B of the radially averaged axial strain".
     Theorem 3.2(3) asserts this only when B > 1 + h, and asserts a <= 0 otherwise. For
     1 < B < 1 + h the number 2h/(B - 1) exceeds 2, and the inequality is the reverse of the truth:
     for a constant strain w = B the value a_* = 2 - 2h/(B - 1) < 0 is a barrier from below (at
     a = a_* the paper's (17) gives D_X a = -(1 - a_*/2) a_* > 0), so a > 2 - 2h/(B - 1) at every X,
     by the paper's own first-crossing argument run downward. Independent integration of (17):
     h = 0.1, w = 1.05 gives a in [-0.400, 0] on (0, 20], so 2 - a <= 2.4 < 4 = 2h/(B - 1)
     everywhere; h = 0.01, w = 1.005 gives 2 - a <= 2.049 < 4; h = 0.1, w = 1.02 gives
     2 - a <= 2.672 < 10. Theorem 3.2(3)'s own statement (a <= 0) holds in each case. At B <= 1
     the formula is negative or undefined.
   - Why it matters: the abstract is the sentence that will be quoted, and it contradicts the
     theorem it summarizes on a range of strains. Section 1 states the same formula followed by
     "(and a <= 0 when B <= 1 + h)", which reads as two cases but leaves the formula itself
     unconditioned.
   - Fix: abstract: "with the quantitative margin 2 - a >= 2h/(B - 1) whenever the running supremum
     B of the radially averaged axial strain exceeds 1 + h, and a <= 0 otherwise". Section 1: "with
     2 - a >= 2h/(B - 1) when B > 1 + h, where B is the running supremum ..., and a <= 0 when
     B <= 1 + h". Remark 3.5's "the margin (15) is proportional to h" is the B > 1 + h branch; say
     so there too.

2. **Lemma 4.2 claims its conclusions for X >= X_v; its hypothesis and its proof hold for X >= X_b
   (Section 4).**
   - What: the statement reads "Then for X >= X_v the exterior axial residual S_n vanishes, X N_s is
     constant in X, and that constant is K(eta)". The proof uses "a pressure independent of z" and
     the heat form E = c_inf X^{-A} H(2d/X); both hold for X >= X_b only. On [X_v, X_b) one has
     U = V_0 = 0 but E is the annulus profile with its eta-dependence, and the canonical pressure
     Pi(X, eta) = -int_X^inf E^2/(2x) dx integrates across that part of the annulus, so in general
     d_z p != 0 there, S_n = -d Pi_eta + 4 A eta Pi + 2 eta D_X Pi = -L q^{2A+D} d_z p != 0, and
     X N_s is not constant on [X_v, X_b). The lemma's own hypothesis clause, "normalized to vanish
     at infinity and hence a function of (r, t) alone", is likewise true only for X >= X_b. The
     sentence above the lemma ("X N_s is constant there") is right, because "there" is the
     exterior, which Section 2.3 defines as X >= X_b.
   - Why it matters: a stated lemma is false on part of its stated range. Nothing downstream uses
     that range: Proposition 4.3 uses only the limit X -> inf (K = 0 from sqrt(X) T_{0,z} -> 0) and
     the equation V_0 = 0 on [X_v, inf) from (4), which needs only U = 0 there.
   - Fix: "for X >= X_b" in the statement; begin the proof "For X >= X_b, u_r = u_z = 0 and the
     pressure is independent of z, so ...". Keep "U = V_0 = 0 on [X_v, inf)" where Proposition 4.3
     uses it.

3. **The Rayleigh and Ludwieg reading of the cone, and the role of the curve D eta + d U = 0, are
   presented as the paper's own physical reading; both are in Duraiswami and must be credited
   (abstract; Section 1, paragraph 4; Remarks 3.3 and 3.6; Section 6).**
   - What: the abstract says "so the dividing plane has the sign of Rayleigh's centrifugal
     criterion that forbids growth, with Ludwieg's axial-shear term inactive", and Remark 3.6 cites
     Rayleigh, Ludwieg, Leibovich and Stewartson and the manuscript's p. 6 for it, but not
     Duraiswami, who writes on p. 21: "With circulation Gamma = r u_theta, the profile variables
     give d log Gamma / d log X = 1 - a/2, so a > 2 is Rayleigh's criterion for centrifugal
     instability, circulation decreasing outward, and v_s = a(1 + t_s^2) > 2 in Theorem 4.6(iii) of
     OpenAI 2026 is its form with the axial shear included, Ludwieg's criterion for a swirling flow
     with axial shear"; on p. 22 "the Ludwieg condition of the cone is the condition that the pulses
     can grow at all" (with the same growth-rate formula 2a(1 - 2/v_s) evaluated on his profiles);
     and on p. 25 "The cone condition of OpenAI 2026 is Rayleigh's criterion with axial shear". He
     also identifies, on p. 6, the curve D eta + d U = 0 (the paper's H_c = 0) as the curve the
     characteristics of the eta-transport emanate from, and writes "The sign of the axial profile
     U(X, 0) on the dividing plane decides which way information leaves it". The paper's Section 1
     ("the transport coefficient H_c = D eta + d U ... vanishes on that plane exactly when U does")
     and Remark 3.3 present this without the credit.
   - Why it matters: the house bar is credit before "new", and the attribution block already
     records one such miss against the same paper (the moment identity). The barrier theorem, its
     proof and its margin remain the paper's; the reading of a and v_s as Rayleigh's and Ludwieg's
     criteria in these variables, and the characteristic role of D eta + d U = 0 set by the sign of
     U(X, 0), are Duraiswami's.
   - Fix: in Remark 3.6, at the Rayleigh and Ludwieg sentence, add "as Duraiswami reads the cone
     [Duraiswami, p. 21]"; in Section 1's "Two features" paragraph or Remark 3.3, add that
     Duraiswami identifies D eta + d U = 0 as the dividing characteristic, its side set by the sign
     of U(X, 0) [p. 6]; in Section 6 add both to the sentence on what Duraiswami has. The abstract
     needs no change once the text carries the credit.

## MINOR

4. **Theorem 3.2(3), the definition of X_0 (proof, Section 3).** X_0 = sup{X < X_1 : a(X) <= a_*}
   "exists because a(0+) = 0 <= a_*" is not enough: when a_* = 0 and a > 0 on all of (0, X_1), the
   set is empty (this is the generic case for small X, since a ~ (w(0) - 1 - h) X / 2 near the
   axis). The argument is right once X_0 is the left endpoint of the maximal interval ending at
   X_1 on which a > a_*, with X_0 = 0 allowed. Fix: "Let (X_0, X_1] be the maximal interval ending
   at X_1 on which a > a_*; then either X_0 > 0 with a(X_0) = a_* by continuity, or X_0 = 0, which
   forces a_* = 0 since a(0+) = 0."

5. **Theorem 3.2(3), a strict inequality that is not always strict (proof, Section 3).** In the
   case 1 <= B <= 1 + h the text has "(w - 1)(1 - a/2) < B - 1 <= h". When B = 1 and w = 1 at the
   point, both sides are 0. The conclusion D_X a < 0 survives because -(1 - a/2) a < 0, as the
   parenthetical says. Fix: write "<=" there.

6. **Theorem 3.2(4), the Proposition 4.10(ii) clause (statement).** "it violates the inner-edge
   inequality v_s(X_a, eta) > 2 + c_ex of Proposition 4.10(ii) at eta = 0" is imprecise when
   a(X_a, 0) <= 0: then v_s is undefined there and the clause of Proposition 4.10(ii) that fails is
   a(X_a, eta) > 0. Fix: "it violates Proposition 4.10(ii) at eta = 0, through its requirement
   a(X_a, eta) > 0 if a(X_a, 0) <= 0 and through v_s(X_a, eta) > 2 + c_ex if a(X_a, 0) > 0".

7. **Theorem 3.2(4) cites the wrong clause for Lemma 3.1's hypotheses (statement and proof).**
   "Under Theorem 4.6(ii) the profile is stress-free on [0, X_a], so Lemma 3.1 ... applies": the
   smoothness of (phi, U, Pi) and phi > 0 that Lemma 3.1 also needs are Theorem 4.6(i), not (ii).
   Fix: "satisfies Theorem 4.6(i), (ii) and (13)" in the statement, and cite (i) in the proof.

8. **Lemma 3.1, an unneeded clause in the proof (Section 3).** "and using (13) on the whole segment
   the average runs over" is not what makes W(X, 0) = 1 - w(X): the term 2 D eta A_X(U) vanishes
   at eta = 0 through its factor eta for any U, and d_eta A_X(U)(X, 0) = A_X(U_eta)(X, 0) is the
   definition of w. Hypothesis (13) enters Lemma 3.1 only through H_c(X, 0) = U(X, 0) = 0 (and
   Theorem 3.2(2) through D_X U(X, 0) = 0). Fix: delete the clause.

9. **Abstract, "a nonnegative zeroth-order coefficient".** In the second form of (14), as displayed,
   the coefficient of H is -hX/2 <= 0. What the maximum principle needs, and what the proof uses,
   is the nonnegative source hH on the right of the first form. Fix: "satisfies a linear
   second-order equation whose zeroth-order term has the sign that forbids an interior maximum".

10. **Abstract, "no energy source at the inner edge of the annulus".** The theorem concerns the
    point (X_a, 0); at other eta the inner edge may well have v_s > 2. Fix: "at the dividing-plane
    point of the inner edge of the annulus".

11. **Remark 3.5, "the margin near the axis is 2h/3 < 1/150".** Near the axis a -> 0, so the margin
    2 - a is close to 2; it is the bound 2h/(B - 1) of (15) that equals 2h/3 for B = 4. Fix: "the
    bound (15) on the margin is 2h/3 < 1/150 for the axis strain 4".

12. **Section 4, the Duraiswami quotation is not verbatim.** The paper quotes "the construction
    therefore carries axial velocity on the dividing plane: the core is an axial through-flow"
    [p. 20]. The source reads "The leading profile of the OpenAI 2026 construction therefore
    carries axial velocity on the dividing plane: the core is an axial through-flow". Fix: quote
    the sentence as written or mark the elision.

13. **Section 6, "assert no uniform limit as j -> 0".** Lei and Ren write (p. 108) "no uniform
    limit as j -> 0 is asserted", that is, they do not assert one; the paper's phrase can be read as
    their asserting non-uniformity. Fix: "and do not assert a uniform limit as j -> 0". While there:
    their p. 109 sentence "If the shift were zero, the zero of H_0 would be Z = 0, where evenness of
    P_0 would give g(0) = 0; the two shear mechanisms would then weaken at the same point" is the
    closest statement in their paper to the barrier (a linear-model observation, not a theorem) and
    is worth quoting in Section 1 or 6 as the concrete receipt behind "use the barrier as a design
    rationale".

14. **Section 1, "that the construction's critics have asked about".** No source is given, and the
    sources cited ask about j -> 0 (Lei and Ren), not h -> 0. Fix: drop the clause, or cite who
    asked.

15. **Section 1, "and nothing about the Clay alternatives".** The house rule for this paper is no
    statement about Clay (A) or (B) anywhere in the text; the disclaimer is itself a Clay mention,
    and "nothing about the unforced problem" in the same sentence already covers it. Fix: delete
    the clause.

16. **Section 2.2, "two inequalities on p_s".** The two inequalities of the manuscript's (4.21) are
    P_c > 2 and v_s < U(P_c, J_c), stated in the shear frame and involving v_s and t_s as well as
    p_s. Fix: "two inequalities, (4.21), on the cone coordinates (P_c, J_c, v_s)".

17. **Bibliography.** Lei and Ren's arXiv title reads "Part I: Construction ..." (colon); the paper
    has "Part I. Construction". Match the source. The other three arXiv entries, the OpenAI entry
    (166 pp., sha256) and the four classical references check out.

18. **`paper/common/README.md`, the set table and the writer line.** The table lists four papers and
    does not carry this one; the title-block bullet says "Claude Fable 5.1 for two of the
    mathematics papers". Fix: add the row (October 1, 2026, Claude Fable 5.1,
    `paper/ns-dividing-plane/`) and make it three.

19. **Remark 3.4, where j_0 > 0 enters the manuscript's existence proof (optional sharpening).** The
    remark rightly does not claim an analytic symmetric solution. One sentence would locate the
    gap: Proposition B.2's contraction (pp. 146-148) is set up around the datum phi_0 of (B.3),
    which is defined for j_0 = 0 as well; j_0 > 0 is used in Section B.1 for Z(eta_0) > 0 and in
    Proposition B.3's exit alternative (B.19), not visibly in the existence argument. Stated as an
    observation, not a theorem, this says why the paper's hypothesis (13) is the natural one to
    assume directly.

20. **Verification record and the research record, three small things.** (a) Running
    `checks/midplane_barrier.py` writes its JSON to the record path by default with a fresh
    `generated_utc` stamp, so a reviewer's run dirties the committed record (it did here; restored).
    Default the `--json` output outside the record, or drop the stamp. (b) In the case h = 0,
    w = 1 + X/2 the sampled `sup_a` prints as exactly 2.0 while `a_below_2` is true because it is
    computed from the sign of D_X H (min 7.7e-21 > 0), not from the sampled a; Section 5 item 2's
    "a < 2 ... in every case" is right, but say that the sign is read from D_X H, since a reader of
    the JSON will see 2.0. (c) The build leaves `main.aux` and `main.out` untracked in the paper
    directory; `paper/unfolded-zeros/` carries a `.gitignore` for them, and this directory should
    too.

## Checked and correct

- The sha256 of the OpenAI PDF; printed page = PDF page; 166 pages. The p. 5 quotation is verbatim.
  (4.1) p. 24; Lemma 4.1 and (4.2) p. 25; (4.3)-(4.4) p. 25; (4.6)-(4.7) p. 26; (4.8)-(4.10) p. 26;
  (4.11) p. 27; Proposition 4.2 with (4.13)-(4.14) p. 27; (4.15) p. 28; Lemma 4.3 and (4.16) p. 28,
  whose N_s line I rederived from (4.9) by hand: the eta factors D(M - eta M_eta) + 4 h eta S
  - d S_eta + X(4 A eta Pi - d Pi_eta) are the manuscript's, with 1 - A = D and 2A - 2D = 4h;
  (4.20) p. 30; "required by the viscous waves" p. 31 and the r^{-2}, r^{-1} tails p. 30;
  Theorem 4.6 on pp. 32-34 with clauses (ii), (iii), (v) quoted verbatim from p. 33, (4.25) and
  (4.28)-(4.29) on p. 33; Proposition 4.10(ii) verbatim on p. 37; lambda_0^2 = 2 a F_0^2 (1 - 2/v_s)
  displayed just above (7.1) on p. 74; (B.1) with 0 < j_0 <= .05 on p. 144; Proposition B.2 on
  p. 146; (B.21) on p. 149; (B.25) on p. 151; Lemma A.8's identity int r (u_z^2 + p) dr =
  q^{1-2A} int (U^2 - E^2/2) dX on p. 141; l = 1 + X phi_X / phi on p. 26.
- Lemma 3.1: (4.14) rederived from Lemma 4.1 and (4.7) (the h term enters as + h(1 - 2 eta U) H on
  the transport side, from T_{-h}; the W bracket closes through L V_0/X); the viscous identity (12)
  from (r d_r)^2 (H/r) - H/r = 4 D_X (D_X - 1) H / r; the factor 2/X from r^2 = 2 q X; (4.13)_1
  recovered from the balance with H = 2 X phi / C, so the sign convention is the manuscript's; the
  restriction to eta = 0 uses L = d = 1, H_c(X, 0) = U(X, 0) and no parity.
- Theorem 3.2: (1) the first-crossing argument, including the closed endpoint X_a and the h = 0
  uniqueness step; (2); (3) the Riccati form D_X l = l(1 - l - (X/2)(w - 1)) + hX/2 and (17)
  rederived from (14), and (17) agrees with (B.25) with p_1 = a; the three cases of the brace sign
  (with the two wording points above); the barrier at a = 2 as the B = inf case; (4) the
  growth-rate algebra 2 a F_0^2 (1 - 2/a) = 2 F_0^2 (a - 2) and the bound -4 h F_0^2/(B - 1).
- Attempted breaks: the only freedom in (14) is the continuous function w and h >= 0, and the proof
  uses no bound on w; the checker's fifteen cases (constant, decreasing, unbounded, oscillating
  strains) all obey (15), and the constant-strain suprema reproduce with an independent integrator
  (1.99310 at h = 1/100, 1.93103 at h = 1/10, 2 - 5.9e-12 at h = 0 against the paper's 5.6e-12,
  both below the respective bounds); the asymmetric datum breaks (13) at the axis as stated
  (U_0(0) = 1/20, U_1(0) = 451/4000). No profile with a(X, 0) >= 2 on a stress-free core with
  U(X, 0) = 0 exists, by the proof; none was found.
- Remark 3.3's explicit profile phi = 1, U = (1 + h) eta: S_q = 0 checked by hand (W = 1 - (1 + h) L,
  and -W - h(1 - 2(1 + h) eta^2) = 0). The symmetric class {U odd, phi even, Pi even} is invariant
  under (4.13) with (4.7) (W, S_q even; H_c, S_n odd), so Remark 3.4's formal propagation is right.
- Proposition 4.1 is Duraiswami's p. 20 argument and is credited as such; the convergence claims
  hold (compact U, regular axis, E^2 ~ X^{-1-2h}). Lemma 4.2: 4 A eta Pi - d Pi_eta = -eta E^2 is
  Z_{-2A} Pi = 0; the cancellation 4 h eta R - d R_eta - eta X E^2 = 0 I verified from the
  z-independence of the swirl alone (Z_{-A} E = 0 and one integration by parts, no heat formula
  needed), so it is exact for every z-independent exterior swirl; K(eta) as displayed.
  Proposition 4.3: both eta-equations and their one-dimensional solution spaces, the evenness and
  the C^1 remark, the boundedness of S_inf for h > 0, and Remark 4.4's h = 0 degeneracy.
- Constantin, Ignatova and Vicol: Remark 2.6 and footnote 9 are on p. 11 and say what Remark 4.5
  says; "adjacent rather than a chain" is a fair reading. Lei and Ren: the quotation is on p. 108,
  inside the cited pp. 107-109, and (8.9)-(8.10) are on p. 108. Duraiswami: the S(inf, 0) < 0
  argument on p. 20, the cone failing on every matched profile on p. 21, the growth-rate figure on
  p. 22.
- The four arXiv identifiers, titles, authors and versions. The checker (53/53 flags, 1.1 CPU s)
  and the arenas (5 + 3 tests). The numbers in Remark 3.5 and Section 5 (phi_1(0) = -299/400,
  w = 4 + (351/40) X + ..., radius 0.288, a = 0.266 at X = 0.144, 3.9e-12).
- Format: 12 pages; the house title block; the attribution block with the division of labor, the
  provenance, the Astra review in one clause, "No human mathematician has reviewed this paper",
  and the place in the set without calling any paper the first; no em dashes and no British
  spellings in the source; the figure renders and its caption matches the data.

## Literature check (receipt)

Queries run on 2026-10-01 between 20:38 and 20:44 EDT.

- arXiv API, `all:"OpenAI" AND all:"Navier-Stokes"` (40 newest): 2609.35406 (Lei, Ren),
  2609.28591 (Siren Call, an essay), 2609.26790 (Cheskidov, Dai, Palasek, cascade mechanisms),
  2609.24490 (Niemi, Hopf texture), 2609.20803 (Constantin, Ignatova, Vicol), 2609.17642
  (Duraiswami), 2609.13056 (Schorlepp, Rosenhaus, Falkovich, vorticity instanton), 2609.10269 and
  2609.10262 (density of blow-up forces), 2303.12093 (unrelated).
- arXiv API, `abs:"OpenAI" AND abs:blowup`, `abs:"OpenAI" AND abs:blow-up`, `all:"Navier-Stokes"
  AND all:forced AND all:"self-similar" AND all:"blow-up" AND all:similarity AND all:anisotropic`,
  `abs:"reflection symmetry" AND abs:"Navier-Stokes" AND abs:blowup`: subsets of the list above;
  the last returned nothing.
- Abstract pages fetched for 2609.26790, 2609.13056, 2609.24490, 2609.14292 (Liu): none mentions
  the leading profile's symmetry, a dividing plane or midplane, or Rayleigh's criterion; Liu's
  abstract does not mention the OpenAI construction at all.
- Web search (five queries): "OpenAI 'Finite Time Blowup for Navier-Stokes' reflection symmetry
  dividing plane angular momentum monotone symmetric core obstruction"; "OpenAI Navier-Stokes
  blowup construction critique 'Rayleigh' criterion swirl shear a < 2 symmetric profile 'j_0'
  midplane"; "arXiv September 2026 OpenAI Navier-Stokes finite time blowup forced analysis response
  papers symmetric leading profile anisotropy exponent h"; "'OpenAI' Navier-Stokes blowup
  'midplane' OR 'mid-plane' OR 'dividing plane' OR 'symmetric core' leading profile swirl angular
  momentum"; "'Finite Time Blowup for Navier-Stokes' OpenAI Theorem 4.6 stress cone 'v_s' OR
  'vs > 2' symmetric profile cannot satisfy". Hits: the manuscript, Duraiswami, Lei and Ren,
  Constantin, Ignatova and Vicol, press and blog items, and unrelated older preprints.
- Full-text greps of the three cited preprints for "symmetr", "reflection", "dividing plane",
  "midplane", "Rayleigh", "Ludwieg", "shift".

What exists: the manuscript's physical sentence (p. 5); Duraiswami's moment obstruction (p. 20),
his Rayleigh and Ludwieg reading of a > 2 and v_s > 2 with d log Gamma / d log X = 1 - a/2 (p. 21),
his characteristic curve D eta + d U = 0 set by the sign of U(X, 0) (p. 6), and his outer-edge
observation that positive stress needs a < 2 near X_b, where v_s > 2 "must come from t_s" (p. 21);
Lei and Ren's linear-model remark that at zero shift "the two shear mechanisms would then weaken at
the same point" (p. 109). None of these states or proves that the angular momentum along the
dividing plane of a stress-free core with U(X, 0) = 0 is strictly increasing, that a(X, 0) < 2
there for every strain, or the margin 2h/(B - 1). Search silence is not a priority claim; the
paper's own wording, "priority unestablished rather than established", is the right one.

## Verdict

On the bar "proved, new after a literature check with a receipt, wanted":

- Proved: yes. Theorem 3.2 is a correct theorem about the manuscript's equation (4.13)_1 restricted
  to the dividing plane under U(X, 0) = 0, with the manuscript's displayed formulas as the only
  input, and its consequence for Theorem 4.6(iii) and Proposition 4.10(ii) at the point (X_a, 0)
  is exactly stated. Proposition 4.1 is Duraiswami's and is credited. Proposition 4.3 is correct.
  Lemma 4.2 is correct on X >= X_b and must be restated so (item 2). The abstract's margin sentence
  is false on a range of strains and must be conditioned (item 1).
- New after a literature check with a receipt: the theorem and its margin, yes, as far as the
  receipt above reaches; the physical reading is not, and item 3 moves its credit to Duraiswami.
- Wanted: yes, in the sense the paper claims and no more: it turns the manuscript's own design
  sentence into a theorem with a quantitative margin, and it says nothing about the construction's
  validity, the unforced problem, or other flows.

Scoping: the claims are scoped as the house rules require, with two edits. The paper repeatedly
restricts itself to the leading profile, the stress-free core, and clauses (ii)-(iii) of
Theorem 4.6 as imposed; Remark 3.7 and the abstract's last sentence say what is not claimed; the
Clay mention (item 15) should go, and the inner-edge sentence of the abstract (item 10) should name
the point. No human has reviewed the paper and it says so. The attribution block names the Astra
review in one clause; it must now name this review as well, in the house pattern, which is the
writer's job after this report, not the reviewer's.

---

## Addendum (2026-10-01, 21:0x EDT, after the report was committed as b8a7569)

Read after the report: `docs/research/2026-10-01-ns-open-map/attempts/midplane-obstructions.md`,
`reviews/astra/REVIEW.md`, `RESPONSE.md`, `DISPOSITION.md` and `reviews/claude/REVIEW-astra.md`.
Every Astra item that bears on the paper (A1-A9, B1-B6, C1-C3, D1-D4) is applied in the paper.
Three were applied incompletely, and each is already an item of this report, so nothing is added
to the MINOR list:

- A4 (the margin is WRONG as an unrestricted formula; the valid statement is piecewise): applied
  to Theorem 3.2(3), but the abstract and Section 1 kept the unconditioned formula. This is item 1.
- A5 (the inner-edge contradiction needs a case split; never write v_s at a = 0): applied for
  Theorem 4.6(iii), but the Proposition 4.10(ii) clause of Theorem 3.2(4) still named
  v_s(X_a, eta) > 2 + c_ex in the a <= 0 case. This is item 6.
- B3 ("Beyond X_b, use the heat exterior ... X N_s = K throughout that exterior"): the paper's
  Lemma 4.2 wrote X_v for the range. This is item 2.

The F items concern `reviews/claude/REVIEW-astra.md`, not the paper, and a grep confirms the three
wording repairs landed there. `reviews/astra/REVIEW.md` and `LAST-MESSAGE.md` differ only by a
trailing newline. The record's attempt file carries the same three gaps where it mirrors the paper
(its remark 3's unconditioned "proportional to h", its relaxed form's X_v, its Proposition 4.10(ii)
wording), and item 8's clause and item 12's quotation as well; the disposition ledger
(`DISPOSITION.md`) lists where each was applied.
