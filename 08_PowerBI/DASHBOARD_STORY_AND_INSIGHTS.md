# ONBOARD360 — Dashboard Analytical Story, Chart Audit & Executive Insights
**Document ID:** PBI-INS-001  
**Author:** Hriday Singh Sobti (Senior Business Analyst & Solution Architect)  
**Date:** 2026-09-28  
**Scope:** Complete 5-Page Dashboard Audit & 12-Chart Narrative Storyline  
**Status:** COMPLETE & VERIFIED  

---

## 1. The End-to-End Analytical Story Architecture

The ONBOARD360 dashboard is designed not as a disconnected collection of metrics, but as a **single, rigorous diagnostic sequence** that guides senior leadership from symptom to root cause, architectural remedy, and financial return:

```
[Figure 1 & 2: Macro Performance & Channels]
                 │
                 ▼
[Figure 3: Lifecycle Outcomes & Funnel Drop-off]
                 │
                 ▼
[Figure 4 & 5: Lead Time Breakdown — Active Touch vs. Idle Queue Wait]
                 │
                 ▼
[Figure 6: Little's Law Backlog & Queue Congestion Dynamics]
                 │
                 ▼
[Figure 7 & 8: Pareto Root Causes of 83% Rework Defect Loops]
                 │
                 ▼
[Figure 9: Target State Operational Benchmark Trajectory]
                 │
                 ▼
[Figure 10: Dynamic What-If Financial Sensitivity Simulator]
                 │
                 ▼
[Figure 11 & 12: Activity-Based Costing & 3-Year DCF / NPV Realization]
```

---

## 2. Page-by-Page & Chart-by-Chart Forensic Audit

---

### PAGE 1: ONBOARDING COMMAND CENTER (EXECUTIVE OVERVIEW)

#### Figure 1 — Monthly Application Inflow vs. SLA Breach Rate Trend (2025)
* **What Business Question It Answers**: Is application volume surging, and how effectively is operations maintaining customer service commitments over time?
* **Why It Is Needed**: Executive leadership requires visibility into operational stability across seasonal volume peaks.
* **What It Shows**: Monthly intake volume (steady at ~43,300 applications/month, total 520,000) mapped against the monthly percentage of applications breaching the 48-hour SLA threshold.
* **Key Insight**: The SLA breach rate hovered consistently between 45.2% and 46.8% all year, averaging **45.92%** (238,784 breaches). It does not fluctuate with seasonal volume spikes; it is a permanent systemic defect of the queue architecture.
* **Why The Insight Matters**: Disproves the operational myth that delays are seasonal. The onboarding engine is structurally broken regardless of volume.
* **Who Is Affected**: All retail applicants (delayed onboarding), Customer Support (surging status tickets), and Retail Leadership (missed deposit targets).
* **Improvement / Action**: Replace batch-driven handoffs with event-driven straight-through processing (STP) to eliminate queue hold times.
* **What Chart Should Come Next**: Figure 2 (Where is this incoming volume originating?).
* **Executive Takeaway**: NovaBank fails its customer SLA on nearly 1 out of every 2 applications (45.92%) every single month. Adding temporary labor cannot fix a structurally queue-bound process.

---

#### Figure 2 — Intake Volume & Channel Mix Breakdown
* **What Business Question It Answers**: Which customer acquisition channels drive the highest onboarding demand and warrant prioritization?
* **Why It Is Needed**: Capital and engineering resources must focus on customer-preferred channels.
* **What It Shows**: Total 520,000 application distribution: Mobile App (50.0%, 260,000 apps), Web Portal (28.0%, 145,600 apps), Branch Assisted (12.0%, 62,400 apps), Affiliate Partners (10.0%, 52,000 apps).
* **Key Insight**: Digital self-service channels account for **78.0% of total volume** (405,600 applications), yet mobile suffers from the highest rework and abandonment rates due to mobile camera quality variance.
* **Why The Insight Matters**: 4 out of 5 customers onboard via handheld screens, making mobile capture quality the primary lever for operational transformation.
* **Who Is Affected**: Mobile applicants, Digital Product Managers, and Level-1 Operations reviewers.
* **Improvement / Action**: Deploy client-side WebAssembly computer vision directly into the mobile camera viewfinder (FR-001).
* **What Chart Should Come Next**: Figure 3 (What happens to these applications across customer segments?).
* **Executive Takeaway**: Mobile and Web capture 78% of all customers. Upgrading the mobile camera capture experience is the highest-ROI operational investment available.

