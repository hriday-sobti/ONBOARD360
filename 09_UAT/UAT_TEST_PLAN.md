# ONBOARD360 — User Acceptance Testing (UAT) Master Test Plan
**Document ID:** UAT-PLN-001  
**Version:** 1.0.0 (Baselined)  
**Lead Test Analyst:** Lead Business Analyst & QA Lead  
**Stakeholder Approvals:** Head of Banking Operations, Head of Compliance, VP of Retail Banking  

---

## 1. Test Strategy & Scope
The ONBOARD360 UAT framework validates that the implemented onboarding platform satisfies all 10 Business Requirements, 35 Functional Requirements, and 10 Business Rules under real-world operational conditions.
* **Testing Scope**: Client-side document capture, OCR text parsing, fuzzy watchlist screening, Straight-Through Processing (STP) auto-provisioning, AI Exception Triage routing, Unified Analyst Workbench queue handling, and regulatory audit logging.
* **Entry Criteria**: All functional code deployed to Staging; system integration tests passing at $\ge 98\%$; test data provisioned across 4 regions and 4 risk tiers.
* **Exit Criteria**: 100% execution of 32 core UAT test cases; 0 Critical or High severity defects open; formal sign-off from Retail, Ops, and Compliance leads.

---

## 2. Test Environment & Persona Profiles
* **Applicant Personas**: Retail Clean (John Doe), Blurry ID (Jane Smith), Expired Passport (Mark Davis), Watchlist Fuzzy Match (Mohammed Al-Sayed), PEP Alert (Senator Robert Taylor), SME Director (Acme Corp).
* **Internal Personas**: Tier-1 Operations Analyst, Tier-2 Compliance Officer, Branch Relationship Manager, Systems Administrator.
