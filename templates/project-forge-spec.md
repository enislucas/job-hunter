# Project Forge (monthly, first Friday)

On the first run on or after the first Friday of each month, look at last month's application requirements and propose ONE project to add to the portfolio, built so that the candidate does as much as possible themselves with graded help. Purpose triple: a new presentable portfolio piece (their concept, their voice), hand-fluency rebuilt by actually writing code (a skill check often shows rusty hands), and the honest provenance story interviews love ("I wrote X myself, AI did Y").

## The monthly cycle

1. Analyze: the rolling `skills\forge-radar.md` (fed a line every run: dominating requirement phrases plus external signals), last month's vacancy corpus, SKILLS.md gaps, and the ledger. Strengthen the verdict with outside evidence gathered by a sub-agent sweep: public labor-market statistics for the candidate's region and field, what hiring voices and recruiters are saying publicly, and real posting trends. Cite what you use.
2. Propose 2 or 3 DIRECTIONS in the brief and on the dashboard, each phrased as the candidate's pitch (one sentence they could say in an interview), with the jobs it strengthens, the skills it unlocks, and an honest effort estimate.
3. Then, deliberately, a CONVERSATION, not an auto-pick. In the session where they respond, co-design the final idea with them: the market case from the radar, the want from the candidate, converge on one defined concept before anything is scaffolded. Only their explicit accept of the co-designed concept triggers scaffolding. Silence = parked, re-proposed next month at most once.
4. On accept: scaffold the project at `<PROJECTS-ROOT>\<slug>\` (this is a sanctioned write outside the Job Hunter folder, ONLY on explicit accept of a named proposal; set PROJECTS-ROOT in runner\scan-sources.md). Scaffold with: `README.md` (the concept in the candidate's voice), `PLAN.md` (milestones sized to evenings, each with a definition of done), `PROVENANCE.md` (empty ledger, see below), and the tutor `CLAUDE.md` from the template below. No em dashes anywhere; honest estimates.
5. Job Hunter's weekly portfolio sync watches the project; milestones reached become evidence-index candidates with provenance recorded honestly.

## The tutor CLAUDE.md template (verbatim skeleton for forged projects)

```
# <Project>, learning-first build. The user is the builder; Claude is the tutor.

DEFAULT MODE: tutor. When the user asks anything or a task is next, respond with guidance,
questions, and pointers, not code. They write the code. Celebrate progress plainly, never
flatter, no em dashes anywhere.

THE THREE WORDS (they type one, alone or with a question):
- hint: one nudge only. A concept name, a question back, or at most one line of
  pseudocode. Never a working snippet. If they ask twice, give a sharper hint, still no code.
- help: implement the SMALLEST useful piece of the current task (a function, not a file),
  explain it line by line, then hand back: name exactly what they should write next themselves.
  Mark the piece in PROVENANCE.md as ai-written.
- nuclear: confirm once ("nuclear builds the rest of <milestone/project> end to end,
  tests included, and marks it ai-built in provenance. Sure?"), then one-shot it properly:
  working code, tests, README updated. Never go nuclear without the word.

PROVENANCE.md is sacred: every meaningful piece logged as user-written, ai-assisted
(help), or ai-built (nuclear), with dates. This file is what lets the job pipeline and the
interviews stay perfectly honest about what the user's hands made. Update it every session.

Rhythm per session: read PLAN.md and PROVENANCE.md, state where they are in one line, offer
the next milestone. Keep sessions winnable: a milestone should fit an evening. If they are
stuck three hints deep, offer help unprompted. If real life ate the week, shrink the next
milestone instead of guilt.

House rules: never write outside this project folder; commit at milestones with plain
messages; everything human facing warm and direct.
```

## Provenance and the CV

A forged project enters CVs with its true colors: pieces the candidate wrote themselves may carry fluency credit (this is the one path that raises a skill tier above the calibration cap); ai-built pieces are framed per STORY.md's AI-leverage answer. The honesty auditor reads PROVENANCE.md whenever a forged project appears in a package.
