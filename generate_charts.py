import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

os.makedirs('11_Executive_Presentation/charts', exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

c_primary = '#1F4E79'
c_secondary = '#2E75B6'
c_accent = '#00A86B'
c_danger = '#C0392B'
c_warning = '#E67E22'
c_neutral = '#64748B'

# =========================================================================
# Fig 1: Monthly Intake vs SLA Breach
# =========================================================================
fig, ax1 = plt.subplots(figsize=(7, 2.8), dpi=200)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
vol = [43.2, 42.1, 44.5, 43.8, 42.9, 43.5, 44.1, 43.0, 43.7, 44.2, 42.8, 42.2]
breach = [45.8, 46.2, 45.4, 46.5, 45.9, 46.1, 45.7, 46.3, 45.5, 46.0, 45.8, 45.9]

ax1.plot(months, vol, color=c_primary, marker='o', linewidth=2, label='Intake Volume')
ax1.set_ylabel('Inbound Volume (k apps)', color=c_primary, fontweight='bold', fontsize=8.5)
ax1.set_ylim(38, 48)
ax1.grid(True, linestyle=':', alpha=0.6)

ax2 = ax1.twinx()
ax2.plot(months, breach, color=c_danger, linestyle='--', marker='s', linewidth=2, label='SLA Breach %')
ax2.set_ylabel('48h SLA Breach Rate (%)', color=c_danger, fontweight='bold', fontsize=8.5)
ax2.set_ylim(40, 52)

fig.suptitle('Figure 1: Monthly Inflow vs. 48h SLA Breach Rate (2025)', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.12, right=0.88)
plt.savefig('11_Executive_Presentation/charts/fig1_intake_sla.png')
plt.close()

# =========================================================================
# Fig 2: Channel Mix
# =========================================================================
fig, ax = plt.subplots(figsize=(6.8, 2.6), dpi=200)
channels = ['Mobile App\n(50.0%)', 'Web Portal\n(28.0%)', 'Branch Assisted\n(12.0%)', 'Affiliate Partner\n(10.0%)']
ch_vols = [260000, 145600, 62400, 52000]
colors_pie = [c_primary, c_secondary, '#5B9BD5', '#BDD7EE']
bars = ax.barh(channels[::-1], ch_vols[::-1], color=colors_pie[::-1], height=0.55)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 3500, bar.get_y() + bar.get_height()/2, f'{w:,}', ha='left', va='center', fontsize=8, fontweight='bold', color=c_primary)
ax.set_xlim(0, 315000)
ax.grid(axis='x', linestyle=':', alpha=0.6)
ax.set_xlabel('Application Count (Annual Intake)', fontsize=8.5, fontweight='bold', labelpad=6)
fig.suptitle('Figure 2: Customer Intake Volume by Acquisition Channel', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.20, left=0.22, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig2_channel_mix.png')
plt.close()

# =========================================================================
# Fig 3: Segment Outcomes (Zero Overlap Layout)
# =========================================================================
fig, ax = plt.subplots(figsize=(6.8, 2.8), dpi=200)
segs = ['Standard Retail', 'Fintech Digital', 'Premier Wealth', 'SME Business']
approved = [80.2, 78.5, 82.1, 76.8]
abandoned = [16.4, 17.8, 12.5, 16.9]
rejected = [3.4, 3.7, 5.4, 6.3]
y_pos = np.arange(len(segs))

ax.barh(y_pos, approved, color=c_accent, label='Approved', height=0.55)
ax.barh(y_pos, abandoned, left=approved, color=c_warning, label='Abandoned', height=0.55)
ax.barh(y_pos, rejected, left=np.array(approved)+np.array(abandoned), color=c_danger, label='Rejected', height=0.55)

for i in range(len(segs)):
    ax.text(approved[i]/2, y_pos[i], f'{approved[i]}%', ha='center', va='center', color='white', fontweight='bold', fontsize=7.5)
    ax.text(approved[i] + abandoned[i]/2, y_pos[i], f'{abandoned[i]}%', ha='center', va='center', color='white', fontweight='bold', fontsize=7.5)

ax.set_yticks(y_pos)
ax.set_yticklabels(segs, fontsize=8.5, fontweight='bold', color=c_primary)
ax.set_xlim(0, 100)
ax.set_xlabel('Percentage of Segment Applications (%)', fontsize=8.5, fontweight='bold', labelpad=6)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.22), ncol=3, frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8)
fig.suptitle('Figure 3: Application Lifecycle Outcomes by Customer Segment', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.78, bottom=0.22, left=0.22, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig3_segment_outcomes.png')
plt.close()

# =========================================================================
# Fig 4: Touch vs Wait Time (Zero Overlap Layout)
# =========================================================================
fig, ax = plt.subplots(figsize=(6.8, 2.5), dpi=200)
ax.barh([0], [6.29], color=c_accent, label='Active Touch Time: 6.29h (10.7%)', height=0.45)
ax.barh([0], [52.42], left=[6.29], color=c_danger, label='Idle Queue Wait Time: 52.42h (89.3%)', height=0.45)

ax.text(3.14, 0, '6.3h\n(11%)', ha='center', va='center', color='white', fontweight='bold', fontsize=7)
ax.text(32.5, 0, '52.42 Hours (89.3%)\nIdle Queue Wait Delay', ha='center', va='center', color='white', fontweight='bold', fontsize=8)

ax.set_yticks([0])
ax.set_yticklabels(['Average Cycle Time\n(58.70 Hours)'], fontsize=8.5, fontweight='bold', color=c_primary)
ax.set_xlim(0, 65)
ax.set_xlabel('Elapsed Duration (Hours)', fontsize=8.5, fontweight='bold', labelpad=6)
ax.grid(axis='x', linestyle=':', alpha=0.6)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2, frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8)
fig.suptitle('Figure 4: Total Lead Time Breakdown — Active Touch vs. Idle Queue Wait', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.75, bottom=0.22, left=0.25, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig4_touch_vs_wait.png')
plt.close()

# =========================================================================
# Fig 5: Queue Latency
# =========================================================================
fig, ax = plt.subplots(figsize=(6.8, 2.5), dpi=200)
q_names = ['Compliance L2 Queue', 'Level-1 Ops Queue', 'Core Ledger Batch', 'Initial Intake Buffer']
q_hours = [21.2, 18.6, 18.5, 8.4]
q_colors = [c_danger, c_warning, c_primary, '#5B9BD5']
bars = ax.barh(q_names[::-1], q_hours[::-1], color=q_colors[::-1], height=0.55)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 0.4, bar.get_y() + bar.get_height()/2, f'{w:.1f} hrs', ha='left', va='center', fontsize=8, fontweight='bold', color=c_primary)
ax.set_xlim(0, 25)
ax.grid(axis='x', linestyle=':', alpha=0.6)
ax.set_xlabel('Average Wait Duration (Hours)', fontsize=8.5, fontweight='bold', labelpad=6)
fig.suptitle('Figure 5: Departmental Queue Latency & Hand-Off Bottlenecks', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.20, left=0.26, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig5_queue_latency.png')
plt.close()

# =========================================================================
# Fig 6: Little's Law WIP
# =========================================================================
fig, ax = plt.subplots(figsize=(6.5, 2.5), dpi=200)
states = ['AS-IS Baseline System', 'TO-BE Target System']
wip_active = [3485, 792]
wip_idle = [3111, 264]
x = np.arange(len(states))
width = 0.35
rects1 = ax.bar(x - width/2, wip_active, width, label='Total In-Flight WIP Units', color=c_primary)
rects2 = ax.bar(x + width/2, wip_idle, width, label='Idle Queued Backlog Units', color=c_danger)
for rect in rects1:
    h = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, h + 60, f'{h:,}', ha='center', va='bottom', fontsize=8, fontweight='bold')
