# Appendix C, explained: Realizing the admissible stress cone (pages 157 to 165)

## The problem this appendix is handed

In the annulus the background's leading residual is minus the divergence of a stress $T_0$ (radial fluxes of azimuthal and axial momentum) that the pulses must supply through averaged quadratic products [pp. 9, 11, 27]. Each family contributes one covariance vector per unit squared amplitude, so the attainable stresses are exactly the nonnegative span of two vectors [p. 82]. Weights must be strictly positive wherever $T_0\ne0$ [p. 10]: frozen frames and approximate columns perturb the directions, which only a strict margin survives, and later corrections linearize around these amplitudes [pp. 73, 74, 83].

The shear decides which directions exist. A pulse grows only if $v_s>2$, since the reference growth rate is $\lambda_0^2=2aF_0^2(1-2/v_s)$ [p. 74]; physically, rotation amplifies and axial shear helps [pp. 5, 6]. (Our reading: with $\Omega=u_\theta/r$, $a=-r\Omega'/\Omega$, so for $b_s=0$ the test says $ru_\theta$ decreases outward, a centrifugal criterion of the kind cited on p. 2.) Growing pulses have polarization fixed by $c_0=-\sqrt{(v_s-2)/2}$, which caps cross-shear flux relative to along-shear flux, and the along-shear part must extract energy [pp. 74, 80 to 83]. The outcome is the cone (7.1), equivalent to (4.22) [pp. 31, 74]. Where $v_s\le2$ nothing grows.

The relaxed condition (4.21) drops $v_s>2$; where $v_s\le2$ it reduces to $P_c>2$ [pp. 31, 32]. The join deliberately delivers only this. The axis continuation switches on the stress by multiplying the stress-free shear by a factor $\kappa$ falling from one to a small $\kappa_0$; $P_c$ depends only on the shear's direction and stays above 2, while $v_s$ scales with $\kappa$ and ends below 1 [pp. 151 to 153]. The moment matching then holds $a$ near $0.8$ and $b_s$ near 0 [p. 38]. The paper reserves the extra inequality for the viscous waves [p. 31]. Appendix C thus inherits a profile admissible on an inner collar and from the intermediate power-law interval outward, and merely relaxed in between (MC.1) [p. 158].

## What a person would try first, and why it fails

**Satisfy the full cone during the join.** The paper declines to [p. 31]. Our reading: keeping $v_s>2$ reinstates the directional inequality, whose window $(2,\mathcal U(P_c,J_c))$ closes as $|J_c|$ grows at fixed $P_c$ (our computation from (4.21)), and past the first collar the continuation does not track $J_c$ [p. 153]. The join would have to thread that window while matching five moments and a pressure datum [pp. 37, 38]. Below level 2 the burden disappears.

**Repair the shear on the bad interval by a slow deformation.** Small slow changes of $E,U$ cannot lift $v_s$ from below 1 past 2; large ones fail twice (our reading). Since $a=1-2X\partial_X\log E$ [p. 27], a change confined to the interval keeps the log-radial average of $a$ there, and at fixed direction $v_s=a(1+t_s^2)$ is proportional to $a$: raising it on the bad set lowers it elsewhere. And an order-one shear change sustained over an order-one stretch of $\log X$ changes $E,U$ by order-one factors, hence the moments, pressure, and $p_s$ that feed the cone test and the exterior [pp. 28, 30].

## The idea, motivated

**A picture (our reading of (4.20) to (4.22) [pp. 30, 31]).** Freeze $p_s$ at a point and plot shear vectors $s=(a,-b_s)$. Then $v_s=|s|^2/a$, so level sets of $v_s$ are circles through the origin, and the stable set $v_s\le2$ is the disk with diameter from $0$ to $(2,0)$. The inequality $P_c>v_s$ reads $|s|^2<p_s\cdot s$: the disk with diameter from $0$ to $p_s$. And $P_c>2$ puts $s$ on one side of the line through the origin and the other crossing point of the two circles. (We checked all three numerically.) Admissible shears lie in the crescent between the circles, trimmed by the directional inequality, which is automatic near the inner circle unless $|J_c|$ is large. The bad input lies inside the stable disk on the $P_c>2$ side. The opening: the admissible set is not convex, and such a point is an average of admissible points just outside the stable disk.

**Freeze $p_s$ (MC.1).** The shear uses logarithmic radial derivatives, while $p_s$, the pressure, and the moments use only values, cumulative integrals, and $\eta$-derivatives [pp. 27, 28, 158]; Lemma 4.4(ii) bounds changes in $p_s$ with no radial derivative of a difference [pp. 29, 30]. A small, fast change can therefore move the shear at order one and $p_s$ barely.

**A loop with the given mean.** A fast small oscillation keeps values nearly fixed only if its derivative averages to zero over a period, so the shears visited must average to the original one [p. 158]. Two consequences (our reading). Each admissible member has $p_s\cdot s_L>2a_L$, a linear inequality that survives averaging, so $P_c>2$ at the input is forced: the relaxed hypothesis is exactly what a loop needs below level 2. And along a fixed ray the level is linear, so members must spread in direction; each member's level is $v_s+a\,\mathrm{Var}(t)$ [p. 160].

So write shears as multiples of $(1,t)$ with mean $t_s$ (MC.2) [p. 159]. The obvious $t=t_s+A\sin\theta'$ is not quite right: $P_c(t)=P_c(t_s)+p_{s,2}(t-t_s)$ falls below 2 on one side once $A>(P_c(t_s)-2)/|p_{s,2}|$ (our reading), yet a variance up to $3/a$ may be needed [pp. 159, 160]. The allowed directions form a half-line. The repair is an exponential tilt (C.5), making $P_c(t)-P_c(t_s)=d_0(w-1)$ with $w=e^{\mu p_{s,2}\sin\theta'}/M_e$ a positive weight of mean one [p. 159]. Excursions are bounded on the harmful side and unbounded on the helpful one; log-convexity of $M_e$ makes the variance strictly increasing in $\mu$ (C.6), its asymptotics make it unbounded, and one $\mu_{\max}$ serves everywhere (C.7) [p. 159]. At $p_{s,2}=0$ it is the plain sine [p. 159].

