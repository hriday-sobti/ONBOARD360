# ONBOARD360 — Architectural Decision Log (ADR)
**Document ID:** GOV-DEC-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. Decision Inventory

| Decision ID | Decision Title | Status | Date | Context & Rationale | Consequences & Trade-offs |
|---|---|---|---|---|---|
| **ADR-001** | Synthetic Data Generation Architecture (520K+ Records) | **ACCEPTED** | 2026-09-19 | Realistic BA transformation demands empirical evidence with genuine statistical variance, long-tail queues, and realistic defect distributions. | Vectorized NumPy/Pandas generator produces 520,000 core applications, 240K+ reviews, and 118K support tickets with referential integrity. |
| **ADR-002** | Human-in-the-Loop (HITL) AI Exception Triage | **ACCEPTED** | 2026-09-19 | Pure autonomous machine learning in banking KYC creates severe compliance liabilities and regulatory exposure under FATF / FinCEN / FCA rules. | Hardcoded rule pre-filters high-risk, sanctions, and PEP cases to L2 human compliance officers; ML model only routes low-risk document anomalies. |
| **ADR-003** | Upfront Client-Side Computer Vision Validation | **ACCEPTED** | 2026-09-19 | 83.2% of rework was caused by blurry images, glare, and expired IDs. Catching these at the client camera eliminates downstream queue deadlocks. | WebAssembly OpenCV embedded in mobile/web portals; prevents image upload if sharpness < 150 or glare > 8%. |
| **ADR-004** | Event-Driven Kafka Microservices Architecture | **ACCEPTED** | 2026-09-19 | Legacy overnight batch screening added 18.5 hours of artificial delay even for clean applicants, driving 82.8% of support tickets. | Real-time REST APIs and Kafka events enable Straight-Through Processing (<15 mins) and instant stage push notifications. |
| **ADR-005** | Hybrid Relational (3NF) & Analytical (Parquet/Star) Storage | **ACCEPTED** | 2026-09-19 | Need strict transactional auditability for compliance alongside sub-second aggregation speed for Power BI and Python analytics. | PostgreSQL manages transactional consistency and immutable audit logs; columnar Parquet powers data lake analytics. |
