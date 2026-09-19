"""
ONBOARD360 — Exploratory Data Analysis & Root Cause Analysis Engine
Generates detailed statistical distributions, Little's Law queue metrics, and Pareto distributions.
"""

import pandas as pd
import numpy as np

def run_analysis():
    print("Loading generated dataset...")
    df = pd.read_parquet("06_Data_Analysis/data/applications.parquet")
    df_rev = pd.read_parquet("06_Data_Analysis/data/manual_reviews.parquet")
    df_tck = pd.read_parquet("06_Data_Analysis/data/support_tickets.parquet")

    total_apps = len(df)
    
    print("\n--- 1. OVERALL LIFECYCLE METRICS ---")
    tat_mean = df['total_cycle_time_hours'].mean()
    tat_median = df['total_cycle_time_hours'].median()
    tat_p90 = df['total_cycle_time_hours'].quantile(0.90)
    tat_p99 = df['total_cycle_time_hours'].quantile(0.99)
    
    touch_mean = df['touch_time_hours'].mean()
    wait_mean = df['wait_time_hours'].mean()
    pce = (touch_mean / tat_mean) * 100
    
    print(f"Total Applications: {total_apps:,}")
    print(f"TAT Mean: {tat_mean:.2f}h | Median: {tat_median:.2f}h | P90: {tat_p90:.2f}h | P99: {tat_p99:.2f}h")
    print(f"Touch Time Mean: {touch_mean:.2f}h ({(touch_mean/tat_mean*100):.1f}%)")
    print(f"Wait Time Mean:  {wait_mean:.2f}h ({(wait_mean/tat_mean*100):.1f}%)")
    print(f"Process Cycle Efficiency (PCE): {pce:.2f}%")

    print("\n--- 2. OUTCOMES & QUALITY METRICS ---")
    status_counts = df['status'].value_counts()
    print("Application Status Distribution:")
    for stat, count in status_counts.items():
        print(f"  {stat}: {count:,} ({count/total_apps*100:.2f}%)")

    fpy_count = len(df[(df['status'] == 'APPROVED') & (~df['rework_flag'])])
    fpy_rate = (fpy_count / total_apps) * 100
    print(f"First-Pass Yield (FPY): {fpy_rate:.2f}% ({fpy_count:,} apps)")
    print(f"Rework Rate: {df['rework_flag'].mean()*100:.2f}% ({df['rework_flag'].sum():,} apps)")
    print(f"Manual Review Rate: {df['manual_review_flag'].mean()*100:.2f}% ({df['manual_review_flag'].sum():,} apps)")
    print(f"SLA Breach Rate (>48h): {df['sla_breach_flag'].mean()*100:.2f}% ({df['sla_breach_flag'].sum():,} apps)")

    print("\n--- 3. PARETO REWORK DRIVERS ---")
    rework_df = df[df['rework_flag']]['rework_reason'].value_counts()
    rework_pct = (rework_df / rework_df.sum()) * 100
    cum_pct = rework_pct.cumsum()
    pareto_rework = pd.DataFrame({
        'Count': rework_df,
        'Percentage': rework_pct.round(2),
        'Cumulative_Pct': cum_pct.round(2)
    })
    print(pareto_rework)

    print("\n--- 4. CHANNEL FRICTION ANALYSIS ---")
    channel_grp = df.groupby('channel').agg(
        Total=('application_id', 'count'),
        Rework_Rate=('rework_flag', lambda x: x.mean()*100),
        Abandon_Rate=('status', lambda x: (x == 'ABANDONED').mean()*100),
        Avg_TAT=('total_cycle_time_hours', 'mean'),
        SLA_Breach_Rate=('sla_breach_flag', lambda x: x.mean()*100)
    ).round(2)
    print(channel_grp)

    print("\n--- 5. QUEUE BOTTLENECK & LITTLE'S LAW DYNAMICS ---")
    # Arrival rate lambda = 520,000 / (365 * 24) = 59.36 apps/hour
    arrival_rate_per_hr = total_apps / (365 * 24)
    avg_wip_total = arrival_rate_per_hr * tat_mean
    avg_wip_queue = arrival_rate_per_hr * wait_mean
    print(f"System Arrival Rate (lambda): {arrival_rate_per_hr:.2f} applications / hour")
    print(f"Average System Work-In-Progress (WIP = lambda * W): {avg_wip_total:,.0f} active applications")
    print(f"Average Idle Queue Work-In-Progress (WIP_queue): {avg_wip_queue:,.0f} applications queued in backlogs")

    print("\n--- 6. CUSTOMER SUPPORT IMPACT ---")
    total_tickets = len(df_tck)
    total_ticket_cost = df_tck['cost_to_serve_usd'].sum()
    print(f"Total Support Tickets: {total_tickets:,} (Rate: {(total_tickets/total_apps*100):.2f}%)")
    print(f"Total Direct Support Cost: ${total_ticket_cost:,.2f}")
    tck_reasons = df_tck['issue_category'].value_counts()
    print("Ticket Drivers:")
    for cat, cnt in tck_reasons.items():
        print(f"  {cat}: {cnt:,} ({cnt/total_tickets*100:.2f}%)")

if __name__ == "__main__":
    run_analysis()
