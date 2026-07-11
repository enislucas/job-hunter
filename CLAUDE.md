# Job Hunter, operating manual

This folder is Job Hunter: a self-improving job-application machine you run by saying Go. This file is the law of every session here. It is written so that a capable model at maximum thinking can run every day alone. When this manual and any other document disagree, this manual wins, except for the user's own words in `inputs\corrections.md`, which win over everything.

New here? The one-time personalization lives in `SETUP.md` (who you are, your evidence, your search preferences, whether the values module is on, your paths and the saver shortcut). Every `<placeholder>` in the memory and template files is filled there. The first-session script for an AI assistant is `ONBOARDING-GUIDE.md`.

## Routing

- User says Go and `PIPELINE-STATE.md` says Phase 3: run THE DAILY LOOP below.
- User says Go and no `PIPELINE-STATE.md` exists yet: this is a fresh clone. Do the setup interview in `ONBOARDING-GUIDE.md` first (or point them at `SETUP.md`), build their profile trio and preferences, then run the loop.
- User says Go mid-build (state says a build is in progress): read `RESUME-NOTE.md`, continue.
- Anything else the user says: it is either a correction (log it, apply it) or a task; when in doubt, do the daily loop after handling the message.

## Invariants (never self-editable; changes only by the user's written word)

1. PREPARE ONLY. Never submit, send, post, email, or create an account anywhere. Drafts stay drafts. The user presses every send button.
2. EVIDENCE OR SILENCE. Every claim on any CV or letter traces to `profile\EVIDENCE-INDEX.md`. The never-claim list there is absolute. Skill wording = the LOWER of skill-test tier (`inputs\skill-test-results.md`) and documented evidence.
3. VALUES FLOOR (optional module). If the user enabled the values module in SETUP.md: `research\HALAL-RUBRIC-TEMPLATE.md` plus `memory\shaykh-rulings.md` (rulings win). ASK-tier is never packaged. When unsure, the values queue, never optimism. If the module is off, skip every values step; nothing else changes.
4. STAY HOME. Never write outside this Job Hunter folder, except the desktop shortcut the user approved and, on the user's explicit accept, a forged project under the PROJECTS-ROOT configured in `runner\scan-sources.md`. Never touch other sessions' folders, processes, or windows.
5. NO EM DASHES in anything human facing. Warm, direct, plain voice per `profile\STORY.md`.
6. HONEST REPORTING. Failures with output. Never log a step as done without pointing at its artifact.
7. USAGE RULES. If your assistant exposes a usage meter, watch it. Near a session limit: pause in place, small sleeps, keep `runner\heartbeat.txt` fresh, resume after reset. Near a model-quota threshold: stop safely (commit, update RESUME-NOTE.md and PIPELINE-STATE.md), do not burn the rest of the quota.
8. MODEL ECONOMY. Use cheaper, faster sub-agents for bulk reading and web sweeps; reserve your most capable model for precision audits. Never spend money; anything that would cost goes to the brief's "Needs your call".

## Hard stops (never decide alone; put in "Needs your call" and continue other work)

Submitting or sending anything; relaxing the values floor or flipping an ASK verdict without a logged ruling; deleting or rewriting memory ledgers; changing invariants or board charters; naming a referee (ask the user each time); real spending; contacting any human.

## THE DAILY LOOP (target: 3 to 7 packages, quality first, about 3 to 5 hours)

### Step 0, the gate. Print this block in chat, filled in, before any work:

```
GATE | date: <today's date> | cwd verified: yes/no | state: <PIPELINE-STATE.md line>
corrections: <n> new items read from inputs\corrections.md and inputs\corrections-drops\*
search preferences read: yes (inputs\search-preferences.md, newest statements win)
journey events parsed: <n> into memory\journey.md | ledger updates: <statuses moved>
rules loaded: <count from memory\RULES.md> | lessons: <count, any at 2+ hits>
last 3 log entries read: yes | board mode today: STANDING/FULL because <trigger>
usage glance: <meter %, session warning yes/no> | skill results present: yes/no
first Friday this month and Forge not yet run: yes/no (if yes, Project Forge runs today)
saver alive: yes/no (GET http://127.0.0.1:7345/ping; if no, RESTART IT: open the Startup shortcut JobHunter-Saver in shell:startup, then re-ping; the saver also SERVES the whole app at http://127.0.0.1:7345/, which is what the desktop shortcut opens)
```

JOURNEY PLAUSIBILITY GUARD: swept journey lines that jump implausibly (an offer with no submitted before it, interview stages on a conversation-only entry, several stages committed within one minute) are probably UI testing: put them in "Needs your call" for confirmation instead of writing them into journey.md blindly.

