# ONBOARD360 — AI Exception Triage Model Card & Governance Specification
**Document ID:** GOV-AI-001  
**Version:** 1.0.0 (Baselined)  
**Standard:** NIST AI Risk Management Framework & EU AI Act High-Risk Governance  

---

## 1. Model Overview & Purpose
* **Model Name**: ONBOARD360 Intelligent Exception & Document Triage Engine
* **Model Type**: Supervised Random Forest Classifier with Hardcoded Rule Guardrails
* **Intended Purpose**: Automates the categorization, scoring, and routing of onboarding exceptions. Low-risk document defects (e.g., blurry image from a low-risk retail applicant) are routed directly to real-time customer self-service remediation, while complex risks, PEP alerts, and sanctions holds are routed to human compliance investigators.
* **Prohibited Use**: Autonomous regulatory de-risking or account declination without human compliance sign-off.

---

## 2. Regulatory Guardrails & Human-in-the-Loop (HITL) Controls
In accordance with FATF Recommendation 10 and FCA Senior Managers Regime:
1. **Zero High-Risk Leakage**: The model architecture enforces a pre-classification deterministic rule: Any applicant with `risk_tier in ['HIGH', 'PEP']` or `watchlist_match_score >= 85` bypasses machine learning scoring and is assigned to the L2 Compliance Queue.
2. **Explainability**: For every model decision, the engine provides the top-3 feature importances (`risk_tier`, `rework_reason`, `sharpness_score`) rendered in the Analyst Workbench.
3. **Auditability**: Every prediction, probability vector, and routing event is logged with a cryptographic hash to the PostgreSQL audit table.
