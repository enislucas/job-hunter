# Portfolio scan sources (weekly sync, CLAUDE.md weekly rhythm)

The pipeline re-scans these every Monday run (or when you say "sync portfolio") and folds anything new into `profile\EVIDENCE-INDEX.md`, `skills\SKILLS.md` evidence levels, and `linkedin\SUGGESTIONS.md`. Paths live here, not in the manual, because your folder structure will change over time; if a path is missing, search siblings for the renamed folder and note it in the run log, never fail silently.

## Configure this first (SETUP.md, step "portfolio sync")

Fill in the real locations of your work. Leave a line blank or delete it if it does not apply to you. Use absolute paths. Add as many project roots as you have.

```
GITHUB-USER: <your-github-username>            # gh repo list <user> pulls new public repos
PROJECT-ROOT: <path to your main projects folder>
PROJECT-ROOT: <path to a second projects folder, optional>
NOTES-ROOT:   <path to a second-brain / notes / agent-infra folder, optional>
PIPELINES-ROOT: <path to other automation or work-flow folders, optional>
STUDY-ROOT:   <path to coursework, grades, assignments, optional>
```

## What gets scanned each Monday

1. GitHub: `gh repo list <GITHUB-USER> --limit 50` plus `gh api users/<GITHUB-USER>/repos` for public metadata; read new repos' READMEs. A new public repo becomes candidate evidence plus a LinkedIn featured-link suggestion. (The gh CLI must be installed and authenticated once; see SETUP.md.)
2. Each PROJECT-ROOT: new folders or new READMEs become new evidence candidates.
3. NOTES-ROOT: orchestration and system-design evidence (an agent network, a second brain, and so on).
4. PIPELINES-ROOT: other automation you have built; discover by listing, do not assume subfolder names, because these restructure often.
5. STUDY-ROOT: new grade documents and new assignments.

Discovery over hardcoded paths: if a configured path no longer exists, list its parent and look for a renamed sibling before giving up, and note the discovery in the run log.

## Provenance tagging (binding for how projects are presented)

Three gradients exist and must be recorded per project so the honesty auditor and your CV stay exact about what your hands actually made:

- (A) Your idea, attempted solo, then AI-built into a full app. Lead with these in interviews; the concept and the itch were yours.
- (B) Fully AI-developed with little direct control from you. Present these as what they prove: you can direct AI to a validated, tested product. Never imply hand-design.
- (C) Systems you designed and directed rule by rule. The strongest ownership story of all.

Interviews and CVs lead with A and C; B is presented as evidence of AI-direction and validation skill, never as hand-design. New projects proposed by the monthly Project Forge should be mold A: your concept, AI execution, presentable, and honestly provenance-tracked in the project's `PROVENANCE.md`.
