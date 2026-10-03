# Adversarial review and follow-on investigation: "Approximate Antiunitary Symmetry as a Matching Problem"

Reviewer: Claude (Fable 5.1). Baseline: commit `9820d1ed1e61381cb22185740377f7d2ee99a6f1`
(HEAD at review start; paper directory clean; the rendered PDF in
`Documents/Codex/2026-09-28/che/outputs/` is byte-identical to `main.pdf`).
Date: September 29, 2026 (EDT). All files referenced below live in
`paper/antiunitary-matching/reviews/claude/`.

## Verdict

**What survives.** Everything the manuscript proves is correct. The main
theorem (exact reduction of the penalized antiunitary problem to a weighted
matching), the lemma that squared entries of a skew-symmetric contraction lie
in Edmonds' matching polytope and fill it in convex hull, and every corollary
and proposition (commuting tuples, rigidity and stability, parity, hard
constraint, perturbation bound, dual certificates, the sorted-spectrum
recurrence) were reconstructed independently before the manuscript's own
audit was read, and no error was found. The supplied numerical and exact
checks reproduce. New exact checks over complex unitaries (Gaussian-rational
Cayley transforms), adversarial structured unitaries, and an independent
multistart optimizer found nothing below the theorem's value.

**What fails.** No mathematical statement fails. Two hypotheses are stronger
than needed (the rigidity proposition does not need positive costs, only a
unique optimal matching; the hard-constraint corollary needs no sign
condition). One typo (`max` outside math mode). The novelty framing needs
one correction: the entire single-observable case (one Hermitian matrix,
hard or soft penalty) is a routine consequence of Wigner's normal form,
Kramers' theorem and Mirsky's inequality, which the manuscript does not say;
the substantive content is the general-cost theorem, hence the tuple case
with two or more observables, carried by the hull lemma.

**What appears new.** The hull lemma and the general weighted identity were
not found in the literature after 77 targeted searches (reviewer plus a
background search agent), framed between Birkhoff-von Neumann (unitaries) and
O'Meara-Pereira 2013 (Hermitian unitaries, where the hull is strictly smaller
than the degree polytope). Priority is not established; the lemma is
elementary enough to be folklore somewhere.

**What matters.** The lemma turns out to answer two open questions that
J. J. Gil posed independently in Entropy 28:877 (published 2026-08-04) about
the maximal coherence of density matrices with prescribed intrinsic
populations: his third question (global optimality of the adjacent pairing
beyond the "aligned class") follows directly from the lemma, and his first
question (fixed populations and fixed Youla values) is settled here by a new
inequality (Theorem G) whose proof is independent of the manuscript. That is
the strongest external evidence that the manuscript's core object is worth
having. The other new results are a sharp characterization of when diagonal
(vertex) costs keep the problem combinatorial, a quantitative Kramers
inequality in every unitarily invariant norm, and the observation that the
standard SDP relaxation of the unitary constraint cannot see the parity
obstruction.

## 1. Correctness and completeness

Claim-by-claim table: `06-claim-audit.md` (33 items). Independent proof
reconstruction, written before reading `PROOF-AUDIT.md`:
`01-proof-reconstruction.md`. Summary of the substantive inferences:

* Transpose versus conjugate transpose: `S = (U + U^T)/2` and `K = (U - U^T)/2`
  are complex symmetric and complex skew, contractions but not normal; no
  step uses Hermiticity. The identity `U conj(U) + I = 2 S conj(U)` rests on
  `U^T conj(U) = (U^* U)^T = I`. Correct.
* Congruence versus similarity: the substitution `U = V W V^T` is right; the
  key fact is `V^T conj(V) = I`. Correct.
* Contraction and rank: an odd-order principal skew block has zero
  determinant over the complex field; its squared Frobenius norm is at most
  its rank because its singular values are at most one. Correct.
* Constants: two per matched pair, `4 tau` per unmatched vertex; verified
  exactly (rational arithmetic) for real orthogonal and complex unitaries.
