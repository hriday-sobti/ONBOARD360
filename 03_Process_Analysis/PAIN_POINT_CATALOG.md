# ONBOARD360 — Operational Pain Point Catalog & RCA Linkage
**Document ID:** PRC-PNT-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. Traceable Operational Pain Point Matrix

| Pain Point ID | Process Stage | Symptom / Operational Failure | Root Cause Hypothesis | Quantified Impact | Downstream Impacted Artifacts |
|---|---|---|---|---|---|
| **PNT-01** | ST-02 (Upload) | Blurry, cropped, or reflective ID uploads accepted by portal. | Client-side validation lacks computer vision quality gating before upload. | 41.2% of all rework cases; +72h delay. | FR-001, FR-002, Story US-DOC-01, UAT-01 |
| **PNT-02** | ST-03 (Screening) | High false-positive watchlist flags for common names. | Rigid string matching without fuzzy match scoring or phonetic filtering. | 28.5% of manual review escalations; +18h wait time. | FR-010, FR-011, Story US-KYC-02, UAT-08 |
| **PNT-03** | ST-04 (L1 Review) | L1 analysts manually re-keying passport numbers and dates of birth. | Disconnected OCR engine; failed auto-population of core forms. | 1.8h touch time per flagged case; $2.4M labor overhead. | FR-005, FR-006, Story US-OPS-01, UAT-04 |
| **PNT-04** | ST-05 (Rework) | Customers do not respond to email requests for days, or abandon entirely. | Asynchronous non-interactive email notifications; no mobile deep-linking. | 24.8% customer abandonment; 39.8h average rework lag. | FR-020, FR-021, Story US-NOT-01, UAT-14 |
| **PNT-05** | ST-06 (L2 Review) | Compliance investigators navigating 5 separate browser windows for screening. | Lack of unified analyst workbench; manual adverse media Googling. | 3.5h touch time per high-risk file; SLA breaches. | FR-015, FR-016, Story US-OPS-03, UAT-12 |
| **PNT-06** | ST-07 (Provisioning)| Overnight batch delay before account number is created and credentials issued. | Legacy batch job execution instead of real-time core REST API calls. | +18.5h wait time even after compliance approval. | FR-030, Story US-SYS-01, UAT-22 |
