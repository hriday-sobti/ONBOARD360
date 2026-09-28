# ONBOARD360 — Personal Contribution & Evidence Dossier
**Document ID:** GOV-CON-001  
**Author:** Hriday Singh Sobti  
**Date:** 2026-09-28  
**Standard:** Personal Contribution Forensics & Stakeholder Value Realization  
**Status:** COMPLETE & VERIFIED  

---

## 1. Executive Summary of Baseline & Added Contributions

### 1.1 Original Baseline (The AS-IS Reality)
NovaBank International operated a 15-year-old customer onboarding architecture that suffered from acute operational friction across four international operating regions (UK/EU, US, APAC, LatAm):
* **Turnaround Time (TAT)**: 58.70 hours from initial submission to account funding.
* **Idle Queue Invisibility**: 52.42 hours (89.29% of elapsed cycle time) spent sitting in unmonitored batch queues between disconnected departments. Active analyst touch time accounted for only 6.29 hours (10.71%).
* **Severe Rework Defect Loops**: First-pass yield was only 58.12%; 33.35% (173,429 applications annually) required manual document rework because web and mobile upload interfaces accepted blurry, glare-obscured, or expired identity documents without validation.
* **Overburdened Compliance & Operations**: 41.12% of all applications (213,842 cases) were escalated to manual human review queues. Compliance analysts were swamped with false-positive watchlist hits caused by rigid exact-string matching.
* **Customer Abandonment & Support Escalation**: 16.25% of all applicants (84,500 customers) abandoned the onboarding funnel before completion, resulting in massive pipeline drop-off. Concurrently, 118,602 inbound customer service tickets were logged ($1.41M cost), 82.8% of which were "Where is my account?" status inquiries caused by lack of visibility.
* **High Unit Cost**: Direct operational expense reached $67.45 per onboarded account, totaling $27.97M annually in direct operating expenditure.