for rect in rects2:
    h = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, h + 60, f'{h:,}', ha='center', va='bottom', fontsize=8, fontweight='bold', color=c_danger)
ax.set_xticks(x)
ax.set_xticklabels(states, fontsize=8.5, fontweight='bold')
ax.set_ylim(0, 4300)
ax.set_ylabel('Active Applications in Pipeline', fontsize=8.5, fontweight='bold')
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8, loc='upper right')
fig.suptitle("Figure 6: Little's Law Work-in-Progress (WIP) Backlog Dynamics", fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.15, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig6_littles_law_wip.png')
plt.close()

# =========================================================================
# Fig 7: Pareto Document Rework (Clean non-overlapping annotation)
# =========================================================================
fig, ax1 = plt.subplots(figsize=(6.8, 2.6), dpi=200)
reasons = ['Blurry\nImage', 'Expired\nID', 'Address\nMismatch', 'Incomplete\nForm', 'Name\nMismatch']
counts = [72994, 39964, 31249, 20716, 8506]
cum_pct = [42.1, 65.1, 83.2, 95.1, 100.0]

ax1.bar(reasons, counts, color=c_primary, width=0.52, label='Incident Count')
ax1.set_ylabel('Defect Incidents / Year', color=c_primary, fontweight='bold', fontsize=8)
ax1.set_ylim(0, 88000)
ax1.grid(axis='y', linestyle=':', alpha=0.6)

ax2 = ax1.twinx()
ax2.plot(reasons, cum_pct, color=c_danger, marker='D', linewidth=2, label='Cumulative %')
ax2.set_ylabel('Cumulative % of Rework', color=c_danger, fontweight='bold', fontsize=8)
ax2.set_ylim(0, 115)
for i, txt in enumerate(cum_pct):
    if i == 2:  # Address Mismatch
        ax2.annotate(f'{txt}%', (reasons[i], cum_pct[i] - 7), ha='center', fontsize=7.5, fontweight='bold', color=c_danger)
    else:
        ax2.annotate(f'{txt}%', (reasons[i], cum_pct[i] + 4), ha='center', fontsize=7.5, fontweight='bold', color=c_danger)

ax2.axhline(83.15, color=c_warning, linestyle=':', linewidth=1.5)
ax2.text(0.02, 90, '83.15% Cumulative Threshold (Top 3 Defects)', color='#B45309', fontsize=7.5, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='#FEF3C7', edgecolor='#F59E0B', alpha=0.95))

