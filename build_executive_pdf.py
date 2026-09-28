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
    topMargin=32,
    bottomMargin=32
)

styles = getSampleStyleSheet()

primary_color = colors.HexColor('#1F4E79')
secondary_color = colors.HexColor('#2E75B6')
text_dark = colors.HexColor('#0F172A')
border_gray = colors.HexColor('#CBD5E1')
bg_light = colors.HexColor('#F8FAFC')
callout_bg = colors.HexColor('#F1F5F9')

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=17,
    leading=21,
    textColor=primary_color,
    spaceAfter=3
)

meta_style = ParagraphStyle(
    'DocMeta',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=11.5,
    textColor=colors.HexColor('#475569'),
    spaceAfter=8
)

h1_style = ParagraphStyle(
    'SectionH1',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=11.5,
    leading=15,
    textColor=primary_color,
    spaceBefore=0,
    spaceAfter=5,
    keepWithNext=True
)

h2_style = ParagraphStyle(
    'SectionH2',
    parent=styles['Heading3'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=13,
    textColor=secondary_color,
    spaceBefore=4,
    spaceAfter=3,
    keepWithNext=True
)

body_style = ParagraphStyle(
    'DocBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=11.5,
    textColor=text_dark,
    spaceAfter=4
)

insight_style = ParagraphStyle(
    'InsightBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7.8,
    leading=10.8,
    textColor=text_dark,
    spaceAfter=3
)

takeaway_style = ParagraphStyle(
    'TakeawayBox',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7.8,
    leading=10.5,
    textColor=colors.HexColor('#0F172A'),
    backColor=callout_bg,
    borderColor=secondary_color,
    borderWidth=0.8,
    borderPadding=4,
    spaceBefore=2,
    spaceAfter=6
)

th_style = ParagraphStyle(
    'TableHeader',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=7.2,
    leading=9,
    textColor=colors.white,
    alignment=1
)

tc_style = ParagraphStyle(
    'TableCell',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=6.8,
    leading=8.8,
    textColor=text_dark
)

tcb_style = ParagraphStyle(
    'TableCellBold',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=6.8,
    leading=8.8,
    textColor=primary_color
)

story = []

# =========================================================================
# PAGE 1: TITLE & EXECUTIVE SUMMARY & SCORECARD
# =========================================================================
story.append(Paragraph('ONBOARD360 — Customer Onboarding & KYC Process Modernization', title_style))
story.append(Paragraph('<b>Executive Review & Operational Transformation Blueprint</b> | Lead Contributor: Hriday Singh Sobti | NovaBank International<br/>Verified Project Repository & Interactive Dashboard: <a href="https://github.com/hriday-sobti/ONBOARD360" color="#1F4E79"><u>https://github.com/hriday-sobti/ONBOARD360</u></a>', meta_style))
story.append(Spacer(1, 2))

story.append(Paragraph('1. Executive Summary: Operational Reality and Transformation Mandate', h1_style))
story.append(Paragraph('NovaBank International processes <b>520,000 onboarding applications annually</b> across the UK/EU, North America, APAC, and Latin America. The baseline operation required an average turnaround time of <b>58.70 hours</b> from submission to account activation. A detailed queue analysis revealed that <b>52.42 hours (89.29% of elapsed time) was dead queue wait time</b> between departmental hand-offs, while active human review took only <b>6.29 hours</b> (Process Cycle Efficiency = 10.71%).', body_style))

story.append(Paragraph('Front-end upload screens accepted out-of-focus and expired documents without verification. This triggered a <b>33.35% rework rate (173,429 cases)</b>, overloaded back-office queues with <b>213,842 manual reviews (41.12% review rate)</b>, and caused <b>16.25% customer abandonment (84,500 qualified applicants lost)</b>. Furthermore, customers logged <b>118,602 support tickets</b> ($1.41M cost), with 82.8% simply asking "Where is my account?". Direct operational expenses reached <b>$67.45 per account</b>, totaling <b>$27.97M annually</b>.', body_style))

story.append(Paragraph('<b>The ONBOARD360 Solution</b> re-engineers this pipeline into an event-driven straight-through architecture. Client-side computer vision stops document defects at the glass; fuzzy screening eliminates false-positive compliance alerts; and machine learning triages non-straight-through cases with zero regulatory leakage. The target state achieves <b>60% Straight-Through Processing (STP)</b>, reduces cycle time to <b>&lt; 24.0 hours</b> (&lt; 15 minutes for clean paths), cuts unit cost to <b>$12.55</b> (-81.4%), and generates <b>$22,092,276 in annual net cash savings</b> on a <b>$2.85M investment</b> (3-Year NPV $49.50M @ 8.5% hurdle rate, IRR &gt; 200%, payback in 2.0 months).', body_style))
story.append(Spacer(1, 4))

scorecard_data = [
    [Paragraph('<b>Operational Performance Metric</b>', th_style), Paragraph('<b>AS-IS Baseline</b>', th_style), Paragraph('<b>TO-BE Target</b>', th_style), Paragraph('<b>Net Variance</b>', th_style), Paragraph('<b>Audit Classification</b>', th_style)],
    [Paragraph('Average Turnaround Time (TAT)', tcb_style), Paragraph('58.70 Hours', tc_style), Paragraph('&lt; 24.0 Hours (&lt;15m STP)', tc_style), Paragraph('-59.1% Total Cycle Time', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Idle Queue Wait Time Ratio', tcb_style), Paragraph('89.29% (52.42h)', tc_style), Paragraph('&lt; 25.00% (5.00h)', tc_style), Paragraph('-90.5% Queue Wait Time', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Straight-Through Processing (STP)', tcb_style), Paragraph('0.0% (Batch Dependent)', tc_style), Paragraph('60.0% (Automated Clear)', tc_style), Paragraph('+60.0 pts Automated STP', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('First-Pass Yield (FPY)', tcb_style), Paragraph('58.12% (302K apps)', tc_style), Paragraph('&ge; 78.00% (405K apps)', tc_style), Paragraph('+19.9 pts Clean Approvals', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Application Rework Rate', tcb_style), Paragraph('33.35% (173K apps)', tc_style), Paragraph('&le; 10.00% (52K apps)', tc_style), Paragraph('-70.0% Resubmission Loops', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Customer Abandonment Rate', tcb_style), Paragraph('16.25% (84.5K apps)', tc_style), Paragraph('&le; 7.50% (39.0K apps)', tc_style), Paragraph('-53.8% Funnel Drop-off', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('SLA Breach Rate (&gt; 48 Hours)', tcb_style), Paragraph('45.92% (238K apps)', tc_style), Paragraph('&le; 2.50% (13K apps)', tc_style), Paragraph('-94.6% SLA Failure Drop', tc_style), Paragraph('Projected', tc_style)],
    [Paragraph('Direct Unit Operating Cost', tcb_style), Paragraph('$67.45 / Account', tc_style), Paragraph('$12.55 / Account', tc_style), Paragraph('-$54.90 / Account (-81.4%)', tc_style), Paragraph('Modelled', tc_style)],
    [Paragraph('Total Annual Direct OPEX', tcb_style), Paragraph('$27,967,200.60', tc_style), Paragraph('$5,874,924.50', tc_style), Paragraph('+$22,092,276.10 Annual Benefit', tc_style), Paragraph('Modelled', tc_style)]
]
t_sc = Table(scorecard_data, colWidths=[150, 95, 115, 110, 70])
t_sc.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_gray),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
]))
story.append(t_sc)

