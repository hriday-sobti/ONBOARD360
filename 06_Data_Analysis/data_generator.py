"""
ONBOARD360 — High-Performance Synthetic Dataset Generator
Author: Lead Business Analyst & Data Architect
Generates 520,000+ realistic customer onboarding applications with relational integrity.
"""

import os
import sys
import time
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_onboard360_data(n_records: int = 520000, seed: int = 42, output_dir: str = "06_Data_Analysis/data"):
    print(f"[{datetime.now()}] Starting generation of {n_records:,} onboarding applications...")
    start_time = time.time()
    os.makedirs(output_dir, exist_ok=True)
    np.random.seed(seed)

    # 1. Base Dimensions
    customer_types = ["Standard_Retail", "Premier_Wealth", "SME_Business", "Fintech_Digital"]
    p_customer_types = [0.55, 0.12, 0.18, 0.15]

    channels = ["Mobile_App", "Web_Portal", "Branch_Assisted", "Affiliate_Partner"]
    p_channels = [0.50, 0.28, 0.12, 0.10]

    regions = ["UK_EU", "US", "APAC", "LATAM"]
    p_regions = [0.45, 0.30, 0.15, 0.10]

    product_types = ["Checking_Standard", "Premier_Checking", "Savings_HighYield", "SME_Operating_Account"]
    p_product = [0.50, 0.15, 0.20, 0.15]

    # Generate Arrays
    print(f"[{datetime.now()}] Generating core application attributes...")
    app_ids = [f"APP-{1000000 + i}" for i in range(n_records)]
    cust_ids = [f"CUST-{2000000 + i}" for i in range(n_records)]
    
    assigned_cust_type = np.random.choice(customer_types, size=n_records, p=p_customer_types)
    assigned_channel = np.random.choice(channels, size=n_records, p=p_channels)
    assigned_region = np.random.choice(regions, size=n_records, p=p_regions)
    assigned_product = np.random.choice(product_types, size=n_records, p=p_product)

    # Application Dates across 2025 (365 days)
    base_date = datetime(2025, 1, 1)
    random_seconds = np.random.randint(0, 365 * 86400, size=n_records)
    app_dates = [base_date + timedelta(seconds=int(s)) for s in random_seconds]

    # Risk Tier Assignment (Conditional on customer type and region)
    print(f"[{datetime.now()}] Modeling risk tiers and AML screening...")
    risk_tiers = []
    for ct, reg in zip(assigned_cust_type, assigned_region):
        if ct == "SME_Business":
            p = [0.60, 0.25, 0.12, 0.03]  # Low, Med, High, PEP
        elif ct == "Premier_Wealth":
            p = [0.70, 0.20, 0.08, 0.02]
        elif reg == "LATAM":
            p = [0.65, 0.22, 0.11, 0.02]
        else:
            p = [0.82, 0.13, 0.04, 0.01]
        risk_tiers.append(np.random.choice(["LOW", "MEDIUM", "HIGH", "PEP"], p=p))
    risk_tiers = np.array(risk_tiers)

    # Document Image Quality & Rework modeling
    print(f"[{datetime.now()}] Modeling document quality and rework drivers...")
    # Mobile app has slightly higher glare/blur, Branch has lowest
    blur_probs = np.where(assigned_channel == "Mobile_App", 0.38,
                 np.where(assigned_channel == "Web_Portal", 0.32,
                 np.where(assigned_channel == "Affiliate_Partner", 0.40, 0.12)))
    
    is_rework = np.random.random(size=n_records) < blur_probs
    
    rework_reasons = []
    rework_choices = ["Blurry_Image", "Expired_ID", "Address_Proof_Mismatch", "Incomplete_Form", "Name_Mismatch"]
    rework_p = [0.42, 0.23, 0.18, 0.12, 0.05]
    
    for rew in is_rework:
        if rew:
            rework_reasons.append(np.random.choice(rework_choices, p=rework_p))
        else:
            rework_reasons.append("None")
    rework_reasons = np.array(rework_reasons)

    # Manual Review Flag (Driven by Rework, Risk Tier, or Channel)
    print(f"[{datetime.now()}] Modeling manual compliance review routing...")
    manual_review_prob = np.where(risk_tiers == "PEP", 0.98,
                         np.where(risk_tiers == "HIGH", 0.92,
                         np.where(risk_tiers == "MEDIUM", 0.65,
                         np.where(is_rework, 0.55, 0.18))))
    manual_review_flag = np.random.random(size=n_records) < manual_review_prob

    review_teams = []
    for mr, rt, rew in zip(manual_review_flag, risk_tiers, is_rework):
        if not mr:
            review_teams.append("None")
        elif rt in ["HIGH", "PEP"]:
            review_teams.append("L2_Compliance")
        elif rew:
            review_teams.append("L1_Ops")
        else:
            review_teams.append("L1_Ops" if np.random.random() < 0.7 else "L2_Compliance")
    review_teams = np.array(review_teams)

    # Outcomes: APPROVED, REJECTED, ABANDONED
    print(f"[{datetime.now()}] Calculating application lifecycle outcomes...")
    # Abandonment is heavily correlated with Rework and long queue times
    abandon_prob = np.where(is_rework & (assigned_channel == "Mobile_App"), 0.35,
                   np.where(is_rework, 0.28,
                   np.where(risk_tiers == "HIGH", 0.15, 0.08)))
    is_abandoned = np.random.random(size=n_records) < abandon_prob

    # Rejections driven by confirmed sanctions/PEP or severe fraud
    reject_prob = np.where(risk_tiers == "PEP", 0.32,
                  np.where(risk_tiers == "HIGH", 0.25, 0.03))
    is_rejected = (~is_abandoned) & (np.random.random(size=n_records) < reject_prob)

    status = np.where(is_abandoned, "ABANDONED",
             np.where(is_rejected, "REJECTED", "APPROVED"))

    # Cycle Times: Touch Time vs Wait Time (Hours)
    print(f"[{datetime.now()}] Modeling cycle times, queues and touch durations...")
    # Touch time: lognormal centered around 2-15 hours
    base_touch = np.where(manual_review_flag, 
                          np.random.lognormal(mean=2.4, sigma=0.4, size=n_records), # ~11-15 hrs
                          np.random.lognormal(mean=0.8, sigma=0.3, size=n_records)) # ~2.2 hrs
    touch_time_hours = np.round(np.clip(base_touch, 0.5, 36.0), 2)

    # Wait time: Massive queue delays if manual review or rework
    base_wait = np.where(is_rework & manual_review_flag,
                         np.random.lognormal(mean=4.8, sigma=0.4, size=n_records), # ~120-160 hrs
                np.where(manual_review_flag,
                         np.random.lognormal(mean=4.2, sigma=0.4, size=n_records), # ~65-90 hrs
                np.where(is_rework,
                         np.random.lognormal(mean=3.8, sigma=0.3, size=n_records), # ~45 hrs
                         np.random.lognormal(mean=2.2, sigma=0.5, size=n_records)))) # ~9-12 hrs
    wait_time_hours = np.round(np.clip(base_wait, 1.0, 320.0), 2)
    
    total_cycle_time_hours = np.round(touch_time_hours + wait_time_hours, 2)
    sla_breach_flag = total_cycle_time_hours > 48.0

    # Support Tickets
    # Ticket probability surges when wait time > 48h or rework
    ticket_prob = np.where(sla_breach_flag & is_rework, 0.48,
                  np.where(sla_breach_flag, 0.32,
                  np.where(is_rework, 0.22, 0.05)))
    has_support_ticket = np.random.random(size=n_records) < ticket_prob

    # Assembly of Applications DataFrame
    print(f"[{datetime.now()}] Assembling applications dataframe...")
    df_apps = pd.DataFrame({
        "application_id": app_ids,
        "customer_id": cust_ids,
        "application_date": app_dates,
        "customer_type": assigned_cust_type,
        "country": np.where(assigned_region == "UK_EU", np.random.choice(["GBR", "DEU", "FRA"], size=n_records),
                   np.where(assigned_region == "US", "USA",
                   np.where(assigned_region == "APAC", np.random.choice(["SGP", "AUS"], size=n_records),
                   np.random.choice(["BRA", "MEX"], size=n_records)))),
        "region": assigned_region,
        "product_type": assigned_product,
        "channel": assigned_channel,
        "risk_tier": risk_tiers,
        "rework_flag": is_rework,
        "rework_reason": rework_reasons,
        "manual_review_flag": manual_review_flag,
        "review_team": review_teams,
        "status": status,
        "touch_time_hours": touch_time_hours,
        "wait_time_hours": wait_time_hours,
        "total_cycle_time_hours": total_cycle_time_hours,
        "sla_breach_flag": sla_breach_flag,
        "has_support_ticket": has_support_ticket
    })

    # Save to Parquet & CSV Sample
    parquet_path = os.path.join(output_dir, "applications.parquet")
    sample_csv_path = os.path.join(output_dir, "applications_sample_10000.csv")
    print(f"[{datetime.now()}] Writing {parquet_path}...")
    df_apps.to_parquet(parquet_path, index=False)
    print(f"[{datetime.now()}] Writing sample {sample_csv_path}...")
    df_apps.head(10000).to_csv(sample_csv_path, index=False)

    # 2. Child Table: Manual Reviews (~243k records)
    print(f"[{datetime.now()}] Generating child table: manual_reviews...")
    df_reviews = df_apps[df_apps["manual_review_flag"]].copy()
    n_reviews = len(df_reviews)
    review_ids = [f"REV-{3000000 + i}" for i in range(n_reviews)]
    analyst_ids = [f"ANL-{np.random.randint(101, 250)}" for _ in range(n_reviews)]
    review_durations = np.round(df_reviews["touch_time_hours"].values * 60, 1) # minutes
    
    df_rev_table = pd.DataFrame({
        "review_id": review_ids,
        "application_id": df_reviews["application_id"].values,
        "queue_name": np.where(df_reviews["review_team"] == "L2_Compliance", "L2_AML_Sanctions", "L1_Document_Exception"),
        "analyst_id": analyst_ids,
        "duration_minutes": review_durations,
        "decision": np.where(df_reviews["status"] == "APPROVED", "APPROVE",
                    np.where(df_reviews["status"] == "REJECTED", "REJECT", "REQUEST_REWORK"))
    })
    rev_parquet_path = os.path.join(output_dir, "manual_reviews.parquet")
    df_rev_table.to_parquet(rev_parquet_path, index=False)

    # 3. Child Table: Support Tickets (~110k records)
    print(f"[{datetime.now()}] Generating child table: support_tickets...")
    df_tickets = df_apps[df_apps["has_support_ticket"]].copy()
    n_tickets = len(df_tickets)
    ticket_ids = [f"TCK-{4000000 + i}" for i in range(n_tickets)]
    ticket_channels = np.random.choice(["In_App_Chat", "Phone_IVR", "Email_Helpdesk"], size=n_tickets, p=[0.55, 0.30, 0.15])
    ticket_categories = np.where(df_tickets["sla_breach_flag"], "Status_Inquiry_WhereIsMyAccount",
                        np.where(df_tickets["rework_flag"], "Document_Upload_Failure", "General_Clarification"))
    cost_to_serve = np.where(ticket_channels == "In_App_Chat", 8.50,
                    np.where(ticket_channels == "Phone_IVR", 18.00, 12.00))

    df_tck_table = pd.DataFrame({
        "ticket_id": ticket_ids,
        "application_id": df_tickets["application_id"].values,
        "channel": ticket_channels,
        "issue_category": ticket_categories,
        "resolution_time_mins": np.random.randint(5, 45, size=n_tickets),
        "cost_to_serve_usd": cost_to_serve
    })
    tck_parquet_path = os.path.join(output_dir, "support_tickets.parquet")
    df_tck_table.to_parquet(tck_parquet_path, index=False)

    elapsed = time.time() - start_time
    print(f"[{datetime.now()}] Data generation completed successfully in {elapsed:.2f} seconds.")
    print(f"Summary Statistics:")
    print(f"Total Applications: {len(df_apps):,}")
    print(f"Average Turnaround Time: {df_apps['total_cycle_time_hours'].mean():.2f} hours")
    print(f"Average Touch Time: {df_apps['touch_time_hours'].mean():.2f} hours")
    print(f"Average Wait Time: {df_apps['wait_time_hours'].mean():.2f} hours")
    print(f"First-Pass Yield (Approved without rework): {(len(df_apps[(df_apps['status']=='APPROVED') & (~df_apps['rework_flag'])]) / len(df_apps) * 100):.2f}%")
    print(f"Rework Rate: {(df_apps['rework_flag'].mean() * 100):.2f}%")
    print(f"Manual Review Rate: {(df_apps['manual_review_flag'].mean() * 100):.2f}%")
    print(f"Abandonment Rate: {((df_apps['status'] == 'ABANDONED').mean() * 100):.2f}%")
    print(f"SLA Breach Rate (>48h): {(df_apps['sla_breach_flag'].mean() * 100):.2f}%")
    print(f"Support Tickets Created: {len(df_tck_table):,}")

if __name__ == "__main__":
    generate_onboard360_data(n_records=520000)
