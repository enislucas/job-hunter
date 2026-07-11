# Sources: the read-only hunting handbook (Netherlands)

This is a real, useful Netherlands job-hunting handbook, kept as-is in the public template because it is genuinely handy. Scope: Netherlands, English-language internships, working-student, entry-level, and traineeships of 12 months or less, in Data Science and Operations Research. It shows how to search each source read-only, with no account and no automated application, ever. Prepare only, never submit. If you hunt in a different country or field, replace this file with your own equivalent.

Standing rules for every source: read at human pace, never loop through search-result pagination automatically, never store or republish listings beyond what you need to decide whether to apply, and never automate any apply, message, connect or follow action.

## Title set used to build every query

Core titles: Data Analyst, Data Scientist, Data Engineer, Machine Learning Engineer, Business Intelligence Analyst, Analytics Engineer, Operations Research Analyst, Optimization Consultant, Supply Chain Analyst, Planning Analyst, Pricing Analyst, Business Analyst (quantitative).

Level and contract modifiers: Intern, Internship, Working Student, Werkstudent (keep the Dutch legal term even in English searches, employers use it), Trainee, Traineeship, Graduate Programme, Junior, Entry Level, Starter.

These match research\JOB-GLOSSARY.md, so title reasoning stays consistent across the pipeline.

---

## 1. Indeed NL (nl.indeed.com)

Read-only: no account needed to view search results or full job pages. An account is only for Indeed's own "easily apply" and saved searches.

URL pattern: `https://nl.indeed.com/jobs?q=<query>&l=<location>&fromage=<days>&jt=<jobtype>&radius=<km>`

Exact query strings:
- `q="data analyst"&jt=internship`
- `q="data scientist" (intern OR graduate OR junior)`
- `q="operations research"`
- `q="supply chain analyst" (junior OR intern)`
- `q="business analyst" junior`
- `q="planning analyst"`
- `q="pricing analyst"`
- `q=werkstudent data`
- `q=traineeship data`
- Location: `l=Nederland` for the whole country, or `l=<your-city>&radius=50` for a commute-realistic sweep.
- jt values that work: fulltime, parttime, contract, internship, temporary.
- Freshness: `fromage=1`, `fromage=3`, `fromage=7`.

English filter: use the sidebar "Vacaturetaal" checkbox for Engels. A URL language shortcut did not reliably filter (results were still mostly Dutch), so rely on the sidebar checkbox and still eyeball each posting's language.

Refresh cadence: daily, with `fromage=1` or `2`. Generic titles return 1,000-plus hits and turn over multiple times a day.

ToS: Indeed's ToS requires prior written permission for robots/spiders/automated means and forbids automating the apply flow; robots.txt disallows `/job/`, `/jobs/[country]/`, `/viewjob?`, `/jobroll` for general bots. Practical read: reading rendered search and detail pages one at a time at human pace is the ordinary use; never build an unattended `start=` pagination loop, never automate submission.

---

## 2. LinkedIn Jobs (public pages)

Read-only: the guest (logged-out) view shows the results list and most individual job pages, but a sign-in modal appears after a limited number of results or scrolling. Treat guest view as good for the first page or two of any query only.

URL pattern: `https://www.linkedin.com/jobs/search/?keywords=<query>&location=Netherlands&f_TPR=<seconds>&f_E=<levels>&f_JT=<types>`

Exact query strings:
- `keywords="data analyst" intern&f_E=1,2`
- `keywords="data scientist" graduate&f_E=1,2`
- `keywords="operations research"&f_E=1,2`
- `keywords="working student" data`
- `keywords="supply chain analyst"&f_E=1,2`
- `keywords=traineeship data analytics`
- Parameters (unofficial, corroborated): `f_TPR=r86400` past 24h, `r604800` past week, `r2592000` past month; `f_E`: 1 Internship, 2 Entry level (use `1,2`); `f_JT`: I Internship, F Full-time, P Part-time, T Temporary, C Contract.

English filter: no language facet exists. Most NL tech and international postings are already English; skim each one manually.

Refresh cadence: daily with `f_TPR=r86400`. High volume and heavily duplicated by recruiter cross-posting, so a tight 24-hour window avoids re-reading the same postings.

ToS, the strictest here: the User Agreement (section 8.2) forbids crawlers, plugins and bots, and forbids copying data obtained through aggregators; robots.txt disallows the guest search paths themselves. LinkedIn actively enforces. Practical read: lowest automation tolerance of all sources. Read a small, bounded number of individual pages per run, the same as a human clicking a handful of links, never paginate automatically, never automate any action.

