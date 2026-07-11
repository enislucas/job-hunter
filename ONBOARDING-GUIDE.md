# Onboarding guide: the deep intake

Instructions for the AI assistant running its first sessions with a new Job Hunter user. Read this whole file before saying a word to them. Read CLAUDE.md too; it is the law. This file is the first-days script.

## Why this file demands so much

Job Hunter's original build had an unfair advantage: the assistant had access to the user's complete history (documents, transcripts, old applications, project folders, years of notes). You have none of that. Everything the machine will ever claim on a CV must be earned NOW, through documents and questions. Budget 100 to 120 questions across 2 to 4 sessions of 30 to 45 minutes. This is not bureaucracy; it is the difference between a machine that writes true, specific, defensible applications and a machine that writes pretty fiction.

Fast lane: if the user explicitly wants the 10-minute version, run only Phases 2 and 7 in one batch, mark every claim SELF-tier, keep CV wording conservative, and tell them plainly that depth (and quality) can be added any later session. Offer the deep intake again after their first package review; most people opt in once they see what specificity buys.

## Iron rules for the interviewer

1. Documents beat memory. Whenever a document can answer a question block, ask for the document instead and mine it. People misremember their own grades, dates and titles; paper does not.
2. Batches of 8 to 12 questions, never a wall. Use the structured-question tool if available; otherwise numbered lists. Offer a recommended default wherever one exists so lazy answers are still good answers.
3. "I don't know" and "skip" are always valid and never punished. A skipped answer becomes a conservative default plus an open item, never a guess.
4. WRITE FILES AFTER EVERY BATCH. If the session dies at question 40, questions 1 to 39 must already live on disk. Track position in `inputs/onboarding-state.md` (phase, last question number, open items) so any model can resume cold.
5. Verdict discipline from day one: every extracted claim lands in the evidence index as VERIFIED (a document proves it), SELF (their word, plausible, use softly), or DEAD (contradicted, never use). When a document contradicts their memory, the document wins, and you say so kindly.
6. Their words are law on constraints and preferences; your job is honesty on claims. Never soften their constraints; never let a claim survive that they could not defend in an interview.
7. Tone: warm, direct, zero flattery, no em dashes. One honest compliment is allowed when the evidence genuinely deserves it.

## Phase 0: the two-minute framing (no questions)

Explain in plain words: what the machine does (hunts, filters, prepares; they press every send button), what it never does (submit, email, spend, leave the machine), what this interview builds (their evidence index, story, preferences and optional values floor), and that the depth pays off in every future application. Then start.

## Phase 1: the document harvest (replaces ~40 questions when it works)

Ask them to drop into `inputs/onboarding-drops/` whatever exists of:
D1. Current CV, and EVERY old CV or cover letter they still have (old applications are a goldmine of claims to verify or kill).
D2. Diplomas, transcripts, grade lists (official beats self-made).
D3. LinkedIn profile export (profile page, More, Save to PDF).
D4. Letters of recommendation or reference emails.
D5. Certificates (language, courses, licenses).
D6. Links or paths to project folders and repositories (a GitHub username counts).
D7. Anything they wrote themselves that they consider "their voice at its best" (an essay, a long email, a report) for the voice fingerprint.

Mine everything into evidence rows with sources BEFORE asking Phase 3 questions; then ask only about gaps and conflicts. If they have almost no documents, the question count in Phases 2 to 4 roughly doubles; say so honestly and add a session.

## Phase 2: identity and eligibility (Q1 to Q14)

Q1 Full name as it should appear on applications. Q2 City and country of residence. Q3 Citizenship(s). Q4 Work permit or sponsorship needs where they will apply (a knockout question everywhere; know the honest answer). Q5 Phone for applications. Q6 Email for applications (one inbox they actually watch). Q7 LinkedIn URL. Q8 GitHub or portfolio URL if any. Q9 Languages spoken, honest level per language (spoken vs written if different). Q10 Language(s) applications should be written in. Q11 Degrees held and in progress: exact program names, institutions, start and expected end dates. Q12 Current life status: studying, working, both, neither, until when. Q13 Certifications with dates and verifiable numbers. Q14 Date-of-birth and photo policy per local norms (recommended default in most of Europe: neither on the CV; see `research/ATS-PRINCIPLES.md`).

## Phase 3: history mining (Q15 to Q44)

Q15 List EVERY job, gig, internship, volunteer role and leadership post, even small or informal ones; people always under-report, and the machine decides later what makes the cut. Then loop per item (Q16 to Q21, reserve Q27 to Q44 for the loops):
Q16 What did you actually do, in plain words? Q17 The title exactly as a reference would confirm it (if it was informal, keep it informal). Q18 Numbers you can defend live: how many, how much, how often, what changed because of you. Q19 Who could confirm this, and may we ever name them (recommended referee policy: ask-you-each-time). Q20 Anything about this item that must NOT appear publicly (family businesses, sensitive employers). Q21 Why did it end?
Then: Q22 Education extras: courses beyond the program, self-study with artifacts, competitions. Q23 Community and leadership: clubs, councils, faith or community roles, any teaching or tutoring, with numbers. Q24 Awards, rankings, evaluations (top X percent, a 9/10 review), each with where it is written down. Q25 Past job applications: where, when, how far, how it ended (seeds the memory: never double-apply, learn from history). Q26 The two or three weak spots an interviewer might poke (failed courses, gaps, short stints): write honest framings NOW, before they are needed.

## Phase 4: projects and skill provenance (Q45 to Q66)

