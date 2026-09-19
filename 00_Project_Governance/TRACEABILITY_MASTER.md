# ONBOARD360 — Requirements Traceability Master Matrix (RTM)
**Document ID:** GOV-TRC-001  
**Version:** 1.0.0 (Baselined)  
**Traceability Scope:** 100% Forward and Backward Bidirectional Traceability  

---

## 1. End-to-End Bidirectional Traceability Matrix
This matrix maps the complete lifecycle from the original operational Problem Statement through Business Requirements, Functional Requirements, Business Rules, User Stories, Solution Components, to UAT Validation.

| Problem / Pain Point | Business Req (BR) | Functional Req (FR) | Business Rule (BRULE) | User Story (Agile) | Solution / Architecture Component | UAT Test Case | Validation Status |
|---|---|---|---|---|---|---|---|
| **PNT-01**: Blurry / glare ID uploads causing 42.1% rework | **BR-003**: Document Defect Elimination | **FR-001**: Real-time OpenCV Quality Check | **BRULE-001**: Laplacian Sharpness $\ge 150$ | **US-DOC-01**: Real-time Camera Feedback | Mobile / Web Viewfinder Computer Vision Wasm | **UAT-01, UAT-02, UAT-03, UAT-31** | **VERIFIED / PASS** |
| **PNT-01**: Expired identification documents accepted | **BR-003**: Document Defect Elimination | **FR-002**: Automated OCR Expiration Check | **BRULE-002**: Expiry > CurrentDate + 90d | **US-DOC-03**: Detect Expired Documents | Cloud OCR Parsing Engine | **UAT-04, UAT-05** | **VERIFIED / PASS** |
| **PNT-01**: Address proof and data entry mismatch | **BR-003**: Document Defect Elimination | **FR-003**: Address Bureau Match Check | **BRULE-003**: Postal match confidence $\ge 85$ | **US-CAP-01**: Postal Code Autofill | Address Bureau REST Client | **UAT-06, UAT-23** | **VERIFIED / PASS** |
| **PNT-02**: Watchlist false positives causing 18h delays | **BR-004**: Fuzzy Watchlist Screening | **FR-010**: Jaro-Winkler Fuzzy Match Engine | **BRULE-004, BRULE-005, BRULE-006** | **US-KYC-01, US-KYC-02**: Fuzzy Match | Watchlist Screening Microservice | **UAT-07, UAT-08, UAT-09, UAT-10** | **VERIFIED / PASS** |
| **PNT-03**: L1 Analysts overloaded with low-risk reviews | **BR-005**: AI Exception Triage | **FR-015**: ML Exception Classifier | **BRULE-007**: AI Triage confidence $\ge 0.85$ | **US-AI-01, US-AI-02**: Auto-Remediation | Scikit-Learn Triage Model & Router | **UAT-11, UAT-12, UAT-13** | **VERIFIED / PASS** |
| **PNT-04**: Customer abandonment at rework stage (24.8%) | **BR-006**: Omnichannel Continuity | **FR-020**: Session State Serialization | **BRULE-009, BRULE-010**: Chrono reminders | **US-CAP-02**: Cross-Device Magic Link | Redis Session Cache & Messaging Svc | **UAT-14, UAT-21, UAT-22** | **VERIFIED / PASS** |
| **PNT-04**: 82.8% support tickets asking "Where is my account?"| **BR-007**: Real-time Status Notifications | **FR-025**: Event-Driven Push Dispatcher | **BRULE-008**: Proactive SMS at 24h | **US-SYS-03, US-SYS-04**: Push Updates | Apache Kafka & Notification Svc | **UAT-15, UAT-30** | **VERIFIED / PASS** |
| **PNT-05**: Analysts navigating 5 tabs; high touch time | **BR-009**: Unified Analyst Workbench | **FR-009**: Single-Pane-of-Glass Workbench | **BRULE-004, BRULE-009**: SLA queue timers | **US-OPS-01, US-OPS-02**: Workbench UI | Operations React UI / REST BFF | **UAT-19, UAT-20, UAT-29** | **VERIFIED / PASS** |
| **PNT-06**: Overnight batch delay for account creation | **BR-001, BR-002**: Sub-24h TAT & 60% STP | **FR-030**: Core Ledger Provisioning REST API | **BRULE-007**: Authorize Instant STP | **US-SYS-01, US-SYS-02**: Real-time Account | Core Banking Ledger REST Adapter | **UAT-16, UAT-17, UAT-32** | **VERIFIED / PASS** |
| **Governance**: Regulatory audit trail and data protection | **BR-008**: Cryptographic Auditability | **FR-035**: Cryptographic Hash Audit Log | Standard ISO 27001 / GDPR compliance | **US-SYS-05**: Immutable Compliance Log | PostgreSQL Hash Sink & Security Perimeter | **UAT-18, UAT-27, UAT-28** | **VERIFIED / PASS** |

---

## 2. Traceability Health Check
* **Total Business Requirements**: 10 (100% covered by FRs, Stories, and UAT Cases)
* **Total Functional Requirements**: 10 Core Specs (100% mapped and tested)
* **Total User Stories**: 35+ Backlog Stories (100% linked to Epics and Acceptance Criteria)
* **Total UAT Cases**: 32 Multi-tier Scenarios (100% passing in test execution)
* **Orphaned Requirements / Uncovered Items**: None. Every business requirement connects directly to downstream functional requirements, stories, and verified test cases.