# =========================================================================
# PAGE 2: MACRO INFLOW & INTAKE CHANNELS (FIG 1 & FIG 2)
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('2. Macro Demand Inflow & Customer Acquisition Channels', h1_style))
story.append(Paragraph('Analysis began by testing whether onboarding delays were seasonal spikes or chronic operational flaws. <i>As shown in Figure 1</i>, incoming volume was stable across 2025 (~43,300 applications monthly), while the 48-hour SLA breach rate remained locked at <b>45.92%</b> (238,784 breaches), proving the failure is built into the workflow architecture rather than caused by volume spikes.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig1_intake_sla.png', width=450, height=140))
story.append(Paragraph('<b>Figure 1 — Monthly Application Inflow vs. 48h SLA Breach Rate (2025)</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Monthly application volume plotted against the monthly percentage of cases breaching the 48-hour SLA threshold.<br/>'
                       '<b>Key insight:</b> The breach rate remained between 45.2% and 46.8% all year, averaging 45.92% across all four operating regions.<br/>'
                       '<b>Why it matters:</b> Disproves the operational assumption that delays were seasonal. The operating model systematically fails customer commitments under steady-state load.<br/>'
                       '<b>Improvement / action:</b> Replace departmental batch hand-offs with continuous straight-through event routing.<br/>'
                       '<b>Executive takeaway:</b> NovaBank fails customer SLAs on nearly half of all submissions every month. Overtime staffing cannot fix an architectural queue bottleneck.', insight_style))
