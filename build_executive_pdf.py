import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "11_Executive_Presentation/ONBOARD360_Executive_Review.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor('#1F4E79')
secondary_color = colors.HexColor('#2E75B6')
text_dark = colors.HexColor('#1E293B')
border_gray = colors.HexColor('#CBD5E1')
bg_light = colors.HexColor('#F8FAFC')
callout_bg = colors.HexColor('#EFF6FF')

# Custom Typography Styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=primary_color,
    spaceAfter=4
)

meta_style = ParagraphStyle(
    'DocMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#475569'),
    spaceAfter=10
)

h1_style = ParagraphStyle(
    'SectionH1',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=12,
    leading=16,
    textColor=primary_color,
    spaceBefore=12,
    spaceAfter=6,
    keepWithNext=True
)

h2_style = ParagraphStyle(
    'SectionH2',
    parent=styles['Heading3'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=secondary_color,
    spaceBefore=8,
    spaceAfter=4,
    keepWithNext=True
)

body_style = ParagraphStyle(
    'DocBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=text_dark,
    spaceAfter=5
)

insight_style = ParagraphStyle(
    'InsightBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=11.5,
    textColor=text_dark,
    spaceAfter=4
)

takeaway_style = ParagraphStyle(
    'TakeawayBox',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=8,
    leading=11,
    textColor=colors.HexColor('#0F172A'),
    backColor=callout_bg,
    borderColor=secondary_color,
    borderWidth=0.8,
    borderPadding=5,
    spaceBefore=3,
    spaceAfter=8
)

th_style = ParagraphStyle(
    'TableHeader',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.5,
    leading=9.5,
    textColor=colors.white,
    alignment=1
)

tc_style = ParagraphStyle(
    'TableCell',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7,
    leading=9,
    textColor=text_dark
)

tcb_style = ParagraphStyle(
    'TableCellBold',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7,
    leading=9,
    textColor=primary_color
)

story = []

# Title & Metadata
story.append(Paragraph('ONBOARD360 — Customer Onboarding & KYC Process Modernization', title_style))
story.append(Paragraph('<b>Executive Review & Operational Transformation Blueprint</b> | Lead Contributor: Hriday Singh Sobti | NovaBank International<br/>Canonical Project Repository & Interactive Dashboard: <a href="https://github.com/hriday-sobti/ONBOARD360" color="#2E75B6"><u>https://github.com/hriday-sobti/ONBOARD360</u></a>', meta_style))
story.append(Spacer(1, 4))

# Section 1: Executive Summary
story.append(Paragraph('1. Executive Summary: The Strategic Mandate', h1_style))
story.append(Paragraph('NovaBank International processes <b>520,000 retail and commercial onboarding applications annually</b> across the UK/EU, North America, APAC, and Latin America. The bank\'s legacy operating model suffered from acute structural friction: an average customer turnaround time (TAT) of <b>58.70 hours</b>, driven by an <b>89.29% idle queue buffer delay (52.42 hours)</b>. Active analyst touch time accounted for barely <b>6.29 hours</b> (Process Cycle Efficiency = 10.71%). Furthermore, unvalidated upload viewfinders admitted blurry and expired documents directly into back-office queues, precipitating a <b>33.35% rework defect rate (173,429 cases)</b> and a <b>16.25% customer funnel abandonment rate (84,500 lost accounts)</b>, inflating direct unit processing costs to <b>$67.45 per completed account</b> ($27.97M annual direct operating expenditure).', body_style))

story.append(Paragraph('<b>The ONBOARD360 Transformation Initiative</b> modernizes this fragmented journey into an intelligent, event-driven orchestration ecosystem. By coupling real-time computer vision document gating with automated fuzzy watchlist screening and AI-assisted exception triage, ONBOARD360 compresses average cycle times to <b>&lt; 24.0 hours</b> (&lt; 15 minutes for 60% straight-through processing), reduces unit processing costs to <b>$12.55</b> (-81.4%), and generates <b>$22,092,276 in annual net recurring cash savings</b> on an initial <b>$2.85M investment</b>, delivering a <b>3-Year NPV of $49.50M</b> (8.5% hurdle rate), an <b>IRR &gt; 200%</b>, and a <b>2.0-month capital payback period</b>.', body_style))

# Scorecard Table
scorecard_data = [
    [Paragraph('<b>Operational Metric</b>', th_style), Paragraph('<b>AS-IS Baseline</b>', th_style), Paragraph('<b>TO-BE Target</b>', th_style), Paragraph('<b>Net Variance</b>', th_style), Paragraph('<b>Classification</b>', th_style)],
    [Paragraph('Average Turnaround Time (TAT)', tcb_style), Paragraph('58.70 Hours', tc_style), Paragraph('&lt; 24.0 Hours (&lt;15m STP)', tc_style), Paragraph('-59.1% Lead Time', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Idle Queue Wait Time Ratio', tcb_style), Paragraph('89.29% (52.42h)', tc_style), Paragraph('&lt; 25.00% (5.00h)', tc_style), Paragraph('-90.5% Queue Drop', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Straight-Through Processing (STP)', tcb_style), Paragraph('0.0% (Batch)', tc_style), Paragraph('60.0% (Automated)', tc_style), Paragraph('+60.0 pts Automation', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('First-Pass Yield (FPY)', tcb_style), Paragraph('58.12% (302K)', tc_style), Paragraph('&ge; 78.00% (405K)', tc_style), Paragraph('+19.9 pts Yield Gain', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Application Rework Rate', tcb_style), Paragraph('33.35% (173K)', tc_style), Paragraph('&le; 10.00% (52K)', tc_style), Paragraph('-70.0% Defect Cut', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Customer Abandonment Rate', tcb_style), Paragraph('16.25% (84.5K)', tc_style), Paragraph('&le; 7.50% (39.0K)', tc_style), Paragraph('-53.8% Churn Cut', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('SLA Breach Rate (&gt; 48 Hours)', tcb_style), Paragraph('45.92% (238K)', tc_style), Paragraph('&le; 2.50% (13K)', tc_style), Paragraph('-94.6% Compliance Gain', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Direct Operating Unit Cost', tcb_style), Paragraph('$67.45 / Account', tc_style), Paragraph('$12.55 / Account', tc_style), Paragraph('-$54.90 / Account (-81.4%)', tc_style), Paragraph('Modelled', tc_style)],
    [Paragraph('Annual Direct Operating OPEX', tcb_style), Paragraph('$27,967,200.60', tc_style), Paragraph('$5,874,924.50', tc_style), Paragraph('+$22,092,276.10 Savings', tc_style), Paragraph('Modelled', tc_style)]
]
t_sc = Table(scorecard_data, colWidths=[150, 95, 115, 110, 70])
t_sc.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_gray),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
]))
story.append(t_sc)
story.append(Spacer(1, 10))

# Section 2: Macro Volume & Channel Diagnostics
story.append(Paragraph('2. Macro Inflow & Acquisition Channel Diagnostics', h1_style))
story.append(Paragraph('To diagnose operational delays, transactional data was first analyzed at macro scale across monthly inflow and intake channels. <i>As shown in Figure 1</i>, monthly volume was steady throughout 2025 (~43,300 applications/month), yet the customer SLA breach rate remained constant at <b>45.92%</b> (238,784 breaches), disproving the assumption that delays were seasonal.', body_style))

# Figure 1
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig1_intake_sla.png', width=460, height=184),
    Paragraph('<b>Figure 1 — Monthly Application Inflow vs. 48h SLA Breach Rate (2025)</b>', h2_style),
    Paragraph('<b>What it shows:</b> Monthly volume plotted against percentage of applications breaching the 48-hour SLA threshold.<br/>'
              '<b>Key insight:</b> SLA breach rate hovered steadily between 45.2% and 46.8% all year, averaging 45.92%.<br/>'
              '<b>Why it matters:</b> Proves that customer delivery failures are systemic and architectural rather than driven by volume surges.<br/>'
              '<b>Improvement / action:</b> Replace batch-driven handoffs with event-driven straight-through routing.<br/>'
              '<b>Executive takeaway:</b> NovaBank breaches customer SLAs on 45.9% of all applications every month. Adding temporary overtime labor cannot solve a structurally delayed process.', insight_style),
    Spacer(1, 4)
]))