* Convex hull versus realizability: correctly separated. Extra fact
  established here: strict mixtures of two matchings can be realized by one
  matrix (explicit `3 x 3` real orthogonal example with `x = (1/2, 1/2, 0)`),
  so uniqueness of the optimal matching is genuinely needed for rigidity.
* Attainment: real signed swaps, exact for every stated hypothesis.
* Degeneracies: `n = 1`, `tau = 0`, zero costs, repeated eigenvalues, ties,
  odd `n` all consistent.
* Duality, the sorted recurrence (exchange identities `2(d-a)(c-b) >= 0`
  and `2(c-a)(d-b) >= 0`), the hard constraint, the perturbation bound:
  correct.

Where each hypothesis is used, and what happens without it: nonnegativity of
`c` is used once (to drop the symmetric-part term). With diagonal costs the
exact identity becomes Theorem A(a) in `04-new-results.md`, the matching
formula holds under `2 c_ij >= c_ii + c_jj`, and outside that condition it
can fail: for `c = I_3` the true minimum is `4 tau + 2 tau/(1 + 6 tau)`
(a continuous rotation about `(1,1,1)`), below the formula's `1 + 4 tau`
for every `tau`. Negative costs also break it.

## 2. Independent falsification (record in `02-checks/`)

| Check | What it does | Result |
|---|---|---|
| `supplied-rerun/` | Reruns `verify.py`, `verify_exact.py` from baseline | 0 failures; counts identical; BFGS success flag 82 vs 80 (environment) |
| `exp01` | Exact Gaussian-rational complex unitaries (Cayley), decomposition, odd sets, lower bound; exact complex skew unitaries for the hard constraint | 44 unitaries, 232 odd-set checks, 176 bounds, 20 skew unitaries; 0 failures |
| `exp02` | Phased permutations, DFT and circulants, odd-cycle rotations, Haar near a 3-cycle, tie mixtures; Cayley-chart L-BFGS multistart (60 starts) | worst energy minus bound `-7e-15`; 0 alarms; non-swap minimizers only at ties |
| `exp03`, `exp03b` | Gil objective: free and prescribed Youla values, random + local search; LPs | bounds never exceeded; coarse polytope LP not tight (0.045), full-family LP tight to `1e-17` |
| `exp04` | Vertex-penalty identity on Haar unitaries; formula under `w >= 0`; `c = I_3` curve; random violators | identity exact to `4e-14`; formula never violated under `w >= 0` (540 cases); `c = I_3` minima equal the closed form at 10 values of `tau`; 28 of 108 violators break the formula |
| `exp05` | Kramers bound, all Schatten norms and Ky Fan partial sums, random skew unitaries; minimization over `T` | 1,200 checks, min slack `-5e-15`; bound attained to `1e-15` |
| `exp06` | Shor SDP relaxation (cvxpy/SCS) and explicit certificate | value 0 for odd `n` with `c = 0` (true `4 tau`); certificate feasible |
| `exp07` | Noncommuting pairs: multistart truth vs sandwich bound from a commuting approximant vs projection bound | see Section 4 |
| `exp08` | Synthetic Zeeman ring: physical `T` commutator vs spectral bound | bound holds; operator-norm bound within 0.05 percent at weak field |

Failed or ambiguous runs are recorded, not hidden: the first version of
`exp07` used a Jacobi joint-diagonalizer that did not converge (it reported a
nonzero commuting-approximant error even for an exactly commuting tuple);
it was replaced by an eigenbasis-of-random-combination start with L-BFGS
refinement, and the run was repeated. Multistart minima are estimates, not
certificates; they are only used as upper bounds on the truth or as
agreement with closed forms.

## 3. Novelty and significance (`07-literature-comparison.md`, agent report in `03-literature/`)

* Correctly labeled classical: Edmonds, Wigner, Kramers, odd-dimension facts
  (citable to Wigner 1960 or Garcia-Tener 2009, Lemma 4.2).
* Routine consequences of classical theorems, presented without saying so:
  the single-observable case (Prop D(a) gives the derivation). The one-pair
  Frobenius distance is in Pinter et al., Quantum 10, 2047 (2026).
