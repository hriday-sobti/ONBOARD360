# ONBOARD360 — Master Metric Dictionary & KPI Catalog
**Document ID:** GOV-MET-001  
**Version:** 1.0.0 (Baselined)  
**Standard:** Enterprise Data & Operational Governance  

---

## 1. Master Metric Catalog

| Metric ID | Metric Name | Category | Exact Mathematical Formula | Data Source Table(s) & Fields | Target (TO-BE) | Baseline (AS-IS) |
|---|---|---|---|---|---|---|
| **KPI-01** | **Total Cycle Time (TAT)** | Efficiency | $\text{activation\_date} - \text{application\_date}$ (in hours) | `applications.activation_date`, `applications.application_date` | **< 24.0 hrs** | **128.4 hrs** |
| **KPI-02** | **Active Touch Time** | Efficiency | $\sum (\text{stage\_end} - \text{stage\_start})$ for active human/agent interactions | `manual_reviews.duration_mins`, customer interaction logs | **< 2.5 hrs** | **11.2 hrs** |
| **KPI-03** | **Queue Wait Time** | Efficiency | $\text{Total Cycle Time} - \text{Active Touch Time}$ | Derived: $\text{KPI-01} - \text{KPI-02}$ | **< 21.5 hrs** | **117.2 hrs** |
| **KPI-04** | **Process Cycle Efficiency (PCE)** | Efficiency | $\frac{\text{Active Touch Time}}{\text{Total Cycle Time}} \times 100$ | Derived: $\frac{\text{KPI-02}}{\text{KPI-01}} \times 100$ | **> 40.0%** | **8.7%** |
| **KPI-05** | **Straight-Through Processing (STP) Rate** | Automation | $\frac{\text{Count}(\text{Applications approved with 0 manual interventions})}{\text{Total Applications}} \times 100$ | `applications.manual_review_flag = FALSE` and `status = 'APPROVED'` | **$\ge$ 60.0%** | **12.4%** |
| **KPI-06** | **First-Pass Yield (FPY)** | Quality | $\frac{\text{Count}(\text{Applications approved without any rework or rejection})}{\text{Total Applications Submitted}} \times 100$ | `applications.rework_flag = FALSE` and `status = 'APPROVED'` | **$\ge$ 78.0%** | **38.6%** |
| **KPI-07** | **Rework Rate** | Quality | $\frac{\text{Count}(\text{Applications requiring document re-submission/correction})}{\text{Total Applications}} \times 100$ | `applications.rework_flag = TRUE` | **$\le$ 10.0%** | **34.2%** |
| **KPI-08** | **Manual Review Rate** | Operational | $\frac{\text{Count}(\text{Applications routed to L1/L2 compliance queues})}{\text{Total Applications}} \times 100$ | `applications.manual_review_flag = TRUE` | **$\le$ 22.0%** | **46.8%** |
| **KPI-09** | **Customer Abandonment Rate** | Experience | $\frac{\text{Count}(\text{Applications initiated but dropped before completion})}{\text{Total Applications Initiated}} \times 100$ | `applications.status = 'ABANDONED'` | **$\le$ 8.0%** | **24.8%** |
| **KPI-10** | **SLA Breach Rate** | Governance | $\frac{\text{Count}(\text{Applications exceeding standard 48h SLA})}{\text{Total Applications Processed}} \times 100$ | `applications.sla_breach_flag = TRUE` | **$\le$ 3.0%** | **31.4%** |
| **KPI-11** | **Support Contact Rate** | Experience | $\frac{\text{Count}(\text{Support tickets raised})}{\text{Total Applications}} \times 100$ | `support_tickets` joined on `application_id` | **$\le$ 5.0%** | **21.2%** |
| **KPI-12** | **Unit Cost per Application** | Financial | $\frac{\text{Total Annualized Onboarding Operating Costs}}{\text{Total Successfully Onboarded Applications}}$ | Activity-based costing model: Ops wages + vendor API costs + support overhead | **$\le$ $18.50** | **$54.20** |

---

## 2. Metric Aggregation & Reporting Standards
* **Time Grain**: Daily operational tracking; weekly queue monitoring; monthly executive scorecards.
* **Dimensional Slicers**: Region (`UK_EU`, `US`, `APAC`, `LATAM`), Customer Tier (`Standard_Retail`, `Premier_Wealth`, `SME_Business`, `Fintech_Digital`), Channel (`Mobile_App`, `Web_Portal`, `Branch_Assisted`, `Affiliate_Partner`), Product Type (`Checking`, `Savings`, `Credit_Card`, `Business_Account`).
* **Auditability Rule**: No KPI value may be reported in executive summaries without a corresponding SQL validation query and underlying data lineage trace.
