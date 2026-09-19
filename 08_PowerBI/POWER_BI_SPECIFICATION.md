# ONBOARD360 — Power BI Enterprise Dashboard Architecture & Specifications
**Document ID:** PBI-SPEC-001  
**Version:** 1.0.0 (Baselined)  
**Target PBIX File:** `08_PowerBI/ONBOARD360.pbix`  

---

## 1. Power BI Star Schema Data Model

```
       ┌────────────────────────┐         ┌────────────────────────┐
       │     Dim_Calendar       │         │      Dim_Customer      │
       │ • DateKey (PK)         │         │ • CustomerID (PK)      │
       │ • Date, Month, Year    │         │ • CustomerType, Region │
       └───────────┬────────────┘         └───────────┬────────────┘
                   │                                  │
                   │ 1:N                              │ 1:N
                   ▼                                  ▼
       ┌───────────────────────────────────────────────────────────┐
       │                     Fact_Applications                     │
       │ • ApplicationID (PK)      • RiskTier                      │
       │ • CustomerID (FK)         • ReworkFlag, ManualReviewFlag  │
       │ • DateKey (FK)            • Status, SLA_BreachFlag        │
       │ • Channel, ProductType    • CycleTimeHrs, WaitHrs, TouchHrs│
       └───────────┬──────────────────────────────────┬────────────┘
                   │ 1:N                              │ 1:N
                   ▼                                  ▼
       ┌────────────────────────┐         ┌────────────────────────┐
       │   Fact_ManualReviews   │         │  Fact_SupportTickets   │
       │ • ReviewID (PK)        │         │ • TicketID (PK)        │
       │ • ApplicationID (FK)   │         │ • ApplicationID (FK)   │
       │ • QueueName, Duration  │         │ • Channel, CostToServe │
       └────────────────────────┘         └────────────────────────┘
```

---

## 2. Five-Page Executive Dashboard Wireframes

### Page 1: Onboarding Command Center (Executive Overview)
* **Top KPI Cards**: Total Applications (520K), Average TAT (58.7h -> Target 24h), First-Pass Yield (58.1% -> Target 78%), Straight-Through Processing Rate (Target 60%), Abandonment Rate (16.2%), Total Annual OPEX ($27.9M).
* **Visual 1 (Line & Clustered Column)**: Monthly Application Volume vs. SLA Breach Rate trend across 2025.
* **Visual 2 (Donut Chart)**: Applications by Channel (Mobile 50%, Web 28%, Branch 12%, Affiliate 10%).
* **Visual 3 (Stacked Bar Chart)**: Lifecycle Status (Approved, Abandoned, Rejected) segmented by Customer Tier.
* **Slicers**: Region, Date Range, Channel, Risk Tier.

### Page 2: Process Bottleneck & Queue Dynamics
* **Visual 1 (Waterfall / Decomposition Tree)**: Total Cycle Time (58.70h) decomposed into Touch Time (6.29h, 10.7%) and Queue Wait Time (52.42h, 89.3%).
* **Visual 2 (Clustered Bar Chart)**: Average Queue Wait Hours by Review Team (L1 Ops vs L2 Compliance vs Batch).
* **Visual 3 (Scatter Plot)**: Touch Time vs. Wait Time with bubble size representing SLA Breaches.

### Page 3: Root Cause & Document Defect Pareto Center
* **Visual 1 (Pareto Chart)**: Rework Reasons count (Bars) and Cumulative % (Line): Blurry Images (42.1%), Expired IDs (23.0%), Address Mismatches (18.0%), Incomplete Forms (11.9%).
* **Visual 2 (Matrix Table)**: Rework Rate and Abandonment Rate drilled down by Channel and Customer Type.

### Page 4: Transformation Impact & What-If Simulator
* **Visual 1 (Gauge Charts)**: Current vs. Target gauges for TAT, FPY, and Unit Operating Cost.
* **Visual 2 (Scenario Parameter Slicer)**: Interactive slider adjusting STP Rate (40% to 80%) dynamically recalculating projected annual dollar savings ($16M - $27M).

### Page 5: Executive Action Center
* **Visual 1 (Action Grid Table)**: Problem -> Root Cause Evidence -> Proposed Requirement -> Owner -> Expected Impact.
