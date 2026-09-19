# ONBOARD360 — Quantified Business Problem Statement
**Document ID:** BUS-PRB-001  
**Version:** 1.0.0 (Baselined)  
**Organization:** NovaBank International  
**Domain:** Global Retail & Commercial Banking Operations  

---

## 1. Context & Operational Background
NovaBank International's aggressive digital acquisition strategy has scaled customer application inflow to **520,000 applications annually**. However, the operational onboarding backbone has remained tethered to legacy siloed architectures, point-to-point batch interfaces, and extensive manual review protocols. 

The onboarding journey encompasses four distinct regulatory and verification milestones:
1. **Customer Identity Verification (CIP)**: Identity document capture, OCR text extraction, and biometrics.
2. **Customer Due Diligence (CDD) & Risk Categorization**: AML watchlist screening, Sanctions verification, PEP identification, and adverse media checks.
3. **Document Completeness & Authenticity Validation**: Proof of address verification, income verification, and corporate registry checks for commercial entities.
4. **Account Provisioning & Core Ledger Integration**: Account number generation, debit card issuance, and initial funding enablement.

---

## 2. Core Problem Dimensions

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                           THE FRICTION MULTIPLIER                             │
├───────────────────────────────┬───────────────────────────────┬───────────────┤
│ High Rework Rate (34.2%)      │ Manual Review Overload (46.8%)│ Wait Time 91% │
│ • Illegible image uploads     │ • False-positive sanctions    │ • Inter-team  │
│ • Expired identification      │ • Low-risk document queues    │   queue delays│
│ • Address mismatches          │ • Analyst fatigue & burn      │ • 117h idle   │
└───────────────┬───────────────┴───────────────┬───────────────┴───────┬───────┘
                │                               │                       │
                ▼                               ▼                       ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│ BUSINESS IMPACT: 24.8% Abandonment | 31.4% SLA Breaches | $54.20 Unit Cost   │
└───────────────────────────────────────────────────────────────────────────────┘
```

### Dimension A: Severe Turnaround Time (TAT) & Cycle Time Drag
* **Metric**: Average end-to-end onboarding cycle time stands at **128.4 hours (~5.35 days)** against an operational SLA threshold of **48.0 hours**.
* **Root Breakdown**: Active touch time accounts for only **11.2 hours (8.7%)**, while unmanaged queue wait time consumes **117.2 hours (91.3%)**. Applications sit dormant in departmental handoff buffers between Retail Operations, KYC L1, and Compliance L2.
* **SLA Breaches**: **31.4%** of all applications violate regulatory and customer service level agreements (> 48 hours).

### Dimension B: First-Pass Yield (FPY) Deficit & Chronic Rework Loops
* **Metric**: First-Pass Yield is depressed at **38.6%**.
* **Impact**: **34.2%** of all applications enter an asynchronous rework cycle where customers are contacted via email to re-upload documents. The primary drivers are:
  1. Blurry or glare-compromised camera uploads (41.2% of rework).
  2. Expired identity cards or passports (22.8% of rework).
  3. Proof-of-address recency breaches (> 90 days old) or name mismatch (19.4% of rework).
  4. Incomplete forms and omitted mandatory fields (16.6% of rework).
* Each rework cycle adds an average of **72 to 96 hours** of turnaround delay and multiplies customer support inquiries.

### Dimension C: Operational Congestion & Manual Review Routing
* **Metric**: **46.8%** of all applications (243,360 applications annually) are diverted into manual review queues.
* **Driver**: Legacy screening rules employ rigid string-matching algorithms without fuzzy-logic tuning or risk context. A minor typographic variance in an applicant's middle name triggers an automated Level-1 compliance hold, forcing analysts to manually verify benign records.
* **Labor Strain**: Manual reviews consume over **136,000 analyst hours annually**, creating massive operational backlogs, queue deadlocks, and high staff attrition.

### Dimension D: Customer Abandonment & Revenue Forfeiture
* **Metric**: **24.8%** of applicants (128,960 potential customers annually) abandon their applications before account activation.
* **Customer Journey Churn**: 64% of drop-offs occur immediately after a rework notification is received, where customers switch to competing digital challenger banks offering instant verification.
* **Financial Impact**: At an estimated customer Lifetime Value (LTV) of $450 in net interest margin and fee income, abandonment represents an annual unrealized revenue opportunity of **$58.0M+**.

### Dimension E: Unsustainable Unit Economics
* **Metric**: Direct operational processing cost is **$54.20 per completed application**.
* **Cost Composition**:
  * Manual Operations Labor (L1/L2 Analysts): $28.60 (52.8%)
  * Customer Service Support Contacts: $11.40 (21.0%)
  * Legacy Vendor API & Third-Party Search Fees: $9.80 (18.1%)
  * Rework & Mailing Overhead: $4.40 (8.1%)

---

## 3. Consequence of Inaction
If NovaBank maintains its current AS-IS operating model:
1. Operational compliance costs will escalate past **$28.1M annually** as application volumes grow.
2. Market share among tech-native retail and SME demographics will decline sharply against fintech competitors offering sub-15-minute onboarding.
3. Elevated SLA breach rates (31.4%) expose the bank to heightened regulatory scrutiny from the FCA, FinCEN, and regional regulatory bodies for inadequate operational resilience.