---

## 3. Magnet.me

Read-only: no account needed to browse and read full vacancy text. Account only to apply, follow, or save.

URL pattern: `https://magnet.me/en/vacatures?query=<query>&country=nl`. On-page filters: job type (Internship, Graduate Internship, Traineeship, Job), work-experience band, education level (MBO, HBO, WO bachelor, WO master), function, sector, salary, distance. Use the on-page checkboxes and read the resulting URL rather than hand-building the job-type facet.

Exact query strings: `query=data+analyst`, `query=data+scientist`, `query=operations+research`, `query=supply+chain`, `query=business+analyst`, `query=working+student+data`, each with the Internship or Traineeship checkbox.

English filter: no dedicated English-only checkbox; the `en` vs `nl-NL` path only changes the interface, not posting language. Bias English by using English keywords (internship, not stage) and skip Dutch teasers by eye.

Refresh cadence: every 2 to 3 days. Graduate/student focused, turns over slower than Indeed or LinkedIn.

ToS, with a real nuance: robots.txt is unusually open (`Allow: /`, `Crawl-delay: 1`) but specifically disallows any URL containing `query=` or `country=`, which is exactly what the search box produces. Practical read: do the keyword search interactively (a human or a single one-off read, not a repeated bot loop on that URL), then read plain listing pages without those parameters (for example `/nl-NL/vacatures/amsterdam`) and individual vacancy pages reached by following links, respecting the 1-second delay.

---

## 4. AcademicTransfer

Read-only: no account needed; every listing and the search are open.

URL pattern: `https://www.academictransfer.com/en/jobs/?keyword=<query>`, with discipline and hours filters and Academic / Non-academic / All tabs.

Exact query strings: `keyword=data+science`, `keyword=operations+research`, `keyword=data+analyst`, `keyword=research+assistant`, `keyword=optimization`, `keyword=machine+learning`. Use the Non-academic tab to surface research-support and technical staff roles rather than PhD or postdoc positions.

Fit note: primarily PhD, postdoc and academic-staff postings, so a low but occasionally valuable hit rate for junior researcher, research software engineer or data-steward roles at TU Delft, TU Eindhoven, CWI and other research institutes that are genuinely 12-month-or-less and non-PhD. This is the natural board for Dutch-university leads.

English filter: not needed, every listing is in English by default.

Refresh cadence: weekly; academic postings turn over on the order of weeks.

ToS: Terms cover personal data and cookies only; robots.txt disallows only `/account/` and `/apply/`. Best practice: set up the built-in saved-search RSS or email alert per core query instead of polling, a sanctioned automated-refresh channel.

---

## 5. iamexpat jobs

Read-only: no account needed to browse or read. Account only for alerts and click tracking.

URL pattern: `https://www.iamexpat.nl/career/jobs-netherlands?search=<query>`, with facets for location, category, work arrangement, required language, career level and job type.

Exact query strings: `search=data+analyst`, `search=data+scientist`, `search=operations+research`, `search=supply+chain`, `search=working+student`, `search=graduate+programme`, `search=trainee`. Check the Career level facet on the day for Student, Entry level or Graduate values.

English filter: the whole site is English by design (an expat portal) and exposes a Required-language facet, so a search can specifically require English or exclude Dutch-required roles. One of only two sources built around the English-speaker use case (with Undutchables).

Refresh cadence: every 2 to 3 days.

ToS: robots.txt disallows `/job/`, `/jobProvider/`, `/jobs-iframe/`, but not the `/career/jobs-netherlands` search and listing paths. Since the canonical single-posting route `/job/` is disallowed, read individual postings by following on-page links from the listing page, not by mass-requesting `/job/` URLs.

---

## 6. Undutchables

Read-only: no account needed to browse the vacancy list or read postings. Registering a profile is optional, only for applying through the agency.

URL pattern: keyword search box at `https://undutchables.nl/vacancies`, with Discipline (Administrative, Commercial, Financial, IT-Engineering, Logistic, and more) and spoken-language filters.

Exact query strings: "data analyst", "data scientist", "business analyst", "supply chain", "planning", "junior consultant", with Language set to English and Discipline set to IT-Engineering or Commercial. A generalist multilingual agency, not a DS/OR specialist, so expect low hit density; subscribe to the email alert to cover gaps.