---

#### Figure 3 — Lifecycle Status Outcomes by Customer Segment
* **What Business Question It Answers**: Are application approvals, drop-offs, and rejections uniform across customer tiers, or are high-value segments disproportionately penalized?
* **Why It Is Needed**: High-margin wealth and SME customers must not be lost to friction in standard retail pipelines.
* **What It Shows**: Volume breakdown across Approved (79.74%), Abandoned (16.25%), and Rejected (4.01%) for Standard Retail, Fintech Digital, Premier Wealth, and SME Business.
* **Key Insight**: Fintech Digital and Standard Retail applicants experience the highest abandonment rates (**17.8% and 16.4%**), whereas Premier Wealth experiences extended cycle times due to manual paperwork escalations.
* **Why The Insight Matters**: 84,500 qualified applicants abandon the bank annually before funding their accounts, destroying $58M+ in customer lifetime value.
* **Who Is Affected**: Retail Sales, Commercial Banking, and Prospective Depositors.
* **Improvement / Action**: Implement omnichannel session resumption (FR-020) and automated postal prefill to eliminate form fatigue.
* **What Chart Should Come Next**: Figure 4 (Why are customers abandoning? Where is the time actually going?).
* **Executive Takeaway**: 16.25% of all applicants drop out before finishing. Reducing customer effort via automated prefill and instant approvals will rescue over 45,000 accounts annually.

---

### PAGE 2: PROCESS BOTTLENECK & QUEUE DYNAMICS

#### Figure 4 — Lead Time Decomposition: Active Touch Time vs. Idle Queue Wait Time
* **What Business Question It Answers**: Is onboarding delay caused by lengthy analyst work or by idle queue waiting?
* **Why It Is Needed**: Directly answers whether the bank needs more operational headcount or a new orchestration architecture.
* **What It Shows**: Deconstructed average turnaround time (58.70 hours) into active analyst processing touch time (6.29 hours, 10.71%) and idle buffer wait time (52.42 hours, 89.29%).
* **Key Insight**: Over **89.3% of the customer's waiting time** is spent sitting idle in unworked departmental queues between Retail Operations, KYC L1, and Compliance L2. Active human touch represents barely 10% of the timeline.
* **Why The Insight Matters**: Process Cycle Efficiency (PCE) is an abysmal 10.71%. Doubling analyst headcount would only affect the 6.29 hours of touch time; eliminating queue handoffs resolves the 52.42 hours of dead time.
* **Who Is Affected**: Operations Leadership, Workforce Planning, and Branch Teams.
* **Improvement / Action**: Replace asynchronous queue batch transfers with real-time Kafka event streaming and Straight-Through Processing.
* **What Chart Should Come Next**: Figure 5 (Which departmental queues are accumulating this 52.42 hours of idle wait time?).
* **Executive Takeaway**: Customers wait 58.7 hours not because reviews take long (6.3h), but because files sit untouched in queues for 52.4 hours. The problem is queue latency, not analyst productivity.

---

#### Figure 5 — Departmental Queue Latency & Hand-off Delays
* **What Business Question It Answers**: Where in the organizational hierarchy do applications sit idle the longest?
* **Why It Is Needed**: Pinpoints the exact operational hand-offs that cause SLA failure.
* **What It Shows**: Average queue wait hours accumulated across 4 stages: Initial Intake Buffer (8.4h), Level-1 Operations Queue (18.6h), Level-2 Compliance Escalation Queue (21.2h), and Core Ledger Batch Provisioning (18.5h).
* **Key Insight**: Compliance L2 review queues and Core Banking overnight batch ledgers generate **39.7 hours of combined delay** (75.7% of total queue latency).
* **Why The Insight Matters**: Clean applications are delayed by overnight batch accounting runs, while compliance investigators are buried under false-positive sanctions alerts.
* **Who Is Affected**: Compliance Investigators, Core Banking IT, and Tier-1 Ops Managers.
* **Improvement / Action**: Implement synchronous Core Banking REST provisioning (FR-030) and Jaro-Winkler fuzzy watchlist screening (FR-010).
* **What Chart Should Come Next**: Figure 6 (What is the resulting operational work-in-progress inventory across the bank?).
* **Executive Takeaway**: Overnight batch core runs (18.5h) and Compliance backlogs (21.2h) create a 40-hour dead zone. Real-time REST APIs and intelligent screening eliminate both bottlenecks.

