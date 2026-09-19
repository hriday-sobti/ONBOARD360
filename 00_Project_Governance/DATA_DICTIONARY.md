# ONBOARD360 — Master Data Dictionary & Relational Schema
**Document ID:** GOV-DAT-001  
**Version:** 1.0.0 (Baselined)  
**Database Architecture:** PostgreSQL 15+ Compatible / Parquet Analytical Storage  

---

## 1. Entity-Relationship Overview
The ONBOARD360 transactional data model mirrors an enterprise core onboarding infrastructure normalized to Third Normal Form (3NF) for transactional auditability and denormalized into star-schema fact tables for high-speed analytical processing.

```
       ┌──────────────────┐
       │    customers     │
       └────────┬─────────┘
                │ 1:N
                ▼
       ┌──────────────────┐
       │   applications   │◄────────────────────────────┐
       └────────┬─────────┘                             │
                │                                       │
     ┌──────────┼──────────────────────┬─────────────┐  │
 1:N │      1:N │                  1:N │         1:N │  │
     ▼          ▼                      ▼             ▼  │
┌─────────┐┌───────────┐         ┌───────────┐ ┌────────────────┐
│documents││kyc_checks │         │manual_revs│ │support_tickets │
└─────────┘└───────────┘         └───────────┘ └────────────────┘
```

---

## 2. Table Specifications

### 2.1 Table: `customers` (Master Entity)
Stores baseline demographic, jurisdictional, and risk segmentation data for applicants.
* `customer_id` (VARCHAR(36), PK, UUID): Unique system identifier.
* `first_name` (VARCHAR(50)): Customer given name (anonymized/synthetic).
* `last_name` (VARCHAR(50)): Customer surname.
* `email` (VARCHAR(100)): Contact email address.
* `customer_type` (VARCHAR(20), NOT NULL): Enum (`Standard_Retail`, `Premier_Wealth`, `SME_Business`, `Fintech_Digital`).
* `country` (VARCHAR(3), NOT NULL): ISO-3 country code (`GBR`, `DEU`, `FRA`, `USA`, `SGP`, `AUS`, `BRA`, `MEX`).
* `region` (VARCHAR(10), NOT NULL): Region code (`UK_EU`, `US`, `APAC`, `LATAM`).
* `risk_category` (VARCHAR(10), NOT NULL): Initial calculated risk tier (`LOW`, `MEDIUM`, `HIGH`, `PEP`).
* `created_at` (TIMESTAMP, NOT NULL): Initial profile creation timestamp.

### 2.2 Table: `applications` (Core Transaction Fact)
Primary transaction record tracking end-to-end onboarding lifecycle.
* `application_id` (VARCHAR(36), PK, UUID): Unique application transaction ID.
* `customer_id` (VARCHAR(36), FK -> `customers.customer_id`, NOT NULL).
* `application_date` (TIMESTAMP, NOT NULL): Application submission timestamp.
* `channel` (VARCHAR(20), NOT NULL): Enum (`Mobile_App`, `Web_Portal`, `Branch_Assisted`, `Affiliate_Partner`).
* `product_type` (VARCHAR(25), NOT NULL): Enum (`Checking_Standard`, `Premier_Checking`, `Savings_HighYield`, `SME_Operating_Account`).
* `status` (VARCHAR(20), NOT NULL): Enum (`APPROVED`, `REJECTED`, `ABANDONED`, `PENDING_REVIEW`).
* `document_status` (VARCHAR(20), NOT NULL): Enum (`VERIFIED`, `REWORK_REQUIRED`, `REJECTED_FRAUD`, `PENDING`).
* `kyc_status` (VARCHAR(20), NOT NULL): Enum (`PASS`, `FAIL_SANCTIONS`, `FAIL_PEP`, `MANUAL_ESCALATION`).
* `risk_status` (VARCHAR(20), NOT NULL): Enum (`CLEARED_AUTO`, `EDD_REQUIRED`, `HIGH_RISK_DECLINED`).
* `manual_review_flag` (BOOLEAN, NOT NULL): `TRUE` if routed to human compliance queue.
* `review_team` (VARCHAR(25)): Team handling review (`None`, `L1_Ops`, `L2_Compliance`, `EDD_Special_Investigations`).
* `rework_flag` (BOOLEAN, NOT NULL): `TRUE` if applicant was prompted to resubmit info.
* `rework_reason` (VARCHAR(50)): Primary rework trigger (`None`, `Blurry_Image`, `Expired_ID`, `Address_Proof_Mismatch`, `Incomplete_Form`, `Name_Mismatch`).
* `total_cycle_time_hours` (FLOAT): Total duration from submission to completion/abandonment.
* `touch_time_hours` (FLOAT): Active human or customer touch time.
* `wait_time_hours` (FLOAT): Idle wait time in queues.
* `sla_breach_flag` (BOOLEAN, NOT NULL): `TRUE` if cycle time exceeded SLA (48.0 hrs).
* `approval_date` (TIMESTAMP): Timestamp of final approval.
* `activation_date` (TIMESTAMP): Timestamp of account funding/activation.