English filter: English-speaker-first agency; every listing is in English and there is a dedicated Language filter.

Refresh cadence: weekly; boutique volume, the alert covers the rest.

ToS: no explicit anti-scraping clause found. Small agency, no published crawling policy, so default conservative: read the list and postings at a real job-seeker's pace, no bulk pagination.

---

## 7. Blue Lynx

Read-only: no account needed to browse; account only to apply or upload a CV.

URL pattern: no free-text keyword box was found. Use the pre-built language and sector paths: `https://bluelynx.com/jobs/english-jobs-in-the-netherlands/` plus sector paths such as `/jobs/it-and-software-development-jobs-in-the-netherlands/`, `/jobs/engineering-jobs-in-the-netherlands/`, `/jobs/logistics-jobs-in-the-netherlands/`. Scan titles by hand for data, analytics or OR roles.

English filter: built into the URL structure (`/english-jobs-in-the-netherlands/`), the cleanest language pre-filter of any source here.

Refresh cadence: weekly; low volume, generalist agency.

ToS and reliability: the Disclaimer asserts copyright and requires written permission to copy content. Automated fetches of the disclaimer page and robots.txt both returned HTTP 403 (the main `/jobs/` listing did load), signalling active bot protection. Practical read: treat Blue Lynx as manual-browse-only, a human or a single interactive load, not automated fan-out.

---

## 8. Google Jobs

Read-only: no account at all. Google Jobs is the Jobs carousel inside ordinary Google Search, reached through a normal `https://www.google.com/search?q=<query>`. There is no separate login-free Google Jobs site and no consumer read API.

Exact query strings (plain language works best):
- `data analyst jobs netherlands`
- `data science internship netherlands english`
- `operations research jobs netherlands`
- `working student data amsterdam`
- `traineeship data analytics netherlands`
- `"junior operations research" netherlands`
- Cross-check boards without opening them: `site:linkedin.com/jobs data analyst intern netherlands`, `site:indeed.com/nl data scientist netherlands`.
- Cross-check a named employer: `site:[company].com careers` or `site:[company].nl vacatures`.

English filter: append "english" as a soft signal or use Google Search Settings > Languages. The Jobs panel has location and job-type chips but no language chip, so skim and skip Dutch-only postings by eye.

Refresh cadence: daily; cheap and low risk, resurfaces the underlying boards.

ToS: regular Google Search under Google's general Terms, not a scraping situation, as long as each query is a normal human-rate single search. Avoid any bulk "Google Jobs scraper" tool; automated SERP scraping at volume is against Google's Terms even though a single manual query is not.

---

## 9. Direct career pages

Read-only: no account needed anywhere; career pages carry JobPosting structured data specifically to be indexed.

Method (no single URL pattern):
1. Find the page: `site:[company].com careers`, `site:[company].nl vacatures`, or `"[company]" careers`.
2. Notice the ATS from the URL, which tells you the read pattern: Workday `[company].wd3.myworkdayjobs.com/...` (public filterable list), Recruitee `[company].recruitee.com` (plain public listings), Homerun `[company].homerun.co/`, SmartRecruiters `jobs.smartrecruiters.com/[company]/...`, SAP SuccessFactors (public but JS-heavy). AFAS is HR/payroll software, not an ATS, so an AFAS company still runs a real ATS underneath.
3. Use the page's own search or category filter for Data, Analytics, Operations Research, Supply Chain, Trainee, Intern and Werkstudent, and read every result regardless of exact title match, because small employers mislabel roles (this is why JOB-GLOSSARY.md exists).

English filter: switch the site NL/EN toggle to English first; even then some employers write the vacancy text itself in Dutch, so this stays a judgment call.

Refresh cadence: weekly per company, batched across your whole employer list on one weekly sweep alongside Undutchables, Blue Lynx, AcademicTransfer and Magnet.me.

ToS: ordinary read-only browsing is the intended use; never attempt automated form-fill or submission, and check an individual company's own robots.txt before any repeated automated fetch, since some NL corporates block generic bots on their main domain while wanting the jobs subdomain indexed.

Example direct pages that use these ATS patterns (build your own list from your target employers): careers.philips.com/student/nl/en, careers.signify.com/global/en/internships, sioux.eu student page, jobs.thermofisher.com, careers.ortec.com, jads.nl/vacancies, euflex.nl (TU/e), careers.aholddelhaize.com and werk.ah.nl, careers.bol.com, careersatcoolblue.com, nl.jobs.jumbo.com, haskoning.com/en/careers, careers.klm.com.

