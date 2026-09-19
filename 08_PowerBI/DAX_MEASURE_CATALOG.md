# ONBOARD360 — Production DAX Measure Catalog (25+ Enterprise Measures)
**Document ID:** PBI-DAX-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. Core Production DAX Measures

### Category 1: Volume & Outcome Measures
```dax
// 1. Total Inbound Applications
Total Applications = COUNTROWS(Fact_Applications)

// 2. Approved Applications Count
Approved Applications = 
CALCULATE(
    COUNTROWS(Fact_Applications),
    Fact_Applications[Status] = "APPROVED"
)

// 3. Approval Rate %
Approval Rate % = 
DIVIDE([Approved Applications], [Total Applications], 0) * 100

// 4. Abandoned Applications Count
Abandoned Applications = 
CALCULATE(
    COUNTROWS(Fact_Applications),
    Fact_Applications[Status] = "ABANDONED"
)

// 5. Abandonment Rate %
Abandonment Rate % = 
DIVIDE([Abandoned Applications], [Total Applications], 0) * 100

// 6. First-Pass Approvals (FPY)
First Pass Approvals = 
CALCULATE(
    COUNTROWS(Fact_Applications),
    Fact_Applications[Status] = "APPROVED",
    Fact_Applications[ReworkFlag] = FALSE
)

// 7. First-Pass Yield (FPY) %
First Pass Yield % = 
DIVIDE([First Pass Approvals], [Total Applications], 0) * 100
```

### Category 2: Efficiency & Cycle Time Measures
```dax
// 8. Mean Turnaround Time (TAT) in Hours
Average TAT Hours = AVERAGE(Fact_Applications[TotalCycleTimeHours])

// 9. Median Turnaround Time in Hours
Median TAT Hours = MEDIAN(Fact_Applications[TotalCycleTimeHours])

// 10. Average Active Touch Time
Average Touch Time Hours = AVERAGE(Fact_Applications[TouchTimeHours])

// 11. Average Idle Wait Time
Average Wait Time Hours = AVERAGE(Fact_Applications[WaitTimeHours])

// 12. Process Cycle Efficiency (PCE) %
Process Cycle Efficiency % = 
DIVIDE([Average Touch Time Hours], [Average TAT Hours], 0) * 100

// 13. SLA Breach Count (>48 Hours)
SLA Breaches = 
CALCULATE(
    COUNTROWS(Fact_Applications),
    Fact_Applications[SLA_BreachFlag] = TRUE
)

// 14. SLA Breach Rate %
SLA Breach Rate % = 
DIVIDE([SLA Breaches], [Total Applications], 0) * 100
```

### Category 3: Quality & Operational Burden
```dax
// 15. Rework Application Count
Rework Applications = 
CALCULATE(
    COUNTROWS(Fact_Applications),
    Fact_Applications[ReworkFlag] = TRUE
)

// 16. Rework Rate %
Rework Rate % = 
DIVIDE([Rework Applications], [Total Applications], 0) * 100

// 17. Manual Review Applications Count
Manual Review Applications = 
CALCULATE(
    COUNTROWS(Fact_Applications),
    Fact_Applications[ManualReviewFlag] = TRUE
)

// 18. Manual Review Rate %
Manual Review Rate % = 
DIVIDE([Manual Review Applications], [Total Applications], 0) * 100
```

### Category 4: Financial & Transformation Benefit Measures
```dax
// 19. Baseline AS-IS Annual Operating Cost
AS-IS Total Operating Cost = 
VAR L1_Cost = CALCULATE(COUNTROWS(Fact_ManualReviews), Fact_ManualReviews[QueueName] = "L1_Document_Exception") * 1.8 * 42.0
VAR L2_Cost = CALCULATE(COUNTROWS(Fact_ManualReviews), Fact_ManualReviews[QueueName] = "L2_AML_Sanctions") * 3.5 * 65.0
VAR Support_Cost = SUM(Fact_SupportTickets[CostToServeUSD])
VAR Vendor_Cost = [Total Applications] * 9.80
VAR Rework_Admin = [Rework Applications] * 4.40
RETURN L1_Cost + L2_Cost + Support_Cost + Vendor_Cost + Rework_Admin

// 20. Unit Operating Cost per Approved Application
Unit Cost per Approved Application = 
DIVIDE([AS-IS Total Operating Cost], [Approved Applications], 0)

// 21. Projected TO-BE Annual Operating Cost (Base Case)
TO-BE Total Operating Cost = 
VAR TO_BE_L1 = [Total Applications] * 0.08 * 0.8 * 42.0
VAR TO_BE_L2 = [Total Applications] * 0.03 * 1.5 * 65.0
VAR TO_BE_Support = SUM(Fact_SupportTickets[CostToServeUSD]) * 0.25
VAR TO_BE_Vendor = [Total Applications] * 4.20
VAR TO_BE_Cloud = 420000.0
RETURN TO_BE_L1 + TO_BE_L2 + TO_BE_Support + TO_BE_Vendor + TO_BE_Cloud

// 22. Projected Annual Net Cost Savings
Projected Annual Savings = 
[AS-IS Total Operating Cost] - [TO-BE Total Operating Cost]

// 23. Interactive What-If Projected Savings (Parameter Driven)
WhatIf_Projected_Savings = 
VAR Selected_STP = 'STP_Scenario_Parameter'[STP_Value] // e.g. 0.60
VAR Modeled_Savings = [AS-IS Total Operating Cost] * (Selected_STP / 0.60) * 0.78
RETURN Modeled_Savings
```