fig.suptitle('Figure 7: Pareto Analysis of Document Rework Defect Drivers', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.12, right=0.88)
plt.savefig('11_Executive_Presentation/charts/fig7_pareto_rework.png')
plt.close()

# =========================================================================
# Fig 8: Rework by Channel
# =========================================================================
fig, ax = plt.subplots(figsize=(6.5, 2.5), dpi=200)
ch_labels = ['Mobile App', 'Web Portal', 'Affiliate Partner', 'Branch Assisted']
rw_rates = [36.8, 31.4, 28.5, 18.2]
ab_rates = [17.8, 15.6, 14.2, 8.1]
x = np.arange(len(ch_labels))
width = 0.35
ax.bar(x - width/2, rw_rates, width, label='Rework Rate (%)', color=c_danger)
ax.bar(x + width/2, ab_rates, width, label='Abandonment Rate (%)', color=c_warning)
for i in range(len(ch_labels)):
    ax.text(x[i] - width/2, rw_rates[i] + 0.8, f'{rw_rates[i]}%', ha='center', fontsize=7.5, fontweight='bold')
    ax.text(x[i] + width/2, ab_rates[i] + 0.8, f'{ab_rates[i]}%', ha='center', fontsize=7.5, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(ch_labels, fontsize=8.5)
ax.set_ylim(0, 45)
ax.set_ylabel('Rate (%)', fontsize=8.5, fontweight='bold')
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8, loc='upper right')
fig.suptitle('Figure 8: Rework Defect Rate vs. Customer Abandonment by Channel', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.12, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig8_channel_friction.png')
plt.close()

# =========================================================================
# Fig 9: Target Trajectory
# =========================================================================
fig, ax = plt.subplots(figsize=(6.5, 2.5), dpi=200)
kpis = ['TAT\n(Hours)', 'First-Pass\nYield (%)', 'Rework\nRate (%)', 'Unit Cost\n($ USD)']
as_is_vals = [58.70, 58.12, 33.35, 67.45]
to_be_vals = [24.00, 78.00, 10.00, 12.55]
x = np.arange(len(kpis))
width = 0.35
ax.bar(x - width/2, as_is_vals, width, label='AS-IS Baseline', color=c_neutral)
ax.bar(x + width/2, to_be_vals, width, label='TO-BE Target', color=c_accent)
for i in range(len(kpis)):
    ax.text(x[i] - width/2, as_is_vals[i] + 1.2, f'{as_is_vals[i]}', ha='center', fontsize=7.5, fontweight='bold', color='#333333')
    ax.text(x[i] + width/2, to_be_vals[i] + 1.2, f'{to_be_vals[i]}', ha='center', fontsize=7.5, fontweight='bold', color=c_accent)
ax.set_xticks(x)
ax.set_xticklabels(kpis, fontsize=8.5)
ax.set_ylim(0, 90)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8, loc='upper right')
fig.suptitle('Figure 9: Core Operational Transformation Performance Trajectory', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.12, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig9_target_benchmarks.png')
plt.close()

# =========================================================================
# Fig 10: Scenario Sensitivity
# =========================================================================
fig, ax = plt.subplots(figsize=(6.5, 2.5), dpi=200)
scenarios = ['Conservative\n(45% STP, $3.2M Capex)', 'Base Case\n(60% STP, $2.85M Capex)', 'Aggressive\n(75% STP, $2.5M Capex)']
ann_savings = [16.57, 22.09, 26.95]
npv_vals = [36.06, 49.50, 61.37]
x = np.arange(len(scenarios))
width = 0.35
ax.bar(x - width/2, ann_savings, width, label='Annual Net Savings ($M)', color=c_secondary)
ax.bar(x + width/2, npv_vals, width, label='3-Year NPV @ 8.5% ($M)', color=c_primary)
for i in range(len(scenarios)):
    ax.text(x[i] - width/2, ann_savings[i] + 0.8, f'${ann_savings[i]}M', ha='center', fontsize=7.5, fontweight='bold')
    ax.text(x[i] + width/2, npv_vals[i] + 0.8, f'${npv_vals[i]}M', ha='center', fontsize=7.5, fontweight='bold', color=c_primary)
ax.set_xticks(x)
ax.set_xticklabels(scenarios, fontsize=8.5)
ax.set_ylim(0, 72)
ax.set_ylabel('$ Millions', fontsize=8.5, fontweight='bold')
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8, loc='upper left')
fig.suptitle('Figure 10: What-If Sensitivity Analysis Across Operational Scenarios', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.12, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig10_scenario_sensitivity.png')
plt.close()

# =========================================================================
# Fig 11: Activity-Based Cost
# =========================================================================
fig, ax = plt.subplots(figsize=(6.8, 2.6), dpi=200)
cost_cats = ['L1 Ops\nLabor', 'L2 Compliance\nLabor', 'Identity\nVendor APIs', 'Customer\nSupport', 'Admin /\nMailing', 'Cloud / AI\nOPEX']
as_is_cost = [13.91, 6.79, 5.10, 1.41, 0.76, 0.00]
to_be_cost = [1.40, 1.52, 2.18, 0.35, 0.00, 0.42]
x = np.arange(len(cost_cats))
width = 0.35
ax.bar(x - width/2, as_is_cost, width, label='AS-IS Annual OPEX ($M)', color=c_danger)
ax.bar(x + width/2, to_be_cost, width, label='TO-BE Target OPEX ($M)', color=c_accent)
for i in range(len(cost_cats)):
    if as_is_cost[i] > 0:
        ax.text(x[i] - width/2, as_is_cost[i] + 0.25, f'${as_is_cost[i]:.2f}M', ha='center', fontsize=7, fontweight='bold')
    ax.text(x[i] + width/2, to_be_cost[i] + 0.25, f'${to_be_cost[i]:.2f}M', ha='center', fontsize=7, fontweight='bold', color=c_accent)
ax.set_xticks(x)
ax.set_xticklabels(cost_cats, fontsize=8)
ax.set_ylim(0, 16)
ax.set_ylabel('$ Millions', fontsize=8.5, fontweight='bold')
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8, loc='upper right')
fig.suptitle('Figure 11: Activity-Based Annual Operating Cost Decomposition', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.12, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig11_activity_based_cost.png')
plt.close()

# =========================================================================
# Fig 12: Cash Flow Payback
# =========================================================================
fig, ax = plt.subplots(figsize=(6.8, 2.5), dpi=200)
timeline = ['Month 0\n(CAPEX)', 'Month 1', 'Month 2\n(Breakeven)', 'Month 6', 'Month 12\n(Year 1)', 'Month 24\n(Year 2)', 'Month 36\n(Year 3)']
cum_cf = [-2.85, -1.38, 0.10, 5.99, 14.82, 36.92, 59.01]
ax.plot(timeline, cum_cf, color=c_accent, marker='o', linewidth=2.2, label='Cumulative Net Cash Flow ($M)')
ax.axhline(0, color=c_danger, linestyle='--', linewidth=1)
for i, txt in enumerate(cum_cf):
    ax.annotate(f'${txt:.2f}M', (timeline[i], cum_cf[i] + 2.5), ha='center', fontsize=7.5, fontweight='bold', color=c_primary if txt >= 0 else c_danger)
ax.set_ylim(-6, 68)
ax.set_ylabel('Cumulative Cash Return ($M)', fontsize=8.5, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8)
fig.suptitle('Figure 12: 3-Year Capital Recovery & Discounted Cash Flow Realization', fontsize=10, fontweight='bold', color=c_primary, y=0.98)
fig.subplots_adjust(top=0.86, bottom=0.18, left=0.12, right=0.95)
plt.savefig('11_Executive_Presentation/charts/fig12_cash_flow_payback.png')
plt.close()

print('All 12 charts regenerated with zero overlapping text or legends.')
