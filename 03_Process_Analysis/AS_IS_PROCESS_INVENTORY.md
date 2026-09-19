# ONBOARD360 — AS-IS Process Inventory & Cycle Time Decomposition
**Document ID:** PRC-ASI-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. AS-IS Process Stage Inventory & Touch vs. Wait Breakdown
The AS-IS customer onboarding lifecycle consists of 8 sequential stages, heavily interrupted by asynchronous queues and manual handoffs:

| Stage ID | Process Stage Name | Primary Actor / Team | Supporting Systems | Avg Touch Time (Hrs) | Avg Queue Wait Time (Hrs) | Total Stage Lead Time (Hrs) | First-Pass Yield (%) | Stage Pain Points & Failure Modes |
|---|---|---|---|---|---|---|---|---|
| **ST-01** | Application Initiation & Form Capture | Customer | Web Portal / Mobile App | 0.75 | 0.00 | 0.75 | 82.0% | Incomplete addresses; form validation lacks real-time postal lookup. |
| **ST-02** | Document Upload & Submission | Customer | Legacy Document Repository | 0.50 | 4.20 | 4.70 | 65.8% | Camera glare, blurry text, cropped corners; no pre-upload verification. |
| **ST-03** | Automated CIP & Watchlist Screening | System | Legacy Core Batch / LexisNexis | 0.15 | 18.50 | 18.65 | 71.2% | Nightly batch execution; rigid string matching causes high false positives. |
| **ST-04** | Document Quality & OCR Review | L1 Ops Analyst | Shared Inbox / Imaging Portal | 1.80 | 28.40 | 30.20 | 62.0% | Manual data re-keying; manual inspection of expired IDs; massive queue buffer. |
| **ST-05** | Customer Rework & Resubmission | Customer / Ops | Email / Support Desk | 1.20 | 38.60 | 39.80 | 42.0% | Customer notified via non-interactive email; 72h customer response lag; high drop-off. |
| **ST-06** | Level-2 Compliance & AML Investigation | L2 Compliance | AML Case Management | 3.50 | 22.10 | 25.60 | 78.5% | Multi-system data collation; manual adverse media searching on search engines. |
| **ST-07** | Account Creation & Provisioning | IT Core Engine | Mainframe Core Ledger | 0.80 | 4.20 | 5.00 | 95.0% | Mainframe queue delays; batch overnight account provisioning. |
| **ST-08** | Customer Welcome & Initial Funding | Customer | Mobile App / Core Banking | 2.50 | 1.20 | 3.70 | 85.0% | Opaque credentials delivery; delays in debit card virtual token generation. |
| **TOTAL**| **End-to-End Onboarding Lifecycle** | **Blended** | **Enterprise Stack** | **11.20** | **117.20** | **128.40** | **38.6%** | **Process Cycle Efficiency (PCE) = 8.7%** |

---

## 2. Process Flow Architecture (ASCII BPMN Model)

```
[Start Event: Applicant Submits Data]
         │
         ▼
[ST-01: Form Capture] ──► [ST-02: Document Upload]
                                   │
                                   ▼
                   [ST-03: Nightly Batch Screening]
                                   │
                                   ▼
                   [Gateway: Watchlist / OCR Flag?]
                    ├── (Clear: 53.2%) ──► [ST-07: Account Provisioning] ──► [ST-08: Activation]
                    │                                                             │
                    └── (Flagged: 46.8%)                                          ▼
                             │                                             [End Event: Active]
                             ▼
                   [ST-04: L1 Ops Document Review Queue]
                             │
                             ▼
                   [Gateway: Document Legible & Valid?]
                    ├── (Valid) ──────► [ST-06: L2 Compliance Review]
                    │                               │
                    └── (Invalid: 34.2%)            ├── (Cleared) ──► [ST-07: Provisioning]
                             │                      │
                             ▼                      └── (Declined) ──► [End Event: Rejected]
                   [ST-05: Rework Email]
                             │
                             ▼
                   [Gateway: Customer Resubmits?]
                    ├── (Resubmits: 75.2%) ──► Loop back to ST-04
                    └── (Abandons: 24.8%)  ──► [End Event: Abandoned]
```
