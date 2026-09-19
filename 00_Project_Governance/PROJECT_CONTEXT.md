# ONBOARD360 — Project Context & Foundation Document
**Document ID:** GOV-CTX-001  
**Version:** 1.0.0 (Baselined)  
**Organization:** NovaBank International  
**Project:** ONBOARD360 — AI-Assisted Customer Onboarding & KYC Process Transformation Platform  
**Lead Role:** Lead Business Analyst & Solution Architect  
**Classification:** Internal Portfolio & Architectural Specification  

---

## 1. Executive Context & Institutional Background
**NovaBank International** is a mid-tier global retail and commercial banking institution operating across four key regional jurisdictions:
1. **United Kingdom & European Union (UK/EU)**: Regulated under FCA, PRA, EBA, and GDPR.
2. **North America (United States - US)**: Regulated under FinCEN (BSA/USA PATRIOT Act), OCC, and CFPB.
3. **Asia-Pacific (Singapore - SG & Australia - AU)**: Regulated under MAS and AUSTRAC.
4. **Latin America & Emerging Markets (LatAm)**: Local jurisdictional AML/CFT frameworks.

NovaBank delivers personal accounts, premier wealth accounts, SME commercial banking, and digital fintech checking products. Over the past 24 months, aggressive digital customer acquisition campaigns expanded inbound application volume to **over 520,000 applications per annum**. However, the underlying onboarding infrastructure, Know Your Customer (KYC) operations, and Customer Due Diligence (CDD) workflows have failed to scale, relying on fragmented legacy core banking systems, manual document re-keying, and siloed compliance review queues.

---

## 2. Business Problem Definition
The current customer onboarding lifecycle is impaired by structural operational friction:
1. **Prolonged Cycle Times (Turnaround Time - TAT)**: Average onboarding cycle time stands at **128.4 hours (~5.35 days)** from initial application submission to active account funding. In corporate and high-risk retail tiers, TAT reaches 240+ hours.
2. **Excessive Idle & Queue Wait Time**: Of the 128.4 hours total cycle time, active touch time (human review and customer input) represents only **11.2 hours (8.7%)**. The remaining **117.2 hours (91.3%)** is unmanaged queue wait time between disconnected departmental handoffs.
3. **Severe First-Pass Yield (FPY) Deficit & High Rework**: First-pass approval rate is only **38.6%**. Over **34.2%** of all applications trigger manual rework cycles due to illegible document uploads, expired identification, mismatch in optical character recognition (OCR), or missing proof-of-address.
4. **Operational Bottlenecks & Over-Escalation**: **46.8%** of all incoming applications are routed into manual review queues, overwhelming Level-1 (L1) and Level-2 (L2) compliance teams with low-risk, false-positive alerts.
5. **Customer Drop-Off & Abandonment**: High operational friction drives a customer abandonment rate of **24.8%**, heavily concentrated at the document submission and rework stages, directly forfeiting lifetime customer value (LTV).
6. **Escalating Operating Costs**: The average operational cost per onboarded application has climbed to **$54.20**, eroding retail acquisition margins.

---

## 3. Transformation Vision & Business Objectives
The ONBOARD360 transformation initiative transitions NovaBank from a reactive, manual, queue-bound operating model to an **intelligent, rules-driven, AI-assisted orchestration platform**:
* **Target 1 — Cycle Time Reduction**: Slash average end-to-end onboarding TAT from 128.4 hours to **< 24.0 hours** (a **> 81% reduction**), with Straight-Through Processing (STP) paths completing in under 15 minutes.
* **Target 2 — Straight-Through Processing (STP)**: Achieve **≥ 60% STP** for low-risk, verified digital retail applications.
* **Target 3 — First-Pass Yield Improvement**: Elevate FPY from 38.6% to **≥ 78%** via real-time client-side document quality validation and guided upload wizards.
* **Target 4 — Rework Reduction**: Compress application rework rate from 34.2% to **≤ 10%**.
* **Target 5 — Intelligent Exception Triage**: Deploy an AI-Assisted Exception & Document Triage engine with human-in-the-loop controls to automate 70% of low-risk exception routing, saving compliance teams > 50,000 manual review hours annually.
* **Target 6 — Cost per Application**: Reduce operating cost per application from $54.20 to **≤ $18.50** (a **65.8% unit cost savings**).

---

## 4. Analytical & Technical Scope
### In-Scope:
1. Complete BA artifact suite: BRD, FRD, RACI, Process Inventory, 30+ User Stories with Gherkin acceptance criteria, Traceability Matrix, and 30+ UAT Scenarios.
2. Complete AS-IS vs. TO-BE BPMN 2.0 workflow models and gap analysis.
3. Realistic synthetic multi-table transactional dataset representing **520,000+ customer applications** spanning a 12-month baseline period across 5 channels, 4 customer types, and 4 global regions.
4. Rigorous Python & SQL analytics suite examining bottlenecks, Little's Law queue dynamics, Pareto root-cause distributions, and SLA breach correlations.
5. Machine Learning & Rule-based AI Exception Triage service (LightGBM/Random Forest + Decision Engine) complete with audit trails, confidence thresholds, and human-in-the-loop fallback logic.
6. Financial Cost-Benefit & ROI model detailing CAPEX, OPEX, 3-year NPV, IRR, and payback period across Base, Conservative, and Aggressive scenarios.
7. Power BI 5-page enterprise dashboard specification and DAX measure catalog.
8. Implementation roadmap, change management plan, and executive board presentation.

### Out-of-Scope:
* Autonomous regulatory de-risking without human compliance oversight (all High/PEP risks mandate human sign-off).
* Direct migration of physical branch mainframe hardware.

---

## 5. Governance & Operational Methodology
Every operational finding, business requirement, and cost saving in this project follows standard process engineering practices:
$$\text{AS-IS Bottleneck} \xrightarrow{\text{Data Evidence}} \text{Root Cause} \xrightarrow{\text{Requirement}} \text{Solution Design} \xrightarrow{\text{UAT Validation}} \text{Quantified Benefit}$$
All financial projections are derived from explicit activity-based costing equations and reconciled against baseline operational staffing.