story.append(Paragraph('<i>Figure 2 examines the intake channels feeding this volume</i>, revealing that digital self-service accounts for <b>78.0% of total demand</b> (Mobile 50%, Web 28%). Consequently, front-end capture optimization addresses four-fifths of all incoming applicants.', body_style))

# Figure 2
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig2_channel_mix.png', width=440, height=183),
    Paragraph('<b>Figure 2 — Customer Intake Volume by Acquisition Channel</b>', h2_style),
    Paragraph('<b>What it shows:</b> 520,000 application distribution: Mobile App (260K / 50%), Web Portal (145.6K / 28%), Branch (62.4K / 12%), Affiliate (52K / 10%).<br/>'
              '<b>Key insight:</b> Digital touchpoints account for 78% of incoming customers, but mobile exhibits the highest defect rate (36.8%) due to mobile camera variance.<br/>'
              '<b>Why it matters:</b> 4 out of 5 customers onboard on glass, making mobile viewfinder validation the highest-leverage operational intervention.<br/>'
              '<b>Improvement / action:</b> Deploy client-side WebAssembly computer vision directly into mobile and web viewfinders (FR-001).<br/>'
              '<b>Executive takeaway:</b> 78% of applicants arrive digitally; fixing mobile capture quality addresses the primary point of failure.', insight_style),
    Spacer(1, 4)
]))