* Apparently new: Lemma 2.2, Theorem 2.1 for general nonnegative costs,
  hence the tuple corollary, the dual certificates and stability estimates.
* Gil 2026 (full text read from PubMed Central; formulas verified from the
  MathJax source): no overlap of results; his Theorem 2 is the aligned-class
  special case; his open questions are answered here (Theorems C and G).
  The paper has no citations yet on Semantic Scholar.
* Skew Schur-Horn results (Sanyal-Sottile-Sturmfels 2011 Prop. 3.10; Tam
  1998) treat one linear entry per block, not squared moduli of all entries;
  Theorem G is outside them.

## 4. Applications (`05-application.md`)

1. Gil's fixed-population coherence problem (worked in full): closed-form
   global maxima with and without prescribed Youla values, a new family of
   valid inequalities, and numerical confirmation. Value: converts a
   subclass statement into a global one for a quantity that enters his
   purity and entropy identities.
2. Time-reversal breaking bounds (synthetic demonstration): the free-`T`
   theorem yields, for a prescribed physical `T`, a certified spectral lower
   bound; the useful form is the operator-norm version of Theorem B, nearly
   tight at weak field in a spin-orbit ring with Zeeman splitting.
3. Noncommuting tuples (exp07, corrected run): for nearly commuting pairs
   the theorem gives a practical near-optimal construction (the matching
   optimizer of a joint-diagonalization approximant, evaluated on the true
   tuple, is within 0.1 percent of the multistart optimum at perturbation
   0.1 and within 6 percent at perturbation 1.0), while the manuscript's
   sandwich lower bound is loose (factor 2 to 4 off already at perturbation
   0.6) and the reviewer's projection lower bound
   `sup_{|t|=1} Phi_tau(t . H)` sits about one third below the truth. No
   exact formula for noncommuting tuples; the gap was not closed.

## 5. Extensions and discoveries (`04-new-results.md`, LaTeX: `extension-note.tex/.pdf`)

Proved: Theorem A (vertex penalties, sharp condition, explicit continuous
minimizer); Theorem B and Corollary B' (quantitative Kramers in every
unitarily invariant norm; distance to even-multiplicity matrices); Prop D
(classical route for one observable, tuple obstruction); Prop E (Shor gap
certificate); Prop F (rigidity under uniqueness); Theorem C and Theorem G
(Gil's questions); Prop H (normal matrices, Floquet relation). Abandoned or
open: a combinatorial description when `w` is not nonnegative; the joint
hull of `(|S_ij|^2, |K_ij|^2)`; Theorem G for general (non-product) weights;
exactness for noncommuting tuples.

## 6. Separation statement

The directory `reviews/openai` was never listed, read, or searched; no
conversation-search, memory or agent tool was used to retrieve the other
reviewer's work; the background literature agent was instructed to use web
tools only and reported no local file access. `reviews/` did not exist when
this review started. Two incidental observations are disclosed: at the end
of the session a listing of the parent directory `reviews/` showed that
`reviews/openai/` now exists (its contents were never listed or read), and
the `git push` output showed that the shared branch had advanced by four commits
that are not mine before my first commit was made (their messages, diffs and
files were not inspected; only their count was read; my commits stage only
`reviews/claude/`). No
content of the other review reached this reviewer.

## 7. Strongest defensible result

Lemma 2.2 of the manuscript, in the form: for every complex skew-symmetric
contraction `K`, the vector of squared moduli `(|K_ij|^2)_{i<j}` lies in
Edmonds' matching polytope, and the convex hull of these vectors is that
polytope. It is short, it carries the manuscript's main theorem for general
costs and tuples, and it resolves an explicitly posed open question in an
unrelated literature (Gil 2026). Its significance is that it exposes a
parity constraint that no degree-based or first-level semidefinite
relaxation of the unitary group can see, and that it converts a
Grassmannian-orbit optimization into linear optimization over a polytope
whose vertices are matchings. The reviewer's Theorem G shows the same
mechanism survives when the singular values of `K` are prescribed, which the
lemma alone does not cover.