JOURNEY PARSING at the gate: every status report from the user (free words, any channel) becomes dated events in `memory\journey.md` per its stage vocabulary, and moves the coarse status in `memory\applications.md`. Special stages from the app: `accepted-suggestion` keeps the package prepared and marks it journal-tracked; `rejected-suggestion` moves the ledger row to withdrawn and logs the reason as a correction (it teaches ranking). Dashboard regeneration bakes acceptance states and per-application movement logs from journey.md. On any rejected or ghosted event: write the REASONS block (max 5 lines, hypothesis not autopsy). On offer and beyond: top of "Needs your call". On JOB: keep logging key activities whenever reported; that log drafts the next CV. Ghost rule: 3+ weeks of silence after a submitted stage = ghosted event proposed in the brief (the user confirms).

SEARCH PREFERENCES: `inputs\search-preferences.md` governs discovery and ranking every run. Free text, newest wins on conflict, archives processed change-entries to `archive\corrections\`. It can narrow or redirect anything EXCEPT the invariants (values floor, honesty, prepare-only). The dashboard's preferences box downloads/commits a replacement file; the Downloads sweep treats `search-preferences.md` as a REPLACEMENT for the standing file (after archiving the old one), not as a corrections drop.

DOWNLOADS SWEEP first (zero-friction flow): browser pages that fall back from the saver cannot write into this folder, so a one-click download lands files in the user's Downloads folder (its path is set in SETUP.md). Sweep it read-only for Job Hunter outputs: `*-feedback.md`, `skill-test-results.md`, `journey-update*.md` (parse lines `- <app-id> | <stage> | <note>` into memory\journey.md events plus ledger moves), `search-preferences*.md` (REPLACES the standing inputs file, archive the old one), tip-choice files (also match browser dedupe suffixes like `skill-test-results (1).md`, newest wins). COPY new ones into `inputs\corrections-drops\` and process from there; NEVER delete, move, or edit anything inside Downloads (read-only territory). Avoid re-ingesting by checking names against `archive\corrections\`. (When the saver is up, commits arrive directly in `inputs\corrections-drops\` and this sweep is a backstop.)

SKILL RESULTS FIRST ARRIVAL: the first time skill-test results appear (swept or placed directly), recalibrate skill tiers in EVIDENCE-INDEX per the mapping rule, then re-run the honesty check on the skill wordings of every prepared-but-not-submitted package BEFORE preparing anything new; adjust and re-render where needed and say so in the brief.

Processing corrections: every item in `inputs\corrections.md` and every file in `inputs\corrections-drops\` becomes an entry in `memory\corrections-log.md` (C-number, verbatim words, proposed rule, status). Ledger statuses move only from the user's reports. New values rulings go to `memory\shaykh-rulings.md` and flip cached verdicts in `memory\companies.md`. Rule edits: max 3 per run, each citing its C-number. Then DELETE processed items from inputs\corrections.md (leave the header), and move processed drop files to `archive\corrections\`.

### Step 1, discover (about 60 min, sub-agent fan-out)

Sweep per `docs\sources-nl.md` (or your own regional sources file) with titles from `research\JOB-GLOSSARY.md`. Collect full posting texts immediately and verbatim; postings vanish. Respect each source's language and level filters; traineeships over your cap are out.

### Step 2, remember

Dedupe against `memory\applications.md` and `memory\companies.md`. Never package the same vacancy twice.

### Step 3, screen

Knockouts first (D1 in CV-RULES): work authorization, location or hybrid per rule R-002, availability, language (hard requirements in a language the user lacks are an automatic drop). Then the values verdict if the module is on: cached in `memory\companies.md`, or fresh per the rubric procedure (core business, category table, role proximity, doubt = ASK). Record every fresh verdict with reasoning and date.

### Step 4, decode

Any new title gets a plain-words entry in `research\JOB-GLOSSARY.md`.

### Step 5, rank

Expected value: evidence fit x employer quality x deadline pressure x practicality (commute, hours, and any practice-feasibility signals). Warm routes and known humans first, always (rule R-001).

### Step 6, package the top picks

Per vacancy, folder `packages\YYYY-MM-DD_company_role-slug\`:

1. Re-fetch the posting live before writing anything (stale-vacancy tripwire). Save `vacancy.md` verbatim with URL and timestamp.
2. Values verdict block confirmed and cached (if the module is on).
3. Tailor the CV from `templates\cv-master.md`: pick blocks per the vacancy, mirror its honest keywords, order sections per CV-RULES B10. Every line's evidence id stays in `tailoring-notes.md`.
4. Letter per `templates\letter-framework.md` and CV-RULES C1 to C5. The company hook must be verified against the company's own site during this run (a sub-agent fetches; the letter cites nothing unverified).
5. Render: `py runner\render_cv.py <package-folder>` produces cv.docx, cv.pdf, letter.docx, letter.pdf. OPEN the PDFs and eyeball: one column, no clipping, fonts sane. A package with unopened outputs does not ship.
6. Application page: `<slug>.html` inside the package folder, per `templates\app-page-spec.md` (everything embedded, feedback module, status chips, commit button targeting the saver, quick-verify checklist derived from `FAILURE-MODES.md`).
7. Audits, both blocking, fresh-context sub-agents: honesty audit (every claim vs EVIDENCE-INDEX; kill on any unverifiable claim) and, if the module is on, values audit (verdict sound, ASK never packaged). Their verdicts go in the board minutes.
8. Email-channel applications also get `email-draft.md` (and a mail draft only if mail tools are present in this session).

### Step 7, brief

`briefs\YYYY-MM-DD-brief.md` plus html twin per `templates\brief.md`: TLDR, packages table, values queue, skills delta plus featured project from `skills\PROJECT-QUEUE.md`, new glossary entries, tips (lifecycle below), corrections applied and rules changed, "Needs your call", honest numbers (prepared, submitted, responses, acceptance rate).

### Step 8, regenerate the dashboard

`dashboard.html` per `templates\dashboard-spec.md`: stats from the ledger, application pages newest first, values queue, skills snapshot, tips with parking lot. Bake tip states from `memory\tips.md`. Every application card carries: (a) a countdown (data-deadline for fixed deadlines, data-posted for rolling posts; the page's script renders days live), and (b) a rough success chance as a RANGE with a one-line reason, estimated by this run's model. Estimation rules: fit strength x pool size x practicality; rolling postings DECAY with age (early applicants win disproportionately; a 30+ day old rolling post loses a band), fixed-deadline postings hold until the cliff; every run re-verifies each open posting is alive (dead = status expired in the ledger, card marked CLOSED). Label the numbers honestly as rough model estimates, never as data.

### Step 8b, forge radar (every run, 2 minutes)

Append one dated line to `skills\forge-radar.md`: the 3 to 5 requirement phrases that dominated today's corpus, plus any external signal touched (public labor-market stats, hiring voices, posting trends). This rolling evidence is what the first-Friday Project Forge consumes; without it the monthly proposal starves.

### Step 8c, test requests

Any `test-request-*.md` in the drops (from the dashboard's Skills and Tests panel): build the requested test THIS run as a self-contained HTML in the folder root following the Skill Check's pattern (autosave, commit-or-download, results to inputs\), link it from the dashboard's tests list, and mention it in the brief.

### Step 8d, version

Job Hunter carries a version, shown in the app's sidebar footer and tagged in git. Bump the minor (v2.1, v2.2...) when a run adds or changes a feature, and note it in the brief's TLDR; plain fix-only runs keep the number. History: v2.0, first public release.

### Step 9, self-improve and close

LESSONS hit counters (2+ hits proposes promotion to RULES via board; 12 weeks quiet archives). Board per modes below. Update `skills\SKILLS.md` from today's postings. `linkedin\SUGGESTIONS.md` if evidence shifted. Append `pipeline_log.md` (newest on top: what, counts, spend, deviations). Update `PIPELINE-STATE.md`, commit to git with a plain message. Completion signal: two short beeps, one long, plus one spoken sentence (only when the user is likely awake; log the judgment).

## Board

Charters in `board\members\` are system prompts; use them verbatim when spawning reviewers. STANDING (every run): chair applies the blocking checklists to every package plus one rotating lens. FULL (all seven, parallel, best model for the two auditors, faster models for lenses): on template changes, acceptance below 60 percent over a week, a new employer category, four weeks since last FULL, or the user asks. Verdict format: `VERDICT: PASS | BLOCK | ADJUST` plus max 5 lines. Disagreements are logged, never averaged. Minutes append to `board\minutes.md`. (If the values module is off, the values auditor is not convened.)

## Tips lifecycle

New idea worth the user's time = a tip: add to `memory\tips.md` as `T-nnn | proposed | <one line> | <date>`. Surface in brief and dashboard with three choices. The user's choice arrives via corrections; update the ledger (done, parked, declined). Parked tips resurface monthly, gently, never nag.

## Format contracts, filled examples (FICTIONAL demo data, replace on first real run)

Ledger row:
`| 2026-01-05_borealis_or-analyst-intern | 2026-01-05 | Borealis Logistics | OR Analyst Internship | packages\2026-01-05_borealis_or-analyst-intern | portal | prepared | 2026-01-05 | fits 20h/week |`

companies.md entry: see the `## borealis-logistics` example in memory\companies.md; always include Verdict, Reasoning, Practice notes, Applications, Last checked.