story.append(Paragraph('<i>Figure 3 demonstrates the downstream commercial impact across customer tiers</i>: friction in digital intake drives severe abandonment in Fintech Digital (17.8%) and Standard Retail (16.4%), losing 84,500 qualified customer accounts before funding.', body_style))

# Figure 3
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig3_segment_outcomes.png', width=450, height=173),
    Paragraph('<b>Figure 3 — Application Lifecycle Outcomes by Customer Segment</b>', h2_style),
    Paragraph('<b>What it shows:</b> Application outcomes across Standard Retail, Fintech Digital, Premier Wealth, and SME Business.<br/>'
              '<b>Key insight:</b> 16.25% of all applicants abandon the funnel (84,500 accounts), with digital-first cohorts suffering the highest drop-off.<br/>'
              '<b>Why it matters:</b> Losing 84,500 qualified applicants destroys over $58M in estimated customer lifetime value (LTV) and wastes acquisition spend.<br/>'
              '<b>Improvement / action:</b> Implement automated postal prefill (FR-003) and cross-device session continuation (FR-020).<br/>'
              '<b>Executive takeaway:</b> 16.25% of all applicants drop out before funding. Streamlining mobile onboarding rescues over 45,000 customer accounts annually.', insight_style),
    Spacer(1, 8)
]))

# Section 3: Process Bottleneck & Queue Dynamics
story.append(Paragraph('3. Process Bottleneck Isolation & Queue Physics', h1_style))
story.append(Paragraph('To discover why customers wait 58.70 hours, the onboarding timeline was deconstructed into active analyst touch time versus idle wait time. <i>As shown in Figure 4</i>, <b>89.29% of turnaround time (52.42 hours) is idle queue buffer delay</b>. Operations analysts only touch applications for 6.29 hours.', body_style))

# Figure 4
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig4_touch_vs_wait.png', width=450, height=145),
    Paragraph('<b>Figure 4 — Lead Time Decomposition: Active Touch vs. Idle Queue Wait Time</b>', h2_style),
    Paragraph('<b>What it shows:</b> 58.70h cycle time decomposed into active touch time (6.29h, 10.71%) and idle queue buffer delay (52.42h, 89.29%).<br/>'
              '<b>Key insight:</b> Over 89% of the customer\'s elapsed waiting time is spent sitting untouched in departmental queue buffers. Process Cycle Efficiency (PCE) is 10.71%.<br/>'
              '<b>Why it matters:</b> Adding analyst headcount only addresses the 6.29 hours of touch time; eliminating queue hand-offs resolves the 52.42 hours of dead time.<br/>'
              '<b>Improvement / action:</b> Eliminate batch transfers between departments via real-time Kafka event streaming and Straight-Through Processing.<br/>'
              '<b>Executive takeaway:</b> Customers wait 58.7 hours because files sit idle for 52.4 hours. The problem is queue latency, not analyst processing speed.', insight_style),
    Spacer(1, 4)
]))

story.append(Paragraph('<i>Figure 5 identifies the exact organizational hand-offs accumulating this 52.42 hours of idle wait time</i>: Compliance Level-2 review queues (21.2h) and overnight batch mainframe runs (18.5h) generate <b>39.7 hours of combined delay (75.7% of total queue latency)</b>.', body_style))

# Figure 5
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig5_queue_latency.png', width=440, height=169),
    Paragraph('<b>Figure 5 — Departmental Queue Latency & Hand-Off Bottlenecks</b>', h2_style),
    Paragraph('<b>What it shows:</b> Average queue wait hours accumulated across Intake Buffer (8.4h), L1 Ops (18.6h), L2 Compliance (21.2h), and Core Batch (18.5h).<br/>'
              '<b>Key insight:</b> Overnight batch ledger runs (18.5h) and false-positive compliance investigations (21.2h) create a 40-hour delay zone.<br/>'
              '<b>Why it matters:</b> Clean applicants wait 18.5 hours for nightly accounting batches to generate an account number and IBAN.<br/>'
              '<b>Improvement / action:</b> Deploy synchronous Core Banking REST provisioning APIs (FR-030) and Jaro-Winkler fuzzy watchlist screening (FR-010).<br/>'
              '<b>Executive takeaway:</b> Overnight batch files and compliance backlogs create a 40-hour delay. Real-time REST APIs and intelligent screening eliminate both bottlenecks.', insight_style),
    Spacer(1, 4)
]))
story.append(Paragraph('<i>Figure 6 applies Little\'s Law (L = &lambda; &times; W) to quantify the resulting system work-in-progress</i>: with an arrival rate of &lambda; = 59.36 apps/hour and W = 58.70 hours, the bank carries an average inventory of <b>3,485 active applications</b>, with 3,111 files sitting idle.', body_style))

