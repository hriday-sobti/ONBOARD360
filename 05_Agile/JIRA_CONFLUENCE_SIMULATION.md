# ONBOARD360 — Agile Product Delivery Simulation (Jira & Confluence)
**Document ID:** AGL-SIM-001  
**Version:** 1.0.0 (Baselined)  
**Classification:** Enterprise Agile Delivery Simulation (Confluence Space & Jira Project)  

---

## 1. Jira Project Setup & Configuration
* **Project Name**: ONBOARD360 — Customer Onboarding Transformation
* **Project Key**: `ONB360`
* **Delivery Framework**: Scrum (2-Week Sprint Cadence)
* **Estimation Metric**: Story Points (Fibonacci: 1, 2, 3, 5, 8, 13)
* **Team Velocity Baseline**: 54 Story Points / Sprint (Cross-functional team of 6 engineers, 1 BA, 1 QA, 1 Designer)

---

## 2. Sprint Release Schedule (Phase 1 Rollout)

### Sprint 1 (Sprint 1.1 — Foundation & Edge Capture)
* **Sprint Goal**: Enable client-side document quality validation and basic address auto-completion on Mobile and Web.
* **Committed Stories**:
  * `ONB360-101`: Address postal code auto-lookup (`US-CAP-01`, 5 pts)
  * `ONB360-102`: Real-time camera viewfinder blur & glare gating (`US-DOC-01`, 8 pts)
  * `ONB360-103`: Automated OCR extraction & field prefill (`US-DOC-02`, 8 pts)
  * `ONB360-104`: OCR expiration date validation (`US-DOC-03`, 5 pts)
  * `ONB360-105`: Interactive field formatting & error prompts (`US-CAP-03`, 3 pts)
  * `ONB360-106`: Core Banking REST API adapter foundation (`US-SYS-01`, 8 pts)
  * `ONB360-107`: Cryptographic compliance audit log sink (`US-SYS-05`, 8 pts)
* **Total Velocity**: 45 Story Points (Burndown on schedule; 0 defects carried over).

### Sprint 2 (Sprint 1.2 — Intelligent Screening & Real-time Core)
* **Sprint Goal**: Deploy Jaro-Winkler fuzzy sanctions screening and sub-1,500ms core account provisioning for STP.
* **Committed Stories**:
  * `ONB360-201`: Jaro-Winkler fuzzy watchlist screening engine (`US-KYC-01`, 8 pts)
  * `ONB360-202`: Phonetic double-metaphone name matching (`US-KYC-02`, 5 pts)
  * `ONB360-203`: Automated PEP identification & mandatory L2 freeze (`US-KYC-03`, 8 pts)
  * `ONB360-204`: Real-time core account provisioning API (`US-SYS-01`, 8 pts)
  * `ONB360-205`: Digital wallet virtual debit card tokenization (`US-SYS-02`, 5 pts)
  * `ONB360-206`: Kafka event-driven stage notification dispatcher (`US-SYS-03`, 5 pts)
  * `ONB360-207`: 3D Facial liveness verification (`US-DOC-05`, 5 pts)
* **Total Velocity**: 44 Story Points.

### Sprint 3 (Sprint 1.3 — AI Exception Triage & Self-Service Remediation)
* **Sprint Goal**: Integrate machine learning triage engine and WhatsApp 1-click camera remediation.
* **Committed Stories**:
  * `ONB360-301`: Random Forest exception classification service (`US-AI-01`, 13 pts)
  * `ONB360-302`: WhatsApp/SMS 1-click camera deep-link generator (`US-AI-02`, 8 pts)
  * `ONB360-303`: Top-3 feature explainability card in workbench (`US-AI-03`, 8 pts)
  * `ONB360-304`: Deterministic High-Risk/PEP bypass guardrail (`US-AI-04`, 5 pts)
  * `ONB360-305`: Cross-device session persistence via magic link (`US-CAP-02`, 5 pts)
  * `ONB360-306`: SME corporate registry automated lookup (`US-CAP-04`, 5 pts)
* **Total Velocity**: 44 Story Points.

### Sprint 4 (Sprint 1.4 — Unified Analyst Workbench & Hardening)
* **Sprint Goal**: Launch single-pane-of-glass operations workbench and complete enterprise UAT sign-off.
* **Committed Stories**:
  * `ONB360-401`: Unified Analyst single-pane-of-glass workbench (`US-OPS-01`, 8 pts)
  * `ONB360-402`: Dynamic SLA countdown timers & priority queues (`US-OPS-02`, 5 pts)
  * `ONB360-403`: Integrated external registry & adverse media viewer (`US-OPS-03`, 5 pts)
  * `ONB360-404`: Pre-approved standardized remediation templates (`US-OPS-04`, 5 pts)
  * `ONB360-405`: Mandatory analyst decline justification codes (`US-OPS-05`, 5 pts)
  * `ONB360-406`: Customer service 360-degree timeline search (`US-SYS-04`, 5 pts)
  * `ONB360-407`: End-to-end UAT hardening & security pen test (`NFR-001/002`, 8 pts)
* **Total Velocity**: 41 Story Points.

---

## 3. Simulated Confluence Space Structure
* **Space Home**: `ONBOARD360 Product & Transformation Knowledge Base`
  * **01 Architecture & Specs**: System Architecture, API Contracts, Data Dictionary
  * **02 Sprint Ceremonies**: Sprint Goals, Retrospectives, Velocity Tracking
  * **03 Compliance & Security**: AML Guardrails, GDPR Controls, Audit Logging
  * **04 Operations Playbooks**: Analyst Workbench User Guide, Exception Triage SOP