Loop per project (Q45 to Q51, reserve Q55 to Q66):
Q45 What is it and what problem does it solve, one sentence, in THEIR words (that sentence often becomes a letter line). Q46 Stack and methods, honestly. Q47 State: idea, half-built, working, shipped, used by real people? Numbers if any (tests, users, accuracy, scale). Q48 Public? Repo and demo links. Q49 PROVENANCE, the question that matters most: what did THEIR hands write versus AI versus teammates? (Gradients: their idea + their hands; their idea, AI-built; AI-built with little input; team project and their slice.) Every project is presented at its true gradient forever; this keeps interviews safe. Q50 Would they happily take 10 minutes of technical questions on it? If not, it appears more carefully. Q51 Anything embarrassing in the repo to clean before an employer looks?
Then: Q52 Self-rate top skills, one honest word each: solid, working, rusty, took-a-course-once. Q53 Which in-demand skills do they know they lack? Q54 Schedule the Skill Check (`Job Hunter Skill Check.html`), explaining the rule that CV wording uses the LOWER of test result and documented evidence, so admitting rust is safe and gaming the test only hurts them.

## Phase 5: story and voice (Q67 to Q78)

Q67 Why this field, the honest version (the cover-letter version gets written from it later). Q68 What work makes them lose track of time? Q69 Two or three short true stories with a number in them (letter fuel: something organized, fixed, built, taught). Q70 What should an employer know that no document shows? Q71 What must applications NEVER say about them (false-feeling framings)? Q72 Words to ban beyond the house bans. Q73 Directness dial for letters: polite-formal to blunt-warm. Q74 Which D7 writing sample sounds most like them, and why? Q75 Realistic dream companies, up to five, and the draw (check later that the draw survives their values screen). Q76 Companies or sectors refused regardless of pay. Q77 Their current 30-second "tell me about yourself", recorded verbatim (improving it becomes a measurable before and after). Q78 How should the assistant address them?

## Phase 6: the values module (Q79 to Q90), optional, always asked, never assumed

Q79 Do they want an ethical floor on employers at all? (No: module off, skip to Phase 7.) Q80 Which framework: the shipped example is an Islamic halal rubric (`research/HALAL-RUBRIC-TEMPLATE.md`); it adapts to other religious frameworks, ESG screens, or a plain exclusion list. Q81 Hard exclusions, any role, no discussion: confirm, edit, extend the template defaults. Q82 Gray categories, one verdict each (allow, exclude, hold-for-authority): consultancies serving excluded clients; mixed-revenue retail; travel and hospitality; payments; pensions and insurance-adjacent; delivery of mixed goods. Q83 Who is their authority for doubtful cases (a scholar, an advisor, their own study)? The machine writes ready-to-ask questions for that authority and NEVER resolves doubt by optimism. Q84 Practice constraints to check per employer: prayer times, Friday or Sabbath obligations, dietary and social-event boundaries, dress, travel limits. Q85 Should values-related facts appear on the CV, and how generically? Q86 Rulings they ALREADY hold from their authority: cache them now, dated; they are law. Q87 Does role proximity matter (working ON an excluded stream versus merely at a company that has one)? Q88 to Q90: the follow-ups these answers always generate.

## Phase 7: search preferences (Q91 to Q104)

Q91 Fields and role families in priority order. Q92 Role levels: internship, working student, entry, mid, contract. Q93 Regions, city constraints, max commute minutes, and whether hybrid stretches the limit (how many office days). Q94 Remote, hybrid, on-site: preferences and dealbreakers. Q95 Hours per week NOW; full-time from when. Q96 Earliest start dates (internships may differ from jobs). Q97 Salary floor, or "suggest from market data" (recommended default). Q98 Program-length caps (traineeships, contracts). Q99 Packages per run (default 3 to 7, quality first). Q100 Channels refused (certain platforms, agencies). Q101 People they already know at target companies: warm routes multiply response rates, the machine always proposes the human first. Q102 Job alerts: prepare the links for them to activate? Q103 Deadline style: apply-early-always or weekly batches? Q104 Calendar constraints coming (exams, travel, religious seasons, a thesis).

## Phase 8: calibration and the never-claim list (Q105 to Q112)

Q105 Present every borderline claim from the documents, one by one: keep, soften, or kill (killed = the DEAD list; this step has caught real contradictions between old cover letters and official transcripts). Q106 Read the seeded never-claim list out loud; they confirm it as binding. Q107 Agree the honest AI-provenance sentence about how their projects were built, so it is never improvised in an interview. Q108 Risk appetite: stretch applications yes or no, and the ratio. Q109 Their three biggest fears about this process; map each to a tripwire in `FAILURE-MODES.md` and show the mapping. Q110 Autonomy check, read back verbatim: never submits, never emails, never spends; if they request auto-submit, the answer is no, with the reasons (platform terms, error blast radius, the value of their final eyes). Q111 Run cadence and which model runs it. Q112 What did this interview fail to ask? (Write the answer into this file's improvement notes; the next user inherits it.)

## Output contract (what must exist on disk when onboarding ends)

- `profile/PROFILE.md`: the synthesized profile, every fact sourced.
- `profile/EVIDENCE-INDEX.md`: claim-to-proof rows with VERIFIED, SELF and DEAD verdicts, plus the binding never-claim list.
- `profile/STORY.md`: positioning, honest weak-spot framings, voice rules, the provenance answer.
- `inputs/search-preferences.md`: their standing orders.
- Values module configured on or off; if on: rubric edited, authority named, cached rulings dated, category table set.
- `memory/applications.md` backfilled with their history; `memory/journey.md` seeded.
- `templates/cv-master.md` blocks filled from the evidence index.
- The Skill Check done or scheduled; tiers applied per the mapping rule.
- `inputs/onboarding-state.md` marked COMPLETE, open items listed.
- A first brief that says, honestly, what the machine knows, what it still lacks, and what it would hunt tomorrow.

Then, and only then, Go means Go.

## Improvement notes (Q112 answers accumulate here)

(none yet)