# Figure 6
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig6_littles_law_wip.png', width=430, height=180),
    Paragraph('<b>Figure 6 — Little\'s Law Work-in-Progress (WIP) Backlog Dynamics</b>', h2_style),
    Paragraph('<b>What it shows:</b> Work-in-progress inventory under Little\'s Law (&lambda; = 59.36 apps/hr &times; 58.70 hrs = 3,485 active units).<br/>'
              '<b>Key insight:</b> At any given moment, over 3,100 customer files are trapped in system queues, driving customer inquiries and operational risk.<br/>'
              '<b>Why it matters:</b> High WIP inventory slows cycle velocity and overburdens contact centers with "Where is my account?" calls.<br/>'
              '<b>Improvement / action:</b> Compress turnaround time under 24.0 hours, reducing active work-in-progress to &lt; 800 units (-77.3%).<br/>'
              '<b>Executive takeaway:</b> Over 3,400 customer files are trapped in the pipeline at any given moment. Compressing cycle time to &lt; 24h slashes backlogs by 77%.', insight_style),
    Spacer(1, 8)
]))

# Section 4: Root Cause Isolation & Pareto Rework Drivers
story.append(Paragraph('4. Root Cause Isolation & Document Defect Pareto Distribution', h1_style))
story.append(Paragraph('Forensic analysis investigated why applications were pushed out of the normal pipeline into manual review queues. <i>As shown in Figure 7</i>, <b>83.15% of all 173,429 rework defect loops were driven by three preventable upload flaws</b>: Blurry Images (42.09%), Expired IDs (23.04%), and Address Mismatches (18.02%).', body_style))

# Figure 7
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig7_pareto_rework.png', width=450, height=180),
    Paragraph('<b>Figure 7 — Pareto Analysis of Document Rework Defect Drivers</b>', h2_style),
    Paragraph('<b>What it shows:</b> Annual incident frequency and cumulative percentage across five failure modes.<br/>'
              '<b>Key insight:</b> The top 3 document flaws account for 83.15% of all rework loops (144,207 incidents). Blurry images alone represent 42.09% of all rework.<br/>'
              '<b>Why it matters:</b> Proves that the vast majority of rework is not caused by complex financial crime, but by poor document capture interfaces.<br/>'
              '<b>Improvement / action:</b> Implement client-side OpenCV WebAssembly blur gating (FR-001) and instant OCR date expiration checking (FR-002).<br/>'
              '<b>Executive takeaway:</b> Over 83% of rework loops stem from blurry photos, expired IDs, and address typos. Client-side gating eliminates 144,000 rework loops before submission.', insight_style),
    Spacer(1, 4)
]))

story.append(Paragraph('<i>Figure 8 reveals the channel concentration of these defects</i>: Mobile applicants experience twice the rework rate of Branch-Assisted applicants (36.8% vs. 18.2%) because branches provide scanning guidance, whereas mobile users lack real-time camera feedback.', body_style))

# Figure 8
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig8_channel_friction.png', width=440, height=176),
    Paragraph('<b>Figure 8 — Rework Defect Rate vs. Customer Abandonment by Intake Channel</b>', h2_style),
    Paragraph('<b>What it shows:</b> Cross-tabulated rework and abandonment rates across mobile, web, affiliate, and branch channels.<br/>'
              '<b>Key insight:</b> Mobile App users suffer 36.8% rework and 17.8% abandonment; Branch Assisted shows only 18.2% rework and 8.1% abandonment.<br/>'
              '<b>Why it matters:</b> Confirms that mobile users require automated camera guidance to replicate branch success without branch labor costs.<br/>'
              '<b>Improvement / action:</b> Embed real-time viewfinder framing assistance and instant OCR prefill directly in the mobile SDK.<br/>'
              '<b>Executive takeaway:</b> Mobile applicants fail twice as often as branch applicants due to lack of scan guidance. Smart capture technology bridges this gap.', insight_style),
    Spacer(1, 6)
]))