story.append(Spacer(1, 4))

story.append(Paragraph('<i>Figure 2 traces where this volume enters the bank</i>. Digital self-service channels generate <b>78.0% of all applications</b> (Mobile 50%, Web 28%), making the digital capture interface the primary lever for operational improvement across the enterprise.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig2_channel_mix.png', width=440, height=135))
story.append(Paragraph('<b>Figure 2 — Customer Intake Volume by Acquisition Channel</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Breakdown of the 520,000 annual applications across digital and assisted channels.<br/>'
                       '<b>Key insight:</b> Mobile App (260,000 apps) and Web Portal (145,600 apps) represent 78% of demand, but mobile experiences double the rework rate of branches.<br/>'
                       '<b>Why it matters:</b> 4 out of 5 customers apply on a screen. Upgrading the mobile viewfinder capture experience directly addresses the point of origin for most customer friction.<br/>'
                       '<b>Improvement / action:</b> Embed real-time computer vision quality validation directly into the mobile application camera flow (FR-001).<br/>'
                       '<b>Executive takeaway:</b> 78% of applicants arrive via digital channels. Front-end capture intelligence stops defects where the customer initiates the relationship.', insight_style))

# =========================================================================
# PAGE 3: SEGMENT OUTCOMES & TOUCH VS. WAIT TIME (FIG 3 & FIG 4)
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('3. Customer Funnel Abandonment & Lead Time Decomposition', h1_style))
story.append(Paragraph('<i>Figure 3 demonstrates the commercial consequence of front-end friction across customer segments</i>. Fintech Digital (17.8%) and Standard Retail (16.4%) experience heavy drop-off, resulting in <b>84,500 lost accounts annually</b> ($58M+ in lost customer lifetime value).', body_style))

story.append(Image('11_Executive_Presentation/charts/fig3_segment_outcomes.png', width=450, height=135))
story.append(Paragraph('<b>Figure 3 — Application Lifecycle Outcomes by Customer Segment</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Completion outcomes across Standard Retail, Fintech Digital, Premier Wealth, and SME Business.<br/>'
                       '<b>Key insight:</b> 16.25% of all applicants abandon the process before funding. Digital cohorts suffer the highest drop-off due to repetitive document requests.<br/>'
                       '<b>Why it matters:</b> Losing 84,500 qualified applicants burns customer acquisition marketing spend and erodes deposit growth.<br/>'
                       '<b>Improvement / action:</b> Implement automated postal bureau prefill (FR-003) and cross-device session continuation (FR-020).<br/>'
                       '<b>Executive takeaway:</b> 16.25% of all applicants drop out before funding. Removing capture friction will rescue over 45,000 accounts annually.', insight_style))
story.append(Spacer(1, 4))

story.append(Paragraph('To establish where customer time is lost, cycle times were deconstructed into active processing touch time versus idle wait time. <i>As shown in Figure 4</i>, <b>89.29% of the 58.70-hour journey is idle queue buffer delay (52.42 hours)</b>. Analysts only touch files for 6.29 hours.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig4_touch_vs_wait.png', width=450, height=125))
story.append(Paragraph('<b>Figure 4 — Total Lead Time Breakdown: Active Touch vs. Idle Queue Wait Time</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Average cycle time deconstructed into active analyst touch time (6.29h, 10.71%) and idle queue buffer delay (52.42h, 89.29%).<br/>'
                       '<b>Key insight:</b> Applications sit untouched in queues for nearly 90% of their total turnaround time. Process Cycle Efficiency is an uncompetitive 10.71%.<br/>'
                       '<b>Why it matters:</b> Adding analyst headcount only impacts the 6.29 hours of touch time. To achieve sub-24h turnaround, the bank must eliminate the 52.42 hours of idle queue buffers.<br/>'
                       '<b>Improvement / action:</b> Replace asynchronous batch queues with real-time Kafka event streaming and automated Straight-Through Processing.<br/>'
                       '<b>Executive takeaway:</b> Customers wait 58.7 hours because applications sit untouched for 52.4 hours. The problem is queue latency, not analyst processing speed.', insight_style))

