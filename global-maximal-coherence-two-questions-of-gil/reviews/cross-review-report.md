**Astra referee review of the Gil note**

Reviewed September 29, 2026 (EDT), after `git pull --ff-only`. The reviewed manuscript is the version last changed in commit `f37590d`; its SHA-256 is `42673800298b59d3382ef7dc12bf2b2e2db2b767d8b6cc5025d7d54f99d3e935`. I examined the four requested files, the permitted companion hull lemma, Gil's full text and equations, and the literature identified below. No excluded file was opened. The required README contains a prior-review summary; the conclusions below rest on my own derivations and computations.

**1. MAJOR - Theorem 4.1 is an immediate consequence of classical multiplicative singular-value majorization. The novelty discussion misses this antecedent.**

Location: Remark 4.4, especially `main.tex:354` through line 370, and the README's presentation of the inequality.

There is a short proof using A. Horn, *On the Singular Values of a Product of Completely Continuous Operators*, PNAS 36 (1950), 374-375, especially the product inequality in the proof of Theorem 3. I checked both original pages. This supplies a materially stronger comparison than the manuscript's discussion of an ordinary trace inequality. [Horn's paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC1063207/).

Here is the derivation, independently supplied by this referee. Put \(D=\operatorname{diag}(\sqrt{a_1},\ldots,\sqrt{a_n})\) and \(T=DMD\). Because \(T^T=-T\), its singular values are \(t_1,t_1,\ldots,t_m,t_m\), with an additional zero in odd dimension. Apply the classical product inequality twice, at each even index \(2\ell\):

\[
 \prod_{k=1}^{\ell}t_k^2
 =\prod_{j=1}^{2\ell}\sigma_j(DMD)
 \le \left(\prod_{j=1}^{2\ell}\sigma_j(D)^2\right)
      \prod_{j=1}^{2\ell}\sigma_j(M)
 =\prod_{k=1}^{\ell}
       \bigl(s_k^2a_{2k-1}a_{2k}\bigr).
\]

Both vectors on the two sides are decreasing. Thus
\[
 (t_k^2)_{k=1}^m
 \prec_{w,\log}
 (s_k^2a_{2k-1}a_{2k})_{k=1}^m.
\]
Weak log-majorization implies weak majorization, by applying the increasing convex exponential to the logarithms. Zeros follow by continuity, for example by approximating \(a\) and the Youla values by positive values while keeping a Youla frame fixed. Consequently,
\[
 \sum_{i<j}a_i a_j|M_{ij}|^2
 =\tfrac12\|DMD\|_F^2
 =\sum_k t_k^2
 \le\sum_k s_k^2a_{2k-1}a_{2k}.
\]
The adjacent block matrix gives equality. This covers the entire real and complex statement, including odd dimensions.

This does not identify a previous paper that prints precisely the note's population formula. It does establish that the inequality follows directly from classical majorization, without the new layer-cake argument or specialized skew-diagonal results. The application to Gil's questions can still be useful.

Concrete fix: cite Horn, give this derivation, and describe Theorem 4.1 as a sharp consequence of classical singular-value inequalities, with an alternative layer-cake proof yielding the nested-set inequalities. Reassess any claim of a new spectral inequality separately from the application and the squared-entry polyhedral viewpoint.

**2. MAJOR - Corollary 5.1(1) drops the support restriction and is false as written on the boundary.**

Location: `main.tex:391` through line 398.

Theorem 3.1 explicitly restricts the matching problem to the support of \(A\) when populations vanish. Corollary 5.1(1) instead says that an optimizing state's support is a maximum-weight matching for the weights \(b\), without that restriction.

Use the manuscript's own boundary data:
\[
 a=(1/2,1/2,0,0),\qquad b_{12}=1,\qquad b_{34}=10,
\]
with other weights zero. Gil's metaspin convention forces \(M_{34}=0\). The state maximum is \(1\), whereas the maximum-weight matching on all four vertices has weight \(11\) and contains the inactive edge \(34\). No state's metaspin support can be that matching.

Concrete fix: state that Youla values are free and that the matching is taken on \(\{i:a_i>0\}\), with all inactive entries zero. Alternatively, assume all populations are positive in item (1). Carry the same support convention into item (3). This is a defect in the corollary, not in either main proof.

**3. MINOR - Trace normalization is missing from the explicit density-matrix hypotheses.**

Location: `main.tex:63`, Theorem 3.1, and the density-matrix consequence of Theorem 4.1.

