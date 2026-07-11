# Application page spec (one interactive HTML per package)

File: `packages\<id>\<id>.html`, self-contained, design tokens identical to the dashboard (canvas #04060a, gradient header #4a8fff to #b06bff to #e068ff, green expect #7cd99e, amber #f5c46f, purple #b06bff, code #8fd0ff on #10182a, Segoe UI). localStorage prefix `jh_app_<id>_`. No em dashes.

Sections in order:

1. Header: kicker "Job Hunter · application", company + role as gradient h1, status line (deadline, location, salary if known, values verdict chip in green when the module is on).
2. THE JOB IN PLAIN WORDS: 3 to 5 sentences, what you would actually do all day, from the glossary plus the posting. No jargon without translation.
3. WHY YOU: 3 bullets, each tying one requirement phrase (verbatim, quoted) to one evidence item with its number.
4. VALUES (only if the module is on): verdict, the 2 to 3 sentence reasoning, practice notes, unknowns as unknowns.
5. HOW TO APPLY: the exact URL as a clickable link, expected steps (portal fields, assessments known for this employer), upload checklist table (which file from this folder goes where), the named human if found plus a 3-line outreach note to send yourself.
6. HONEST GAPS: what this vacancy wants that you lack, with a suggested honest interview answer each.
7. QUICK VERIFY (3 minutes, from FAILURE-MODES.md): the standing checks plus any package-specific ones, as checkboxes.
8. YOUR FEEDBACK: status chips (will submit today / submitted / needs changes / declined) plus a why-field; one textarea per artifact: CV, letter, reasoning and company choice, values verdict. Everything autosaves.
9. Footer bar: [Commit feedback] posting `<id>-feedback.md` to the saver (falls back to a download named the same); the toast says the run picks it up next time. [Copy feedback] as fallback. Progress counter.

Also on every page: a `<link rel="icon" href="../../runner/job-hunter.ico">` after the title (Edge app windows show the globe otherwise); a plain "back to Job Hunter" link to `../../dashboard.html` as the first element inside the wrap; and a DOCUMENTS section above How-to-apply with direct relative links to cv.pdf, cv.docx, letter.pdf, letter.docx plus the full folder path in a `.path` span so files can be grabbed without a file-explorer hunt.

The serializer writes markdown: id, date, status, per-artifact feedback, quick-verify boxes state. The gate step ingests these files, updates the ledger and corrections-log, then archives them.
