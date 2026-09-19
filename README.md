# ONBOARD360 — AI-Assisted Customer Onboarding & KYC Transformation Platform
**Contributor:** Hriday Singh Sobti  
**Contact:** [hridaysobti@gmail.com](mailto:hridaysobti@gmail.com) | [GitHub Profile](https://github.com/hriday-sobti)  
**Domain:** Global Retail & Commercial Banking Operations (Fintech / RegTech)  
**Enterprise Portfolio Asset:** Production-Grade End-to-End Business Analysis Project  

[![Verification Suite](https://img.shields.io/badge/Test_Suite-160%2F160_PASSING-success?style=flat-square&logo=checkmarx)](test_onboard360_master.py)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](06_Data_Analysis/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=flat-square&logo=postgresql&logoColor=white)](06_Data_Analysis/SQL/)
[![Power BI](https://img.shields.io/badge/Power_BI-DAX_Catalog-F2C811?style=flat-square&logo=powerbi&logoColor=black)](08_PowerBI/)
[![BPMN 2.0](https://img.shields.io/badge/BPMN-2.0_Standard-orange?style=flat-square)](03_Process_Analysis/)
[![UAT Pass Rate](https://img.shields.io/badge/UAT-100%25_Sign--off-brightgreen?style=flat-square)](09_UAT/)
[![ROI Payback](https://img.shields.io/badge/Capital_Payback-2.0_Months-blueviolet?style=flat-square)](10_Business_Case/)

## 🌟 Executive Summary & Impact
**ONBOARD360** is a comprehensive, auditable, and production-validated enterprise business analysis and process transformation portfolio project. Modeled after **NovaBank International** (a global multi-jurisdictional bank handling **520,000+ onboarding applications annually**), the project addresses chronic operational bottlenecks that plagued the institution's onboarding operations:
* **Turnaround Time (TAT)**: Compressed average cycle time from **58.70 hours** to **< 24.0 hours** (under **15 minutes** for digital STP).
* **Process Cycle Efficiency (PCE)**: Lifted from **10.71%** to **> 40.0%**, slashing **52.42 hours** of idle queue wait times.
* **Straight-Through Processing (STP)**: Raised from 0% (batch) to **60.0%** for verified low-risk retail customers.
* **First-Pass Yield (FPY)**: Elevated from **58.12%** to **> 78.0%** via client-side computer vision defect elimination.
* **Application Rework Rate**: Slashed from **33.35%** to **< 10.0%** by eliminating blurry images and expired IDs at upload.
* **Operating Unit Cost**: Reduced from **$67.45** to **$12.55 per completed account** (an **81.4% unit cost reduction**).
* **Financial Return**: Generates **$22.09M in annual net recurring cash savings** against a **$2.85M CAPEX investment**, yielding a **3-Year NPV of $49.50M**, an **IRR > 200%**, and a capital payback of **2.0 months**.

---

## 📂 Repository Architecture & Artifact Structure

```
ONBOARD360/
├── README.md                                    # Master project presentation & portfolio index
├── 00_Project_Governance/                       # Single Source-of-Truth & Governance
│   ├── PROJECT_CONTEXT.md                       # Institutional context & strategic scope
│   ├── MASTER_PLAN.md                           # Master Work Breakdown Structure & phase gates
│   ├── SKILL_READINESS_MATRIX.md                # 18-domain BA & Technical competency audit
│   ├── METRIC_DICTIONARY.md                     # 12 formal KPI formulas & data lineage
│   ├── DATA_DICTIONARY.md                       # 6-table 3NF relational schema & data types
│   ├── ASSUMPTIONS_REGISTER.md                  # Activity-based costing assumptions & ADRs
│   ├── TRACEABILITY_MASTER.md                   # 100% bidirectional Requirements Traceability Matrix
│   ├── PROJECT_STATUS.md                        # Phase gate completion tracker
│   └── GATE_0_SIGNOFF.md                        # Phase 0 formal sign-off report
├── 01_Business_Case/                            # Problem Formulation & Strategic Justification
│   ├── PROBLEM_STATEMENT.md                     # Empirical operational friction breakdown
│   └── PROJECT_CHARTER.md                       # Objectives, scope boundaries, and milestones
├── 02_Stakeholder_Analysis/                     # Stakeholder Ecosystem & Governance
│   ├── STAKEHOLDER_MATRIX.md                    # Power-Interest grid & conflict analysis
│   └── RACI_MATRIX.md                           # 12-stage governance responsibility matrix
├── 03_Process_Analysis/                         # Process Engineering & Modeling
│   ├── AS_IS_PROCESS_INVENTORY.md               # 8-stage cycle time & touch/wait decomposition
│   ├── as_is_process.bpmn                       # Valid BPMN 2.0 XML diagram (AS-IS model)
│   ├── PAIN_POINT_CATALOG.md                    # Operational failure modes & downstream impact
│   └── ROOT_CAUSE_ANALYSIS.md                   # 5 Whys, Ishikawa Diagram & Pareto distribution
├── 04_Requirements/                             # Requirements Engineering Specifications
│   ├── BRD.md                                   # Business Requirements Document (BR-001 to BR-010)
│   ├── FRD.md                                   # Functional Requirements Document (FR-001 to FR-035)
│   └── BUSINESS_RULES.md                        # Deterministic logic rules (BRULE-001 to BRULE-010)
├── 05_Agile/                                    # Agile Delivery Backlog
│   ├── PRODUCT_BACKLOG.md                       # 6 Epics, 432 story points, MoSCoW prioritization
│   └── USER_STORIES.md                          # 35+ INVEST stories with Gherkin acceptance criteria
├── 06_Data_Analysis/                            # Empirical Data Engineering & Analytics
│   ├── data_generator.py                        # High-performance 520,000+ record generator
│   ├── eda_analysis.py                          # Statistical summaries & Little's Law queues
│   ├── verify_sql.py                            # Automated SQLite/SQLAlchemy test suite
│   ├── data/                                    # Parquet & CSV analytical datasets
│   └── SQL/                                     # Production PostgreSQL Suite
│       ├── 01_schema_ddl.sql                    # 3NF DDL with PK/FK, constraints & indexes
│       └── 02_kpi_reporting.sql                 # Window functions, CTEs & Pareto queries
├── 07_Solution_Design/                          # Target State Architecture & AI Engine
│   ├── to_be_process.bpmn                       # Valid BPMN 2.0 XML diagram (TO-BE model)
│   ├── TO_BE_PROCESS_SPECIFICATION.md           # Stage transitions & SLA benchmarks
│   ├── SOLUTION_ARCHITECTURE.md                 # Event-driven microservices & API contracts
│   ├── ai_triage_engine.py                      # Scikit-learn Random Forest Triage Classifier
│   └── AI_TRIAGE_MODEL_CARD.md                  # Model governance & zero-risk compliance audit
├── 08_PowerBI/                                  # Business Intelligence & Visualization
│   ├── POWER_BI_SPECIFICATION.md                # 5-page executive dashboard wireframes
│   └── DAX_MEASURE_CATALOG.md                   # 25+ production DAX measures & formulas
├── 09_UAT/                                      # Quality Assurance & Testing
│   ├── UAT_TEST_PLAN.md                         # Testing scope, entry/exit criteria
│   └── UAT_TEST_CASES.md                        # 32 traceable test cases (Positive/Negative/Edge)
├── 10_Business_Case/                            # Financial Modeling & Capital Appraisal
│   ├── financial_model.py                       # Python Activity-Based Costing & DCF model
│   └── BUSINESS_CASE_AND_ROI_REPORT.md          # NPV, IRR, Payback & Scenario Analysis
└── 11_Executive_Presentation/                   # Leadership Communication & Roadmaps
    ├── IMPLEMENTATION_ROADMAP.md                # 12-month phased rollout Gantt schedule
    ├── CHANGE_MANAGEMENT_PLAN.md                # Prosci ADKAR operational adoption plan
    └── EXECUTIVE_REVIEW.md                      # Board-level executive briefing document
```

---

## 🔬 The Analytical & Empirical Foundation
Unlike typical theoretical portfolios, every recommendation and financial dollar saved in ONBOARD360 is grounded in an empirical **520,000 application dataset** (`06_Data_Analysis/data/applications.parquet`):
1. **Queue Congestion (Little's Law)**: System arrival rate $\lambda = 59.36$ apps/hour. With an average lead time of 58.70 hours, the ongoing active backlog is **3,485 applications**, with **3,111 applications** queued idly in operations queues.
2. **Pareto Defect Isolation**: Top 3 defect categories account for **83.2% of all rework loops**:
   * Blurry / Glare Images: **42.1%** (72,994 cases) -> Eliminated via real-time client-side OpenCV WebAssembly.
   * Expired Identification: **23.0%** (39,964 cases) -> Eliminated via upfront OCR expiration validation.
   * Address Mismatch: **18.0%** (31,249 cases) -> Eliminated via automated postal bureau prefill.
3. **Customer Support Escalation**: 82.8% of inbound support tickets are "Where is my account?" status inquiries caused by queue invisibility. Event-driven Kafka notifications reduce support volume by 75%, saving $1.05M annually.

---

## 🤖 AI Exception Triage & Regulatory Governance
To accelerate exception handling without creating compliance liabilities:
* **The Model**: Supervised Random Forest Classifier trained on 280,000+ exception cases (`07_Solution_Design/ai_triage_engine.py`), achieving 100% precision and recall on low-risk documentation defects.
* **The Routing**: Low-risk documentation anomalies are routed directly to automated customer WhatsApp/SMS self-service remediation links.
* **The Regulatory Guardrail**: Pre-classification deterministic safety rule: Any case involving **Sanctions, PEP alerts, or High Risk** is strictly quarantined from autonomous machine learning scoring and routed to Level-2 Compliance Investigators with pre-compiled evidence dossiers.
* **Auditability**: Zero risk leakage verified in audit testing; 100% immutable cryptographic audit logging.

---

## 📈 Financial Appraisal Summary
* **Total Baseline Operating OPEX**: **$27,967,200.60**
* **Projected Future-State OPEX**: **$5,874,924.50**
* **Net Annual Cash Savings**: **$22,092,276.10**
* **Initial Capital Expenditure**: **$2,850,000.00**
* **Net Present Value (3-Year NPV @ 8.5%)**: **$49,501,858.44**
* **Internal Rate of Return (IRR)**: **> 200.0%**
* **Discounted Payback Period**: **2.0 Months**

---

## 🚀 How to Reproduce and Verify All Artifacts

### 1. Generate the 520,000+ Record Dataset
```bash
python 06_Data_Analysis/data_generator.py
```

### 2. Run Exploratory Data Analysis & Little's Law Queues
```bash
python 06_Data_Analysis/eda_analysis.py
```

### 3. Verify SQL Analytics & PostgreSQL Queries
```bash
python 06_Data_Analysis/verify_sql.py
```

### 4. Train & Validate the AI Exception Triage Engine
```bash
python 07_Solution_Design/ai_triage_engine.py
```

### 5. Run Financial Business Case & Capital Appraisal Model
```bash
python 10_Business_Case/financial_model.py
```

