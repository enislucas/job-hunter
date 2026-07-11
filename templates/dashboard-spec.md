# Dashboard spec (Job Hunter mission control)

## Layout

App shell, three columns: fixed left SIDEBAR (small logo, nav buttons switching panels client-side, last panel remembered in localStorage jh_dash_panel), MAIN column (max 900px), right RAIL (deadlines with live countdowns, quick links, honest numbers; hidden under 1360px). Panels: Overview (stats, up-next note, latest-run note), Applications (cards with countdown and chance per the rules in CLAUDE.md step 8), Journal (see below), Preferences (see below), Skills and Projects (calibrated table plus Forge explainer), Values queue (open questions plus cached rulings summary; hidden if the values module is off), Tips, How it works.

APPLICATIONS panel: sort bar (newest, most likely to land, closest, pay per hour, AI best deal) driven by per-card data attributes (data-date, data-chance, data-dist minutes, data-pay per hour with unknowns estimated and marked, data-deal 0-100 composite judged by the run); accept/reject buttons per card (persist, auto-commit accepted-suggestion or rejected-suggestion with an optional reason prompt; rejected cards grey); cards auto-expire visually when data-deadline passes. Structured cards everywhere use the .cardhead + .kv (label:value grid) pattern; no wall-of-text paragraphs.

JOURNAL panel: shows ONLY accepted applications, each an interview-style row (stage chips: submitted, acknowledged, online-assessment, recruiter-call, interview, offer, rejected, ghosted, withdrawn; a note textarea; localStorage persisted), a history table from memory\journey.md, and one Commit button producing `journey-update.md` containing only touched rows as `- <app-id> | <stage> | <note>`. The gate's sweep parses that file into journey events and ledger moves, then archives the copy.

PREFERENCES panel: interview-style questions with the CURRENT standing answers preselected (role mix, hours, work mode, commute, salary floor, packages per run, free-text extras; keys and localStorage jh_p_*). Commit produces a structured `search-preferences.md`; the saver REPLACES the standing inputs file with it (archive the old one). Bake the preselections from the standing file at every regeneration.

File: `dashboard.html` in the folder root. Regenerated at the end of every run from the markdown truth (ledger, tips, briefs, packages). Self-contained, same design tokens, localStorage prefix `jh_dash_`. Title: "Job Hunter". The desktop shortcut opens the served app (http://127.0.0.1:7345/) which returns this file.

Content inventory (all panels):

1. Header: Job Hunter logo mark (inline SVG, hexagonal crosshair motif, gradient #4a8fff to #b06bff to #e068ff on #04060a), kicker with last-run date, one-line status ("X prepared, Y submitted, Z responses").
2. STATS ROW: prepared total, submitted, responses, interviews, acceptance rate (submitted unchanged / prepared), packages this week. Honest numbers from memory\applications.md only.
3. TODAY / LATEST RUN: the newest brief's TLDR verbatim plus a link to the full brief html.
4. APPLICATIONS: newest first, one card per package: company, role, date, status chip, link to its application page, PLUS per card a live countdown span (class cd, data-deadline for fixed deadlines or data-posted for rolling; the script converts to "closes in N days" / "posted N days ago", red when 3 days or fewer remain or the post is stale) and a rough success chance shown as a range with a one-line reason (class sc). Chance rules live in CLAUDE.md step 8: model estimate, rolling posts decay with age, fixed deadlines hold, every run re-verifies liveness and marks dead posts CLOSED. Label the numbers honestly as rough model estimates, never as data.
5. VALUES QUEUE (module-gated): open questions from memory\shaykh-rulings.md's waiting list, each with its 30-second question text.
6. SKILLS SNAPSHOT: top 5 demands vs your level (from skills\SKILLS.md), the featured project of the week, link to the Skill Check if results are missing.
7. TIPS: from memory\tips.md. Proposed tips show three buttons (accept and done, accept and park, decline) that mark state in localStorage and appear in the feedback commit; the PARKING LOT lists parked tips with their dates.
8. HOW YOUR MACHINE WORKS: the standing short chapter (phases done, the daily loop in a few sentences, where things land, how corrections work, the never-submits promise).
9. SEARCH PREFERENCES: show the standing preferences from inputs\search-preferences.md baked at generation, plus a free-text area and a Commit button producing `search-preferences.md`; the saver REPLACES the standing file with it (archive the old one first).
10. JOURNEY TRACKER: a table from memory\journey.md, one row per application, the stage chain arrow-joined, historical closures included; explanation line that free-words reports become stages, rejections get a max-5-line reasons hypothesis, and a landed JOB keeps logging key activities.
11. Footer: version and links to the newest brief, key docs, the Skill Check, and the guides.

Regeneration procedure (every run, step 8 of the daily loop): read ledger, tips, newest brief; rewrite dashboard.html in full from this spec; never hand-edit the html.
