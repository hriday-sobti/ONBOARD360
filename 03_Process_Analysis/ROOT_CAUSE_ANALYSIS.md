# ONBOARD360 — Root Cause Analysis (RCA) & Ishikawa Breakdown
**Document ID:** PRC-RCA-001  
**Version:** 1.0.0 (Baselined)  
**Methodologies:** 5 Whys, Ishikawa (Fishbone) Diagram, Pareto 80/20 Distribution  

---

## 1. Executive RCA Summary
Empirical analysis of the 520,000 application dataset reveals that the onboarding crisis is not primarily caused by compliance complexity, but rather by **asynchronous document rework loops and unmanaged queue buffers**. 
* **89.3%** of the onboarding turnaround time is idle queue wait time (52.42 hours out of 58.70 hours total).
* Top 3 document defects (**Blurry Images 42.1%**, **Expired IDs 23.0%**, and **Address Mismatches 18.0%**) account for **83.2%** of all rework cases (classic Pareto principle).
* 82.8% of inbound customer service tickets are "Where is my account?" status inquiries triggered directly by queue delays.

---

## 2. The 5 Whys Root Cause Investigation

### Failure Mode 1: Excessive Turnaround Time (TAT) & SLA Breaches
1. **Why is onboarding TAT exceeding 48 hours for 45.9% of applicants?**  
   *Because applications sit in manual operations queues for an average of 52.4 hours before an analyst reviews them.*
2. **Why do applications sit in queue buffers for over 52 hours?**  
   *Because 41.1% of all applications require human analyst intervention, generating an overwhelming backlog of over 3,100 active queued applications at any given moment.*
3. **Why do 41.1% of applications require human intervention?**  
   *Because 33.4% have document defect rework flags and rigid watchlist screening generates high false-positive alerts.*
4. **Why do 33.4% of applications have document defects?**  
   *Because the mobile and web portals accept raw photos without evaluating image resolution, blur, glare, or expiration dates.*
5. **ROOT CAUSE 1:**  
   **The frontend onboarding portal lacks real-time, client-side computer vision validation and automated guided capture, allowing defective documents to pollute downstream compliance workflows.**

---

### Failure Mode 2: High Customer Abandonment (16.3% to 18.5% on Mobile)
1. **Why are customers abandoning their applications midway through the process?**  
   *Because they receive an email stating their uploaded ID was rejected and requesting resubmission.*
2. **Why does document resubmission trigger abandonment?**  
   *Because the notification is a static, one-way email that provides vague feedback (e.g., "Document Invalid") without specifying the exact error or providing a 1-click mobile camera link.*
3. **Why does the email lack specific feedback?**  
   *Because the L1 analyst selects generic decline codes, and the legacy core messaging system lacks dynamic deep-linking capabilities.*
4. **Why does the customer choose not to resubmit?**  
   *Because competing fintech neobanks provide instant in-app account creation with automated verification in under 5 minutes.*
5. **ROOT CAUSE 2:**  
   **Lack of interactive, guided self-service remediation and transparent real-time status tracking causes high customer drop-off at friction points.**

---

## 3. Ishikawa (Fishbone) Cause-and-Effect Diagram

```
   PEOPLE / ORGANIZATION                      PROCESS / GOVERNANCE
   ┌─────────────────────────────────┐        ┌─────────────────────────────────┐
   │ • Analyst burnout & fatigue     │        │ • Asynchronous email rework loops│
   │ • Siloed L1 vs L2 review teams  │        │ • Over-escalation to L2 queues  │
   │ • Fragmented regional training  │        │ • Lack of straight-through flow │
   └────────────────┬────────────────┘        └────────────────┬────────────────┘
                    │                                          │
                    ├──────────────────────────────────────────┤
                    │                                          │
   ┌────────────────┴────────────────┐        ┌────────────────┴────────────────┐
   │ • Client accepts blurry photos  │        │ • Rigid exact-string watchlist  │
   │ • Disconnected legacy core batch│        │ • No fuzzy name matching score  │
   │ • No client-side edge validation│        │ • Disjointed multi-system data  │
   └─────────────────────────────────┘        └─────────────────────────────────┘
   TECHNOLOGY / INTEGRATION                   POLICY / REGULATORY RULES
                                                                       │
                                                                       ▼
                                                          [ONBOARDING BOTTLENECK]
                                                          • 58.7h Cycle Time
                                                          • 89.3% Wait Time
                                                          • 33.4% Rework Rate
```

---

## 4. Pareto Rework Distribution Table

| Rework Failure Category | Annual Count | Percentage | Cumulative Pct | Target Solution / Requirement |
|---|---|---|---|---|
| **Blurry / Glare Image** | 72,994 | 42.09% | 42.09% | FR-001: Client-Side Computer Vision Quality Gate |
| **Expired Identification** | 39,964 | 23.04% | 65.13% | FR-002: Real-time OCR Expiry Date Validation |
| **Address Proof Mismatch** | 31,249 | 18.02% | 83.15% | FR-003: Automated Postal & Utility Bureau Lookup |
| **Incomplete Form Fields** | 20,716 | 11.94% | 95.10% | FR-004: Interactive Field Validation & Form Prefill |
| **Name Typo / Mismatch** | 8,506 | 4.90% | 100.00% | FR-010: Jaro-Winkler Fuzzy Matching Algorithm |
| **TOTAL** | **173,429** | **100.00%** | **100.00%** | **Eliminates > 80% of current rework volume** |