corrections-log entry:
```
## C-001 | 2026-01-06 | source: corrections-drops\2026-01-06_borealis-feedback.md
- What happened: the user marked the letter "needs changes", said the second paragraph sounds generic.
- Their words: "..."
- Proposed rule: letters name one concrete fact from the team's own work, not the company slogan.
- Status: adopted as R-003
```

Board minute:
```
## 2026-01-05 | STANDING | packages: borealis, cobalt
- honesty_auditor: PASS (borealis), ADJUST (cobalt: "led team of 6" not in evidence; changed to "worked in a team of 6")
- values_auditor: PASS both (cached verdicts 2026-01-05)
- rotating lens (recruiter): PASS
- chair: shipped after adjustment; spend 2 sub agents
```

## Skill-tier mapping (binding)

From `inputs\skill-test-results.md` auto-scores per module: 0 to 3 of 6 scorable = "refresh needed", the skill is NOT claimable beyond documented coursework; 4 to 5 = "working basics", claimable as working knowledge when evidence agrees; 6 = solid, claimable up to the evidence level. Written answers can raise a borderline module by one band if genuinely correct; grade strictly and log the grading in the run's log entry. No results file = evidence-only tiers (conservative).

## Monthly rhythm: Project Forge (first Friday)

On the first run on or after each month's first Friday, run the Project Forge per `templates\project-forge-spec.md`: analyze last month's requirement corpus, propose ONE portfolio project as the user's own pitch with the three learning modes (hint, help, nuclear), and on their explicit accept scaffold it at `<PROJECTS-ROOT>\<slug>\` (PROJECTS-ROOT set in scan-sources.md) with the tutor CLAUDE.md from the spec. Provenance stays sacred; forged projects are the one path that can raise skill tiers above the calibration cap, because the user's own hands wrote the code.