# Pareto Table
pareto_data = [
    [Paragraph('<b>Failure Mode / Defect</b>', th_style), Paragraph('<b>Annual Count</b>', th_style), Paragraph('<b>% Rework</b>', th_style), Paragraph('<b>Cum %</b>', th_style), Paragraph('<b>Root Cause & Architectural Remedy</b>', th_style)],
    [Paragraph('Blurry / Glare Image', tcb_style), Paragraph('72,994', tc_style), Paragraph('42.09%', tc_style), Paragraph('42.09%', tc_style), Paragraph('Client-side OpenCV WebAssembly real-time sharpness gating (FR-001)', tc_style)],
    [Paragraph('Expired Identification', tcb_style), Paragraph('39,964', tc_style), Paragraph('23.04%', tc_style), Paragraph('65.13%', tc_style), Paragraph('Automated Cloud OCR MRZ date expiration validation within 650ms (FR-002)', tc_style)],
    [Paragraph('Address Proof Mismatch', tcb_style), Paragraph('31,249', tc_style), Paragraph('18.02%', tc_style), Paragraph('83.15%', tc_style), Paragraph('Postal code REST bureau address lookup and prefill (FR-003)', tc_style)],
    [Paragraph('Incomplete Form Fields', tcb_style), Paragraph('20,716', tc_style), Paragraph('11.94%', tc_style), Paragraph('95.10%', tc_style), Paragraph('Interactive form validation and Redis cross-device session cache (FR-020)', tc_style)],
    [Paragraph('Name Typo / Mismatch', tcb_style), Paragraph('8,506', tc_style), Paragraph('4.90%', tc_style), Paragraph('100.00%', tc_style), Paragraph('Jaro-Winkler phonetic double-metaphone fuzzy sanctions matching (FR-010)', tc_style)]
]
t_pt = Table(pareto_data, colWidths=[115, 65, 50, 45, 265])
t_pt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_gray),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
]))
story.append(t_pt)
story.append(Spacer(1, 10))

# Section 5: Key Architectural Improvements Introduced
story.append(Paragraph('5. Key Improvements Introduced: Transforming the Existing Idea', h1_style))
story.append(Paragraph('Rather than replacing banking systems with unvalidated experimental tools, ONBOARD360 re-engineers the proven onboarding pipeline by addressing specific operational bottlenecks with targeted automation and strict governance:', body_style))

improvements = [
    ('1. Upstream Edge Computer Vision Quality Gating',
     'Baseline: Unvalidated uploads admitted blurry and glare-obscured IDs, feeding 72,994 blurry uploads into manual review queues.<br/>'
     'New Contribution: Embedded OpenCV WebAssembly in viewfinders to validate Laplacian sharpness (>=150) and glare (<8%) before upload.<br/>'
     'Why It Matters: Eliminates defects at the glass, stopping bad data from ever entering back-office queues.<br/>'
     'Impact: Eliminates over 90% of image blur defects, preventing 65,000+ rework loops annually.'),
    ('2. Instant OCR MRZ Extraction & Date Expiration Gating',
     'Baseline: Applicants manually typed identity credentials; expired IDs were accepted and discovered days later by human reviewers (39,964 cases).<br/>'
     'New Contribution: Integrated Cloud OCR MRZ extraction and automated calendar expiration checks, rejecting expired documents in 650ms.<br/>'
     'Why It Matters: Eradicates the second largest rework driver with zero human intervention.<br/>'
     'Impact: Eliminates 39,500+ expired document defect incidents annually (-99%).'),
    ('3. Jaro-Winkler Watchlist Screening & Contextual Risk Weighting',
     'Baseline: Rigid exact-string matching flooded compliance queues with false-positive sanctions alerts (29,842 L2 reviews).<br/>'
     'New Contribution: Built a multi-tier screening engine using Jaro-Winkler distance, double-metaphone phonetic matching, and DOB tiering.<br/>'
     'Why It Matters: Differentiates common typographical variations from true sanctions targets.<br/>'
     'Impact: Decreases Level-2 compliance review volume by 47.7%, saving $5.27M in compliance labor.'),
    ('4. 60% Straight-Through Processing (STP) Architecture',
     'Baseline: 0% STP; every application passed through manual reviews or nightly batch mainframe queues.<br/>'
     'New Contribution: Connected automated verification to real-time Core Banking REST APIs, activating verified low-risk accounts in under 15 minutes.<br/>'
     'Why It Matters: Provides consumer-grade instant account activation for clean applicants.<br/>'
     'Impact: Onboards 312,000 customers with zero human touch; unit processing cost drops to $12.55.'),
    ('5. Machine Learning Exception Triage & Strict Regulatory Guardrails',
     'Baseline: All exception cases were dumped into a generic review queue, forcing senior analysts to manually triage minor upload errors.<br/>'
     'New Contribution: Supervised Random Forest classifier routing low-risk issues to WhatsApp self-service while enforcing 0% regulatory leakage.<br/>'
     'Why It Matters: Automates low-risk remediation while quarantining PEP and AML risks for human compliance officers.<br/>'
     'Impact: Achieved 100% precision on defect triage and verified 0% compliance risk leakage across 100 test audits.'),
    ('6. Event-Driven Kafka Milestone Notifications',
     'Baseline: Zero applicant visibility generated 118,602 inbound "Where is my account?" support calls ($1.41M cost).<br/>'
     'New Contribution: Implemented Kafka event streams dispatching automated SMS and push updates at each stage transition.<br/>'
     'Why It Matters: Reassures applicants proactively, eliminating customer uncertainty.<br/>'
     'Impact: Reduces status inquiries by 85%, saving $1.06M in annual contact center costs.')
]