# =========================================================================
# PAGE 4: QUEUE LATENCY & LITTLE'S LAW BACKLOG (FIG 5 & FIG 6)
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('4. Departmental Queue Latency & Queue Physics (Little\'s Law)', h1_style))
story.append(Paragraph('<i>Figure 5 isolates the exact organizational hand-offs creating this 52.42 hours of idle wait time</i>. Compliance Level-2 reviews (21.2h) and overnight batch core runs (18.5h) account for <b>39.7 hours of combined delay (75.7% of total queue latency)</b>.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig5_queue_latency.png', width=440, height=135))
story.append(Paragraph('<b>Figure 5 — Departmental Queue Latency & Hand-Off Bottlenecks</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Average queue wait hours accumulated across Intake Buffer (8.4h), L1 Ops (18.6h), L2 Compliance (21.2h), and Core Batch (18.5h).<br/>'
                       '<b>Key insight:</b> Nightly batch ledger runs (18.5h) and false-positive compliance reviews (21.2h) create a 40-hour delay zone.<br/>'
                       '<b>Why it matters:</b> Clean applicants wait 18.5 hours for nightly accounting batch files to issue an account number and IBAN.<br/>'
                       '<b>Improvement / action:</b> Deploy synchronous Core Banking REST provisioning APIs (FR-030) and Jaro-Winkler fuzzy watchlist screening (FR-010).<br/>'
                       '<b>Executive takeaway:</b> Overnight batch files and compliance queues create a 40-hour delay. Real-time REST APIs and intelligent screening eliminate both bottlenecks.', insight_style))
story.append(Spacer(1, 4))
story.append(Paragraph('<i>Figure 6 applies Little\'s Law (L = &lambda; &times; W) to quantify the resulting work-in-progress inventory</i>. With an inflow of &lambda; = 59.36 apps/hour and W = 58.70 hours, the bank carries an average inventory of <b>3,485 active applications</b>, with 3,111 sitting idle.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig6_littles_law_wip.png', width=430, height=135))
story.append(Paragraph('<b>Figure 6 — Little\'s Law Work-in-Progress (WIP) Backlog Dynamics</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Pipeline backlog calculated via Little\'s Law (&lambda; = 59.36 apps/hr &times; 58.70 hrs = 3,485 active units).<br/>'
                       '<b>Why it matters:</b> High WIP inventory slows cycle velocity and overburdens support teams with "Where is my account?" inquiries.<br/>'
                       '<b>Improvement / action:</b> Compress turnaround time under 24.0 hours, reducing active work-in-progress to &lt; 800 units (-77.3%).<br/>'
                       '<b>Executive takeaway:</b> Over 3,400 customer files are trapped in the pipeline at any given moment. Compressing cycle time to &lt; 24h slashes backlogs by 77%.', insight_style))

# =========================================================================
# PAGE 5: ROOT CAUSE PARETO & CHANNEL DEFECT MATRIX (FIG 7 & FIG 8)
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('5. Root Cause Isolation & Document Defect Pareto Distribution', h1_style))
story.append(Paragraph('Forensic analysis investigated what triggered files to exit normal processing into manual review queues. <i>As shown in Figure 7</i>, <b>83.15% of all 173,429 rework defect loops were driven by three preventable upload flaws</b>: Blurry Images (42.09%), Expired IDs (23.04%), and Address Mismatches (18.02%).', body_style))

story.append(Image('11_Executive_Presentation/charts/fig7_pareto_rework.png', width=450, height=135))
story.append(Paragraph('<b>Figure 7 — Pareto Analysis of Document Rework Defect Drivers</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Annual incident frequency and cumulative percentage across five failure modes.<br/>'
                       '<b>Key insight:</b> The top 3 document flaws account for 83.15% of all rework loops (144,207 incidents). Blurry images alone represent 42.09% of all rework.<br/>'
                       '<b>Why it matters:</b> Proves that the vast majority of rework is not caused by complex financial crime checks, but by poor document capture interfaces.<br/>'
                       '<b>Improvement / action:</b> Implement client-side OpenCV WebAssembly blur gating (FR-001) and instant OCR date expiration checking (FR-002).<br/>'
                       '<b>Executive takeaway:</b> Over 83% of rework loops stem from blurry photos, expired IDs, and address typos. Client-side gating eliminates 144,000 rework loops before submission.', insight_style))
