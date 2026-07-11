# Failure modes and tripwires

Everything that could go wrong, who catches it, and the tripwire that fires before it reaches the candidate. Every application page's quick-verify checklist derives from this file. Owners are board charters in board\members\.

| # | Failure | Owner | Tripwire |
|---|---|---|---|
| F1 | Made-up or unverifiable fact on CV or letter | Honesty auditor (BLOCKING) | Line-by-line trace to EVIDENCE-INDEX.md before any package ships; untraceable in 2 minutes = BLOCK |
| F2 | Skill overshoot (claiming beyond real current ability) | Honesty auditor | Mapping rule: wording = min(skill-test tier, documented evidence); never-claim list absolute |
| F3 | Soft-skill undersell (teaching, leadership, communication evidence missing where the vacancy asks) | Recruiter lens | Explicit undersell check in charter 03; vacancies naming stakeholder or communication skills must surface the candidate's real teaching, leadership and communication evidence from the index |
| F4 | Stale or misscraped vacancy (applying to a dead or changed posting) | Chair | Re-fetch the live posting in the same run before packaging; vacancy.md carries URL and timestamp; STATUS gone = no package |
| F5 | Wrong company facts in the letter hook | Reader voice + chair | Hook facts verified against the company's own site during the run; unverified = rewrite |
| F6 | CV visual defects (clipping, broken fonts, two columns sneaking in, unreadable PDF) | Render step | Every cv.pdf and letter.pdf is OPENED and eyeballed before shipping; unopened outputs do not ship |
| F7 | Values miss (excluded or ask-tier company packaged; role serving an excluded stream) | Values auditor (BLOCKING, optional module) | Cached verdict required, dated within 12 months; role-proximity check; the knowledge hinge per the rulings cache |
| F8 | Broken or wrong links (application URL, demo, GitHub) | Application page quick-verify | Checklist item: click every link once before the candidate does |
| F9 | Fabricated numbers drifting in from old documents | Honesty auditor | DEAD rows in the evidence index are checked by name against every draft |
| F10 | Recycled letter sentences across applications | Reader voice | Company-name test per package; strategist watches cross-run repetition |
| F11 | Silent phase-skipping or optimistic completion logging | Chair | The gate block must be printed filled-in before work; every log claim points at an artifact |
| F12 | Corrections ignored or half-applied | Chair at gate | Corrections inbox processed FIRST every run; same complaint twice in corrections-log = missing rule, strategist must propose one |
| F13 | Crossed-session interference (another agent writing here) | Session guard | Working directory verified before first write; unexplained edits noted in pipeline_log before continuing |
| F14 | Quota burn (session or model limits hit mid-run) | Usage rules | Glance every 15 to 20 min; high session usage = pause in place; model-quota threshold = safe stop, commit, resume notes |
| F15 | Interview ambush (a package claim the candidate cannot defend live) | Domain expert + STORY.md | Honest-gaps section with suggested answers in every application page; sensitive evidence rows carry prepared framings |

Standing quick-verify template per package (3 minutes of the candidate's time): (1) click the application URL, still live? (2) skim the CV pdf: one column, no clipping, the top third reads right; (3) spot-check the two boldest numbers against the named evidence source; (4) letter hook: is the company fact real? (5) values verdict reasoning: two sentences, sound? (skip this line if the values module is off).