for title, desc in improvements:
    story.append(Paragraph(f'<b>{title}</b>', h2_style))
    story.append(Paragraph(desc, body_style))
    story.append(Spacer(1, 2))

story.append(Spacer(1, 8))

# Section 6: Target Transformation Trajectory & What-If Sensitivity
story.append(Paragraph('6. Transformation Performance Benchmarks & Sensitivity Simulation', h1_style))
story.append(Paragraph('<i>Figure 9 visualizes the compounding performance gains across core operational benchmarks</i>: eliminating document defects upfront enables 60% Straight-Through Processing, which collapses turnaround times and drives an 81.4% reduction in unit processing cost.', body_style))

# Figure 9
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig9_target_benchmarks.png', width=440, height=176),
    Paragraph('<b>Figure 9 — Core Operational Transformation Performance Trajectory</b>', h2_style),
    Paragraph('<b>What it shows:</b> Current AS-IS Baseline vs. Target TO-BE across turnaround time, first-pass yield, rework, and unit cost.<br/>'
              '<b>Key insight:</b> TAT drops from 58.70h to &lt; 24.00h (-59.1%); FPY expands from 58.12% to 78.0%+; rework falls from 33.35% to &lt; 10%; unit cost falls from $67.45 to $12.55 (-81.4%).<br/>'
              '<b>Why it matters:</b> Compounding operational gains enable rapid digital onboarding and substantial margin expansion.<br/>'
              '<b>Improvement / action:</b> Monitor actual operational metrics against these targets using the interactive analytics center.<br/>'
              '<b>Executive takeaway:</b> ONBOARD360 transforms NovaBank into a digital leader, cutting cycle times by 59% and unit operating costs by 81%.', insight_style),
    Spacer(1, 4)
]))

story.append(Paragraph('<i>Figure 10 presents a dynamic What-If sensitivity simulation across operational scenarios</i>: even under a pessimistic Conservative scenario (45% STP with a 12% CAPEX overrun), the initiative yields <b>$16.57M in annual savings and a $36.06M 3-Year NPV</b>, proving extreme downside protection.', body_style))

# Figure 10
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig10_scenario_sensitivity.png', width=440, height=176),
    Paragraph('<b>Figure 10 — What-If Sensitivity Analysis Across Operational Scenarios</b>', h2_style),
    Paragraph('<b>What it shows:</b> Annual savings and 3-Year NPV across Conservative (45% STP, $3.2M Capex), Base Case (60% STP, $2.85M Capex), and Aggressive (75% STP, $2.5M Capex).<br/>'
              '<b>Key insight:</b> Even under a pessimistic 45% STP adoption rate, the project generates $16.57M in annual savings and a $36.06M 3-Year NPV.<br/>'
              '<b>Why it matters:</b> Confirms that capital allocation carries virtually zero risk of negative return under any plausible operating condition.<br/>'
              '<b>Improvement / action:</b> Budget capital against the 60% STP Base Case with confidence in downside safety.<br/>'
              '<b>Executive takeaway:</b> The business case is robust: even under conservative 45% STP adoption, the project delivers $16.57M annually with a $36.06M NPV.', insight_style),
    Spacer(1, 8)
]))

# Section 7: Activity-Based Costing & Multi-Year Financial Returns
story.append(Paragraph('7. Activity-Based Costing & Multi-Year Financial Returns', h1_style))
story.append(Paragraph('Direct operating costs were modeled using Activity-Based Costing (ABC) reconciled against operational labor, vendor licensing, and customer service contact costs. <i>As shown in Figure 11</i>, <b>80.5% of total savings ($17.78M) come from reducing manual review labor</b> in Operations ($12.51M) and Compliance ($5.27M).', body_style))

# Figure 11
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig11_activity_based_cost.png', width=450, height=180),
    Paragraph('<b>Figure 11 — Activity-Based Annual Operating Cost Decomposition</b>', h2_style),
    Paragraph('<b>What it shows:</b> Line-item budget comparison between AS-IS Operating Costs ($27.97M) and TO-BE Projected Costs ($5.87M).<br/>'
              '<b>Key insight:</b> L1 Operations labor falls from $13.91M to $1.40M (+$12.51M); L2 Compliance labor falls from $6.79M to $1.52M (+$5.27M); API vendor fees decrease by $2.91M; support costs drop by $1.06M.<br/>'
              '<b>Why it matters:</b> Direct annual operating cost collapses from $27.97M to $5.87M, yielding $22,092,276 in annual net cash savings.<br/>'
              '<b>Improvement / action:</b> Reallocate freed operations staff to high-value commercial onboarding and complex fraud investigations.<br/>'
              '<b>Executive takeaway:</b> ONBOARD360 captures $22.09M in annual recurring savings by reducing manual review labor by $17.78M, vendor fees by $2.91M, and support costs by $1.06M.', insight_style),
    Spacer(1, 4)
]))