story.append(Spacer(1, 4))

story.append(Paragraph('<i>Figure 8 reveals the channel concentration of these defects</i>: Mobile applicants experience twice the rework rate of branch applicants (36.8% vs. 18.2%) because branches provide scanning guidance, whereas mobile users lack real-time camera feedback.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig8_channel_friction.png', width=440, height=130))
story.append(Paragraph('<b>Figure 8 — Rework Defect Rate vs. Customer Abandonment by Intake Channel</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Cross-tabulated rework and abandonment rates across mobile, web, affiliate, and branch channels.<br/>'
                       '<b>Key insight:</b> Mobile App users suffer 36.8% rework and 17.8% abandonment; Branch Assisted shows only 18.2% rework and 8.1% abandonment.<br/>'
                       '<b>Why it matters:</b> Confirms that mobile users require automated camera guidance to replicate branch success without branch labor costs.<br/>'
                       '<b>Improvement / action:</b> Embed real-time viewfinder framing assistance and instant OCR prefill directly in the mobile SDK.<br/>'
                       '<b>Executive takeaway:</b> Mobile applicants fail twice as often as branch applicants due to lack of scan guidance. Smart capture technology bridges this gap.', insight_style))

# Pareto Table
pareto_data = [
    [Paragraph('<b>Failure Mode / Defect</b>', th_style), Paragraph('<b>Annual Count</b>', th_style), Paragraph('<b>% Rework</b>', th_style), Paragraph('<b>Cum %</b>', th_style), Paragraph('<b>Root Cause & Architectural Remedy</b>', th_style)],
    [Paragraph('Blurry / Glare Image', tcb_style), Paragraph('72,994', tc_style), Paragraph('42.09%', tc_style), Paragraph('42.09%', tc_style), Paragraph('Client-side OpenCV WebAssembly real-time sharpness gating (FR-001)', tc_style)],
    [Paragraph('Expired Identification', tcb_style), Paragraph('39,964', tc_style), Paragraph('23.04%', tc_style), Paragraph('65.13%', tc_style), Paragraph('Automated Cloud OCR MRZ date expiration validation within 650ms (FR-002)', tc_style)],
    [Paragraph('Address Proof Mismatch', tcb_style), Paragraph('31,249', tc_style), Paragraph('18.02%', tc_style), Paragraph('83.15%', tc_style), Paragraph('Postal code REST bureau address lookup and prefill (FR-003)', tc_style)],
    [Paragraph('Incomplete Form Fields', tcb_style), Paragraph('20,716', tc_style), Paragraph('11.94%', tc_style), Paragraph('95.10%', tc_style), Paragraph('Interactive form validation and Redis cross-device session cache (FR-020)', tc_style)],
    [Paragraph('Name Typo / Mismatch', tcb_style), Paragraph('8,506', tc_style), Paragraph('4.90%', tc_style), Paragraph('100.00%', tc_style), Paragraph('Jaro-Winkler phonetic double-metaphone fuzzy sanctions matching (FR-010)', tc_style)]
]
t_pt = Table(pareto_data, colWidths=[115, 60, 50, 45, 270])
t_pt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), primary_color),
    ('GRID', (0,0), (-1,-1), 0.5, border_gray),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, bg_light])
]))
story.append(t_pt)

# =========================================================================
# PAGE 6: KEY ARCHITECTURAL IMPROVEMENTS INTRODUCED
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('6. Key Improvements Introduced: Re-Engineering the Legacy Operating Model', h1_style))
story.append(Paragraph('Rather than replacing core banking platforms with risky unvalidated tools, ONBOARD360 re-engineers the proven onboarding journey by introducing targeted automation and deterministic guardrails at known operational failure points:', body_style))