## Weekly rhythm (lightweight)

Monday runs also: refresh `skills\SKILLS.md` ranks from the week's corpus, feature a new project from the queue, resurface parked tips if a month has passed, check `interviews\answers\` for new HR interview material to distill into `interviews\INSIGHTS.md`, and run the PORTFOLIO SYNC per `runner\scan-sources.md`: GitHub (gh CLI) plus the project roots configured there, discovering renamed folders rather than failing on them. New work found = evidence-index candidates plus a LinkedIn suggestion; tag project provenance per the gradient in scan-sources.md.

## Feature registry (every moving part and where it lives; check this before assuming something does not exist)

| Feature | Where |
|---|---|
| Daily loop, gate, invariants | this file |
| The app (panels: overview, applications, journal, prefs, skills and tests, projects, values, tips, about) | dashboard.html, regenerated per templates\dashboard-spec.md |
| In-app Commit to disk AND the app itself | runner\jh_saver.py on 127.0.0.1:7345: serves the folder read-only (dashboard.html at /) and accepts whitelisted /save posts; the desktop shortcut opens http://127.0.0.1:7345/ (same-origin, so commits cannot be browser-blocked); autostart via Startup shortcut JobHunter-Saver; gate restarts it if down; fallback remains download + Downloads sweep |
| Downloads sweep (read-only, copy in, never delete there) | gate step, this file |
| Per-application interactive pages | packages\<id>\<id>.html per templates\app-page-spec.md |
| CV and letter rendering | runner\render_cv.py (utf-8-sig; docx via python-docx, pdf via Edge headless) |
| Blocking audits | board\members\01 (optional) and 02 charters, fresh-context agents per package batch |
| Values law (optional module) | inputs\corrections.md > memory\shaykh-rulings.md (SR-nnn) > research\HALAL-RUBRIC-TEMPLATE.md; cache memory\companies.md |
| Skill calibration | inputs\skill-test-results.md + mapping rule in this file; tests listed on the dashboard; requests via test-request drops |
| Search preferences | inputs\search-preferences.md, read before every hunt |
| Journey tracking | memory\journey.md + journey-update drops; reasons-hypothesis max 5 lines |
| Success chances + countdowns | step 8 rules in this file; decay only for rolling posts |
| Project Forge, FIRST FRIDAY of each month | templates\project-forge-spec.md + skills\forge-radar.md (fed every run by step 8b); scaffold to PROJECTS-ROOT only on accept after a co-design conversation |
| Portfolio sync, Mondays | runner\scan-sources.md (gh CLI + configured roots; discovery, not hardcoded paths) |
| Watchdog for unattended runs 2h+ | runner\watchdog.ps1 pattern, register per run, disable at cleanup |
| Usage rules | invariant 7 |
| Tips lifecycle | memory\tips.md; three replies; parked resurface monthly |
| Provenance gradients for projects | profile\STORY.md + runner\scan-sources.md; PROVENANCE.md in forged projects |

## If things look wrong

Foreign edits you did not make: note in pipeline_log, continue carefully. Render chain broken: ship a markdown CV plus a "Needs your call" line, never an unverified docx. A site blocks scraping: record it in the sources notes and move on. Anything feels like a judgment call above your weight: do the safe half, write the question in "Needs your call", keep going. Never block the whole run on one package.
