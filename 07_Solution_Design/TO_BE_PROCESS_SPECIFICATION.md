# ONBOARD360 — TO-BE Process Specification & Transformation Blueprint
**Document ID:** SOL-PRC-002  
**Version:** 1.0.0 (Baselined)  

---

## 1. Process Transformation Summary
The TO-BE process redesign replaces sequential batch processing with a **parallel, event-driven microservices architecture**. 

| Process Dimension | AS-IS Baseline | TO-BE Target | Structural Transformation Mechanism |
|---|---|---|---|
| **End-to-End TAT** | 58.70 Hours (Avg) | **< 24.0 Hours (Avg) / < 15 Mins (STP)** | Event-driven microservices eliminate 89.3% queue wait buffers. |
| **Straight-Through Processing (STP)** | 0% (Batch) | **$\ge$ 60.0%** | Automated rule gates for Low-Risk & verified document applicants. |
| **First-Pass Yield (FPY)** | 58.12% | **$\ge$ 78.0%** | Upfront client-side Computer Vision (CV) sharpness & glare gating. |
| **Rework Rate** | 33.35% | **$\le$ 10.0%** | Pre-upload verification stops 83.2% of blurry and expired ID errors. |
| **Manual Review Burden** | 41.12% | **$\le$ 18.0%** | AI Exception Triage auto-routes low-risk doc anomalies to self-service. |
| **Customer Abandonment** | 16.25% | **$\le$ 7.5%** | Interactive WhatsApp/SMS 1-click camera remediation vs static email. |
| **SLA Breach Rate (>48h)** | 45.92% | **$\le$ 2.5%** | Queue prioritization based on real-time SLA expiration countdowns. |
| **Unit Operating Cost** | $54.20 | **$\le$ $18.50** | $18.5M+ annual operational savings via automation and labor shift. |

---

## 2. Transformation Logic & Benefit Realization Chain
Every operational modification in the TO-BE process is strictly grounded in evidence:
1. **Evidence**: Pareto analysis demonstrated that Blurry Images (42.1%) and Expired IDs (23.0%) drive 65.1% of all rework loops.
   * **TO-BE Change**: Embed client-side OpenCV WebAssembly into mobile and web portals (FR-001, FR-002).
   * **Benefit**: 80% reduction in document-related rework; eliminates 39.8 hours of downstream rework delay.
2. **Evidence**: 82.8% of customer support tickets are "Where is my account?" status inquiries caused by queue invisibility.
   * **TO-BE Change**: Kafka event stream triggers proactive SMS and push notifications at every stage transition (FR-025).
   * **Benefit**: 75% reduction in inbound support tickets, saving $1.05M annually in direct support costs.
3. **Evidence**: Overnight batch screening caused an automatic 18.5-hour delay even for clean applicants.
   * **TO-BE Change**: Replace legacy mainframe nightly batch with real-time REST API microservices (FR-010, FR-030).
   * **Benefit**: 60% of applicants receive active IBAN and virtual debit card in under 15 minutes.