Which level (MC.3)? By (4.22), just above level 2 the directional inequality is nearly free once $P_c(t)>2$ (our reading), so members sit at $v_*=2+\delta_L/2$, a cutoff leaves points with $v_s\ge2+\delta_L/4$ alone (C.9), and the variance is set to $\rho/a$ (C.10) [p. 160]. The margin $\delta_L$ is chosen after $\mu_{\max}$ (C.8) [p. 159], because the window above 2 narrows as directions spread (our computation).

Directions with mean $t_s$ are not yet vectors with mean $(a,-b_s)$ (MC.4). Members $v(1,t)/(1+t^2)$ traversed at speed $d\varphi/d\theta'=a(1+t^2)/(2\pi v)$ average to $(a,at_s)=(a,-b_s)$, and the period is one exactly because $v=a\langle1+t^2\rangle=v_s+aV$, which is why the variance was $\rho/a$ [p. 160]. Compactness gives the margin $\kappa_L$ in (C.2), and the cutoff leaves the interval's ends untouched (C.3) [pp. 158 to 160].

**Put the loop into the radius (MC.5, MC.6).** With zero-mean periodic antiderivatives $\mathcal A,\mathcal B$ of the deviations (C.11), set $E_N=Ee^{\mathcal A/N}$ and $U_N=U+\mathcal B/N$ at phase $N\log X$ (C.12) [p. 161]. The phase is logarithmic because the shear uses $X\partial_X$, which becomes $D_X+N\partial_\varphi$: the $N$ cancels the $1/N$, and the shear follows the loop up to $O(1/N)$ (C.13) [p. 161]. The phase ignores $\eta$, so values and all $\eta$-derivatives move by $O(1/N)$ (C.14), and so do the moments, the pressure, and $p_s$ (C.15), (C.16), with no radial derivative used [pp. 161, 162]. Radial derivatives of the change are only $O(N^{r-1})$, so the modulated profile is not $C^1$-close [p. 161]. The margin $\kappa_L$ absorbs the $O(1/N)$ [p. 162].

**Restore the moments (MC.7, MC.8).** The moments are cumulative, so an $O(1/N)$ error would reach every larger radius and reinstate stress tails beyond $X_b$ [pp. 30, 162]. A patch was reserved for this correction [p. 129]; there $U=0$ and $E=K(\eta)X^{-1/2-\lambda}$ [p. 162]. At zero coefficients the linearization is block diagonal: two $U$-bumps move $(M,J)$, three $E$-bumps move $(I,S,C_p)$ [p. 162]. Each block pairs bumps with distinct powers of $X$, so a Rolle argument on $\det[x_j^{\alpha_i}]$ gives invertibility, and the exactly quadratic remainder yields to a contraction [pp. 34, 162]. The $U$-block degenerates as $\lambda\to0$, so $\lambda$ is fixed before $N$ [p. 162]. With moments equal at the patch's end and profiles equal beyond, Lemma 4.4(i) makes pressure, radial velocity, and stress identical outside (C.17) [pp. 29, 163]. $N$ is chosen last among profile choices and before $q$ [pp. 157, 163].