Gil's Section 2.1 calls a density matrix “a Hermitian, positive semi-definite, trace-normalized” matrix. The note never explicitly imposes \(\sum_i a_i=1\). Literally, Theorem 3.1 allows \(a=(1,1)\), for which the claimed maximum is over an empty set of density matrices.

Concrete fix: impose \(\sum_i a_i=1\) when introducing populations and in Theorem 3.1. Keep the unrestricted nonnegative \(a_i\) in the matrix inequality of Theorem 4.1, where normalization is unnecessary. I treat this as an omitted standing hypothesis because the intended meaning of “populations” is clear.

**4. MINOR - The comparison with Tam and skew-symmetric Schur-Horn results is narrower than the conclusion drawn from it.**

Location: Remark 4.4 and the README's open literature item.

Tam's published abstract characterizes entries on a fixed matching under unitary congruence: weak-majorization inequalities, with an additional inequality in the even-dimensional full-matching case. That advertised result is not a statement of the weighted squared-entry inequality. [Tam, SIAM J. Matrix Anal. Appl. 19 (1998), 737-754](https://doi.org/10.1137/S0895479896312559).

The Leite-Richa-Tomei abstract concerns Schur-Horn analogues for real and complex skew-symmetric matrices. The related Proposition 3.10 in *Orbitopes*, which I checked in full context, concerns the linear skew-diagonal projection of an orbitope. It is not the nonlinear squared-entry optimization in this note. [Leite, Richa and Tomei](https://doi.org/10.1016/S0024-3795(98)10169-6); [Sanyal, Sottile and Sturmfels, Section 3.2](https://arxiv.org/pdf/0911.5436).

However, the \(n=3\) argument at lines 367-369 only demonstrates the weakness of imposing isolated per-edge bounds. For an actual matrix with prescribed Youla value,
\[
 \sum_{i<j}|M_{ij}|^2=s_1^2,
\]
so the sharp \(n=3\) bound follows immediately from the fixed Frobenius norm and \(a_i a_j\le a_1a_2\). Ignoring that identity cannot establish nonimplication from the surrounding classical theory. Item 1 gives the decisive classical implication in every dimension.

I could not retrieve the complete Tam or Leite-Richa-Tomei articles, so I do not certify that their later applications contain no equivalent formulation. An additional relevant lead is R. Mathias, *The singular values of the Hadamard product of a positive semidefinite and a skew-symmetric matrix*, Linear and Multilinear Algebra 31 (1992), 57-70: \(DMD=(dd^T)\circ M\), with \(d_i=\sqrt{a_i}\), falls directly within that subject. Its accessible abstract loses the displayed inequality, and I did not obtain its full text; I make no priority claim based on it. [Mathias](https://doi.org/10.1080/03081089208818122).

Concrete fix: replace “do not imply” with a precise statement that the cited projection theorems do not directly state the inequality; delete or qualify the \(n=3\) comparison; retain explicit limits on full-text coverage; and incorporate the verified Horn antecedent. Do not equate failure to find the literal formula with an established novelty result.

**5. MINOR - A few statements in the verification code need more precise wording.**

The `pga_free` docstring calls \(4(aa^T)\circ M\) the gradient on skew matrices. Under the Frobenius inner product the matrix gradient is \(2(aa^T)\circ M\); the factor \(4\) is the gradient in independent upper-triangular coordinates. Since the implementation normalizes the direction, this factor does not affect its iterates.

The `snap_isometry` docstring identifies the resulting partial isometries with the extreme points of the contraction ball. An arbitrary deficient-rank partial isometry need not be extreme: the zero matrix in dimension two is an immediate counterexample. The manuscript's more modest description of the operation is correct.

The saved prescribed-spectrum `worst_shortfall` is \(-1.0842021724855044\times10^{-18}\), because every recorded best value is slightly above its bound. A quantity called a shortfall should be clamped below by zero.

Concrete fix: specify the gradient convention, remove the extreme-point parenthetical or restrict it to maximal possible rank, and compute `max(0.0, -min(diffs))`. In Section 6's prescribed-spectrum paragraph, use “not exceeded beyond numerical error” to accommodate the reported positive excess. None of these points invalidates the current numerical results.

**6. CORRECT - The substantive definitions agree with Gil, subject to the normalization correction above.**

I checked Gil's Sections 2.1-2.4, Definition 1, Theorem 2, and equations (3), (7)-(9), (13), (20), and (33). [Gil's full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13512070/).

| Object | Checked interpretation |
| --- | --- |
| Intrinsic populations | The ordered eigenvalues of the real symmetric part in a fixed real structure, placed on the diagonal by a real orthogonal change of basis. They are not generally the eigenvalues of \(\rho\). |
| \(N\) | Real antisymmetric, with \(\rho=A+iN\). The note does not import the older convention with a factor of two. |
| Cohesion | \(\|N\|_F\); squared cohesion is \(\|N\|_F^2=2\sum_{i<j}N_{ij}^2\). Gil's \(P_c^2=2\|N\|_F^2\) is a different normalization. |
| Metaspin and Youla values | \(M_{ij}=N_{ij}/\sqrt{a_i a_j}\) on the support; the singular values are the Youla values repeated twice, plus the odd-dimensional zero. |
| Alignment | Existence of an admissible IRB representative in which \(M\) has matching support. Degenerate populations permit residual rotations. |

Two short phrases in Gil settle the potentially consequential readings. Definition 1 says “there exists a representative of its IRB”; alignment need not hold in every arbitrarily chosen representative of a degenerate IRB. Section 2.3 says the support-defined tensor is “extended by zeros to the inactive subspace”; invisible entries on zero-population axes are not free metaspin variables.

Concrete fix: retain these definitions and explicitly state the fixed-real-structure and zero-extension conventions near the first definition of \(M\).

**7. CORRECT - Theorem 3.1's proof works, including positivity, termination of the exchanges, and zero populations.**

For \(A>0\), congruence by \(A^{1/2}\) makes
\[
 \rho\succeq0\iff I+iM\succeq0.
\]
For real skew \(M\), the eigenvalues of \(iM\) occur as \(\pm s_k\), so this is exactly \(s_k\le1\). Entrywise bounds alone would not suffice, but the proof uses the full operator-norm condition.

The hull lemma is valid for real and complex skew matrices. Row norms give degree constraints. Every odd principal compression is singular and remains a contraction, giving
\[
 2x(E(B))=\|M_B\|_F^2\le |B|-1.
\]
Matching incidence vectors are realized by signed-swap blocks. Thus the convex-hull argument supplies an upper bound and actual attaining matrices, not merely a relaxed optimum.

The exchange argument is complete. Completing a matching cannot decrease a nonnegative weight. In odd dimension, replacing a paired smallest population by an unpaired larger one cannot decrease it. Both displayed four-vertex exchanges have the stated nonnegative gains. For both crossing and nested configurations, the total edge length drops by \(2(k-j)>0\). A terminal perfect matching must be adjacent: otherwise the partner of vertex 1 and the pair containing vertex 2 form a crossing or nesting; remove \(12\) and repeat.

If \(a_i=0\), the \(2\times2\) principal minors give \(|N_{ij}|^2\le a_i a_j=0\). Restrict to the positive support, prove the formula there, and append zeros. This also handles odd support size, a rank-one population matrix, and repeated populations.

My explicit maximizing state has blocks
\[
 \rho_k=
 \begin{pmatrix}
 a_{2k-1}&i\sqrt{a_{2k-1}a_{2k}}\\
 -i\sqrt{a_{2k-1}a_{2k}}&a_{2k}
 \end{pmatrix}.
\]
Their eigenvalues are \(a_{2k-1}+a_{2k}\) and \(0\). Append any unpaired population and inactive zeros. The matrix is Hermitian, positive semidefinite, trace one when the populations are normalized, and has real part exactly \(A\).

Concrete fix: no proof repair is required; add the trace hypothesis and, optionally, this block check.

**8. CORRECT - Every substantive step of Theorem 4.1's layer-cake proof is valid.**

The following checks concern the supplied proof, independently of the alternative proof in item 1.

1. **Layer-cake identity.** Each \(a_i a_j\) is the double integral of the product of its two indicator functions. Averaging the two orders introduces exactly the factor \(1/2\). All sums are finite and all integrands nonnegative, so exchanging sums and integrals is legitimate.

2. **Prefix level sets.** For \(u\ge v\), sorted populations give \(C=[p]\subseteq B=[q]\). Equal populations cause no problem; thresholds at population values are a set of measure zero. Empty prefixes give zero.

3. **Counting the two integrands.** Each edge internal to \(C\) contributes twice and each edge from \(C\) to \(B\setminus C\) once. Thus
   \[
    2\Psi=\|M_{C,B}\|_F^2.
   \]
   Counting adjacent blocks gives exactly the two sums defining \(R(p,q)\), so \(2h=R(p,q)\). The prose at `main.tex:274` should say “one-half the squared Frobenius norm,” consistent with its displayed equation.

4. **Ky Fan.** If \(P\) is the rank-\(p\) orthogonal projection selecting rows of \(M_B\), then
   \[
    \|PM_B\|_F^2=\operatorname{tr}(P M_BM_B^*P)
    \le\sum_{j=1}^p\sigma_j(M_B)^2.
   \]
   This holds for complex matrices as well as real ones.

5. **Submatrix singular values.** Compressing on the left and right by coordinate contractions cannot increase any singular value. Hence \(\sigma_j(M_B)\le\sigma_j(M)\). Since both skew matrices have paired singular values, \(t_k\le s_k\). No Hermitian eigenvalue interlacing assertion is being incorrectly applied to a complex skew matrix.

6. **The three cases.** For \(p=2h\), the upper sum is \(2\sum_{k\le h}t_k^2\). For \(p=2h+1<q\), it is \(2\sum_{k\le h}t_k^2+t_{h+1}^2\). For \(p=q=2h+1\), the last singular value is zero, leaving \(2\sum_{k\le h}t_k^2\). Replacing \(t_k\) by \(s_k\) yields precisely \(R(p,q)\) in each case. These cases exhaust \(0\le p\le q\).

7. **Integration and equality.** Integrating \(\Psi\le h\) proves the theorem. Set \(M=\bigoplus_k s_kJ\), where \(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), and append an odd-dimensional zero. This matrix has exactly the prescribed singular values and attains every needed prefix inequality simultaneously.

For the density-matrix equality case, replace the off-diagonal entries in the blocks of item 7 by \(i s_k\sqrt{a_{2k-1}a_{2k}}\) and its conjugate. Their determinant is \(a_{2k-1}a_{2k}(1-s_k^2)\ge0\). Together with trace one this proves admissibility. If only \(r\) populations are positive, at most \(\lfloor r/2\rfloor\) positive Youla values are possible, and that condition is also sufficient by these blocks. Only orientations supported in that active subspace represent Gil's metaspin tensor.

Proposition 4.2 also follows: the block-norm argument does not require prefix sets. For singleton \(C=B\), \(R(1,1)=0\), so the advertised degree bound \(s_1^2\) should be understood for \(|B|\ge2\). The singleton case is a harmless trivial constraint. Corollary 5.1(3)'s necessary equality condition is correct: each pair of strict population gaps gives a region of positive measure with a constant nonnegative integrand deficit.

Concrete fix: no mathematical repair to the inequality proof is required. Correct the half-norm prose and make the support convention explicit in the corollary.

**9. CORRECT - The main results answer the stated optimization questions, with the note's explicit interpretation of the third question.**

Gil's Section 8.2 asks for the maximum at fixed populations and Youla values over orientations, and separately asks about extending adjacent-pairing optimality “under suitable spectral constraints.” Theorem 4.1 answers the first question exactly. Theorem 3.1 establishes global optimality with free admissible Youla values; Theorem 4.1 additionally establishes the weighted adjacent formula for each prescribed admissible Youla spectrum. Neither theorem characterizes the Gram-map image.

The abstract now restricts its general nonnegative-weight matching assertion to free Youla values, which is correct. It does not claim general-weight alignment at fixed Youla values. The complex matrix inequality is an algebraic extension; only the real skew case supplies the stated density matrices.

Concrete fix: retain the scope qualifications. Add the odd-dimensional zero to the abstract's singular-value list and the support qualification to its positivity statement. Replace the assertion that fixing the spectrum of \(\rho\) makes the question “empty” by the precise observation that it fixes the objective; compatibility with an aligned representative would still be a separate feasibility question. The note does not prove extremizer feasibility under arbitrary additional restrictions on the spectrum of \(\rho\).

**10. CORRECT - All four numerical claims in Remark 4.5 are correct; the value 2.196 can also be certified exactly.**

For the displayed matrix,
\[
 \tfrac12\|M\|_F^2=0.09+0.84+0.84+0.04=1.81,\qquad
 \operatorname{Pf}(M)=0.3(0.2)-\sqrt{0.84}(-\sqrt{0.84})=0.9.
\]
Thus the squared Youla values are the roots of
\(z^2-1.81z+0.81=(z-1)(z-0.81)\).
The singular values are \(1,1,0.9,0.9\), and the objective is \(2.196\).

The three perfect matchings have best values \(2\), \(1.2(1+0.81)=2.172\), and \(0\). Both positive Youla values must be placed, so this exhausts the aligned configurations for a nondegenerate population vector.

For the full nested-set LP, the point
\[
 x_{12}=0.19,\quad x_{13}=x_{24}=0.81,\quad
 x_{14}=x_{23}=x_{34}=0
\]
is feasible and has objective \(2.324\). I checked feasibility in exact rational arithmetic for all \(3^4=81\) nested pairs. A dual certificate is \(0.6\) times the constraint for \(C=\{1,2\},B=[4]\), plus \(0.2\) times each constraint for \(C=\{1,2,3\},B=[4]\) and \(C=\{1,2,4\},B=[4]\). Its right side is
\[
 0.6(2)+0.2(2.81)+0.2(2.81)=2.324,
\]
and its left side is the objective plus
\(1.2x_{14}+1.2x_{23}+0.4x_{34}\).
This proves the LP optimum without relying on a solver.

There is also a global real-orbit certificate for \(2.196\). For a general real \(4\times4\) skew matrix, set
\[
 X=\tfrac12(M_{12}+M_{34},\,M_{13}-M_{24},\,M_{14}+M_{23}),\quad
 Y=\tfrac12(M_{12}-M_{34},\,M_{13}+M_{24},\,M_{14}-M_{23}).
\]
The norm and Pfaffian constraints give
\(\{\|X\|,\|Y\|\}=\{0.95,0.05\}\).
The objective is symmetric in \(X,Y\), so assume \(\|Y\|=0.05\). Then
\[
 \begin{aligned}
 2(X_1+Y_1)^2+2.4(X_2^2+Y_2^2)
 &\le 2.172-0.4(X_1-5Y_1)^2+9.6Y_1^2\\
 &\le 2.196.
 \end{aligned}
\]
The displayed matrix attains equality. Thus the example's continuous maximum is exactly \(2.196\), although a formula for arbitrary weights is a different problem.

Concrete fix: explicitly choose distinct positive populations, for example \(a=(0.4,0.3,0.2,0.1)\), so that nonmatching support proves nonalignment under Gil's existential definition. The numerical counterexample needs no repair. Prefer the explicit LP witness and dual certificate, and optionally replace the random-search sentence by the exact real-orbit certificate.

**11. CORRECT - Section 6 faithfully reports the saved searches and their failures to reach the bound.**

The WSL `python3` environment lacks SciPy. I executed the unchanged `verify_gil.py` through `runpy` with the installed Windows Python 3.12.10, NumPy 2.2.6, and SciPy 1.16.3, matching the saved environment. I intercepted only `Path.write_text` for the JSON destination, captured the generated report in memory, and verified that the existing JSON bytes were unchanged. Every parsed report field exactly matched `verification-gil.json`, including the source SHA-256:
`9516f19bc51b23cc92309bfe2883de2ac75a67b4fe3134faf33d1eeaeaf24592`.

All figures in this table are in squared-cohesion units except the odd-set residual.

| Saved check | Independently reproduced result |
| --- | --- |
| A, optimized largest excess | \(5.551115123125783\times10^{-16}\) |
| A, worst shortfall | \(7.178675857100192\times10^{-5}\) |
| A, tolerance counts | 19/30 within \(10^{-6}\); 30/30 within \(10^{-4}\) |
| B, optimized largest excess | \(1.500466417780899\times10^{-13}\) |
| B, minimum best-minus-bound | \(1.0842021724855044\times10^{-18}\); 30/30 within \(10^{-6}\) |
| Full and prefix LP errors | Each \(5.551115123125783\times10^{-17}\) |
| \(C=B\) LP excess | \(0.019409162878746528\) |
| \(C=B\) plus degree LP excess | \(0.0004419584168336016\), in 4/30 instances |
| Odd-set checks | 8,760; largest residual \(-0.032159502235817206\) |

I also reran check A separately with per-dimension reporting: the worst shortfall occurs at \(n=7\), as Section 6 says. The worst shortfalls at \(n=4,5,6\) are respectively \(1.851243621731058\times10^{-7}\), \(2.8521934975739294\times10^{-5}\), and \(4.05135572854598\times10^{-5}\).

The factor-of-two conversions in Remark 4.3 are correct. Exponential parametrization covers \(\mathrm{SO}(n)\); conjugation by a coordinate sign matrix transfers the other orthogonal component without changing squared entries. These remain local searches and finite controls, not proofs.

Concrete fix: preserve the candid shortfall reporting; apply only the small wording and code corrections in item 5.

**12. CORRECT - US English and the no-em-dash requirement pass for the four reviewed files.**

I checked their text for Unicode em dashes, TeX triple-hyphen em dashes, and the prohibited spelling variants. None was found. The double hyphens in TeX names and ranges produce en dashes, not em dashes.

Concrete fix: none.

**Independent numerical checks and results**

The following computations used separate implementations rather than calling the manuscript's objective, block-bound, LP, or optimizer functions. Unless otherwise stated, objective residuals below use \(F=\sum_{i<j}a_i a_j|M_{ij}|^2\), half the squared cohesion.

- **Seed 8675309, prescribed spectra:** 24 population/spectrum cases at each of \(n=4,5,6\). Population profiles were descending integers, uniform, repeated adjacent values, one zero tail entry, rank two, and rank one, normalized to sum one. Spectra were decreasing from \(0.95\) to \(0.15\), repeated \(0.7\), rank one with value \(1\), and zero; for density-matrix cases, values beyond the support's permitted rank were set to zero. There were 100 real QR orientations and 100 complex QR orientations per case, 14,400 matrices total. General orientations with zero populations tested the algebraic inequality; density assertions used full positive support or orientations restricted to the active support.

| \(n\) | Largest real excess | Largest complex excess | Largest prefix residual | Largest equality-construction error |
| --- | --- | --- | --- | --- |
| 4 | \(5.55\times10^{-17}\) | \(5.55\times10^{-17}\) | \(3.11\times10^{-15}\) | \(0\) |
| 5 | \(3.47\times10^{-17}\) | \(4.86\times10^{-17}\) | \(2.66\times10^{-15}\) | \(0\) |
| 6 | \(4.16\times10^{-17}\) | \(2.78\times10^{-17}\) | \(3.55\times10^{-15}\) | \(6.94\times10^{-18}\) |

- **Proof identities:** 50,544 checks over all nested subsets for selected real and complex matrices; largest excess \(2.00\times10^{-15}\). Discrete layer-cake summation using population gaps agreed with direct objectives within \(4.17\times10^{-17}\). Singular-value reconstruction errors were at most \(1.64\times10^{-15}\). Tested density matrices had minimum eigenvalue at least \(-2.29\times10^{-16}\) and trace error at most \(2.23\times10^{-16}\).

- **Independent optimization:** cyclic exact maximization over real coordinate-plane rotations, 12 random starts for each of the 72 cases, 864 starts total. Every best value reached the formula within \(1.67\times10^{-16}\). This used neither Nelder-Mead nor matrix-exponential coordinates.

- **Seed 8675310, free spectra and matching:** 36 additional population instances across \(n=4,5,6\), including ranks \(n\), \(n-1\), and two. Exhaustive enumeration of all matchings agreed exactly with the adjacent formula. For 7,200 random supported skew contractions, the largest objective excess was \(-6.492370923158464\times10^{-5}\); all constructed density matrices had nonnegative computed minimum eigenvalue.

- **Independent product-weight LPs:** full and prefix nested-set LPs on 36 additional instances, including repeated and zero singular values and some \(s_1>1\) for the purely algebraic statement. Both LP families matched the formula within \(1.11\times10^{-16}\).

- **Classical-majorization cross-check:** 3,600 additional complex matrices at \(n=4,5,6\), including zero populations and repeated or zero singular values. The even-index cumulative-product inequalities in item 1 had largest residual \(1.31\times10^{-17}\); the corresponding partial-sum inequalities had largest residual \(-7.43\times10^{-4}\).

- **Remark 4.5:** direct SVD returned \(1,1,0.9,0.9\) within \(2.23\times10^{-16}\); the matrix objective was \(2.1959999999999997\), the aligned maximum \(2.172\), and the independently built LP optimum \(2.324=581/250\). One hundred independent coordinate-rotation starts reached \(2.1959999999999997\). Exact rational checking found zero violations for the LP witness; the analytic certificates in item 10 establish both optima.

**Verdict:** Theorem 3.1 is proved once the implicit probability normalization is made explicit, and Theorem 4.1 is proved as a real and complex skew-matrix inequality, with a valid density-matrix consequence on the active support. I found no BLOCKING defect in either proof and no numerical counterexample. The manuscript needs revision before submission: its novelty discussion omits a direct classical majorization derivation, and Corollary 5.1(1) is false without the support restriction. The finite checks support the implementations and examples; the proofs, including the independent classical derivation above, establish the mathematical conclusions.
