"""
ONBOARD360 — Financial Cost-Benefit & ROI Model
Computes Activity-Based Costing (ABC) for AS-IS vs. TO-BE, Net Present Value (NPV),
Internal Rate of Return (IRR), and Payback Period across 3 operational scenarios.
"""

import numpy as np
import pandas as pd

def run_financial_model():
    print("=================================================================")
    print("       ONBOARD360 COMPREHENSIVE BUSINESS CASE & ROI MODEL       ")
    print("=================================================================\n")

    # Baseline Annual Volume & Metrics
    annual_volume = 520000
    apps_approved_as_is = 414655
    apps_approved_to_be = 468000 # Higher due to 16.25% -> 6.0% abandonment reduction
    
    # Fully Loaded Labor Rates ($/hr)
    rate_ops_l1 = 42.00
    rate_compliance_l2 = 65.00
    rate_support_agent = 32.00

    # 1. AS-IS Operating Costs
    # Ops Labor: 213,842 reviews * avg touch time (1.8h for L1, 3.5h for L2)
    l1_reviews_as_is = 184000
    l2_reviews_as_is = 29842
    cost_l1_ops_as_is = l1_reviews_as_is * 1.8 * rate_ops_l1
    cost_l2_comp_as_is = l2_reviews_as_is * 3.5 * rate_compliance_l2
    total_ops_labor_as_is = cost_l1_ops_as_is + cost_l2_comp_as_is

    # Support Tickets: 118,602 tickets
    cost_support_as_is = 1408658.00

    # Vendor & Screening API Costs: $9.80 per application
    cost_vendor_as_is = annual_volume * 9.80

    # Mailing & Manual Communications: $4.40 per rework application (173,429 apps)
    cost_rework_admin_as_is = 173429 * 4.40

    total_cost_as_is = total_ops_labor_as_is + cost_support_as_is + cost_vendor_as_is + cost_rework_admin_as_is
    unit_cost_as_is = total_cost_as_is / apps_approved_as_is

    print("--- 1. AS-IS BASELINE ANNUAL OPERATING COSTS ---")
    print(f"L1 Operations Labor:         ${cost_l1_ops_as_is:,.2f}")
    print(f"L2 Compliance Labor:         ${cost_l2_comp_as_is:,.2f}")
    print(f"Total Compliance/Ops Labor:  ${total_ops_labor_as_is:,.2f}")
    print(f"Customer Support Contacts:   ${cost_support_as_is:,.2f}")
    print(f"Legacy Vendor APIs:          ${cost_vendor_as_is:,.2f}")
    print(f"Manual Rework / Admin Cost:  ${cost_rework_admin_as_is:,.2f}")
    print(f"TOTAL AS-IS ANNUAL OPEX:     ${total_cost_as_is:,.2f}")
    print(f"Unit Cost per Approved App:  ${unit_cost_as_is:.2f}\n")

    # 2. TO-BE Projected Operating Costs (Base Case)
    # Straight-Through Processing: 60% of apps require 0 human reviews
    # Remaining 40%: 70% auto-remediated via AI, only 12% total volume hits L1/L2
    l1_reviews_to_be = int(annual_volume * 0.08) # 41,600 apps
    l2_reviews_to_be = int(annual_volume * 0.03) # 15,600 apps
    # Touch time reduced via Unified Workbench (L1: 0.8h, L2: 1.5h)
    cost_l1_ops_to_be = l1_reviews_to_be * 0.8 * rate_ops_l1
    cost_l2_comp_to_be = l2_reviews_to_be * 1.5 * rate_compliance_l2
    total_ops_labor_to_be = cost_l1_ops_to_be + cost_l2_comp_to_be

    # Support Tickets: 75% reduction via proactive status notifications
    cost_support_to_be = cost_support_as_is * 0.25

    # Modern Bundled RegTech API Cost: $4.20 per application
    cost_vendor_to_be = annual_volume * 4.20

    # Ongoing Cloud & AI SaaS OPEX: $420,000 / year
    cost_cloud_saas_to_be = 420000.00

    # Rework Admin Cost: Eliminated via digital self-service ($0)
    cost_rework_admin_to_be = 0.00

    total_cost_to_be = total_ops_labor_to_be + cost_support_to_be + cost_vendor_to_be + cost_cloud_saas_to_be
    unit_cost_to_be = total_cost_to_be / apps_approved_to_be
    annual_gross_benefit = total_cost_as_is - total_cost_to_be

    print("--- 2. TO-BE PROJECTED ANNUAL OPERATING COSTS (BASE CASE) ---")
    print(f"L1 Operations Labor:         ${cost_l1_ops_to_be:,.2f}")
    print(f"L2 Compliance Labor:         ${cost_l2_comp_to_be:,.2f}")
    print(f"Total Compliance/Ops Labor:  ${total_ops_labor_to_be:,.2f}")
    print(f"Customer Support Contacts:   ${cost_support_to_be:,.2f}")
    print(f"Modern RegTech APIs:         ${cost_vendor_to_be:,.2f}")
    print(f"Cloud Infrastructure & SaaS: ${cost_cloud_saas_to_be:,.2f}")
    print(f"TOTAL TO-BE ANNUAL OPEX:     ${total_cost_to_be:,.2f}")
    print(f"Unit Cost per Approved App:  ${unit_cost_to_be:.2f}")
    print(f"ANNUAL GROSS CASH SAVINGS:   ${annual_gross_benefit:,.2f}\n")

    # 3. Capital Investment & Cash Flow Analysis (3-Year Horizon)
    capex_initial = 2850000.00  # Engineering, integration, licensing
    discount_rate = 0.085       # 8.5% hurdle rate

    # Cash flows: Year 0 = -CAPEX, Year 1 = 80% realization, Year 2 = 100%, Year 3 = 100%
    cf_0 = -capex_initial
    cf_1 = annual_gross_benefit * 0.80
    cf_2 = annual_gross_benefit * 1.00
    cf_3 = annual_gross_benefit * 1.00

    cash_flows = [cf_0, cf_1, cf_2, cf_3]
    
    # Net Present Value (NPV)
    npv_3yr = np.npv(discount_rate, cash_flows) if hasattr(np, 'npv') else sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(cash_flows))
    
    # Internal Rate of Return (IRR)
    # Simple search for IRR where sum(cf / (1+r)^t) = 0
    rates = np.linspace(0.01, 2.0, 2000)
    npvs = [sum(cf / ((1 + r) ** t) for t, cf in enumerate(cash_flows)) for r in rates]
    irr = rates[np.argmin(np.abs(npvs))] * 100

    # Payback Period (Months)
    cumulative = 0
    payback_months = 0
    monthly_benefit_y1 = cf_1 / 12.0
    for m in range(1, 37):
        cumulative += monthly_benefit_y1 if m <= 12 else (cf_2 / 12.0)
        if cumulative >= capex_initial and payback_months == 0:
            payback_months = m

    print("--- 3. 3-YEAR INVESTMENT APPRAISAL & ROI ---")
    print(f"Initial Capital Investment (CAPEX): ${capex_initial:,.2f}")
    print(f"Hurdle Discount Rate:               {discount_rate*100:.1f}%")
    print(f"Year 1 Net Cash Inflow:            ${cf_1:,.2f}")
    print(f"Year 2 Net Cash Inflow:            ${cf_2:,.2f}")
    print(f"Year 3 Net Cash Inflow:            ${cf_3:,.2f}")
    print(f"3-Year Net Present Value (NPV):     ${npv_3yr:,.2f}")
    print(f"Internal Rate of Return (IRR):      {irr:.1f}%")
    print(f"Discounted Payback Period:          {payback_months} Months\n")

    # 4. Scenario & Sensitivity Analysis
    print("--- 4. SCENARIO ANALYSIS (CONSERVATIVE vs. BASE vs. AGGRESSIVE) ---")
    scenarios = {
        "Conservative (45% STP, $3.2M Capex)": {"stp": 0.45, "savings_mult": 0.75, "capex": 3200000.0},
        "Base Case (60% STP, $2.85M Capex)":   {"stp": 0.60, "savings_mult": 1.00, "capex": 2850000.0},
        "Aggressive (75% STP, $2.5M Capex)":   {"stp": 0.75, "savings_mult": 1.22, "capex": 2500000.0}
    }
    
    for name, params in scenarios.items():
        sc_benefit = annual_gross_benefit * params["savings_mult"]
        sc_cfs = [-params["capex"], sc_benefit * 0.80, sc_benefit, sc_benefit]
        sc_npv = sum(cf / ((1 + discount_rate) ** t) for t, cf in enumerate(sc_cfs))
        print(f"Scenario: {name}")
        print(f"  Annual Benefit: ${sc_benefit:,.2f} | 3-Yr NPV: ${sc_npv:,.2f}")

if __name__ == "__main__":
    run_financial_model()
