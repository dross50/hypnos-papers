# Astra cross-review

2026-10-01, 17:29 EDT (America/New_York). Assisted research; no human mathematician has reviewed this. Reviewed against the committed attempts at `377f934` and Claude's review at `4032fc3`. All profile variables and numerical profile values below use dimensionless manuscript units; CPU times are in seconds. NS denotes [OpenAI, *Finite Time Blowup for Navier-Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf). I retrieved its 166-page PDF and verified SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. Page references are printed pages.

Theorem I's substantive barrier and piecewise quantitative bound are correct. Theorem II is correct but already proved by Duraiswami on page 20. The sharp form needs a stronger tail condition than the displayed limit in the attempt. Every checker flag passes; those passes do not resolve the tail-condition error or establish novelty.

## A. Theorem I (the dividing-plane barrier)

**Definitions and Lemma 1: CORRECT.** The restored factors agree with NS pp. 26-28:

\[
V_0=\frac X L\{2\eta U-2D\eta\mathcal A_XU-d\partial_\eta\mathcal A_XU\},
\quad W=1-2D\eta\mathcal A_XU-d\partial_\eta\mathcal A_XU,
\quad H_c=D\eta+dU,
\]
\[
S_q=-Wl-h(1-2\eta U)-H_c\partial_\eta\log E.
\]
\[
S_n=-WD_XU-A(1-2\eta U)U-H_cU_\eta-d\Pi_\eta
+4A\eta\Pi+2\eta D_X\Pi.
\]

In particular, $H_c(X,0)=U(X,0)$ exactly. Its vanishing removes $H_\eta$ regardless of the parity of $E$. Smoothness permits differentiation under the radial average, so $W(X,0)=1-w(X)$, where $w=\mathcal A_X(U_\eta)(X,0)$. These conclusions need vanishing on the whole radial segment used by the average, as assumed. Smoothness at the axis concerns $F=E/\sqrt{2X}=\phi/C$, not $E$ itself; the attempt uses the correct regular variable. [NS (4.3)-(4.9), pp. 25-26](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=25).

**Equation (M): CORRECT.** With $H=2X\phi/C$, (4.13)'s first equation and (4.14) give

\[
\frac2X D_X(D_X-1)H
=L^{-1}\{W D_XH+H_cH_\eta+h(1-2\eta U)H\}.
\]

Setting $\eta=0$ gives exactly (M). The sign of $hH$, the factor $2/X$, and the absence of axial diffusion are correct for this leading residual. The attempt's introductory sentence describing the viscous operator is **WRONG as worded**: this expression is $r$ times the radial swirl-viscosity operator, after removing the power of $q$. Explicitly,

\[
r(\partial_{rr}+r^{-1}\partial_r-r^{-2})u_\theta
=q^{-h-1}\frac2X D_X(D_X-1)H.
\]

The checker includes the missing multiplication by $r$; the actual proof uses the correct balance. [NS Proposition 4.2, (4.12)-(4.14), p. 27](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=27).

**Strict positivity, including $h=0$: CORRECT.** Write $Y=D_XH$. For $X>0$,

\[
Y_X=\left(\frac1X+\frac{1-w}2\right)Y+\frac h2H.
\]

Since $C>0$ and $\phi(0,0)>0$, $Y=2\phi(0,0)X/C+O(X^2)>0$ initially. At a first zero, the left derivative is nonpositive, whereas the equation gives $Y_X=hH/2>0$ for $h>0$. A first zero at $X_a$ is excluded by the same one-sided argument. For $h=0$, homogeneous linear uniqueness on every interval bounded away from zero excludes a zero. Equivalently, variation of constants gives a positive initial contribution and a nonnegative integral. No bound on the size or sign of $w$ is needed, only its local continuity. Thus $D_XH>0$ and $a=2-2D_XH/H<2$ everywhere claimed.

