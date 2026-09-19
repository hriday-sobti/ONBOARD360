# ONBOARD360 — Master Business Rules Specification
**Document ID:** REQ-RUL-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. Deterministic Business Rules Catalog

| Rule ID | Domain | Rule Statement / Logic Condition | Evaluation Timing | True Action / System Behavior | False Action / Alternative Path |
|---|---|---|---|---|---|
| **BRULE-001** | Document | `ImageSharpnessScore >= 0.75` AND `GlareRatio <= 0.08` AND `DocumentBoundaryDetected == TRUE` | Client Capture | Accept image and transmit to OCR pipeline. | Reject image immediately with onscreen retake instructions (PNT-01 fix). |
| **BRULE-002** | Document | `DocumentExpiryDate > CurrentDate + 90 Days` | OCR Processing | Mark document expiration check as PASSED. | Trigger immediate error: prompt for non-expired document. |
| **BRULE-003** | Identity | `OCR_Extracted_Name == Form_Entered_Name` (Jaro-Winkler distance $\ge$ 0.92) | Identity Verification | Auto-clear identity match check. | Flag for Name_Mismatch; route to AI Exception Triage. |
| **BRULE-004** | AML / Sanctions | `WatchlistMatchScore >= 85` OR `PEP_Confirmed == TRUE` | Watchlist Screening | **Mandatory L2 Compliance Review**. Freeze auto-approval; assign L2 SLA clock (4.0 hrs). | Check Rule BRULE-005. |
| **BRULE-005** | AML / Sanctions | `WatchlistMatchScore < 70` AND `RiskTier == 'LOW'` | Watchlist Screening | Mark sanctions screening as CLEARED_AUTO. | Check Rule BRULE-006. |
| **BRULE-006** | AML / Sanctions | `WatchlistMatchScore >= 70` AND `WatchlistMatchScore < 85` | Watchlist Screening | Route to AI Exception Triage for false-positive confidence scoring. | N/A |
| **BRULE-007** | Risk / STP | `RiskTier == 'LOW'` AND `DocumentStatus == 'VERIFIED'` AND `KYC_Status == 'PASS'` AND `AddressStatus == 'VERIFIED'` | Risk Gateway | **Authorize Straight-Through Processing (STP)**. Trigger Real-time Core Provisioning. | Route to Analyst Queue or AI Triage. |
| **BRULE-008** | Customer Service| `ApplicationCycleTime > 24.0 Hours` AND `Status == 'PENDING_REVIEW'` | Hourly Batch Clock | Automatically dispatch proactive reassurance SMS: "Your application is under active review by our specialized team." | Maintain standard status monitoring. |
| **BRULE-009** | Retention | `ReworkPromptDispatched == TRUE` AND `NoCustomerResponseHours >= 24.0` | Chrono Worker | Send automated WhatsApp/SMS interactive reminder with 1-click camera deep-link. | Wait until 72-hour expiration threshold. |
| **BRULE-010** | Retention | `ReworkPromptDispatched == TRUE` AND `NoCustomerResponseHours >= 72.0` | Chrono Worker | Transition application status to `ABANDONED_TIMED_OUT`; send final reactivation link. | N/A |
