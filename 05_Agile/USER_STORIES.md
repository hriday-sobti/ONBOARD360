# ONBOARD360 — Master User Story Catalog (35+ INVEST Stories)
**Document ID:** AGL-STY-001  
**Version:** 1.0.0 (Baselined)  
**Standard:** INVEST Principles (Independent, Negotiable, Valuable, Estimable, Small, Testable) with Gherkin Acceptance Criteria  

---

## 1. User Stories by Persona & Epic

### EPIC-01: Customer Digital Onboarding & Form Capture
* **US-CAP-01** (Must Have, 5 pts): *As a retail applicant, I want the onboarding form to auto-complete my address upon entering my postal code, so that I can finish the initial application in under 2 minutes without typing errors.*
  * **Given** an applicant is on the personal details screen,
  * **When** the applicant enters a valid postal code and selects their street number,
  * **Then** the city, state/region, and country fields are automatically populated and locked for editing unless manual override is requested.
* **US-CAP-02** (Must Have, 5 pts): *As a mobile applicant, I want to save my progress and resume on desktop via an encrypted magic link, so that I can switch devices without losing previously entered information.*
* **US-CAP-03** (Should Have, 3 pts): *As an applicant, I want real-time field validation highlighting invalid email or phone formats immediately, so that I do not encounter submission errors at the end of the form.*
* **US-CAP-04** (Must Have, 5 pts): *As an SME business owner, I want to enter my company registration number to auto-pull corporate registry records, so that I do not have to manually upload corporate articles of association.*
* **US-CAP-05** (Could Have, 3 pts): *As a multilingual applicant, I want the interface to support English, Spanish, French, and German, so that I can complete the process in my native language.*

### EPIC-02: Computer Vision & Real-Time Document Validation
* **US-DOC-01** (Must Have, 8 pts): *As a mobile applicant, I want the camera viewfinder to give real-time visual feedback if my ID is blurry or has glare, so that I only submit a clear photo that will not be rejected.*
  * **Given** an applicant activates the camera to capture their passport or driver's license,
  * **When** camera video frames are evaluated for sharpness and glare,
  * **Then** an on-screen visual overlay displays a red warning ("Too Blurry" or "Tilt to Remove Glare") and only auto-snaps when all quality thresholds are met.
* **US-DOC-02** (Must Have, 8 pts): *As an applicant, I want the system to extract my name and date of birth from my ID via OCR and ask me to confirm them, so that I catch typos before submission.*
* **US-DOC-03** (Must Have, 5 pts): *As a compliance officer, I want the OCR engine to detect if a submitted document is expired, so that expired credentials are immediately stopped before manual queues.*
* **US-DOC-04** (Should Have, 8 pts): *As a fraud analyst, I want the system to perform automated hologram and font-tampering checks on document images, so that forged identity documents are flagged immediately.*
* **US-DOC-05** (Must Have, 5 pts): *As an applicant, I want to perform a 3D facial liveness selfie matching my ID photo, so that I prove I am physically present without visiting a bank branch.*
* **US-DOC-06** (Should Have, 5 pts): *As an applicant whose document is rejected for blur, I want to receive immediate actionable instructions explaining how to improve lighting and framing, so that my second attempt succeeds.*

### EPIC-03: Intelligent KYC, AML & Watchlist Automation
* **US-KYC-01** (Must Have, 8 pts): *As an AML compliance officer, I want all applicants screened against UN, OFAC, and EU sanctions lists using fuzzy phonetic matching, so that high-risk individuals cannot open accounts.*
  * **Given** an application is submitted,
  * **When** customer data is matched against sanctions databases,
  * **Then** any match with confidence $\ge 85\%$ generates an immediate L2 freeze and audit log, while matches $< 70\%$ are cleared straight-through.