---

#### Figure 6 — Queue Buffer Congestion & Little's Law WIP Dynamics
* **What Business Question It Answers**: How much active uncompleted inventory is stuck in the bank's pipeline at any single point in time?
* **Why It Is Needed**: Quantifies the bank's operational liability and backlog vulnerability under Little's Law ($L = \lambda \times W$).
* **What It Shows**: System arrival rate ($\lambda = 59.36$ apps/hour) multiplied by mean cycle time ($W = 58.70$ hours) yielding an average active work-in-progress (WIP) of **3,485 applications**, with 3,111 applications idle.
* **Key Insight**: At any given hour, over 3,100 customer applications are parked in limbo, driving continuous risk exposure and inbound customer panic calls.
* **Why The Insight Matters**: High WIP creates operational chaos, increases customer contact frequency, and slows overall cycle velocity.
* **Who Is Affected**: Operations Managers, Risk Officers, and Contact Center Agents.
* **Improvement / Action**: Re-engineer the process to compress $W$ below 24.0 hours, slashing system WIP from 3,485 to under 800 active cases.
* **What Chart Should Come Next**: Figure 7 (What is triggering files to get pushed out of the main flow into these queues?).
* **Executive Takeaway**: Over 3,400 customer files are trapped in the pipeline at any given moment under Little's Law. Compressing cycle time to < 24h cuts operational backlog by 77%.

---

### PAGE 3: ROOT CAUSE & DOCUMENT DEFECT PARETO CENTER

#### Figure 7 — Pareto Distribution of Document Rework Drivers
* **What Business Question It Answers**: Exactly what defects force 173,429 applications into manual rework loops?
* **Why It Is Needed**: Ensures technology teams solve the high-impact root causes rather than low-frequency edge cases.
* **What It Shows**: Frequency and cumulative percentage of all 173,429 rework defect incidents across 5 failure modes: Blurry Image (72,994 / 42.09%), Expired ID (39,964 / 23.04%), Address Proof Mismatch (31,249 / 18.02%), Incomplete Form (20,716 / 11.94%), Name Mismatch (8,506 / 4.90%).
* **Key Insight**: The top 3 document flaws account for **83.15% of all rework loops**. Blurry images alone represent more than 4 out of every 10 rework loops.
* **Why The Insight Matters**: Proves that 83% of rework has nothing to do with complex banking fraud; it is caused by poor camera capture and unvalidated form fields.
* **Who Is Affected**: Retail Applicants (frustration of resubmitting), L1 Reviewers (manual image inspection), and Operations Leadership.
* **Improvement / Action**: Implement real-time client-side OpenCV WebAssembly blur gating (FR-001), OCR expiration date validation (FR-002), and postal code address lookup (FR-003).
* **What Chart Should Come Next**: Figure 8 (Which acquisition channels generate these defects?).
* **Executive Takeaway**: 83.2% of all rework is caused by just three preventable flaws: blurry photos, expired IDs, and address typos. Client-side validation stops 144,000 defect loops before submission.

---

