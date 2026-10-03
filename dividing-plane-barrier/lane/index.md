# The 2026 forced Navier-Stokes blow-up: sources, ledger, and the pull-back record

Owner-directed 2026-09-30 (registration: `docs/DESIGN-BLOWUP-PULLBACK.md`). This
folder holds the record stage I files from and stage II grades against. Times
in this folder are UTC unless marked EDT.

## Primary sources (the ledger is built from these and nothing else)

| Source | Retrieved | Identity |
|---|---|---|
| OpenAI, "Finite Time Blowup for Navier-Stokes", 166 pp. | 2026-09-30 19:46Z, `https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf` | sha256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`, 2,959,204 bytes |
| OpenAI, "Finite Time Blowup for the Euler Equation", 57 pp. | 2026-09-30 19:47Z, `https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf` | sha256 `a0c234518e6c489e16996805023eb2e75c00b7c03455f7a3a5be2c124954bfdd`, 535,142 bytes |
| github.com/openai/NavierStokesAndEuler (Lean 4.34.0-rc2 over Mathlib) | 2026-09-30 | 2,669 files; 816 modules under `NavierStokes/`, 1,839 under `Euler/`; Comparator targets `NavierStokes.Comparator.navier_stokes_breakdown_R3`, `navier_stokes_breakdown_periodic`; permitted axioms propext, Quot.sound, Classical.choice; last push 2026-09-10 |
| Buckmaster, statement, 4 pp. | 2026-09-30, `https://cims.nyu.edu/~tristanb/statement.pdf` | sha256 `8d7723941bcda2fa55c1e74faa6298e04c706d17ff8abd2ad01878039c621f9d` |
| The literature ledger's arXiv ids | 2026-09-30, each verified at `arxiv.org/abs/<id>` by the literature pass | recorded per entry in `LEDGER.md` |

The PDFs and their extracted text are not committed (they are OpenAI's
documents); the hashes above identify the exact bytes every page and equation
reference in the ledger points at.

## Files

- `LEDGER.md`: the mechanism ledger, human form. One block per move of the
  proof (sections 4 to 10, appendices A to C), per move of the Euler paper, per
  lineage result, per wall, and the endpoint. Each block: statement, obligation,
  mechanism, antecedent, cost, the backward question, a checkable computation
  or "none: pure estimate", pages and equations.
- `ledger.json`: the same, machine form, the input of
  `scripts/file_ns_blowup_corpus.py` (stage I) and `scripts/blowup_pullback.py`
  (stage II). Its SHA-256 is recorded in every manifest that consumes it.
- `digests/`: the section digests the ledger was assembled from, as written by
  the digesting agents (one per section), kept verbatim as the working record.
- `EXPLANATION-<section>.md`: the cortex half of stage II, one motivated
  explanation per section, every claim tagged with the page it rests on;
  assisted research, ungraded, never autonomous production.

## Context (paraphrased; not sources of any ledger entry)

- The video that prompted the ask: Matt Parker, "Has a Millennium Prize Problem
  been solved by AI?", Stand-up Maths, 2026-09-21 (`youtube.com/watch?v=c79PsbkHw4A`).
  Segments: the equations and the Clay alternatives (01:38 to 07:29); the
  result, the schematic and the construction read from the paper, including the
  residual trick and the pulses (07:29 to 13:40); the priority dispute and the
  cost figures (13:40 to 16:11); why mathematicians object, the lost journey,
  the squaring-the-circle and quintic analogies (16:11 to 18:56); pure against
  applied, and what happens next (18:56 to 22:10).
- OpenAI's announcement (`openai.com/index/navier-stokes-solution/`, 2026-09-08):
  about 10,000 concurrent agents, 88 hours, on the order of 130 billion output
  tokens; the Euler problem set first; the Lean translation 17 further hours;
  the prize not claimed.
- Clay Mathematics Institute (`claymath.org/news/navier-stokes-announcement/`,
  2026-09-11): the problem "has apparently been settled"; the review is
  deliberately unhurried; recognition follows publication and community vetting.
- Tao's blog, September 2026: "After Math" (De Toffoli and Duede, 2026-09-12),
  "Happy, those able to know the causes of things" (Guillen, 2026-09-13), "If
  math is more than proof, we need to better celebrate the rest of it"
  (Sanderson, 2026-09-18), and Tao's own "Headlines and inside stories"
  (2026-09-23). Gamburd, "The Siren Call of Silicon Leviathan", arXiv
  2609.28591 (2026-09-20).
- Press: CNBC 2026-09-09; NPR 2026-09-22 ("humanity learned nothing (so far)");
  Tufts Daily 2026-09 (Karniadakis on the 70 nm scale where the continuum
  assumption fails for air; Fefferman on Cordoba and Martinez-Zoroa).
- The literature map at `navier.microprediction.org` (pages: equations,
  residual, scaling, core, fluctuating, formal, status, map, timeline).
- Buckmaster's statement: the three results (IPM, Boussinesq, 3D Euler with
  smooth forcing; August 15; Lean August 22), the credit to Cordoba and
  Martinez-Zoroa, and the account of the September 3 to 8 exchange with OpenAI.

## What stands and what does not, in one paragraph

Alternatives (C) and (D) of Fefferman's statement are claimed with a Lean
certificate and a 166-page manuscript that no human had read in full as of
2026-09-20. Alternatives (A) and (B), the unforced problem, are untouched. The
construction is a forced, exactly balanced, non-attracting flow; three
post-publication papers constrain it (analytic forcing near the singular point
forces regularity; the core geometry does not transfer to the similarity
variables as a boundary value problem; blow-up-producing forces are dense
exactly below H^{1/2}), and one names a target for the unforced search (the
positive defect problem). The stance rule of `docs/DESIGN.md` section 1 applies
to every sentence in this folder.