* **US-KYC-02** (Must Have, 5 pts): *As a compliance analyst, I want the screening engine to account for middle-name variations and phonetic spelling differences, so that innocent applicants are not trapped in false-positive queues.*
* **US-KYC-03** (Must Have, 8 pts): *As an AML investigator, I want politically exposed persons (PEPs) to be automatically identified and routed to specialized senior compliance queues, so that enhanced due diligence is conducted according to law.*
* **US-KYC-04** (Should Have, 5 pts): *As a risk analyst, I want adverse media screening conducted via automated news API checks, so that reputational risk is assessed alongside sanction lists.*
* **US-KYC-05** (Must Have, 5 pts): *As an auditor, I want every watchlist check to record the vendor timestamp, match score, and exact list version queried, so that our compliance posture is 100% auditable.*

### EPIC-04: AI-Assisted Exception & Document Triage Engine
* **US-AI-01** (Must Have, 13 pts): *As an operations manager, I want the AI Triage Engine to evaluate non-STP applications and predict whether an exception is a simple document defect or a complex risk issue, so that cases are routed to the right remediation path.*
  * **Given** an application fails automated straight-through validation,
  * **When** the AI Triage model analyzes the case features,
  * **Then** it assigns a confidence score and classifies the case as either "Auto-Customer-Remediation" or "Analyst-Queue-L1/L2".
* **US-AI-02** (Must Have, 8 pts): *As an applicant with an illegible document, I want to receive an instant WhatsApp or SMS prompt with a secure camera link, so that I can resubmit my ID in 30 seconds.*
* **US-AI-03** (Should Have, 8 pts): *As a compliance analyst, I want the AI engine to display the top 3 feature factors contributing to an exception score, so that I understand why the case was routed to me.*
* **US-AI-04** (Must Have, 5 pts): *As a compliance officer, I want all cases involving PEP or Sanctions alerts excluded from automated AI remediation, so that regulatory compliance is strictly maintained.*
* **US-AI-05** (Should Have, 8 pts): *As a solution architect, I want the AI model's precision and recall monitored weekly, so that model drift or bias can be corrected promptly.*

### EPIC-05: Unified Compliance & Operations Analyst Workbench
* **US-OPS-01** (Must Have, 8 pts): *As an L1 operations analyst, I want a single-pane-of-glass dashboard displaying the applicant's photo, OCR text, and highlighted discrepancies side-by-side, so that I can complete a review in under 3 minutes.*
* **US-OPS-02** (Must Have, 5 pts): *As an operations supervisor, I want automated queue balancing that assigns priority based on SLA clocks, so that applications close to breaching 24h are reviewed first.*
* **US-OPS-03** (Should Have, 5 pts): *As an L2 investigator, I want 1-click integration with external corporate registries and adverse media, so that I do not have to copy-paste names into separate browser tabs.*
* **US-OPS-04** (Must Have, 5 pts): *As an operations analyst, I want standard pre-approved remediation message templates, so that customer communications are clear, consistent, and fast.*
* **US-OPS-05** (Must Have, 5 pts): *As an audit officer, I want any analyst approval or rejection to mandate a structured rationale code and mandatory comment, so that decision accountability is enforced.*

### EPIC-06: Core Ledger Integration & Customer Activation
* **US-SYS-01** (Must Have, 8 pts): *As an approved applicant, I want my bank account number and IBAN generated in real time via API, so that I don't have to wait for overnight batch processing.*
* **US-SYS-02** (Must Have, 5 pts): *As a new customer, I want to immediately push my new virtual debit card to Apple Pay or Google Wallet, so that I can start spending instantly.*
* **US-SYS-03** (Must Have, 5 pts): *As an applicant, I want to receive real-time push and SMS updates at every stage of my application, so that I am never left wondering about my account status.*
* **US-SYS-04** (Should Have, 5 pts): *As a customer service agent, I want full visibility into an applicant's real-time onboarding timeline, so that I can instantly answer inbound support inquiries.*
* **US-SYS-05** (Must Have, 8 pts): *As a system administrator, I want cryptographic hashing of all compliance transactions, so that our data integrity meets SOC2 and ISO 27001 standards.*