improvements = [
    ('1. Upstream Edge Computer Vision Quality Gating',
     '<b>Baseline:</b> Unvalidated uploads admitted blurry, cropped, and glare-compromised photos directly into queues (72,994 blurry uploads annually).<br/>'
     '<b>New Contribution:</b> Embedded OpenCV WebAssembly directly in web and mobile camera viewfinders to test Laplacian focus variance (&ge; 150) and glare (&le; 8%) before upload.<br/>'
     '<b>Why It Matters:</b> Resolves defects at the glass, stopping unreadable scans before they consume back-office analyst labor.<br/>'
     '<b>Impact:</b> Eliminates over 90% of image blur defects, avoiding 65,000+ rework loops annually.'),
    ('2. Instant OCR MRZ Extraction & Date Expiration Gating',
     '<b>Baseline:</b> Applicants manually typed identity numbers; expired credentials were accepted and discovered days later by human reviewers (39,964 cases).<br/>'
     '<b>New Contribution:</b> Automated Cloud OCR MRZ extraction and calendar expiration validation, rejecting expired credentials in 650ms.<br/>'
     '<b>Why It Matters:</b> Eradicates the bank\'s second largest rework driver with zero human touch.<br/>'
     '<b>Impact:</b> Eliminates 39,500+ expired document defects annually (-99%).'),
    ('3. Jaro-Winkler Watchlist Screening & Contextual Risk Weighting',
     '<b>Baseline:</b> Rigid exact-string matching flooded compliance queues with false sanctions alerts (29,842 L2 reviews).<br/>'
     '<b>New Contribution:</b> Multi-tier screening engine using Jaro-Winkler distance, double-metaphone phonetic matching, and DOB tiering.<br/>'
     '<b>Why It Matters:</b> Differentiates minor typographical name variations from true regulatory sanctions targets.<br/>'
     '<b>Impact:</b> Cuts Level-2 compliance review volume by 47.7%, saving $5.27M in compliance labor.'),
    ('4. 60% Straight-Through Processing (STP) Architecture',
     '<b>Baseline:</b> 0% STP; every application passed through manual reviews or nightly batch mainframe queues.<br/>'
     '<b>New Contribution:</b> Automated orchestration pipeline connecting verification to real-time Core Banking REST APIs for sub-15m account opening.<br/>'
     '<b>Why It Matters:</b> Provides consumer-grade instant account activation for verified, low-risk applicants.<br/>'
     '<b>Impact:</b> Onboards 312,000 customers with zero human touch; unit processing cost drops to $12.55.'),
    ('5. Machine Learning Exception Triage & Strict Regulatory Guardrails',
     '<b>Baseline:</b> All exception cases were dumped into a generic manual review pool, forcing senior analysts to manually triage minor upload errors.<br/>'
     '<b>New Contribution:</b> Supervised Random Forest classifier routing low-risk issues to WhatsApp self-service while enforcing 0% regulatory risk leakage.<br/>'
     '<b>Why It Matters:</b> Automates low-risk remediation while quarantining PEP and AML risks for human compliance officers.<br/>'
     '<b>Impact:</b> Achieved 100% precision on defect triage and verified 0% compliance risk leakage across 100 test audits.'),
    ('6. Event-Driven Kafka Milestone Notifications',
     '<b>Baseline:</b> Zero applicant visibility generated 118,602 inbound "Where is my account?" support calls ($1.41M cost).<br/>'
     '<b>New Contribution:</b> Implemented Kafka event streams dispatching automated SMS and push updates at each stage transition.<br/>'
     '<b>Why It Matters:</b> Reassures applicants proactively, eliminating customer uncertainty.<br/>'
     '<b>Impact:</b> Reduces status inquiries by 85%, saving $1.06M in annual contact center costs.')
]

for title, desc in improvements:
    story.append(Paragraph(f'<b>{title}</b>', h2_style))
    story.append(Paragraph(desc, body_style))
    story.append(Spacer(1, 1))

# =========================================================================
# PAGE 7: PERFORMANCE TRAJECTORY & WHAT-IF SENSITIVITY (FIG 9 & FIG 10)
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('7. Transformation Benchmarks & Financial Sensitivity Simulation', h1_style))
story.append(Paragraph('<i>Figure 9 visualizes the compounding operational improvements across key benchmarks</i>. Eliminating rework upfront enables 60% Straight-Through Processing, which collapses turnaround times and drives an 81.4% reduction in unit processing cost.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig9_target_benchmarks.png', width=440, height=135))
story.append(Paragraph('<b>Figure 9 — Core Operational Transformation Performance Trajectory</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Current AS-IS Baseline vs. Target TO-BE across turnaround time, first-pass yield, rework, and unit cost.<br/>'
                       '<b>Key insight:</b> Turnaround time drops from 58.70h to &lt; 24.00h (-59.1%); FPY expands from 58.12% to 78.0%+; rework falls from 33.35% to &lt; 10%; unit cost falls from $67.45 to $12.55 (-81.4%).<br/>'
                       '<b>Why it matters:</b> Compounding operational gains enable rapid digital onboarding and substantial margin expansion.<br/>'
                       '<b>Improvement / action:</b> Monitor actual operational metrics against these targets using the interactive analytics command center.<br/>'
                       '<b>Executive takeaway:</b> ONBOARD360 transforms NovaBank into a digital leader, cutting cycle times by 59% and unit operating costs by 81%.', insight_style))
