# ONBOARD360 — Functional Requirements Document (FRD)
**Document ID:** REQ-FRD-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. Functional Requirements Catalog
The Functional Requirements specify the exact technical behaviors, system capabilities, validation rules, and integration endpoints required to satisfy the Business Requirements.

| FR ID | Mapped BR ID | Functional Requirement Description | Input Parameters & Triggers | System Processing Logic | Output / System State Change |
|---|---|---|---|---|---|
| **FR-001** | BR-003 | Real-Time Client-Side Computer Vision Quality Check | User captures/uploads document image via mobile or web portal. | Client-side OpenCV/Wasm inspects image sharpness (Laplacian variance $\ge$ 150), edge boundary completeness, and specular glare ratio (< 8%). | If pass, enables submit button; if fail, renders visual bounding box guide instructing user to retake photo. |
| **FR-002** | BR-003 | Automated OCR Text Extraction & Expiry Validation | Successful document image payload received by onboarding API. | Cloud OCR extracts Machine Readable Zone (MRZ), Full Name, Document Number, and Expiration Date. Validates: $\text{Expiry Date} > \text{Current Date} + 90\text{ days}$. | If expired, displays instant error prompt: "Document Expired. Please upload a valid document." |
| **FR-003** | BR-003 | Automated Address Bureau Verification | User inputs residential address during application step 2. | Calls regional postal bureau and credit reference bureau (e.g., Experian CrossCore) via REST API to match address with identity. | Returns confidence score (0-100). If score $\ge$ 85, marks address verified; if < 85, prompts user for utility bill upload. |
| **FR-010** | BR-004 | Jaro-Winkler Fuzzy Matching Watchlist Screening | Customer legal name and DOB submitted to screening engine. | Matches customer against OFAC, EU, UN, and PEP lists using Jaro-Winkler distance with phonetic double-metaphone weighting. | Match score < 70 -> Cleared automatically; Match score 70-84 -> AI Triage; Match score $\ge$ 85 -> Mandatory L2 Compliance Hold. |
| **FR-015** | BR-005 | Machine Learning AI Exception Triage Classifier | Application flagged for exception or document defect. | Evaluates 12 application features (risk tier, blur score, mismatch delta, channel, product) via trained classification model. | Predicts optimal remediation path: Auto-Prompt User (confidence $\ge$ 0.85) or Route to Specialized Analyst Queue. |
| **FR-020** | BR-006 | Dynamic Session Persistence & Cross-Device Handoff | User pauses application or switches from mobile to desktop. | Session state serialized to encrypted Redis cache with secure 24-hour JWT link sent via SMS/Email. | User resumes exactly at the uncompleted milestone without re-entering verified data. |
| **FR-025** | BR-007 | Event-Driven Multi-Channel Status Dispatcher | Core lifecycle stage transition event published to Kafka broker. | Consumes event (`DOC_VERIFIED`, `KYC_CLEARED`, `ACTION_REQUIRED`) and generates push notification and SMS status message within 5 seconds. | Message logged in customer notification timeline; updates self-service tracker. |
| **FR-030** | BR-002 | Real-Time Core Banking Ledger Provisioning API | All verification milestones cleared (STP or analyst approval). | Dispatches synchronous HTTPS POST request to Core Ledger API with customer payload and risk token. | Generates account number and IBAN in < 1,500ms; issues digital wallet token. |
| **FR-035** | BR-008 | Immutable Cryptographic Audit Log Generator | Any state change, rule outcome, scoring event, or analyst action. | Appends event metadata, user ID, timestamp, and SHA-256 hash of previous block into append-only compliance audit table. | Guarantees non-repudiation and provides full tamper-evident regulatory audit trail. |