State $h\ge0$ explicitly in the abstract lemma. The manuscript itself uses positive $h$; the $h=0$ argument extends this ODE, not the full leading-order approximation, since the separation from axial viscosity disappears there. [NS pp. 24-27](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=24).

**Quantitative margin: CORRECT in its piecewise form; WRONG as an unrestricted equivalent max/min formula.** Avoid using $w$ for both the strain and its supremum. Put $B(X)=\sup_{0<x\le X}w(x)$. The valid statement is

\[
a(X,0)\le A_*(B(X)),\qquad
A_*(B)=
\begin{cases}
0,&B\le1+h,\\
2-2h/(B-1),&B>1+h.
\end{cases}
\]

For $B>1$, this equals $\max\{0,2-2h/(B-1)\}$. At $B=1$ that shorthand is undefined; at $B<1$ it loses the asserted $a\le0$ conclusion. The corresponding margin is $2-a\ge2$ when $B\le1+h$, and $2-a\ge2h/(B-1)$ otherwise. The attempt's unrestricted minimum formula has the same defect.

The proof needs only a small endpoint repair. Fix $X_1$, freeze $B=B(X_1)$, and use

\[
D_Xa=X\{(w-1)(1-a/2)-h\}-(1-a/2)a.
\]

On a connected component where $a>A_*(B)\ge0$, the already proved $a<2$ gives $l=1-a/2>0$. The braces are nonpositive, and $-la<0$, so $D_Xa<0$. This contradicts entering that component from its left endpoint. If the endpoint is zero, use continuity and $a(0)=0$; do not assume a positive crossing radius. When $h=0,B=1$, the braces can equal zero, contrary to the attempt's strict-sign sentence, but $-la<0$ still proves the result. When $h=0,B>1$, $A_*=2$ and strict positivity already settles it. This is a complete proof of the corrected statement, consistent with the stress equation in [NS (B.25), p. 151](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=151).

**Axial shear and the inner-edge contradiction: CORRECT, with a case split.** Vanishing of $U(X,0)$ on the closed core gives $D_XU(X_a,0)=0$, hence $b_s=0$. If $a(X_a,0)>0$, then $v_s=a<2$. If $a(X_a,0)\le0$, the positive lower bound on $a$ already fails. This contradicts the simultaneous requirements of Theorem 4.6(ii)-(iii), and likewise Proposition 4.10(ii). One should not write $v_s=a+b_s^2/a$ at $a=0$. [NS pp. 33, 37](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=33).

**Growth-rate conclusion: CORRECT for $a>0$; the unconditional formula and equation number need fixing.** On that branch, the proposed squared-rate expression, or radicand, is

\[
\lambda_0^2=2F_0^2(a-2)<0.
\]

For $h>0,B>1+h$, the margin even gives $\lambda_0^2\le-4hF_0^2/(B-1)$. The attempt's weaker negative upper bound follows as well. Its final strict inequality requires $h>0$; at $h=0$ that displayed bound is zero, although the radicand remains strictly negative when $a>0$. At $a=0=b_s$, the shear frame itself is undefined, so the conclusion is failure of the pulse construction's hypotheses. For example, $\phi=1, U=(1+h)\eta$ satisfies the first equation of (4.13), has $U(X,0)=0$, and has $a=0$ identically. It does not break the barrier, but shows why its hypotheses alone do not define the frame. The rate formula is **unnumbered above (7.1)** on p. 74; (7.2) defines the carrier and pulse scales. [NS p. 74](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=74).

Two surrounding claims need qualification. The phrase “Rayleigh-stable” describes the sign of this centrifugal criterion, not a proved spectral or nonlinear stability theorem. The exact propagation of symmetry from analytic axis data is **UNCLEAR as justified by twelve computed coefficients**: formal parity follows inductively from the equations, but an actual symmetric solution also needs existence and uniqueness in the stated class. The attempt's constant azimuthal datum is a fixture, not the specially chosen datum of Appendix B, and (B.1) expressly assumes $j_0>0$. Theorem I avoids this issue by assuming $U(X,0)=0$ directly. [NS pp. 144-148](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=144).