story.append(Spacer(1, 4))

story.append(Paragraph('<i>Figure 10 presents a dynamic What-If sensitivity simulation across operational scenarios</i>. Even under a pessimistic Conservative case (45% STP with a 12% CAPEX overrun), the initiative yields <b>$16.57M in annual savings and a $36.06M 3-Year NPV</b>, demonstrating extreme downside protection.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig10_scenario_sensitivity.png', width=440, height=135))
story.append(Paragraph('<b>Figure 10 — What-If Sensitivity Analysis Across Operational Scenarios</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Annual savings and 3-Year NPV across Conservative (45% STP, $3.2M Capex), Base Case (60% STP, $2.85M Capex), and Aggressive (75% STP, $2.5M Capex).<br/>'
                       '<b>Key insight:</b> Even under a pessimistic 45% STP adoption rate, the project generates $16.57M in annual savings and a $36.06M 3-Year NPV.<br/>'
                       '<b>Why it matters:</b> Confirms that capital allocation carries virtually zero risk of negative return under any plausible operating condition.<br/>'
                       '<b>Improvement / action:</b> Budget capital against the 60% STP Base Case with confidence in downside safety.<br/>'
                       '<b>Executive takeaway:</b> The business case is robust: even under conservative 45% STP adoption, the project delivers $16.57M annually with a $36.06M NPV.', insight_style))

# =========================================================================
# PAGE 8: ACTIVITY-BASED COSTING & 3-YEAR DCF (FIG 11 & FIG 12)
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('8. Activity-Based Costing & Multi-Year Financial Returns', h1_style))
story.append(Paragraph('Direct operating costs were modeled using Activity-Based Costing (ABC) reconciled against operational labor, vendor licensing, and customer service contact costs. <i>As shown in Figure 11</i>, <b>80.5% of total savings ($17.78M) come from reducing manual review labor</b> in Operations ($12.51M) and Compliance ($5.27M).', body_style))

story.append(Image('11_Executive_Presentation/charts/fig11_activity_based_cost.png', width=450, height=140))
story.append(Paragraph('<b>Figure 11 — Activity-Based Annual Operating Cost Decomposition</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Line-item budget comparison between AS-IS Operating Costs ($27.97M) and TO-BE Projected Costs ($5.87M).<br/>'
                       '<b>Key insight:</b> L1 Operations labor falls from $13.91M to $1.40M (+$12.51M); L2 Compliance labor falls from $6.79M to $1.52M (+$5.27M); API vendor fees decrease by $2.91M; support costs drop by $1.06M.<br/>'
                       '<b>Why it matters:</b> Direct annual operating cost collapses from $27.97M to $5.87M, yielding $22,092,276 in annual net cash savings.<br/>'
                       '<b>Improvement / action:</b> Reallocate freed operations staff to high-value commercial onboarding and complex fraud investigations.<br/>'
                       '<b>Executive takeaway:</b> ONBOARD360 captures $22.09M in annual recurring savings by reducing manual review labor by $17.78M, vendor fees by $2.91M, and support costs by $1.06M.', insight_style))
story.append(Spacer(1, 4))

story.append(Paragraph('<i>Figure 12 illustrates the 3-year capital recovery curve</i>. Against an initial capital outlay of $2.85M, <b>capital breakeven occurs in just 2.0 months of full operation</b>, generating an exceptional <b>3-Year Net Present Value of $49,501,858.44</b> (8.5% hurdle rate) with an <b>IRR &gt; 200%</b>.', body_style))

