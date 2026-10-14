# Hypnos Math: the papers and every file published with them

This repository holds the five papers of Hypnos Math, four mathematics manuscripts (two papers and
two notes) and one methods paper, with every file published with them: each paper as a PDF with its
source, every review by an AI model beside the written answers to its findings, and every checker, a
program that recomputes a paper's numbers, beside the output it recorded. Each paper was written by
an AI model at the direction of David Ross: Claude Fable 5 or Claude Fable 5.1, made by Anthropic, or
GPT-6 Astra, made by OpenAI. As of October 14, 2026, none of the papers has been peer reviewed, and no
human mathematician has read them.

## What Hypnos is

Hypnos is a research harness run by one person, its owner. A loop that has run since August 11, 2026, with pauses between runs has three
small open AI models (Gemma 4 31B, Gemma 4 26B and Qwen3 32B), on his own graphics cards, write
one-line candidate ideas about the entries of a notebook of mathematics; code filters them, and
Claude Opus 5, a frontier model made by Anthropic that acts as the judge, keeps about 3 in 100 of the
ideas it reads and writes each one into the notebook as an entry. The four mathematics manuscripts
were written in sessions the owner started, three by Claude Fable 5.1 (Anthropic) and one by GPT-6
Astra (OpenAI). How the parts connect, and why it is built this way, is explained at
https://hypnosmath.org/how.

## Where each paper's question came from

The four mathematics manuscripts did not come from the loop in the same way.

- The unfolded-zeros paper (Claude Fable 5.1, Anthropic) is the only one whose chain begins with a
  small model's own line: a ten-word recall of Kadec's theorem on August 12, 2026, kept by the judge
  as a question; more lines and sharper judge-written questions over five weeks; ten programs; on
  September 28 a session the owner started scored six chains of entries and chose this one; the
  paper says its main theorem answers the question the notebook posed.
- The antiunitary paper (GPT-6 Astra, OpenAI): its motivation is five notebook entries of late
  September, two the judge wrote on small-model lines (one a recall of the classical fact that a
  skew-symmetric matrix of odd order has determinant zero, one a false conjecture) and three results
  of programs. The paper calls them motivation, not premises; its main theorem is a reformulation
  the writing session made; no source is recorded for its key tool, the matching polytope.
- The note on Gil's questions (Claude Fable 5.1, Anthropic): the two questions are J. J. Gil's own,
  from Entropy 28(8):877 (August 4, 2026). They surfaced while frontier models reviewed the
  antiunitary paper; GPT-6 Astra's own review answered the free-value question first. No step of the
  note's mathematics came from the harness.
- The dividing-plane note (Claude Fable 5.1, Anthropic): a separate line of work the owner ran with
  frontier-model sessions on the OpenAI forced Navier-Stokes blow-up manuscript. Claude Opus
  sessions wrote a ledger of the construction's moves and eleven section explanations; the
  explanation of Appendix B asked the question and sketched the answer; a Claude Fable 5.1 session
  ranked it first on its map of open questions and wrote the note. No small model's line is among
  its sources; the ledger was filed into the notebook later, on October 7, 2026, as 183 literature
  entries.

The methods paper reports on the harness's own conduct, not on mathematics.

## The papers

Each paper's page on hypnosmath.org explains it in plain words and links to every file published
with it; each file has a page of its own under https://hypnosmath.org/papers/ with its size and
SHA-256.

- **Approximate Antiunitary Symmetry as a Matching Problem**, a paper written by GPT-6 Astra
  (OpenAI) at the direction of David Ross, dated September 28, 2026.
  The paper: [`antiunitary-symmetry-as-a-matching-problem.pdf`](antiunitary-symmetry-as-a-matching-problem.pdf).
  Its files: [`antiunitary-symmetry-as-a-matching-problem/`](antiunitary-symmetry-as-a-matching-problem/).
  Its page: https://hypnosmath.org/research/antiunitary-symmetry-as-a-matching-problem
- **The unfolded zeros of the Riemann zeta function do not form a Riesz basis of exponentials**, a
  paper written by Claude Fable 5.1 (Anthropic) at the direction of David Ross, dated September 29,
  2026.
  The paper: [`unfolded-zeros-not-a-riesz-basis.pdf`](unfolded-zeros-not-a-riesz-basis.pdf).
  Its files: [`unfolded-zeros-not-a-riesz-basis/`](unfolded-zeros-not-a-riesz-basis/).
  Its page: https://hypnosmath.org/research/unfolded-zeros-not-a-riesz-basis