**The edges.** Since $T_0=F(p_s-s)$, its along-shear component is $F(P_c-v_s)>0$ by (4.23), so $T_0$ cannot vanish inside (MC.9) [pp. 32, 163]. The cone test is homogeneous in $T_0$ [p. 32], so at the edges only the limiting direction matters: along the shear at $X_a$, $(1,0)$ with $t_s=0$ at $X_b$, both on the cone's axis, where the directional quantity reaches its maximum 2, so one $\kappa$ works up to both edges (MC.10) [pp. 163, 164]. The weight $\zeta$ of (C.18) matches each edge's flat vanishing, with the bounds (C.19) (MC.11) [pp. 163, 164]. Flatness matters because the amplitudes are square roots of weights bounded below by a multiple of $\zeta$ [p. 82]; a finite-order zero would have a nonsmooth root (our reading), while these extend smoothly by zero [p. 83]. The rest of Theorem 4.6 is support bookkeeping (MC.12) [pp. 164, 165].

## What breaks without each move

- MC.1: the repair would move $p_s$ at order one, leaving no fixed target for a loop.
- MC.2: a symmetric oscillation of $t$ with enough variance pushes $P_c(t)$ below 2 on one side when $p_{s,2}\ne0$.
- MC.3: members would fail $v>2$ or exceed $\mathcal U(P_c(t),J_c(t))$, or the modulation would reach the interval's ends, breaking (C.3).
- MC.4: the loop's vectors would not average to $(a,-b_s)$, so the antiderivatives would drift and values change at order one.
- MC.5: no actual profile would have the loop as its shear.
- MC.6: $p_s$ could drift outside the margin $\kappa_L$, and the modulated profile leave the cone.
- MC.7: $O(1/N)$ moment errors would propagate outward, giving the exterior stress $r^{-2}$ and $r^{-1}$ tails and shifting the pressure normalization.
- MC.8: the exterior identities of Theorem 4.6(ii) and (v) would be unproved, and constants could depend on $q$.
- MC.9: an interior zero of $T_0$ would leave its direction undefined and force a zero amplitude there.
- MC.10: no single $u_*$ could be chosen in section 7.1, and positivity of $H^{-1}T_{0,*}$ could fail near the edges.
- MC.11: the amplitudes $\sqrt{y_\sigma}$ need not extend smoothly by zero, and the $\zeta$-weighted classes of sections 6 to 9 lose their basis.
- MC.12: axis regularity, the reserved patches, or the heat exterior could be disturbed, leaving Theorem 4.6 incomplete.

## Three questions the appendix leaves open

1. **Is the oscillation necessary?** Could a profile meet every clause of Theorem 4.6 without fast modulation, for instance by switching on the stress without shrinking the shear below level 2 [pp. 152, 153]? It matters because the modulated profile has radial derivatives bounded only by powers of $N$ [p. 161] and every later constant depends on $N$ [p. 163]; a non-oscillatory background would be simpler and closer to a physical vortex.

2. **How large are the margins?** The proof yields finite $d_0,\mu_{\max},\delta_L,\kappa_L,N$ without explicit sizes [pp. 159 to 163]. Members of the modulated set sit near level $2+\delta_L/2$, so (our computation, putting $a_L=v/(1+t^2)$ into p. 74) $\lambda_0^2=2F_0^2(v-2)/(1+t^2)$ is small there. It matters because the lower bound for $\lambda_0$ feeds the pulse design [p. 74], and explicit sizes would show where the asymptotic regime begins.

3. **What exactly can loop averaging repair?** At fixed $p_s$, $P_c>2$ is necessary (our reading, above), and this appendix shows it suffices where $v_s\le2$. Our random sampling, with one case checked at 60 digits, found configurations with $p_{s,1}$ near zero and $|p_{s,2}|$ large where the relaxed set is not convex, so averages of admissible shears reach beyond it. Which shears are exactly repairable? It matters because this set is the interface between Appendix B's join and this appendix; a larger set would give the join more room.

## Page tags

pp. 2, 5, 6, 9, 10, 11, 27, 28, 29, 30, 31, 32, 34, 37, 38, 73, 74, 80, 81, 82, 83, 129, 151, 152, 153, 157, 158, 159, 160, 161, 162, 163, 164, 165.

Extraction note: pages 157 to 165 read cleanly; script letters print plain ($\mathcal U$ as $U$ on pp. 31 and 159, $\mathcal A,\mathcal B$ as $A,B$ on p. 161), and tildes print detached (pp. 161 to 163).