---

## 10. Werkzoeken.nl (lowest priority, manual only)

Access could not be reliably confirmed: the homepage and robots.txt both returned HTTP 403 to automated fetch. Known from search results only: search page `https://www.werkzoeken.nl/vacatures/?q=<query>`, a very large mostly-Dutch vacancy pool, with a language filter (English among values) and job-type filters including "stage" and "werkstudent". Try by hand with Dutch role nouns then apply the English language filter: `q=data+analist`, `q=data+scientist`, `q=operations+research`, `q=werkstudent+data`, `q=stage+data`, `q=traineeship+data`. Treat as manual-browse-only; do not spend automated budget here until a human confirms the filters work.

---

## Manual-check list: career sites that block or rotate automated fetching

From live sweeps, these employer career sites blocked automated access (403/410), rotated requisition URLs faster than a fetch could confirm, or ran heavy JavaScript that failed to render. Check each one by hand, at human pace, before assuming an opening is or is not live.

- Signify: careers.signify.com/global/en/internships (some supply-chain intern postings returned HTTP 410 Gone; an Intern Data Analyst was live via LinkedIn).
- bol: careers.bol.com/en/expertise/data-and-analytics/ (best-fit internships churn off the current list quickly).
- Coolblue: werkenbijcoolblue.nl/vacatures/ and careersatcoolblue.com (HTTP 403 on automated access).
- PostNL: postnl.nl/werkenbij/vacatures-voor-hbo-en-wo/ (repeated connection resets; site would not load reliably).
- ProRail: werkenbijprorail.nl/vakgebieden/stages (recurring (Afstudeer)stage listings but the specific URLs had rotated to 404).
- DHL Supply Chain NL: careers.dhl.com/eu/nl/studenten-starters (general programs exist; specific DS/OR requisitions hard to pull). Values-module reminder: an alcohol-logistics unit inside a larger clear group would be excluded; the general group stays clear.
- VDL Groep: werkenbijvdl.nl/vacatures/vakgebieden/ict-automatisering (working-student postings churn; others need 3-plus years). Values-module reminder: a group with a defense subsidiary is ask-tier for defense exposure.
- NS: werkenbijns.nl/werkgebieden/digital/data-analytics (a one-year "Junior Data Talent" program exists and would fit a 12-month cap, but a listing found was "Dutch speaking only"; confirm language before applying).
- Jumbo: nl.jobs.jumbo.com, plus linkedin.com/company/jumbo-supermarkten/jobs or magnet.me/en/company/jumbo (a Junior Data Scientist advertised but location and live status unconfirmed).

Also blocked or stale in other sweeps, worth a manual retry: TomTom (Data Scientist/Engineer intern postings returned "job not found"), Vanderlande and Prime Vision (Students lists showed no live DS/OR), Districon (links broken after a 2026 integration), Werkzoeken.nl and Blue Lynx (403 on fetch), and any Workday-based employer whose deep links go inconsistent (search by requisition number instead).

## Summary table

| Source | Account | Read-only search | English filter | Automated-fetch friendliness | Cadence |
|---|---|---|---|---|---|
| Indeed NL | No | Yes | Sidebar checkbox only | Moderate, human pace, no `start=` loops | Daily |
| LinkedIn Jobs (guest) | No | Yes, capped | None, judgment | Low, guest search path disallowed | Daily |
| Magnet.me | No | Yes | None, judgment | High for plain pages, search endpoint disallowed | 2 to 3 days |
| AcademicTransfer | No | Yes | Not needed, all English | High, plus sanctioned RSS/alert | Weekly |
| iamexpat | No | Yes | Yes, Required-language facet | Moderate, `/job/` disallowed | 2 to 3 days |
| Undutchables | No | Yes | Yes, Language facet | Conservative, no policy found | Weekly |
| Blue Lynx | No | Yes | Yes, in URL structure | Low, 403 on robots/disclaimer | Weekly |
| Google Jobs | No | Yes | Soft, append "english" | High for single human-rate queries | Daily |
| Direct career pages | No | Yes | Site toggle, judgment | High in general, check each robots.txt | Weekly, batched |
| Werkzoeken.nl | No | Unconfirmed | Yes, per site | Unknown, 403 on fetch | Untested |
