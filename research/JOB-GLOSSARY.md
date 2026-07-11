# Job glossary: what these weird titles actually mean

For anyone who has noticed that job names are inconsistent everywhere. They are. The same work gets three names at three companies, and the same name means different work at different companies. This glossary covers the common Data Science and Operations Research titles (and their Dutch-market variants) in plain words: what a junior actually does all day, how the title differs from its nearest neighbor, and the 3 to 5 keywords that keep showing up in postings with that title so you can recognize it in the wild.

Each entry ends with a "Fits" line describing the kind of evidence that matches it. Map those archetypes to your own portfolio in profile\EVIDENCE-INDEX.md. This file is generic; grow it by adding a plain-words entry every time the daily loop meets a new title.

Project archetypes referenced below (map to your own real projects):
- Routing/optimization system: a solver over a real decision problem (routing, scheduling), ideally with an exact model and a heuristic that match.
- Data/ML system: a validated predictive model with honest error metrics, or a data pipeline over a real dataset with tests.
- AI-application system: an LLM app (extraction, retrieval, agents) with a human-in-the-loop gate.
- Stakeholder/delivery evidence: teaching, client work, or a real production pipeline delivered under real constraints.

---

## Data Analyst
What it is: the person who explains what the data says about what happened. A junior spends the day pulling data with SQL, cleaning it, building dashboards (Power BI, Excel), and answering specific questions from the business ("why did returns spike last month"). The most common and most entry-friendly data title.
Nearest neighbor: Data Scientist. The analyst reports and explains the past and present; the scientist builds models to predict the future. If a posting is mostly dashboards and reports, it is an analyst role even if it says "scientist".
Fits: a data/ML system where you handle and make sense of a large real dataset and report the result clearly.
Recurring keywords: SQL, Power BI, dashboards, reporting, Excel.

## Data Scientist
What it is: the person who builds models that predict or classify. A junior frames a question, explores the data, trains and validates a model, and presents what it means. Expect Python (sometimes R), statistics and machine learning.
Nearest neighbor: Data Analyst (predict versus report) on one side, ML Engineer on the other (the scientist prototypes the model; the engineer makes it run reliably at scale).
Fits: a data/ML system with a calibrated prediction model and honest error metrics.
Recurring keywords: Python, machine learning, statistical modelling, predictive, R/Python.

## Data Engineer
What it is: the person who builds and maintains the plumbing that moves and stores data. A junior writes ELT jobs, wires pipelines in cloud tooling (Azure, AWS, Databricks, Snowflake), and keeps data clean and available downstream. Little to no modeling; lots of engineering.
Nearest neighbor: Data Scientist (the engineer builds the plumbing, the scientist drinks the water) and Analytics Engineer (the data engineer moves raw data; the analytics engineer shapes it for analysis).
Fits: a data/ML system with real ingest-and-transform work; the enterprise cloud stack is a common gap to name honestly.
Recurring keywords: SQL, Python, PySpark, Databricks/Snowflake, Azure/AWS, ETL/ELT.

## Analytics Engineer
What it is: the bridge between data engineering and analysis. Takes raw landed data and turns it into clean, tested, documented tables and models (dbt-style) that analysts and BI developers can trust. A junior writes SQL transformations, tests data models, and maintains a warehouse layer.
Nearest neighbor: Data Engineer (infrastructure and ingestion) below it, Data Analyst (consumes the models) above it. The analytics engineer owns the modeling layer in the middle.
Fits: a data/ML system with tested, reproducible data modeling.
Recurring keywords: SQL, data modelling, warehouse, testing, ELT.

## Machine Learning Engineer (ML Engineer)
What it is: the person who makes machine learning run in production, fast and reliably. A junior trains models in PyTorch or TensorFlow, optimizes or compresses them, and packages them for deployment. Heavier on software engineering than a data scientist.
Nearest neighbor: Data Scientist (the engineer ships and scales, the scientist explores) and Data Engineer (the ML engineer owns the model runtime, the data engineer the data runtime).
Fits: a data/ML system showing a deep-learning result and the model-to-decision handoff.
Recurring keywords: PyTorch/TensorFlow, deep learning, deployment, model optimization, Git.

## AI Engineer
What it is: a newer title for the person who builds applications on top of large language and foundation models, rather than training models from scratch. A junior wires up LLM apps, retrieval pipelines (RAG), embeddings, prompting, and evaluation harnesses.
Nearest neighbor: ML Engineer (the AI engineer composes existing foundation models into apps; the ML engineer trains and optimizes models) and Data Scientist.
Fits: an AI-application system (LLM extraction or retrieval with a human confirmation gate).
Recurring keywords: LLM, RAG, embeddings, prompting, LangChain.

