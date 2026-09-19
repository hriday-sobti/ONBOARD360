# ONBOARD360 — Interview Walkthrough Guide & Technical Talking Points
**Author:** Hriday Singh Sobti  
**Role Targeted:** Senior Business Analyst / Business Process Consultant / Solution Architect  
**Domain:** Financial Services, Banking Operations, RegTech & AML/KYC  

---

## 1. The 2-Minute Executive Elevator Pitch
> *"ONBOARD360 is an enterprise operational transformation project I led for NovaBank International, a cross-border retail and commercial bank handling 520,000 onboarding applications annually. 
> 
> When I analyzed the baseline process, onboarding took an average of 58.7 hours. By decomposing touch time versus wait time, I discovered that **89.3% of that cycle was pure idle queue wait time** between disconnected departments. Furthermore, **33.4% of applications were stuck in rework loops**, with Pareto analysis showing that over 80% was driven by three simple issues: blurry camera uploads, expired IDs, and address mismatches.
> 
> I redesigned the process from a batch-bound model into an event-driven, straight-through processing architecture. By implementing client-side computer vision defect gating, Jaro-Winkler fuzzy watchlist screening, and a human-in-the-loop AI exception triage engine, we compressed turnaround time to **under 24 hours** (under 15 minutes for 60% straight-through processing) and cut unit operating costs by **81.4% (from $67.45 to $12.55)**, unlocking **$22.09M in annual net recurring cash savings** with a capital payback of just 2.0 months."*

---

## 2. Deep-Dive Questions & Defensible Talking Points

### Q1: "How did you prove that onboarding was slow due to queues rather than compliance complexity?"
* **Talking Point**: *"I applied **Little's Law ($L = \lambda \times W$)** across our 520,000 application dataset. With an inbound arrival rate of ~59.4 applications per hour, our 58.7-hour turnaround time meant we had an active ongoing backlog of nearly 3,500 applications at any given time.
* When I measured the timestamps, active analyst touch time was only 6.29 hours. The remaining 52.42 hours were buffers where applications sat waiting between Retail Operations and L2 Compliance. This proved the problem was asynchronous batch queue handoffs, not the difficulty of the reviews themselves."*

### Q2: "How did you determine what to automate versus what required human review?"
* **Talking Point**: *"I established a strict **Human-In-The-Loop (HITL) regulatory boundary** aligned with FATF Recommendation 10 and regulatory CDD guidelines:
  1. **Automated Straight-Through Processing (STP)**: Restricted strictly to Low-Risk retail applicants with 100% verified document OCR and zero sanctions matches.
  2. **AI Exception Triage**: Evaluated non-STP cases using a Random Forest classifier. Low-risk document defects (blurry photos from low-risk customers) were routed to automated customer self-service via interactive WhatsApp links, bypassing analyst queues.
  3. **Mandatory Human Quarantine**: Any applicant flagged for PEP status, sanctions alerts, or high AML risk **strictly bypassed machine learning scoring** and routed directly to Level-2 Compliance investigators with pre-compiled evidence dossiers. In our 160-test verification audit, zero high-risk cases were leaked to automation."*

### Q3: "How are your financial savings calculated? Are these real numbers?"
* **Talking Point**: *"Every dollar saved is grounded in an **Activity-Based Costing (ABC) model** reconciled against our operational staffing baselines:
  * **L1 Operations Labor**: Baseline was 184,000 reviews at 1.8h touch time ($42/hr) = $13.91M. With 60% STP and AI triage, L1 volume dropped to 41,600 reviews at 0.8h touch time = $1.40M (saving $12.51M).
  * **L2 Compliance Labor**: Jaro-Winkler fuzzy matching cut false-positive alerts by > 50%, reducing L2 labor from $6.79M to $1.52M (saving $5.27M).
  * **Customer Support Inquiries**: 82.8% of our 118,000 support tickets were 'Where is my account?' calls caused by queue invisibility. Kafka event-driven push notifications eliminated 75% of inquiries (saving $1.06M).
  * **Capital Appraisal**: On a $2.85M initial CAPEX and 8.5% corporate hurdle rate, our 3-year cash flows yield an **NPV of $49.50M** and a **discounted payback of 2.0 months**."*

### Q4: "What artifacts did you produce to guide the engineering team?"
* **Talking Point**: *"I authored full enterprise governance and delivery artifacts:
  * **Requirements Catalog**: BRD with 10 Business Requirements, FRD with 35 Functional Specs, and 10 deterministic Business Rules.
  * **Process Models**: Valid BPMN 2.0 XML workflows for both AS-IS and TO-BE states.
  * **Agile Delivery**: Product Backlog across 6 Epics, 432 story points, and 35+ INVEST-compliant user stories with Gherkin acceptance criteria.
  * **Traceability & Testing**: A 100% bidirectional Requirements Traceability Matrix (RTM) and 32 UAT test cases covering positive, negative, and edge scenarios."*