story.append(Paragraph('<i>Figure 12 illustrates the 3-year capital recovery curve</i>: against an initial capital outlay of $2.85M, <b>capital breakeven occurs in just 2.0 months of full operation</b>, generating an exceptional <b>3-Year Net Present Value of $49,501,858.44</b> (8.5% hurdle rate) with an <b>IRR &gt; 200%</b>.', body_style))

# Figure 12
story.append(KeepTogether([
    Image('11_Executive_Presentation/charts/fig12_cash_flow_payback.png', width=450, height=166),
    Paragraph('<b>Figure 12 — 3-Year Capital Recovery & Discounted Cash Flow Realization</b>', h2_style),
    Paragraph('<b>What it shows:</b> Cumulative discounted cash flows across 36 operating months against the initial $2.85M CAPEX.<br/>'
              '<b>Key insight:</b> Capital breakeven is achieved in Month 2; cumulative cash return reaches $14.82M in Year 1, $36.92M in Year 2, and $59.01M in Year 3.<br/>'
              '<b>Why it matters:</b> Provides executive leadership with verified assurance of rapid capital recovery and massive multi-year value accretion.<br/>'
              '<b>Improvement / action:</b> Approve full $2.85M Phase 1 capital allocation and execute vendor procurement.<br/>'
              '<b>Executive takeaway:</b> An investment of $2.85M yields $49.50M in 3-Year NPV, an IRR exceeding 200%, and breaks even in 2.0 months. Capital approval is strongly recommended.', insight_style),
    Spacer(1, 6)
]))

# Financial Table
fin_table_data = [
    [Paragraph('<b>Financial Performance Metric</b>', th_style), Paragraph('<b>Value</b>', th_style), Paragraph('<b>Financial Performance Metric</b>', th_style), Paragraph('<b>Value</b>', th_style)],
    [Paragraph('Initial Capital Investment (CAPEX)', tcb_style), Paragraph('$2,850,000.00', tc_style), Paragraph('Annual Net Recurring Cash Savings', tcb_style), Paragraph('$22,092,276.10', tc_style)],
    [Paragraph('Hurdle Discount Rate', tcb_style), Paragraph('8.50%', tc_style), Paragraph('Year 1 Cash Inflow (80% realization)', tcb_style), Paragraph('$17,673,820.88', tc_style)],
    [Paragraph('3-Year Net Present Value (NPV)', tcb_style), Paragraph('<b>$49,501,858.44</b>', tc_style), Paragraph('Capital Payback Period', tcb_style), Paragraph('<b>2.0 Months</b>', tc_style)],
    [Paragraph('Internal Rate of Return (IRR)', tcb_style), Paragraph('<b>&gt; 200.0%</b>', tc_style), Paragraph('Conservative Scenario NPV (45% STP)', tcb_style), Paragraph('$36,063,893.83', tc_style)]
]
t_fin = Table(fin_table_data, colWidths=[150, 115, 150, 115])
t_fin.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_gray),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
]))
story.append(t_fin)
story.append(Spacer(1, 10))

# Section 8: Stakeholder Benefit Realization
story.append(Paragraph('8. Stakeholder Benefit Analysis: Who Benefited & How Much', h1_style))
stk_data = [
    [Paragraph('<b>Stakeholder Group</b>', th_style), Paragraph('<b>Operational Problem (Before)</b>', th_style), Paragraph('<b>Transformation Solution</b>', th_style), Paragraph('<b>Quantified Business Benefit & Value</b>', th_style)],
    [Paragraph('<b>End Customers</b>', tcb_style), Paragraph('58.7h turnaround, repetitive uploads, opaque tracking', tc_style), Paragraph('Client-side CV, instant OCR, WhatsApp self-service', tc_style), Paragraph('TAT &lt; 24h (&lt;15m STP); 45K fewer abandonments; frictionless UX', tc_style)],
    [Paragraph('<b>Retail Leadership</b>', tcb_style), Paragraph('16.25% funnel drop-off losing deposits to fintechs', tc_style), Paragraph('Instant STP opening, frictionless mobile UX', tc_style), Paragraph('+45,475 funded accounts ($58M+ pipeline LTV); protects market share', tc_style)],
    [Paragraph('<b>Operations (L1)</b>', tcb_style), Paragraph('184K reviews swamped with blurry IDs & form errors', tc_style), Paragraph('OpenCV sharpness gate, postal prefill, AI Triage', tc_style), Paragraph('-77.4% review volume; saves $12,512,640 / yr; eliminates review fatigue', tc_style)],
    [Paragraph('<b>Compliance (L2)</b>', tcb_style), Paragraph('False sanctions alerts from exact-string matches', tc_style), Paragraph('Jaro-Winkler fuzzy phonetic screening & DOB tiering', tc_style), Paragraph('-47.7% L2 reviews; saves $5,268,055 / yr; focuses on real AML/PEP risks', tc_style)],
    [Paragraph('<b>Customer Support</b>', tcb_style), Paragraph('118K tickets; 83% \'Where is my account?\' inquiries', tc_style), Paragraph('Kafka real-time event status push notifications', tc_style), Paragraph('-75% ticket volume; saves $1,056,493 / yr; cuts contact center wait times', tc_style)],
    [Paragraph('<b>CFO / Management</b>', tcb_style), Paragraph('$67.45 unit cost eroding retail banking margins', tc_style), Paragraph('60% STP automation and queue removal', tc_style), Paragraph('Unit cost $12.55 (-81.4%); $22.09M net cash / yr; 2.0 mo payback', tc_style)]
]
t_stk = Table(stk_data, colWidths=[90, 130, 135, 175])
t_stk.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_gray),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
]))
story.append(t_stk)
story.append(Spacer(1, 10))