### 2.3 Table: `documents` (Child Entity)
Detailed records of each document submitted during onboarding.
* `document_id` (VARCHAR(36), PK, UUID): Unique document identifier.
* `application_id` (VARCHAR(36), FK -> `applications.application_id`, NOT NULL).
* `document_type` (VARCHAR(30), NOT NULL): Enum (`Passport`, `National_ID`, `Drivers_License`, `Utility_Bill`, `Bank_Statement`, `Articles_of_Incorporation`).
* `upload_timestamp` (TIMESTAMP, NOT NULL).
* `ocr_confidence_score` (FLOAT, 0.0 - 1.0): Optical character recognition confidence.
* `image_quality_score` (FLOAT, 0.0 - 1.0): Image resolution and glare metric.
* `verification_result` (VARCHAR(20), NOT NULL): Enum (`VERIFIED_AUTO`, `FLAGGED_BLURRY`, `FLAGGED_EXPIRED`, `TAMPER_DETECTED`, `MANUAL_CLEARED`).
* `rework_attempt_number` (INTEGER, DEFAULT 1): Iteration count of document submission.

### 2.4 Table: `kyc_checks` (Verification Engine Fact)
Automated and manual screening results across AML, Sanctions, and Identity databases.
* `check_id` (VARCHAR(36), PK, UUID): Unique check ID.
* `application_id` (VARCHAR(36), FK -> `applications.application_id`, NOT NULL).
* `check_type` (VARCHAR(25), NOT NULL): Enum (`Identity_CIP`, `Sanctions_Watchlist`, `PEP_Screening`, `Adverse_Media`, `Fraud_Bureau`).
* `vendor_provider` (VARCHAR(30), NOT NULL): Integration partner (`LexisNexis_Bridger`, `Experian_CrossCore`, `Refinitiv_WorldCheck`, `Internal_Core`).
* `check_timestamp` (TIMESTAMP, NOT NULL).
* `match_score` (FLOAT, 0.0 - 100.0): Algorithmic match confidence.
* `disposition` (VARCHAR(20), NOT NULL): Enum (`CLEARED_AUTO`, `FALSE_POSITIVE`, `CONFIRMED_MATCH`, `ESCALATED`).
* `execution_time_ms` (INTEGER): API response latency.

### 2.5 Table: `manual_reviews` (Operational Workflow Fact)
Tracks operational labor, queue wait times, and investigator actions.
* `review_id` (VARCHAR(36), PK, UUID): Unique review action ID.
* `application_id` (VARCHAR(36), FK -> `applications.application_id`, NOT NULL).
* `queue_name` (VARCHAR(30), NOT NULL): Enum (`L1_Document_Exception`, `L2_AML_Sanctions`, `L2_PEP_Review`, `Special_Investigations_Unit`).
* `analyst_id` (VARCHAR(20), NOT NULL): Investigator ID.
* `assigned_at` (TIMESTAMP, NOT NULL).
* `completed_at` (TIMESTAMP).
* `duration_minutes` (FLOAT): Active touch time spent by investigator.
* `decision` (VARCHAR(25), NOT NULL): Enum (`APPROVE`, `REJECT`, `REQUEST_REWORK`, `ESCALATE_L2`).
* `decision_notes` (TEXT): Audit trail justification.

### 2.6 Table: `support_tickets` (Customer Friction Entity)
Customer-initiated inbound support contacts resulting from onboarding friction.
* `ticket_id` (VARCHAR(36), PK, UUID): Unique ticket identifier.
* `application_id` (VARCHAR(36), FK -> `applications.application_id`, NOT NULL).
* `created_at` (TIMESTAMP, NOT NULL).
* `channel` (VARCHAR(15), NOT NULL): Enum (`In_App_Chat`, `Phone_IVR`, `Email_Helpdesk`).
* `issue_category` (VARCHAR(35), NOT NULL): Enum (`Status_Inquiry_WhereIsMyAccount`, `Document_Upload_Failure`, `Rejected_Clarification`, `Technical_Error`).
* `resolution_time_minutes` (FLOAT): Time required to resolve inquiry.
* `cost_to_serve_usd` (FLOAT): Activity cost of contact ($8.50 chat, $18.00 voice phone).