### 1.2 The Analytical Gaps (What Was Missing)
Before this initiative, the bank lacked:
1. **Empirical Process Measurement**: No granular decomposition of active touch time versus queue wait time; management mistakenly assumed analyst slowness caused delays rather than queue buffers.
2. **Defect Root-Cause Isolation**: No statistical Pareto distribution of rework drivers; leadership believed KYC fraud checks caused delays rather than basic photo blurriness.
3. **Queue Dynamics Modeling**: No mathematical model (such as Little's Law) to forecast work-in-progress (WIP) bottlenecks under fluctuating arrival rates.
4. **Structured Requirements Engineering**: No traceable requirements lineage from business problems down to functional API specifications and deterministic business rules.
5. **Intelligent Exception Triage**: No risk-based classification to separate trivial document resubmissions from genuine AML/sanctions alerts.
6. **Reconciled Financial Architecture**: No Activity-Based Costing (ABC) model connecting specific analyst minutes and vendor API fees to overall bank unit economics.

---

## 2. Reconstructed Contributions: Before vs. Change vs. Result

Every major contribution is documented below using the mandatory **Before $\rightarrow$ Change $\rightarrow$ Why $\rightarrow$ Result $\rightarrow$ Evidence** framework:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     TRANSFORMATION CONTRIBUTION MATRIX                                          │
├────────────────────┬────────────────────┬────────────────────┬────────────────────┬─────────────────────────────┤
│ Domain             │ Before             │ Change Introduced  │ Why / Rationale    │ Result & Evidence           │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 1. Process         │ Lead time treated  │ Decomposed 58.70h  │ Pinpoint true time │ Found 89.3% is queue wait   │
│    Decomposition   │ as monolithic delay│ TAT into 6.29h     │ sink rather than   │ (52.42h). PCE is 10.71%.    │
│                    │ (analyst backlog). │ touch & 52.42h wait│ adding headcount.  │ [06_Data_Analysis/          │
│                    │                    │ time per case.     │                    │  eda_analysis.py]           │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 2. Queue Dynamics  │ Static queue size  │ Applied Little's   │ Quantify system WIP│ Proved 3,485 active WIP apps│
│    (Little's Law)  │ assumptions with   │ Law: L = λ * W     │ buffer to size     │ with 3,111 queued idly.     │
│                    │ unmanaged backlogs │ (λ = 59.36 apps/h, │ infrastructure and │ [03_Process_Analysis/       │
│                    │ and SLA breaches.  │ W = 58.70 hours).  │ SLA capacity.      │  ROOT_CAUSE_ANALYSIS.md]    │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 3. Root Cause &    │ Blamed complex KYC │ Pareto analysis of │ Focus engineering  │ Blurry ID (42.1%), Expired  │
│    Pareto Analysis │ regulations for all│ 173,429 rework     │ on top drivers     │ ID (23.0%), Address (18.0%) │
│                    │ rework loops.      │ defect incidents.  │ (83.2% of rework). │ = 83.15% of all rework.     │
│                    │                    │                    │                    │ [root_cause_analysis.xlsx]  │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 4. Upfront Image   │ Raw image upload   │ Client-side OpenCV │ Stop defective     │ Blocks blurry uploads at the│
│    Quality Gating  │ allowed blurry &   │ Wasm gating        │ files before entry │ glass (<800ms). Tested via  │
│                    │ cropped photos into│ (Laplacian var>=150│ into back-office   │ UAT-01 and UAT-02.          │
│                    │ analyst queues.    │ glare <= 8%).      │ queues.            │ [04_Requirements/FRD.md]    │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 5. Automated ID &  │ Manual typing of   │ Cloud OCR MRZ &    │ Eradicate expired  │ Auto-rejects expired IDs in │
│    Address Prefill │ identity details;  │ postal bureau REST │ documents and form │ 650ms; postal code prefill  │
│                    │ frequent typos.    │ prefill APIs.      │ completion typos.  │ cuts entry time by 60%.     │
│                    │                    │                    │                    │ [BUSINESS_RULES.md (BR-002)]│
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 6. Watchlist Fuzzy │ Exact-string match │ Jaro-Winkler with  │ Eliminate false-   │ Cuts false-positive L2      │
│    Screening       │ generated thousands│ phonetic double-   │ positive manual    │ reviews by 47.7%; clears    │
│                    │ of false sanctions │ metaphone matching │ compliance         │ low-risk names instantly.   │
│                    │ alerts.            │ & DOB/country tier.│ bottlenecks.       │ [FRD.md (FR-010)]           │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 7. Straight-Through│ 0% STP; every      │ 60% STP architecture│ Provide consumer-  │ Low-risk apps open account  │
│    Processing (STP)│ application passed │ with real-time Core│ grade onboarding;  │ in < 15m; zero human touch  │
│                    │ through overnight  │ Banking REST API   │ reduce unit cost   │ for 312,000 customers.      │
│                    │ batch queues.      │ provisioning.      │ to $12.55.         │ [to_be_process.bpmn]        │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 8. Machine Learning│ Manual assignment  │ Random Forest      │ Automate self-     │ 100% precision on defects;  │
│    AI Triage & HITL│ of all exception   │ triage engine with │ service; protect   │ 0 compliance risk leakage   │
│                    │ tickets to generic │ zero-leakage human │ bank from AML/PEP  │ on 100 audit test cases.    │
│                    │ queues.            │ compliance gates.  │ regulatory risk.   │ [ai_triage_engine.py]       │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 9. Agile User Story│ Informal feature   │ 6 Epics, 35+ INVEST│ Provide engineering│ 432 story points across     │
│    Engineering     │ wishlists without  │ stories with       │ with unambiguous,  │ 4 sprints; simulated Jira   │
│                    │ acceptance criteria│ Gherkin Given-When-│ testable acceptance│ velocity tracking.          │
│                    │                    │ Then criteria.     │ criteria.          │ [05_Agile/USER_STORIES.md]  │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 10. Traceability   │ Disconnected PRDs, │ 100% bidirectional │ Prove regulatory   │ PNT-01..06 -> BR-01..10 ->  │
│     Engineering    │ spreadsheets, and  │ Requirements       │ compliance and zero│ FR-01..35 -> Stories -> UAT.│
│                    │ isolated test runs.│ Traceability Matrix│ functional gaps.   │ [TRACEABILITY_MASTER.md]    │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 11. Automated UAT  │ Manual ad-hoc spot │ 32 UAT scenarios   │ Guarantee zero-bug │ 160 master test assertions  │
│     Verification   │ checking without   │ and 160-test       │ release readiness  │ pass 100% in 13.99 seconds. │
│                    │ regression safety. │ master Python test │ across code, data, │ [test_onboard360_master.py] │
│                    │                    │ suite.             │ and calculations.  │                             │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼─────────────────────────────┤
│ 12. Activity-Based │ Top-down cost      │ Rigorous ABC DCF   │ Justify $2.85M     │ $22.09M annual net cash     │
│     Financial Case │ estimates lacking  │ model across L1/L2,│ CAPEX to Board with│ savings, 3-Yr NPV $49.50M,  │
│                    │ operational backing│ support, vendors,  │ transparent audit  │ IRR > 200%, 2.0 mo payback. │
│                    │                    │ and cloud OPEX.    │ trail.             │ [financial_model.py]        │
└────────────────────┴────────────────────┴────────────────────┴────────────────────┴─────────────────────────────┘
```

---

## 3. Personal Contribution Forensic Audit

This section details exactly what **Hriday Singh Sobti** personally performed:

### Activity 1: Operational Baseline & Little's Law Queuing Model
* **What I Did**: Structured the empirical baseline across 520,000 annual onboarding applications; derived arrival rate $\lambda = 59.36$ apps/hour; calculated Little's Law WIP queues and touch/wait ratios.
* **Why I Did It**: Executive stakeholders incorrectly assumed application delays were caused by slow analyst review speeds. I needed mathematical proof that 89.3% of the delay occurred while files sat untouched in queue buffers.
* **How I Did It**: Formulated Python analytical scripts (`06_Data_Analysis/eda_analysis.py`) and PostgreSQL CTE window queries (`06_Data_Analysis/SQL/02_kpi_reporting.sql`).
* **Tool Used**: Python (Pandas, NumPy, Scipy), PostgreSQL 15, SQLite.
* **Output Produced**: `03_Process_Analysis/AS_IS_PROCESS_INVENTORY.md`, `06_Data_Analysis/eda_analysis.py`.
* **Business Purpose**: Reorient executive strategy from hiring expensive operational staff to eliminating asynchronous queue wait buffers.
* **Result**: Proved that active touch time is only 6.29 hours while wait time is 52.42 hours (Process Cycle Efficiency = 10.71%).
* **Evidence**: Line 25-32 in `06_Data_Analysis/eda_analysis.py`, Test cases `test_063` through `test_072` in `test_onboard360_master.py`.

### Activity 2: Root Cause Defect Isolation (Pareto Analysis)
* **What I Did**: Categorized and quantified 173,429 rework incidents across five distinct defect failure modes.
* **Why I Did It**: Engineering resources were previously diverted into redesigning backend KYC engines, which contributed to less than 5% of defects. I needed to identify where engineering effort would produce the highest yield reduction.
* **How I Did It**: Built frequency tables, cumulative percentages, and 5-Why Ishikawa root-cause logic.
* **Tool Used**: Python, OpenPyXL, SQL window functions (`SUM() OVER()`).
* **Output Produced**: `03_Process_Analysis/ROOT_CAUSE_ANALYSIS.md`, `03_Process_Analysis/root_cause_analysis.xlsx`.
* **Business Purpose**: Direct architectural investment toward client-side capture interfaces.
* **Result**: Isolated that 83.15% of all rework is driven by three preventable upload defects: Blurry Images (42.09%), Expired IDs (23.04%), and Address Proof Mismatches (18.02%).
* **Evidence**: Query 2 in `06_Data_Analysis/SQL/02_kpi_reporting.sql`, `03_Process_Analysis/root_cause_analysis.xlsx`.

### Activity 3: Requirements Engineering & Deterministic Business Rules
* **What I Did**: Authored 10 Business Requirements (BR-001 to BR-010), 35 Functional Requirements (FR-001 to FR-035), and 10 Deterministic Business Rules (BRULE-001 to BRULE-010).
* **Why I Did It**: Bridged the gap between high-level executive goals (e.g., "reduce turnaround time") and technical specifications (e.g., "Laplacian variance $\ge 150$", "Jaro-Winkler match score $< 70$").
* **How I Did It**: Applied BABOK v3 guidelines and MoSCoW prioritization, specifying exact system inputs, algorithms, thresholds, and outputs.
* **Tool Used**: Markdown, PlantUML, OpenAPI/REST schemas.
* **Output Produced**: `04_Requirements/BRD.md`, `04_Requirements/FRD.md`, `04_Requirements/BUSINESS_RULES.md`.
* **Business Purpose**: Provide an unambiguous implementation contract for engineering and compliance sign-off.
* **Result**: Zero ambiguity in system behavior; explicit thresholds defined for Straight-Through Processing, AI Triage, and Mandatory Escalation.
* **Evidence**: `04_Requirements/BRD.pdf`, `04_Requirements/FRD.pdf`, Tests `test_026` through `test_031`.

### Activity 4: Target State Process Architecture (BPMN 2.0 XML)
* **What I Did**: Engineered the TO-BE process model in standard BPMN 2.0 XML format, defining pools, lanes, service tasks, XOR/AND decision gateways, and message events.
* **Why I Did It**: Replaced disconnected departmental handoffs with an event-driven straight-through orchestration model.
* **How I Did It**: Authored valid BPMN 2.0 XML with semantic tags (`<bpmn:exclusiveGateway>`, `<bpmn:serviceTask>`, `<bpmn:laneSet>`).
* **Tool Used**: BPMN 2.0 XML, XML DOM parsers, Draw.io.
* **Output Produced**: `07_Solution_Design/to_be_process.bpmn`, `07_Solution_Design/TO_BE_PROCESS_SPECIFICATION.md`.
* **Business Purpose**: Define how low-risk applicants bypass manual queues and achieve instant provisioning.
* **Result**: Modelled 60% Straight-Through Processing, reducing average non-exception onboarding time from 58.70 hours to under 15 minutes.
* **Evidence**: `07_Solution_Design/to_be_process.bpmn`, Tests `test_144` through `test_146`.

### Activity 5: Machine Learning Exception Triage & HITL Governance
* **What I Did**: Implemented and trained a Random Forest classification model (`07_Solution_Design/ai_triage_engine.py`) to triage exceptions into automated self-service or specialized human queues, with zero-leakage compliance guardrails.
* **Why I Did It**: To prevent minor document errors from flooding Level-1 operations queues while ensuring 100% regulatory compliance for PEP and high-risk AML cases.
* **How I Did It**: Feature engineered risk tiers, defect categories, sharpness scores, and match deltas; established deterministic post-model guardrails.
* **Tool Used**: Python (Scikit-Learn, Joblib, Pandas).
* **Output Produced**: `07_Solution_Design/model/ai_triage_model.joblib`, `07_Solution_Design/AI_TRIAGE_MODEL_CARD.md`.
* **Business Purpose**: Deliver operational scalability without exposing the bank to AML regulatory fines or enforcement actions.
* **Result**: 100% precision across triage classes; zero compliance risk leakage on 100 randomized audit test cases (0% PEP/AML cases leaked to automation).
* **Evidence**: Tests `test_101` through `test_120` in `test_onboard360_master.py`.

### Activity 6: Activity-Based Costing & Discounted Cash Flow Financial Model
* **What I Did**: Built a comprehensive financial model calculating Activity-Based Costing across L1/L2 labor, support inquiries, vendor APIs, and cloud OPEX; computed 3-Year DCF, NPV, IRR, and payback period across Base, Conservative, and Aggressive scenarios.
* **Why I Did It**: Executive approval of the $2.85M CAPEX required an auditable, conservative financial justification grounded in operational metrics.
* **How I Did It**: Structured DCF equations using an 8.5% hurdle rate and phased realization (80% Year 1, 100% Years 2 & 3).
* **Tool Used**: Python (`financial_model.py`), Microsoft Excel (`ROI_model.xlsx`).
* **Output Produced**: `10_Business_Case/financial_model.py`, `10_Business_Case/ROI_model.xlsx`, `10_Business_Case/BUSINESS_CASE_AND_ROI_REPORT.md`.
* **Business Purpose**: Provide the Chief Financial Officer and Retail Executive Committee with capital investment certainty.
* **Result**: Reconciled $22,092,276.10 in annual net cash savings, a 3-Year NPV of $49,501,858.44, an IRR > 200%, and a 2.0-month capital payback.
* **Evidence**: `financial_model.py`, Tests `test_121` through `test_140`.

### Activity 7: Bidirectional Traceability Engineering
* **What I Did**: Architected a 100% bidirectional Requirements Traceability Matrix linking Business Needs to Business Requirements, Functional Requirements, Business Rules, User Stories, Architecture Components, and UAT Cases.
* **Why I Did It**: Guaranteed zero scope leakage, ensured every line of code solved an approved business problem, and satisfied regulatory audit readiness (FCA/FinCEN).
* **How I Did It**: Built a relational mapping framework across markdown and Excel workbooks.
* **Tool Used**: Markdown, OpenPyXL, automated testing scripts.
* **Output Produced**: `00_Project_Governance/TRACEABILITY_MASTER.md`, `04_Requirements/requirements_traceability.xlsx`.
* **Business Purpose**: Enable forward traceability (verifying all requirements are implemented) and backward traceability (preventing unauthorized scope creep).
* **Result**: 100% coverage verified across all 10 Business Requirements and 35 Functional Requirements.
* **Evidence**: `requirements_traceability.xlsx`, Test `test_031`.

### Activity 8: Master Automated Verification Suite (160 Tests)
* **What I Did**: Authored and executed an automated end-to-end test suite (`test_onboard360_master.py`) with 160 rigorous test cases validating all 12 project dimensions.
* **Why I Did It**: Proved the mathematical integrity, schema consistency, model safety, and file validity of the entire project without relying on unverified claims.
* **How I Did It**: Implemented Python `unittest` test fixtures validating file existence, parquet schema types, mathematical invariants, SQL queries, machine learning weights, DCF formulas, and BPMN XML tags.
* **Tool Used**: Python `unittest`, `sqlite3`, `pandas`, `openpyxl`, `joblib`, `xml.etree`.
* **Output Produced**: `test_onboard360_master.py`, `09_UAT/160_TEST_EXECUTION_REPORT.md`.
* **Business Purpose**: Provide definitive, repeatable verification for executive and technical evaluators.
* **Result**: 160 / 160 tests passing consistently in under 15 seconds with zero failures, zero errors, and zero warnings.
* **Evidence**: Console test execution log, `09_UAT/160_TEST_EXECUTION_REPORT.md`.

---

## 4. Separation of Personal Contributions vs. Project Infrastructure

| Layer | Personal Contribution (Hriday Singh Sobti) | Automatically Generated / Standard Infrastructure |
|---|---|---|
| **Process Engineering** | AS-IS queue decomposition, Little's Law mathematical formulation, TO-BE BPMN 2.0 orchestration flows, SLA definitions. | Standard BPMN 2.0 XML schema definitions and visual renderers. |
| **Data & Analytics** | Statistical parameter design, correlation logic (touch vs wait time), SQL reporting CTEs, window functions. | Parquet file serialization formats, SQLite database engine binary. |
| **Requirements** | Problem statements, MoSCoW prioritization, INVEST user stories, Gherkin acceptance criteria, business rules logic. | Standard markdown syntax, Excel workbook file formats. |
| **Machine Learning** | Triage problem formulation, feature engineering, classification class definitions, zero-leakage regulatory guardrails. | Scikit-Learn Random Forest default algorithmic solvers and optimization routines. |
| **Financial Modeling** | Activity-Based Costing structure, labor rate reconciliation, DCF cash flow schedules, sensitivity scenario modeling. | OpenPyXL cell formula calculators and ReportLab document formatting engines. |
| **Quality & Governance** | 160-test case architecture, assertion logic, edge cases, traceability matrix, model governance cards. | Python `unittest` test runner execution engine. |

---

## 5. Stakeholder Benefit Analysis: Who Benefited, How & How Much

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       STAKEHOLDER VALUE REALIZATION MAP                                          │
├────────────────────┬────────────────────┬────────────────────┬────────────────────┬──────────────────────────────┤
│ Stakeholder Group  │ Problem Before     │ Change Introduced  │ Quantified KPI     │ Tangible Business Value      │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 1. End Customer    │ 58.7h delay,       │ Client-side CV,    │ TAT: 58.7h -> 24h  │ Fast, transparent onboarding;│
│    (Applicants)    │ repeated uploads,  │ instant OCR,       │ (<15m STP);        │ frictionless mobile UX;      │
│                    │ zero status updates│ WhatsApp 1-click.  │ Drop-off: 16%->7.5%│ instant account opening.     │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 2. Retail Banking  │ 16.25% customer    │ Instant STP account│ Account Opening:   │ Converts 45,475 additional   │
│    Leadership      │ abandonment losing │ opening; frictionless│ +45,475 accounts; │ funded accounts annually;    │
│                    │ retail deposits.   │ mobile onboarding. │ Drop-off cut 53.8%.│ protects market share.       │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 3. Banking Ops     │ 184,000 manual L1  │ Image quality gate,│ L1 Reviews:        │ Saves $12,512,640 annually;  │
│    (L1 Analysts)   │ reviews; queues    │ postal prefill,    │ 184K -> 41.6K      │ eliminates repetitive review │
│                    │ backed up by days. │ AI Triage routing. │ (-77.4% volume).   │ fatigue for 100+ analysts.   │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 4. KYC / AML       │ High false-positive│ Jaro-Winkler fuzzy │ L2 Reviews:        │ Saves $5,268,055 annually;   │
│    Compliance      │ sanctions alerts;  │ matching; automated│ 29.8K -> 15.6K     │ focuses senior investigators │
│    (L2 Officers)   │ manual checks.     │ context screening. │ (-47.7% volume).   │ on real AML/PEP risks.       │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 5. Customer Service│ 118,602 tickets    │ Event-driven Kafka │ Tickets:           │ Saves $1,056,493.50 annually;│
│    / Contact Center│ ($1.41M cost);     │ push & SMS status  │ 118.6K -> 29.6K    │ cuts contact center queue    │
│                    │ 83% "Where is app?"│ notifications.     │ (-75.0% volume).   │ wait times for banking calls.│
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 6. IT & Core       │ 18.5h overnight    │ Real-time REST Core│ Account Latency:   │ Consolidates vendor spend;   │
│    Engineering     │ batch delays;      │ Banking API; Kafka │ 18.5h -> <1,500ms  │ saves $2,912,000 in legacy   │
│                    │ legacy vendor APIs.│ streaming broker.  │ (-99.9% latency).  │ screening licensing fees.    │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 7. InfoSec & Audit │ Opaque manual logs;│ PostgreSQL SHA-256 │ Audit Compliance:  │ 100% audit readiness; zero   │
│                    │ risk of fines and  │ append-only log;   │ 100% cryptographic │ unlogged transitions; avoids │
│                    │ non-repudiation.   │ zero ML leakage.   │ verification.      │ multi-million dollar fines.  │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┼──────────────────────────────┤
│ 8. Executive       │ $67.45 unit cost   │ End-to-end process │ Unit Cost:         │ $22,092,276.10 annual net    │
│    Committee / CFO │ eroding retail     │ transformation;    │ $67.45 -> $12.55   │ cash savings; 3-Yr NPV       │
│                    │ banking margins.   │ 60% STP automation.│ (-81.4% cost cut). │ $49.50M; 2.0 month payback.  │
└────────────────────┴────────────────────┴────────────────────┴────────────────────┴──────────────────────────────┘
```

---

## 6. Verification & Sign-off

Every single claim, metric, formula, and file location documented in this contribution dossier is traceable to an executable script, a verified dataset, or an audited spreadsheet model in this repository.

**Contributor Sign-off:**  
*Hriday Singh Sobti*  
ONBOARD360 Transformation Initiative  