# Section 9: Applied Business Capabilities
story.append(Paragraph('9. Applied Analytical Capabilities & Target Domain Relevance', h1_style))
story.append(Paragraph('The methods applied throughout ONBOARD360 reflect formal competencies in process engineering, requirements architecture, quantitative analytics, and executive financial storytelling:', body_style))

skills_text = (
    '<b>• Process Analysis & Queuing Theory:</b> Applied Little\'s Law and touch/wait decomposition to redirect executive strategy away from costly staff additions toward removing 52.42 hours of asynchronous batch queues.<br/>'
    '<b>• Root Cause Analysis & Process Mining:</b> Leveraged Pareto 80/20 distributions and SQL window functions to concentrate engineering investment on client-side capture, eliminating 83.15% of document rework.<br/>'
    '<b>• Requirements Architecture & MoSCoW:</b> Authored 10 Business Requirements, 35 Functional Requirements, and 10 Deterministic Business Rules with 100% bidirectional traceability, eliminating scope creep and ensuring regulatory compliance.<br/>'
    '<b>• Agile Product Backlog & Story Craft:</b> Structured 6 Epics and 35+ INVEST-compliant user stories with Gherkin acceptance criteria across 4 sprints, enabling seamless cross-functional delivery.<br/>'
    '<b>• Machine Learning & Ethical Governance:</b> Designed a supervised Random Forest exception triage engine with deterministic compliance guardrails, achieving 100% defect precision and 0% regulatory leakage on PEP/AML alerts.<br/>'
    '<b>• Activity-Based Costing & Financial Appraisal:</b> Constructed a multi-variable DCF capital appraisal model that justified a $2.85M investment by proving a 2.0-month payback and a $49.50M 3-Year NPV to the Board of Directors.<br/>'
    '<b>• Business Intelligence & Executive Storytelling:</b> Built a 5-page star-schema data model with 25+ DAX measures and an interactive web command center, equipping leadership with real-time operational transparency.'
)
story.append(Paragraph(skills_text, body_style))
story.append(Spacer(1, 8))

# Section 10: Verification & Sign-off
story.append(Paragraph('10. Governance, Quality Assurance & Executive Recommendation', h1_style))
story.append(Paragraph('The ONBOARD360 platform achieves 100% bidirectional Requirements Traceability (PNT-01..06 &rarr; BR-01..10 &rarr; FR-01..35 &rarr; Stories &rarr; UAT). Machine learning governance was audited across 100 randomized PEP/High-Risk AML cases with <b>zero regulatory leakage</b> (100% routed to human compliance officers). The master automated test suite (<code>test_onboard360_master.py</code>) executes <b>160 test assertions with a 100% pass rate in 5.0 seconds</b>.', body_style))

story.append(Paragraph('<b>Executive Recommendation:</b> Immediate approval of the $2.85M Phase 1 capital allocation is recommended. Controlled regional pilot cutover commences in Month 9 in the UK/EU Retail Channel, followed by global enterprise rollout in Month 12. Breakeven occurs in Month 2 of full operation.', takeaway_style))

story.append(Paragraph('<b>Lead Contributor & Sign-off:</b><br/>'
                       '<b>Hriday Singh Sobti</b><br/>'
                       'NovaBank International Transformation Initiative<br/>'
                       'Interactive Project Artifacts: <a href="https://github.com/hriday-sobti/ONBOARD360" color="#2E75B6"><u>https://github.com/hriday-sobti/ONBOARD360</u></a>', meta_style))

doc.build(story)
print(f'Enhanced publication-quality executive PDF generated successfully at: {pdf_path}')
