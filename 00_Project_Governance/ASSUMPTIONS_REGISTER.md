# ONBOARD360 — Master Assumptions Register & Decision Log
**Document ID:** GOV-ASM-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. Assumptions Register

| Assumption ID | Category | Description | Operational Rationale & Source | Confidence | Validation Method |
|---|---|---|---|---|---|
| **ASM-001** | Volume | Annual application baseline is 520,000 applications across retail, SME, and wealth. | Inbound customer demand modeling for mid-tier global bank; verified with historical baseline. | 95% | Validated via `applications` synthetic dataset. |
| **ASM-002** | Cost | Operations Analyst fully-loaded labor rate is $42.00 / hour ($32 base + 31% benefits/overhead). | Standard corporate banking operations benchmark for UK/US blended shared-service centers. | 90% | Activity-Based Costing (ABC) framework. |
| **ASM-003** | Cost | L2 Senior Compliance Analyst labor rate is $65.00 / hour. | Specialized compliance & AML investigator compensation market rate. | 90% | ABC model verification in `10_Business_Case/financial_model.py`. |
| **ASM-004** | Operational | Customer Service contact costs: $8.50 per digital chat ticket; $18.00 per voice phone call. | Gartner & Contact Center Institute banking customer service benchmarks. | 92% | Reconciled against `support_tickets` financial summaries. |
| **ASM-005** | Technical | OCR and computer vision pre-validation can eliminate 75% of blur and document format errors on client-side upload. | Industry RegTech capabilities (Onfido, Jumio, Trulioo benchmarks). | 88% | Tested in AI Triage simulation and UAT edge scenarios. |
| **ASM-006** | Regulatory | High-risk AML and PEP positive matches strictly require Level-2 human compliance review (Zero autonomous AI sign-off). | FATF Recommendation 10, FinCEN CDD Rule, FCA MLR 2017 regulatory mandate. | 100% | Hardcoded in business rules BRULE-004 and BRULE-012. |
| **ASM-007** | Financial | Capital cost of technology implementation is $2,850,000 amortized over 3 years; ongoing cloud/maintenance OPEX is $420,000/year. | Enterprise cloud microservice & integration sizing for mid-tier bank. | 85% | Capital budgeting model in `10_Business_Case/financial_model.py`. |
| **ASM-008** | Discount Rate | Cost of capital / corporate hurdle discount rate is 8.5% for NPV calculations. | NovaBank Treasury standard corporate hurdle rate. | 95% | Baselined in DCF cash flow schedules. |

---

## 2. Architectural Decision Log (ADR)

### ADR-001: Synthetic Data Generation at Scale (520,000+ Applications)
* **Status**: ACCEPTED & BASELINED
* **Context**: A realistic enterprise business analysis project requires empirical evidence reflecting genuine statistical variance, long-tail queues, and complex error distributions rather than trivial toy examples.
* **Decision**: Implement a vector-accelerated NumPy/Pandas synthetic data generator (`06_Data_Analysis/data_generator.py`) that enforces exact mathematical covariance between document blur, manual review routing, queue wait times, customer abandonment, and support ticket creation.
* **Consequences**: Generates 520,000 core applications, 1.2M+ document records, and 240K+ reviews, producing an auditable data foundation for all downstream SQL, Python, and Power BI models.

### ADR-002: Human-In-The-Loop (HITL) Architecture for AI Exception Triage
* **Status**: ACCEPTED & BASELINED
* **Context**: Unconstrained machine learning automation in banking KYC poses severe compliance liabilities and regulatory sanction risk.
* **Decision**: Architect the AI Exception Triage Engine as a decision-support and workflow routing accelerator. The model assigns confidence and classifies error types. Low-risk documentation remediation is routed directly to the customer self-service portal, whereas any compliance ambiguity, PEP alert, or risk score $\ge$ Medium is routed to human queues with pre-computed explanatory features.
* **Consequences**: Eliminates 70% of low-risk operational backlogs while ensuring 100% regulatory auditability and compliance control integrity.