#### Figure 8 — Rework Rate & Abandonment Matrix by Channel & Customer Type
* **What Business Question It Answers**: Where are document defects and customer drop-offs concentrated?
* **Why It Is Needed**: Validates whether in-branch onboarding avoids the defect rate observed in mobile channels.
* **What It Shows**: Cross-tabulated rework and abandonment rates: Mobile App shows 36.8% rework and 17.8% abandonment; Branch Assisted shows 18.2% rework and 8.1% abandonment.
* **Key Insight**: Mobile app users suffer double the rework rate of branch applicants because branches have staff assisting document scanning, while mobile users lack feedback on photo quality.
* **Why The Insight Matters**: Proves that digital self-service requires automated "virtual branch assistant" quality checks at the point of capture.
* **Who Is Affected**: Mobile Banking Engineers, Digital Channel Managers, and Retail Customers.
* **Improvement / Action**: Embed real-time viewfinder framing assistance and instant OCR prefill in the mobile SDK.
* **What Chart Should Come Next**: Figure 9 (What target performance is achievable once these solutions are deployed?).
* **Executive Takeaway**: Mobile applicants fail twice as often as branch applicants due to lack of scan guidance. Bringing automated camera intelligence to the mobile app bridges this gap.

---

### PAGE 4: TRANSFORMATION IMPACT & WHAT-IF SIMULATOR

#### Figure 9 — Core Transformation KPI Benchmark Trajectory (Current vs. Target)
* **What Business Question It Answers**: What operational and customer benchmarks will the bank achieve post-transformation?
* **Why It Is Needed**: Provides clear performance targets for operational managers and project sponsors.
* **What It Shows**: Multi-metric comparison between AS-IS Baseline and TO-BE Target:
  * Turnaround Time: 58.70h $\rightarrow$ < 24.00h (-59.1%)
  * Straight-Through Processing: 0.0% $\rightarrow$ 60.0% (+60.0 pts)
  * First-Pass Yield: 58.12% $\rightarrow$ 78.00%+ (+19.9 pts)
  * Rework Rate: 33.35% $\rightarrow$ < 10.00% (-70.0%)
  * Manual Review Rate: 41.12% $\rightarrow$ < 18.00% (-56.2%)
  * Direct Unit Cost: $67.45 $\rightarrow$ $12.55 (-81.4%)
* **Key Insight**: The transformation delivers compounding operational improvements; reducing rework upfront enables 60% STP, which collapses turnaround times and drives an 81.4% reduction in unit processing cost.
* **Why The Insight Matters**: Demonstrates that operational excellence directly drives competitive pricing and rapid account activation.
* **Who Is Affected**: C-Suite, Heads of Retail and Operations, and End Customers.
* **Improvement / Action**: Maintain strict operational governance against these targets via the Power BI command center.
* **What Chart Should Come Next**: Figure 10 (How sensitive are the financial returns if we achieve different STP levels?).
* **Executive Takeaway**: ONBOARD360 transforms NovaBank into a top-tier digital bank, cutting turnaround time by 59%, slashing unit costs by 81%, and automating 60% of volume.

---

#### Figure 10 — Dynamic What-If Financial Sensitivity Simulator (STP vs. Net Savings)
* **What Business Question It Answers**: What happens to our annual cash savings and 3-Year NPV if straight-through processing falls short of or exceeds the 60% target?
* **Why It Is Needed**: Provides risk officers and finance teams with transparent scenario testing for board capital appraisal.
* **What It Shows**: Interactive sensitivity curve mapping STP rate from 40% to 80% against Annual Operating Savings ($16.5M to $27.0M) and 3-Year Net Present Value ($36.1M to $61.4M).
  * Conservative Case (45% STP, $3.2M Capex): $16.57M Annual Benefit | $36.06M 3-Yr NPV
  * Base Case (60% STP, $2.85M Capex): $22.09M Annual Benefit | $49.50M 3-Yr NPV
  * Aggressive Case (75% STP, $2.5M Capex): $26.95M Annual Benefit | $61.37M 3-Yr NPV
* **Key Insight**: Even under the most pessimistic scenario (45% STP with 12% cost overrun), the project generates **$16.57M in annual recurring savings** and a **$36.06M 3-Year NPV**.
* **Why The Insight Matters**: Establishes that the transformation is financially asymmetrical with virtually zero risk of negative capital return.
* **Who Is Affected**: Chief Financial Officer, Investment Committee, and Enterprise Risk.
* **Improvement / Action**: Baseline financial business case on the 60% STP Base Case with confidence in downside protection.
* **What Chart Should Come Next**: Figure 11 (Where do these savings actually come from across our operating expense budget?).
* **Executive Takeaway**: The business case is robust: even under a conservative 45% STP adoption rate, ONBOARD360 returns $16.57M annually with a $36.06M NPV. The downside is fully protected.