## Data & AI Consultant
What it is: a data scientist or engineer inside a consultancy, so the job is the technical build plus client-facing delivery across rotating projects. A junior builds models or dashboards at a client, runs workshops, and translates between the client and the data.
Nearest neighbor: an in-house Data Scientist (the consultant rotates clients and communicates and sells more) and Business Analyst (the consultant is more technical).
Fits: a stakeholder/delivery evidence piece plus an AI-application or data/ML system.
Recurring keywords: Python, SQL, client, stakeholder, Azure/Databricks.
Values note: consultancies with interest-core clients are ask-tier under the values module; check the client mix.

## Business Analyst (quantitative)
What it is: the person who answers business questions with data and sits between the business and the tech team. A junior writes SQL queries, builds quick models in Python or Excel, and turns a messy business question into an analysis and a recommendation. Some versions are unusually quantitative ("create and optimize models for real-time improvements").
Nearest neighbor: Data Analyst (the business analyst is more decision-and-recommendation focused, less dashboard plumbing) and Operations Research Analyst (the business analyst is broader and less mathematical).
Fits: a data/ML or optimization system that turns a real-world question into a concrete recommendation, plus any operations experience.
Recurring keywords: SQL, Python, business, stakeholder, analytics.

## Business Intelligence Analyst / BI Developer / BI Consultant
What it is: the person who builds the reporting layer: dashboards, KPIs, and self-service reporting the whole business uses. A junior writes SQL, builds and maintains Power BI or Tableau dashboards, and defines the metrics behind them.
Nearest neighbor: Data Analyst (BI is more about repeatable dashboards and the reporting stack; the analyst does more ad-hoc, one-off analysis) and Analytics Engineer (the BI developer builds the front-end reports on top of the analytics engineer's models).
Fits: a Power BI certificate plus a visualization layer that turns a solver's or model's output into something a human can read.
Recurring keywords: Power BI, SQL, dashboards, KPI, reporting.

## Operations Research Analyst / Specialist
What it is: the person who uses mathematical optimization and modeling to make operational decisions better: routing, scheduling, capacity, planning. A junior builds optimization models (MILP, LP, heuristics), validates them, and works with operations teams to put them to use. The mathematical heart of the field.
Nearest neighbor: Data Scientist (OR prescribes the best action; DS predicts what will happen) and Supply Chain Analyst (OR is the method engine; the supply chain analyst applies it to a specific domain).
Fits: a routing/optimization system (exact model plus a heuristic that matches the proven optimum).
Recurring keywords: optimization, MILP/LP, AIMMS or OR-Tools, scheduling/routing, Python.

## Optimization Consultant
What it is: an OR analyst inside a software or consultancy house who builds optimization solutions in a vendor tool for clients. A junior models the client's problem in the tool, configures the solution, and delivers it with the client.
Nearest neighbor: Operations Research Analyst (the consultant is tool- and client-centric; the in-house OR analyst owns one company's problems) and Presales Consultant (the optimization consultant builds the real thing; presales sells it).
Fits: a routing/optimization system, especially any story where you reviewed and fixed a flawed model formulation.
Recurring keywords: optimization, AIMMS, supply chain, modelling, client.

## Presales Consultant / Associate Presales Consultant
What it is: the technical seller. Learns the product deeply and builds demos and proofs of concept that show a prospect how the software solves their specific problem. A junior builds industry-specific demos, translates customer requirements into high-level solution designs, and joins sales conversations.
Nearest neighbor: Optimization Consultant (presales sells and demos, the consultant delivers the real project afterward) and Business Analyst.
Fits: a live public demo of a working proof of concept.
Recurring keywords: supply chain planning, demo/proof of concept, B2B sales, solution design, client.

## Supply Chain Analyst
What it is: the person who applies data and OR to the flow of goods: demand, inventory, distribution, capacity. A junior analyzes supply chain data, runs planning or optimization tooling, and builds forecasts and inventory policies.
Nearest neighbor: Operations Research Analyst (the supply chain analyst is domain-first, the OR analyst is method-first) and Business Analyst (this one is supply-chain-specific).
Fits: an optimization system on assortment, inventory, or distribution, reinforced by any warehouse or operations experience.
Recurring keywords: supply chain, planning, inventory/forecasting, optimization, Excel/Power BI.

## Planning Analyst
What it is: a close cousin of the supply chain analyst, focused specifically on planning: production, workforce, capacity, timetabling. A junior builds and runs planning models and schedules, balances competing constraints, and reports on utilization.
Nearest neighbor: Supply Chain Analyst (the planning analyst is scheduling and capacity focused; the supply chain analyst covers the wider goods flow).
Fits: a scheduling optimization system (a real staged-relaxation planning model), plus any utilization/overbooking work.
Recurring keywords: planning, scheduling, capacity, optimization, forecasting.

## Quantitative Analyst (Quant)
What it is: the person who builds rigorous mathematical and statistical models for decision-making, often finance-flavored (risk, pricing, investment) but also used for any heavy-math modeling role. A junior implements quantitative models, does statistical analysis and validation, and codes in Python or R.
Nearest neighbor: Data Scientist (the quant is more mathematically rigorous and often domain-specific) and Operations Research Analyst (the quant leans stochastic and statistical modeling; OR leans optimization).
Fits: a data/ML or optimization system with a rigorous validation (an exact method validated against brute force, for example).
Recurring keywords: quantitative, modelling, statistics/econometrics, Python/R, validation.
Values note: the "quant" label often sits on finance-adjacent employers, many of which may be ask-tier or excluded under a values filter; check the values tier before the job description.

## Research Software Engineer
What it is: the person who builds and maintains the software and tools a research or data team relies on. A junior writes clean, tested code, often full-stack (Python plus JavaScript or TypeScript, React), contributes to open-source, and builds visualization or data tools. More engineering than analysis.
Nearest neighbor: Data Engineer (the RSE builds applications and tools; the data engineer builds data pipelines) and Data Scientist (the RSE ships software; the scientist ships analysis).
Fits: a shipped, tested tool with a live demo or packaged executables.
Recurring keywords: Python, JavaScript/TypeScript, open-source, tests, Docker.

## Data Science Trainee / Traineeship / Graduate Programme
What it is: less a job than a structured entry path. A cohort program takes a recent graduate, trains them (SQL, cloud, Power BI, soft skills), and rotates them through roles or client placements. A junior does classroom-style training plus real project work.
Nearest neighbor: a direct Junior role (a traineeship adds structured training and rotation, often a secondment model) and an Internship (a traineeship is a paid employee track and longer).
Fits: a stakeholder/delivery evidence piece that proves you deliver under real production conditions.
Recurring keywords: traineeship, graduate, rotation, training, junior.
Values and duration notes: many are secondment models with interest-core clients (ask-tier), and many run longer than 12 months (out of scope if you cap traineeship length).

## Internship (Stage) and Working Student (Werkstudent)
What it is: contract shapes, not job content. An internship is a fixed-term, study-linked placement (sometimes thesis-linked). A working student is an ongoing part-time role, typically 16 to 24 hours a week, alongside enrollment. The technical work is whatever the underlying title is, at reduced hours.
Nearest neighbor: each other (hours and study linkage differ) and a Trainee (interns and working students stay enrolled students; a trainee is a graduate employee).
Fits: any archetype, depending on the underlying title.
Recurring keywords: internship/stage, werkstudent, enrolled, part-time, thesis.

## Business Process Automation and Optimisation (junior)
What it is: the person who improves how an organization's own internal processes run, using data, automation and light optimization. A junior maps business processes, spots automation opportunities, and builds dashboards and simple automations (Power BI, SQL, Python, VBA, DAX).
Nearest neighbor: Operations Research Analyst (process automation is broad and tool-light; OR is deep mathematics) and Business Analyst (this one is automation-and-efficiency focused).
Fits: any process-improvement or quality-gate automation work, plus an operator's eye for inefficiencies.
Recurring keywords: process, automation, optimisation, Power BI, SQL/VBA.

## Forecast Analyst / WFM Forecasting / Forecast Analytics
What it is: the person who predicts future demand or workload and improves the forecasting method itself. A junior analyzes historical data, runs and tunes statistical forecasts, checks accuracy, and works with planning tools.
Nearest neighbor: Data Scientist (the forecast analyst is time-series and planning specific) and Planning Analyst (the forecast analyst produces the forecast the planner then plans against).
Fits: a predictive model, with the honest note that dedicated time-series forecasting is a distinct skill from classification.
Recurring keywords: forecasting, time-series, statistics, demand/workforce, forecasting tools (Kinaxis, Blue Yonder).
