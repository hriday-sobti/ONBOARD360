# ONBOARD360 — Business Requirements Document (BRD)
**Document ID:** REQ-BRD-001  
**Version:** 1.0.0 (Baselined)  
**Author:** Lead Business Analyst  
**Approval:** Retail Executive Committee & Chief Compliance Officer  

---

## 1. Executive Summary & Business Need
NovaBank International processes 520,000 customer applications annually with an unsustainable cycle time of 58.70 hours, an 89.3% queue wait time ratio, a 33.35% rework rate, and an annual direct support burden of $1.41M. The primary business need is to deploy an intelligent, automated onboarding and KYC transformation platform that compresses cycle time below 24 hours, achieves $\ge$ 60% straight-through processing (STP), and reduces unit operating cost by > 60% while maintaining absolute compliance with global regulatory mandates.

---

## 2. Business Requirements Catalog

| Requirement ID | Business Objective & Title | Business Requirement Description | Priority (MoSCoW) | Strategic Alignment | Success Metric / Acceptance Threshold |
|---|---|---|---|---|---|
| **BR-001** | Sub-24h Cycle Time Acceleration | The onboarding platform shall complete end-to-end retail customer onboarding within 24 hours for non-exception cases and under 15 minutes for clean STP paths. | **MUST HAVE** | OBJ-01 (TAT Compression) | Mean TAT < 24.0 hours across total annual volume. |
| **BR-002** | Straight-Through Processing (STP) Enablement | The platform shall automatically verify, clear KYC/AML, provision core accounts, and activate customers without human intervention for verified low-risk applicants. | **MUST HAVE** | OBJ-02 (Automation) | STP rate reaches $\ge$ 60.0% of all submitted applications. |
| **BR-003** | Upfront Document Defect Elimination | The digital portal shall prevent blurry, cropped, glare-compromised, or expired identity documents from entering downstream processing queues. | **MUST HAVE** | OBJ-03 (First-Pass Yield) | Rework rate decreases from 33.35% to $\le$ 10.0%; FPY $\ge$ 78.0%. |
| **BR-004** | Intelligent AML Watchlist Fuzzy Screening | The screening engine shall incorporate fuzzy phonetic matching and context-aware risk weighting to reduce false-positive sanctions and PEP holds. | **MUST HAVE** | OBJ-06 (SLA Compliance) | Watchlist false-positive escalation rate reduced by $\ge$ 50%. |
| **BR-005** | Human-In-The-Loop AI Exception Triage | The platform shall leverage machine learning decision models to evaluate, classify, and prioritize exceptions, auto-remediating low-risk documentation anomalies. | **SHOULD HAVE** | OBJ-07 (Unit Cost Reduction) | 70% of low-risk document exceptions routed directly to customer self-service. |
| **BR-006** | Omnichannel Application Continuity | Applicants shall be able to initiate on mobile, complete on web, or receive in-branch assistance without losing progress or resubmitting data. | **SHOULD HAVE** | OBJ-05 (Abandonment Reduction) | Customer abandonment rate falls from 16.25% to $\le$ 8.0%. |
| **BR-007** | Real-Time Proactive Status Notifications | The platform shall dispatch automated SMS, push, and email progress updates at every stage transition, eliminating customer uncertainty. | **MUST HAVE** | Customer Experience | "Where is my account?" support tickets decrease by $\ge$ 75%. |
| **BR-008** | Regulatory Audit Trail & Explainability | Every automated clearance, score, risk determination, and analyst override shall be immutably recorded in an encrypted audit log. | **MUST HAVE** | Compliance & Audit | 100% compliance audit pass rate; zero unlogged transitions. |
| **BR-009** | Unified Analyst Workbench | Compliance and operations analysts shall work within a consolidated single-pane-of-glass workbench with pre-screened evidence dossiers. | **SHOULD HAVE** | Operational Productivity | L1/L2 analyst touch time per manual review decreases by $\ge$ 45%. |
| **BR-010** | Unit Operating Cost Reduction | The total direct operational cost to onboard an approved customer shall not exceed $18.50 per application. | **MUST HAVE** | Financial Margin | Unit cost reduced from $54.20 to $\le$ $18.50 ($18.5M+ annual savings). |