- **Maximal Coherence for Prescribed Intrinsic Populations and Youla Values: Two Questions of Gil**,
  a note written by Claude Fable 5.1 (Anthropic) at the direction of David Ross, dated September 29,
  2026.
  The note: [`global-maximal-coherence-two-questions-of-gil.pdf`](global-maximal-coherence-two-questions-of-gil.pdf).
  Its files: [`global-maximal-coherence-two-questions-of-gil/`](global-maximal-coherence-two-questions-of-gil/).
  Its page: https://hypnosmath.org/research/global-maximal-coherence-two-questions-of-gil
- **A dividing-plane barrier in the OpenAI forced Navier-Stokes blow-up construction**, a note
  written by Claude Fable 5.1 (Anthropic) at the direction of David Ross, dated October 1, 2026.
  The note: [`dividing-plane-barrier.pdf`](dividing-plane-barrier.pdf).
  Its files: [`dividing-plane-barrier/`](dividing-plane-barrier/).
  Its page: https://hypnosmath.org/research/dividing-plane-barrier
- **Self-Grading Without Self-Deception: Verdict Discipline for a Long-Running Mathematical Research
  Agent**, the methods paper, written by Claude Fable 5 (Anthropic) at the direction of David Ross on
  August 29, 2026. It is published as its PDF alone:
  [`self-grading-without-self-deception.pdf`](self-grading-without-self-deception.pdf).
  Its page: https://hypnosmath.org/research/self-grading-without-self-deception

## How the repository is organized

- Each paper as published, as a PDF at the top level, named after its page on hypnosmath.org. The
  PDFs are here, at the top level, and not in the folders below.
- A folder for each of the four mathematics manuscripts, holding:
  - `main.tex`, the paper's LaTeX source, and its figures where it has any (in `figures/`, or
    `matching-curve.pdf` for the antiunitary paper);
  - `reviews/`: each review beside the written answers to its findings, the file that says what was
    done about each finding and why. Each manuscript had four reviews, by named AI models: two by the
    other company's model and two by models of the writer's own company, each in a fresh session. In
    the file names, `cross-review` and `self-review` mark the first review of each kind; the later two
    are named by their date and their reviewer. The antiunitary
    paper's first two reviews are answered together in `reconciliation-ledger.md`, and its second
    review comes with a seven-page note of the reviewer's own results; the unfolded-zeros paper's
    first review ends with its own written answers. The reviews and the answers keep the internal
    names of the private research repository, and their line numbers point to the version of the
    paper each one read, which was revised afterward. They are published as delivered, with one
    exception: one line of one review, naming a private folder, is withheld from its public copy and
    marked where it stood.
  - `checks/`: the checkers, each beside the output it recorded, and for the antiunitary paper the
    library versions its numerical checker ran with (`requirements.txt`). The antiunitary paper's two
    checkers run from these files, one with the listed library versions and one with only Python's
    standard library; so does the Gil note's checker, which takes about four minutes, and the
    dividing-plane note's checker, which takes about one second, though its test file loads it from a
    path of the private repository and so does not run from these files as they stand. The
    unfolded-zeros paper's checkers read a table of zeta zeros that is not published, so they cannot
    be rerun from these files alone; their recorded outputs are here.
  - for the antiunitary paper, `literature.md`, the search for earlier work made while the paper was
    written;
  - for the dividing-plane note, `lane/`: the material of the line of work the note came from, on the
    OpenAI forced Navier-Stokes blow-up manuscript, begun on September 30, 2026. It holds the ledger,
    a move-by-move account of the manuscript and its Euler companion in 183 entries (`ledger.md`, and
    as data `ledger-v1.1.json` and `ledger-v1.0.json`, the latter frozen as exactly what the small
    models were shown in a one-time test); eleven explanations of the manuscript, one for each of its
    sections 4 to 10 and appendices A to C and one for the Euler companion (`explanation-*.md`), each
    written by a fresh Claude Opus session; and an index of the work (`index.md`).
- `common/hypnos-paper.sty`: the formatting file the four mathematics manuscripts share. Each
  `main.tex` loads it as `../common/hypnos-paper`.
- `MANIFEST.txt`: the SHA-256 and path of every file copied from the private repository to the site,
  which is every file here except the methods paper's PDF (published on September 22, 2026, before
  the list existed), this README and `.gitattributes`. Its last line notes the one withheld line.

## The same bytes as the site

Every file here is byte for byte the one hypnosmath.org serves at the same path, and each file's own
page on the site, under https://hypnosmath.org/papers/, shows its SHA-256, a fingerprint computed from
its bytes. A `.gitattributes` file keeps Git from changing line endings, so a file checked out from
this repository has the same SHA-256 as on the site. The repository is updated once for each release
of the site.

## Contact

The owner would like to know what you make of a paper: right, wrong, known, minor, worth a look, or
not your area. Write to david@hypnosmath.org. He reads and answers replies himself; an error a reader
finds is fixed in the repository and on the site the same day, and the person who reported it is
told; nothing a correspondent sends is given to any AI model without that person's permission.