---

### PAGE 5: EXECUTIVE ACTION & VALUE REALIZATION CENTER

#### Figure 11 — Activity-Based Annual Operating Cost Decomposition (AS-IS vs. TO-BE)
* **What Business Question It Answers**: In which specific budget line items are operational savings generated?
* **Why It Is Needed**: CFO and department heads require auditable accounting line-item variance proof.
* **What It Shows**: Side-by-side cost waterfall comparing AS-IS ($27.97M) against TO-BE ($5.87M):
  * Level-1 Operations Labor: $13.91M $\rightarrow$ $1.40M (+$12.51M savings)
  * Level-2 Compliance Labor: $6.79M $\rightarrow$ $1.52M (+$5.27M savings)
  * Customer Support Inquiries: $1.41M $\rightarrow$ $0.35M (+$1.06M savings)
  * Identity Screening & Vendor APIs: $5.10M $\rightarrow$ $2.18M (+$2.91M savings)
  * Manual Mailing & Admin: $0.76M $\rightarrow$ $0.00M (+$0.76M savings)
  * Cloud & AI SaaS OPEX: $0.00M $\rightarrow$ $0.42M (-$0.42M investment)
  * **Total Annual OPEX: $27.97M $\rightarrow$ $5.87M (+$22.09M Net Cash Savings)**
* **Key Insight**: 80.5% of total savings ($17.78M) come from liberating Operations and Compliance personnel from repetitive manual reviews.
* **Why The Insight Matters**: Frees up 100+ skilled analysts to focus on high-value corporate accounts, complex AML investigations, and fraud prevention.
* **Who Is Affected**: CFO, Head of Operations, Head of Compliance, Head of Customer Service.
* **Improvement / Action**: Execute the Prosci ADKAR change management plan to retrain L1 staff for advanced investigation roles.
* **What Chart Should Come Next**: Figure 12 (What is the capital recovery schedule for this investment?).
* **Executive Takeaway**: ONBOARD360 captures $22.09M in annual recurring savings by reducing manual review labor by $17.78M, vendor fees by $2.91M, and support costs by $1.06M.

---

#### Figure 12 — 3-Year Capital Investment Cash Flow & Payback Horizon
* **What Business Question It Answers**: How quickly does NovaBank recover its $2.85M initial capital investment, and what is the multi-year return profile?
* **Why It Is Needed**: Board of Directors requires formal capital appraisal metrics (NPV, IRR, Payback) before capital release.
* **What It Shows**: Discounted cash flow profile across a 36-month horizon using an 8.5% hurdle discount rate:
  * Month 0: Initial Capital Outlay (-$2,850,000.00)
  * Year 1 (Months 1–12, 80% realization): +$17,673,820.88 net cash inflow
  * Year 2 (Months 13–24, 100% realization): +$22,092,276.10 net cash inflow
  * Year 3 (Months 25–36, 100% realization): +$22,092,276.10 net cash inflow
  * Cumulative 3-Year Undiscounted Cash Return: **+$59,008,373.08**
  * **3-Year Net Present Value (NPV @ 8.5%): $49,501,858.44**
  * **Internal Rate of Return (IRR): > 200.0%**
  * **Capital Payback Period: 2.0 Months** (cumulative cash flow turns positive in Month 2)
* **Key Insight**: The project pays for itself in just **2.0 months of full operation**, generating an exceptional 3-Year Net Present Value of nearly $50M on an initial $2.85M investment.
* **Why The Insight Matters**: Ranks among the highest-returning digital transformation initiatives in the global banking sector.
* **Who Is Affected**: Board of Directors, Chief Executive Officer, and Shareholders.
* **Improvement / Action**: Secure formal Gate-0 capital allocation and initiate Phase 1 vendor procurement immediately.
* **What Chart Concludes The Story**: Complete lifecycle story concluded; leads directly to Board sign-off and phased regional rollout.
* **Executive Takeaway**: An investment of $2.85M delivers $49.50M in 3-Year NPV, an IRR exceeding 200%, and breaks even in 2.0 months. Executive approval is strongly recommended.
