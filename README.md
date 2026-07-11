# Job Hunter

A local-first, self-improving job-application machine you run by saying Go to a coding agent (built for Claude Code, portable to any capable agent). It hunts real vacancies, filters them by your rules, and turns the good ones into complete, ready-to-send packages: a tailored ATS-safe CV, a matching motivation letter, and a one-page brief that explains what the job actually is and why it fits you. Then it remembers everything and gets better each run from your feedback.

The whole thing runs on plain files you can read, plus a tiny local server that serves a dashboard app and saves your feedback straight to disk. Nothing leaves your machine.

## What makes it different

- Blocking honesty auditor. Every claim on a CV or letter must trace to a row in your evidence index, or it does not ship. There is a never-claim list you can never cross. The point is simple: you should be able to sit in any interview relaxed, because nothing on paper is beyond what you can defend.
- Optional values filter. Turn on a personal ethical floor (the shipped example is a halal/Islamic-permissibility rubric; it is equally usable as an ESG screen or a sector exclusion list). Excluded employers are dropped; doubtful ones are held in a queue for you to check, never guessed. Leave it off and it disappears entirely.
- Journey tracking. Every application's life is logged stage by stage (submitted, interview, offer, ghosted, and so on). Rejections get a short honest hypothesis, not an autopsy. A landed job keeps logging your wins, which becomes the first draft of your next CV.
- Project Forge. Once a month it looks at what the market is actually asking for, proposes one portfolio project as your own pitch, and (only if you accept) scaffolds it as a learning build where you write the code with graded help, so your hands stay sharp and your provenance stays honest.
- Local-first, prepare-only. No data leaves the machine. No accounts, no auto-submit, no auto-email. The machine prepares; you press every send button, every time.

## Honest note on how it was built

Job Hunter was built AI-assisted, and that is on purpose. Its whole philosophy is that directing AI to build validated, tested, honest systems is a real and defensible skill, as long as you are transparent about what your hands made versus what the AI made. The tool practices what it preaches: its own provenance is open, and it holds your CV to the same standard it was built under.

## Quickstart

1. Read `GUIDE.html` (the friendly, zero-jargon walkthrough). Open it in any browser.
2. Follow `SETUP.md` to fill in your profile evidence, search preferences, and the saver shortcut. Or just open a Claude Code session in this folder and say Go; on a fresh clone it runs the deep intake: documents first, then 100+ targeted questions in humane batches across a few sessions, building your evidence index as it goes (see `ONBOARDING-GUIDE.md`).
3. Say Go again for a real run. Review the packages in the app, commit feedback, repeat.

The app ships with clearly-fictional demo data (three demo companies, demo projects) so you can click around before personalizing. `CLAUDE.md` is the full operating manual the agent runs from.

## License

PolyForm Noncommercial 1.0.0. In plain words: use it, change it, share it, for any noncommercial purpose, personal job hunting very much included. Selling it, or building a paid product or service on it, requires separate permission. Required notice: Copyright (c) 2026 enislucas (https://github.com/enislucas). See `LICENSE` for the exact terms. Note: the first public snapshot (a few hours on 2026-07-11) carried the MIT license; copies cloned in that window retain MIT rights for that snapshot only.
