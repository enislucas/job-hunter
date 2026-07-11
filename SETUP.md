# Setup: make Job Hunter yours

Job Hunter ships with fictional demo data so you can see it working before you personalize it. This file is the one-time setup. Budget about an hour. Nothing here sends anything anywhere; it is all local. New to what this even is? Read `GUIDE.html` first, then come back.

If you would rather be interviewed than fill files by hand, open a Claude Code session in this folder and say Go. On a fresh clone it runs the setup interview in `ONBOARDING-GUIDE.md`, asks you one batch of questions, and builds everything below from your answers.

## 0. Prerequisites

- Python 3.10+ with `pip install python-docx` (the render chain needs it).
- Microsoft Edge (the render chain prints PDFs with it; already on Windows).
- Optional: the GitHub CLI `gh`, authenticated once (`gh auth login`), for the weekly portfolio sync.
- Claude Code (or an equivalent agent) opened with this folder as its working directory.

## 1. Your profile and evidence (the honesty backbone)

Create a `profile\` folder and fill three files. The auditors will not let a single CV line ship that is not backed here, so this is the most important step.

- `profile\EVIDENCE-INDEX.md`: every CV-usable claim (a skill, a project, a number, a grade, a role) on its own row, each pointing at proof (a file path, a repo URL, a certificate). Mark each row VERIFIED, CONFIRMED, SELF (self-reported, soft form only), DEAD (a claim that turned out false, keep it named so it never drifts back in), or OFF-CV. Add a never-claim list: every skill or fact that must never appear because you cannot defend it in an interview.
- `profile\PROFILE.md`: the master profile, every fact with a source.
- `profile\STORY.md`: your positioning (the honest one-liner, your two or three pillars, your AI-leverage answer if you build AI-assisted, your weak-point framings, and your voice rules for letters). A worked example lives in the template comments; write yours in your own voice.

Then fill `templates\cv-master.md`: replace every `<placeholder>` with your true facts, keeping the block structure. Drop your LinkedIn export, transcripts, and certificates somewhere under `profile\raw\` and index them.

## 2. Search preferences

Open `inputs\search-preferences.md` and replace the `<placeholders>` with your real fields, country, application language, hours, base location and commute rule, traineeship cap, and salary stance. Newest statement always wins later, so you can steer any time by adding a line.

Pick your sources file. `docs\sources-nl.md` is a real Netherlands handbook; if you hunt elsewhere or in another field, replace it with your own equivalent and point CLAUDE.md's Step 1 at it.

## 3. The values module (optional)

Job Hunter can filter employers through a personal ethical floor. It is OFF unless you turn it on.

- To turn it ON: keep `research\HALAL-RUBRIC-TEMPLATE.md` (a halal/Islamic-permissibility example) or rewrite it as your own floor (an ESG screen, a sector exclusion list, a company-values line). Edit its category table to your standing decisions, and clear the FICTIONAL cached rulings out of `memory\shaykh-rulings.md`. Keep `board\members\01_halal_auditor.md`.
- To turn it OFF: delete `board\members\01_halal_auditor.md`, `research\HALAL-RUBRIC-TEMPLATE.md`, and `memory\shaykh-rulings.md`. The daily loop skips every values step and the honesty auditor leads the board. Nothing else breaks.

## 4. Paths for the portfolio sync

Open `runner\scan-sources.md` and fill the config block at the top: your GitHub username and the absolute paths to your project folders, notes, and coursework. Leave a line blank if it does not apply. The Monday sync reads these; if a folder is renamed later it searches siblings rather than failing.

## 5. The saver, its Startup entry, and the desktop shortcut

The saver (`runner\jh_saver.py`) does two jobs: it serves the app at `http://127.0.0.1:7345/` and it writes your in-app commits straight to disk. Run it once to test, then make it autostart and give yourself a desktop icon. Run these from the repo root in PowerShell.

Test it:

```powershell
pythonw runner\jh_saver.py   # starts silently; check http://127.0.0.1:7345/ping returns {"ok": true}
```

Autostart it at login (a Startup-folder shortcut named JobHunter-Saver):

```powershell
$repo   = (Get-Location).Path
$pyw    = (Get-Command pythonw).Source
$saver  = Join-Path $repo 'runner\jh_saver.py'
$startup = [Environment]::GetFolderPath('Startup')
$sc = New-Object -ComObject WScript.Shell
$lnk = $sc.CreateShortcut((Join-Path $startup 'JobHunter-Saver.lnk'))
$lnk.TargetPath       = $pyw
$lnk.Arguments        = "`"$saver`""
$lnk.WorkingDirectory = $repo
$lnk.IconLocation     = (Join-Path $repo 'runner\job-hunter.ico')
$lnk.Save()
```

Desktop shortcut that opens the app in an Edge app window:

```powershell
$repo = (Get-Location).Path
$edge = (Get-Command msedge -ErrorAction SilentlyContinue).Source
if (-not $edge) { $edge = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' }
$desktop = [Environment]::GetFolderPath('Desktop')
$sc = New-Object -ComObject WScript.Shell
$lnk = $sc.CreateShortcut((Join-Path $desktop 'Job Hunter.lnk'))
$lnk.TargetPath   = $edge
$lnk.Arguments    = '--app=http://127.0.0.1:7345/'
$lnk.IconLocation = (Join-Path $repo 'runner\job-hunter.ico')
$lnk.Save()
```

You should see: a Job Hunter icon on your desktop that opens a chromeless dark window, and a green dot in the app's sidebar meaning the saver is live. If the dot is red, the app still works; it just falls back to downloading commits, which the next run sweeps from your Downloads folder.

Set your Downloads path: the daily loop sweeps your browser's Downloads folder as a backstop. Tell CLAUDE.md (or the assistant, once) where it is if it is not the default `%USERPROFILE%\Downloads`.

## 6. First run

Open Claude Code in this folder and say Go. It reads your profile trio and preferences, hunts, filters, and prepares a few packages. Review them in the app, commit feedback, and you are running. Delete the FICTIONAL demo rows from the `memory\` files whenever you like; the first real run replaces them anyway.