## B. Theorem II (the dividing-plane flux identity) and its sharp form

**Literal Theorem II: CORRECT.** Equation (4.15) defines $S=\int_0^X(U^2-E^2/2)\,dx$, and Theorem 4.6(v) imposes $S(\infty,\eta)=0$ for every $\eta\in[-1,1]$. Thus the equality of the two integrals is immediate. The positive exterior amplitude makes their common value positive. Compact radial support of $U$, regularity at the axis, and $E\sim c_\infty X^{-A}$, with $2A=1+2h>1$, make the integrals finite. Stress freedom in the core is unnecessary for this conclusion. It requires axial velocity somewhere on each entire slice; it does not locate that velocity at the axis or within the core. [NS pp. 28, 33](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=28).

**The sharp form's exterior equation: CORRECT.** In the region where $U=0$, (4.7) gives

\[
V_0=-L^{-1}(2D\eta M_\infty+dM_\infty').
\]

Hence $V_0=0$ implies $dM_\infty'+2D\eta M_\infty=0$, with solutions $M_\infty=c(1-\eta^2)^D$ on $(-1,1)$. Oddness of $U$, and therefore of $M_\infty$, forces $c=0$. These steps are **CORRECT**. In the manuscript's range $0<D<1/2$, $C^1$ endpoint regularity of $M_\infty$ already forces $c=0$, even without oddness. Thus “sharp” should not be read as a minimal-hypothesis claim. [NS (4.7), p. 26; (4.29), p. 33](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=26).

**Reading (4.16) and its tail constant: CORRECT with the canonical pressure and heat exterior retained.** Both components agree with the PDF:

\[
Q_s=-W+\frac{(1-h)I-D\eta I_\eta-dJ_\eta+2(h-D)\eta J}{XH},
\]

\[
XN_s=-XWU+D(M-\eta M_\eta)+4h\eta S-dS_\eta
+X(4A\eta\Pi-d\Pi_\eta).
\]

All restored $\eta$ factors are correct. Let

\[
K(\eta)=D(M_\infty-\eta M_\infty')+4h\eta S_\infty-dS_\infty'.
\]

Beyond $X_b$, use the heat exterior, not merely $U=0$. Its physical pressure, normalized to zero at infinity, depends only on $r,t$. The chain rule then gives

\[
4A\eta\Pi-d\Pi_\eta=-2\eta X\Pi_X=-\eta E^2.
\]

Writing $R(X,\eta)=\tfrac12\int_X^\infty E^2\,dx$, we have $S=S_\infty+R$. The heat exterior gives $S_n=0$, so $(XN_s)_X=0$. Moreover $R,R_\eta,XE^2\to0$ for fixed $h>0$, uniformly in $\eta$, using the smooth heat-factor expansion. Consequently $XN_s=K$ throughout that exterior. Equivalently, the exterior remainder cancels exactly:

\[
4h\eta R-dR_\eta-\eta XE^2=0.
\]

This supplies the cancellation missing from the attempt's abbreviated proof. A pressure constant depending on $\eta$ cannot be silently allowed; the normalization matters. [NS (4.16), p. 28; (4.25), (4.29), p. 33; Lemma A.6, p. 138](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=138).

**The displayed tail hypothesis: WRONG.** By (4.11), in the exterior,

\[
T_{0,z}=\frac{XN_s}{L\sqrt{2X}}=\frac{K(\eta)}{L\sqrt{2X}}.
\]

Thus $T_{0,z}\to0$ holds even when $K\ne0$. It does not mean absence of an $r^{-1}$ tail. Replace it by

\[
\sqrt X\,T_{0,z}\longrightarrow0,
\]

or equivalently by $rT_z\to0$ at fixed physical $q,\eta$. The latter product equals $q^{-A}K/L$. The corrected hypothesis forces $K=0$. If the entire exterior-zero-stress clause of Theorem 4.6(ii) is retained, it already implies this stronger condition; calling the unweighted limit a relaxation then obscures which assumption is doing the work. [NS (4.11), p. 27; Lemma 4.9, p. 36](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=36).

**Last ODE step: CORRECT after that fix.** With $M_\infty=0$ and $K=0$,

\[
dS_\infty'=4h\eta S_\infty,\qquad
S_\infty=c(1-\eta^2)^{-2h}.
\]

Boundedness at either endpoint forces $c=0$ for $h>0$. Boundedness of an integral over an infinite radial interval does not follow from smoothness on finite rectangles alone. Here it follows from compact support of $U$ and the uniform integrable heat tail of $E^2$. The sharp form is therefore proved with the weighted tail condition and those explicit hypotheses.

At $h=0$, the ODE formally permits constants. However the prescribed nonzero heat exterior then has $E^2=c_\infty^2/X$, so $S_\infty$ is not finite when $U$ has compact support. The attempt's limiting observation is an ODE degeneracy, not an example in the same finite-moment exterior class. [NS (4.29), p. 33; (A.32), p. 138](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=138).

## C. The checker

Both requested command-line entry points ran under WSL `/usr/bin/python3` 3.12.3, with NumPy 2.4.0, SciPy 1.18.1, SymPy 1.14.0, and mpmath 1.3.0. SciPy was missing and was installed in the user environment. Because both runners normally overwrite committed receipts, I executed their unchanged entry points and requested arguments through `runpy`, intercepting only `Path.write_text` in memory. Computation and stdout were unchanged; neither committed JSON was rewritten.

| Runner | Result | Comparison with committed receipt |
|---|---|---|
| `midplane_barrier.py --order 12` | Exit 0; all 53 Boolean values true; 2.886455126 CPU seconds | All rational coefficients and flags match. Eight floating-point leaves differ, with maximum absolute difference below $4.45\times10^{-16}$ dimensionless units. Timestamp and CPU measurements differ as expected. |
| `moment_matrix_bounds.py` | Exit 0; all 21 Boolean values true; 4.113607211 CPU seconds | Every mathematical field matches exactly as serialized; only timestamp and CPU measurement differ. |

The midplane series gives $X_{\max}=0.1441798809471406$, maximum $a=0.26601861065173016$, and maximum series-versus-ODE difference $3.897743239278384\times10^{-12}$, all dimensionless. Its partial flux is $-0.008901958759995908$, compared with $-0.008901958759995906$ in the receipt. All five functions in `test_ns_midplane_barrier.py` and all three in `test_ns_moment_matrix_bounds.py` also passed when invoked directly. This was execution of the eight test functions, not a pytest session.

The checks catch inconsistencies between the implemented chain-rule identities, angular equation, Riccati equation, sampled ODE solutions, and computed formal coefficients. The moment checker tests Floater's determinant bounds on 160 generated cases and 16 moment blocks, the two-by-two identity, and the sampled linear determinant collapse. These are useful regression checks.

They do **not** establish source fidelity independently of PDF inspection, global inequalities from finite samples, series convergence from twelve coefficients, symmetry of an actual solution from finite parity checks, or novelty. Part A6 verifies (4.16) on one explicit profile, not arbitrary functions. Part C substitutes candidate solutions into already supplied ODEs; it does not derive the tail condition, test the exterior cancellation, or distinguish $T_{0,z}\to0$ from $\sqrt X T_{0,z}\to0$. The tail-condition error therefore passes every flag. The numerical running maximum of sampled $w$ is not a certified supremum, and the finite coefficient-ratio estimate is not a convergence-radius certificate. The full series recurrence is not independently checked against both full profile equations by the midplane residual test.

No counterexample to the substantive Theorem I exists within its stated smooth, positive, regular-axis class with $h\ge0$: the variation-of-constants proof in A applies to every resulting continuous $w$, including every admissible analytic datum accepted by the series solver. Producing $a\ge2$ would require $D_XH\le0$, contradicting that proof. This conclusion rests on the ODE argument, not on the fifteen numerical fixtures. I did not claim an exhaustive numerical search.

## D. The bar of the ask, judged independently

The following is my own literature receipt, from searches and direct source inspection on 2026-10-01 EDT. Search results are discovery aids; the mathematical verdicts below use the primary PDFs.

| Literal search query or direct check | What returned, and consequence |
|---|---|
| `"Navier-Stokes" "dividing plane" "monotone" symmetric core` | Duraiswami-related material and unrelated flow literature; no exact monotonicity lemma identified. |
| `"2609.35406" "shift" core` and `"Lei" "Ren" "2609.35406"` | No useful indexed passage for the shift; retrieved the pinned 245-page v2 PDF directly. |
| `"2609.17642" symmetric moment identities` and `"Navier-Stokes" "symmetric core" "moment"` | Duraiswami and unrelated moment/flow results. Direct reading of p. 20 found the exact proof of the flux obstruction. |
| `"Navier-Stokes" "angular momentum" "symmetric" "barrier" self similar` and `"Navier-Stokes" "stress-free" "monotone" profile` | General transport-barrier, flow, and turbulence results; no matching theorem found. |
| `"dividing plane" "angular momentum" "Navier" "2026"` and `"Navier-Stokes" "dividing-plane" barrier` | The construction's design discussion, Duraiswami, and seminar commentary; no independent quantitative barrier proof identified. |
| `"Navier-Stokes" "no axial" "angular momentum" profile symmetric` and `"midplane" "2h" "Navier"` | General swirl and unrelated midplane calculations; no matching strain-supremum estimate identified. |
| Full-text search of Lei-Ren v2 for `reflection`, `symmetric core`, `maximum principle`, `circulation`, `monoton`, and zero-shift passages; direct reading of Sections 2.5 and 8.1-8.3 | The relevant material is the moment definition on pp. 16-17 and the core/model/shift analysis on pp. 105-114. No universal Theorem I or quantitative margin was located. |
| Direct reading of Duraiswami v1 pp. 20-22 and CIV v2 Remark 2.6 and footnote 9 | Duraiswami proves the symmetry obstruction algebraically; CIV concerns analytic continuation from exterior velocity vanishing, not this barrier. |

**Theorem I.** Proved: **yes**, after the formula/domain repairs in A. New: **the exact general lemma and quantitative margin were not found in this search; priority remains unestablished**. The qualitative reason for breaking symmetry is already in NS p. 5. [Lei and Ren v2, pp. 107-109](https://arxiv.org/pdf/2609.35406v2#page=107) derive the axis slopes, choose the shift $j>0$, separate the zero of their transport coefficient from the pressure symmetry point, and explain the failure of their axial forcing at that point when $j=0$. Their (8.9)-(8.10) are on **p. 108**, not p. 107, in this pinned PDF. Their linear model retains axis data and is explicitly not generally a stress-free nonlinear solution. It does not prove Theorem I for arbitrary smooth cores, nor its running-supremum bound. [Duraiswami pp. 20-22](https://arxiv.org/pdf/2609.17642v1#page=20) discuss centrifugal shear and computed cone failure, but do not provide this ODE positivity theorem. Wanted: useful to readers verifying the design rationale in NS and Lei-Ren, and to the local EXPLANATION-B question about leading-order symmetry. That is an explanatory use, not evidence that a named author posed this exact lemma as an unresolved research problem.

**Theorem II.** Proved: **yes** for the literal identity; **yes after correction** for the tail implication. New: **no** for the literal obstruction. Duraiswami p. 20 explicitly uses $S(\infty,\eta)=0$, oddness of $U$, and $S(\infty,0)=-\tfrac12\int E(X,0)^2\,dX<0$. That is the complete proof, not numerical evidence awaiting promotion to a theorem. Giving the equality on every slice is simply rearranging the same defining identity. Claude's statement that this source contains no proof is **WRONG**. [Duraiswami v1, p. 20](https://arxiv.org/pdf/2609.17642v1#page=20). Lei-Ren Section 2.5 gives the same mixed moment, but does not state the symmetry obstruction there. [Lei-Ren v2, pp. 16-17](https://arxiv.org/pdf/2609.35406v2#page=16). The corrected weaker-assumption tail formulation was not located in these readings, but is an elementary consequence of the printed integrated residual and heat exterior, and its priority has not been established. Wanted: Duraiswami's profile-matching problem demonstrates a concrete use, already served by his proof.

[Constantin, Ignatova and Vicol v2, Remark 2.6 and footnote 9, p. 11](https://arxiv.org/pdf/2609.20803v2#page=11) use nonzero axial velocity at the axis together with exterior meridional vanishing; their (A.12) is on p. 30. Theorem II only ensures velocity somewhere on a slice. It does not establish their axis hypothesis. The attempt correctly avoids claiming that implication.

**The pair does not meet “proved, new, wanted” as two new results.** The newness leg definitely fails for Theorem II; the sharp form as printed also fails at its tail hypothesis. Theorem I supplies a correct, potentially useful explicit proof and bound, but this receipt does not establish mathematical priority. I do **not** recommend starting a research-result write-up in `paper/ns-<slug>/` under the current bar. If a further targeted priority check establishes a contribution in the exact barrier or its quantitative margin, an owner-facing sample could present that one result, credit the known flux obstruction to Duraiswami, and include the corrected tail corollary. It should not claim two new obstructions, novelty for the symmetry-breaking rationale, full flow stability, a full-annulus obstruction, or a conclusion about different leading equations or higher-order constructions.

## E. Claude's target 2 (Lemma A.1 through Floater)

The application is **CORRECT**, and **tool, not a result** is the right disposition. Changing to $x=e^y$, integrating the exponential determinant against positive bump densities, and bounding the separated support gaps gives the stated two-sided determinant bound; cofactors then give an explicit inverse bound. The small-gap loss is $O(\lambda^{-1})$ for the two indicated blocks, with other data fixed and separated. This is a specialization of [Floater v3, Theorems 1-2, p. 3](https://arxiv.org/pdf/2603.19900v3#page=3), applied to [NS Lemma A.1 and Corollary A.3, pp. 126-128](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=126). Two reporting qualifications: `mp.norm(B**-1, 1)` computes the entrywise sum of absolute values, not the induced matrix one-norm (`mp.mnorm`); it remains a valid upper bound but its receipt label is imprecise. [mpmath 1.3.0 norm documentation](https://mpmath.org/doc/current/matrices.html#norms). Also the claimed constant scaled inverse values are limiting trends, not constants across the tested range: the E-block value changes from about 332 to 386 dimensionless units. Floater's Theorem 2 bounds the determinant divided by both Vandermonde products, and a simple linear vanishing assertion assumes an isolated exponent collision, not simultaneous arbitrary collisions. None of these points overturns the application or gives it novelty.

## F. Claude's review of your attempts (reviews/claude/REVIEW-astra.md)

Agreement and disagreements are recorded separately in [RESPONSE.md](./RESPONSE.md). I agree with the substantive algebraic and instrument verdicts and their stated limits. I preserve the distinction between an instrument containing known mathematics and a classification whose novelty is unestablished; the latter is not a finding that its exact statement is already published. The response also corrects the omitted nonzero qualification in one rank summary, separates the higher-order question from the proved leading-order barrier, and removes an imprecise physical label. No disagreement is averaged into a consensus verdict.