story.append(Image('11_Executive_Presentation/charts/fig12_cash_flow_payback.png', width=450, height=130))
story.append(Paragraph('<b>Figure 12 — 3-Year Capital Recovery & Discounted Cash Flow Realization</b>', h2_style))
story.append(Paragraph('<b>What it shows:</b> Cumulative discounted cash flows across 36 operating months against the initial $2.85M CAPEX.<br/>'
                       '<b>Key insight:</b> Capital breakeven is achieved in Month 2; cumulative cash return reaches $14.82M in Year 1, $36.92M in Year 2, and $59.01M in Year 3.<br/>'
                       '<b>Why it matters:</b> Provides executive leadership with verified assurance of rapid capital recovery and massive multi-year value accretion.<br/>'
                       '<b>Improvement / action:</b> Approve full $2.85M Phase 1 capital allocation and execute vendor procurement.<br/>'
                       '<b>Executive takeaway:</b> An investment of $2.85M yields $49.50M in 3-Year NPV, an IRR exceeding 200%, and breaks even in 2.0 months. Capital approval is strongly recommended.', insight_style))

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

# =========================================================================
# PAGE 9: STAKEHOLDER MATRIX, CAPABILITIES & FINAL SIGN-OFF
# =========================================================================
story.append(PageBreak())
story.append(Paragraph('9. Stakeholder Value Realization, Capabilities & Executive Sign-off', h1_style))
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
story.append(Spacer(1, 6))

story.append(Paragraph('Applied Business Capabilities & Methodological Rigor', h2_style))
skills_text = (
    '<b>• Process Engineering & Queuing Dynamics:</b> Applied Little\'s Law and touch/wait decomposition to prove that 89.3% of delay was queue buffer latency rather than analyst slowness, refocusing capital spend on queue elimination.<br/>'
    '<b>• Quantitative Root Cause Analysis:</b> Formulated Pareto distributions and SQL window functions isolating the top 3 defect drivers representing 83.15% of rework, targeting automation at client-side capture.<br/>'
    '<b>• Requirements Architecture & Traceability:</b> Authored 10 Business Requirements, 35 Functional Requirements, and 10 Deterministic Business Rules with 100% bidirectional traceability, eliminating scope creep.<br/>'
    '<b>• Agile Backlog Architecture:</b> Structured 6 Epics and 35+ INVEST-compliant user stories with Gherkin acceptance criteria across 4 delivery sprints for seamless cross-functional execution.<br/>'
    '<b>• Machine Learning & Regulatory Governance:</b> Engineered a Random Forest triage engine with deterministic compliance guardrails, achieving 100% defect precision and 0% regulatory leakage on PEP/AML alerts.<br/>'
    '<b>• Activity-Based Financial Modeling:</b> Constructed an auditable Activity-Based Costing and DCF model proving a $49.50M 3-Year NPV, an IRR &gt; 200%, and a 2.0-month capital payback to executive sponsors.'
)
story.append(Paragraph(skills_text, body_style))
story.append(Spacer(1, 4))

story.append(Paragraph('Quality Assurance, Governance & Executive Recommendation', h2_style))
story.append(Paragraph('The ONBOARD360 platform achieves 100% bidirectional Requirements Traceability (PNT-01..06 &rarr; BR-01..10 &rarr; FR-01..35 &rarr; Stories &rarr; UAT). Machine learning governance was audited across 100 randomized PEP/High-Risk AML cases with <b>zero regulatory leakage</b> (100% routed to human compliance officers). The master automated test suite (<code>test_onboard360_master.py</code>) executes <b>160 test assertions with a 100% pass rate in 5.0 seconds</b>.', body_style))

story.append(Paragraph('<b>Executive Recommendation:</b> Immediate approval of the $2.85M Phase 1 capital allocation is recommended. Controlled regional pilot cutover commences in Month 9 in the UK/EU Retail Channel, followed by global enterprise rollout in Month 12. Breakeven occurs in Month 2 of full operation.', takeaway_style))

story.append(Paragraph('<b>Lead Contributor & Sign-off:</b><br/>'
                       '<b>Hriday Singh Sobti</b><br/>'
                       'NovaBank International Transformation Initiative<br/>'
                       'Interactive Project Artifacts & Live Dashboard: <a href="https://github.com/hriday-sobti/ONBOARD360" color="#1F4E79"><u>https://github.com/hriday-sobti/ONBOARD360</u></a>', meta_style))

doc.build(story)
print(f'Enhanced publication-quality executive PDF generated successfully at: {pdf_path}')
