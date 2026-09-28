"""
ONBOARD360 — Excel Workbooks & PDF Reports Generator
Generates all binary spreadsheet models and formal PDF presentation dossiers mandated by Section 82.
"""

import os
import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_excel_artifacts():
    print("Generating enterprise Excel spreadsheets (.xlsx)...")
    header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
    data_font = Font(name="Arial", size=10)
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )

    def style_sheet(ws, headers, rows):
        ws.append(headers)
        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col_idx)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center")
        
        for r_idx, row in enumerate(rows, start=2):
            ws.append(row)
            for c_idx in range(1, len(row) + 1):
                cell = ws.cell(row=r_idx, column=c_idx)
                cell.font = data_font
                cell.border = thin_border
                if isinstance(cell.value, (int, float)):
                    cell.alignment = Alignment(horizontal="right")
                else:
                    cell.alignment = Alignment(horizontal="left")
        
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = col[0].column_letter
            ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

    # 1. Stakeholder Matrix
    wb_stk = Workbook()
    ws_stk = wb_stk.active
    ws_stk.title = "Stakeholder_Matrix"
    headers_stk = ["Stakeholder Group", "Key Persona", "Interests & Objectives", "Primary Pain Point", "Power", "Interest", "Engagement Strategy"]
    rows_stk = [
        ["Retail Leadership", "Head of Retail", "Volume, revenue, market share", "24.8% abandonment rate", "HIGH", "HIGH", "Manage Closely / Steering Committee"],
        ["Compliance & AML", "Chief Compliance Officer", "Zero audit issues or fines", "Fear of black-box automation", "HIGH", "HIGH", "Manage Closely / Formal Sign-off Gates"],
        ["Banking Operations", "Head of Banking Ops", "Queue backlog, productivity", "46.8% manual review rate", "HIGH", "HIGH", "Manage Closely / Co-design Workbench"],
        ["End Customers", "Retail Applicants", "Sub-15m onboarding", "Repetitive document rework", "LOW", "HIGH", "Keep Informed / Usability Testing"],
        ["Customer Service", "VP Customer Experience", "First-contact resolution", "21.2% support contact rate", "MEDIUM", "HIGH", "Keep Satisfied / Status Updates"],
        ["IT & Engineering", "Chief Technology Officer", "Scalability, low tech debt", "Legacy batch core integrations", "HIGH", "MEDIUM", "Keep Satisfied / Arch Review Board"],
        ["Information Security", "CISO", "Data privacy, encryption", "PII handling in cloud/AI", "HIGH", "MEDIUM", "Meet Requirements / Infosec Sign-off"]
    ]
    style_sheet(ws_stk, headers_stk, rows_stk)
    os.makedirs("02_Stakeholder_Analysis", exist_ok=True)
    wb_stk.save("02_Stakeholder_Analysis/stakeholder_matrix.xlsx")

    # 2. Root Cause Analysis
    wb_rca = Workbook()
    ws_rca = wb_rca.active
    ws_rca.title = "Pareto_Root_Cause"
    headers_rca = ["Failure Mode / Defect", "Annual Count", "% of Rework", "Cumulative %", "Root Cause", "Proposed Solution"]
    rows_rca = [
        ["Blurry / Glare Image", 72994, 42.09, 42.09, "Client camera lacks real-time sharpness check", "Client-side OpenCV Wasm Gating"],
        ["Expired Identification", 39964, 23.04, 65.13, "Portal accepts expired dates without check", "Automated OCR Expiration Validation"],
        ["Address Proof Mismatch", 31249, 18.02, 83.15, "Manual address input typos", "Automated Postal Bureau Prefill"],
        ["Incomplete Form Fields", 20716, 11.94, 95.10, "Complex legacy form design", "Interactive Real-time Validation"],
        ["Name Typo / Mismatch", 8506, 4.90, 100.00, "Rigid exact-string matching", "Jaro-Winkler Fuzzy Matching Engine"]
    ]
    style_sheet(ws_rca, headers_rca, rows_rca)
    os.makedirs("03_Process_Analysis", exist_ok=True)
    wb_rca.save("03_Process_Analysis/root_cause_analysis.xlsx")

    # 3. Requirements Traceability
    wb_rtm = Workbook()
    ws_rtm = wb_rtm.active
    ws_rtm.title = "Traceability_Matrix"
    headers_rtm = ["Pain Point ID", "Business Req (BR)", "Functional Req (FR)", "Business Rule", "User Story", "Solution Component", "UAT Test ID", "Status"]
    rows_rtm = [
        ["PNT-01", "BR-003", "FR-001", "BRULE-001", "US-DOC-01", "Client-side OpenCV WebAssembly", "UAT-01, 02, 03", "PASSED"],
        ["PNT-01", "BR-003", "FR-002", "BRULE-002", "US-DOC-03", "Cloud OCR Parsing Engine", "UAT-04, 05", "PASSED"],
        ["PNT-01", "BR-003", "FR-003", "BRULE-003", "US-CAP-01", "Postal Bureau REST Client", "UAT-06, 23", "PASSED"],
        ["PNT-02", "BR-004", "FR-010", "BRULE-004", "US-KYC-01", "Jaro-Winkler Watchlist Service", "UAT-07, 08, 09, 10", "PASSED"],
        ["PNT-03", "BR-005", "FR-015", "BRULE-007", "US-AI-01", "Random Forest AI Triage Engine", "UAT-11, 12, 13", "PASSED"],
        ["PNT-04", "BR-006", "FR-020", "BRULE-009", "US-CAP-02", "Redis Encrypted Session Cache", "UAT-14, 21, 22", "PASSED"],
        ["PNT-04", "BR-007", "FR-025", "BRULE-008", "US-SYS-03", "Kafka Notification Worker", "UAT-15, 30", "PASSED"],
        ["PNT-05", "BR-009", "FR-009", "BRULE-004", "US-OPS-01", "Unified Analyst Workbench UI", "UAT-19, 20, 29", "PASSED"],
        ["PNT-06", "BR-001", "FR-030", "BRULE-007", "US-SYS-01", "Core Ledger REST API Adapter", "UAT-16, 17, 32", "PASSED"],
        ["GOV", "BR-008", "FR-035", "ISO27001", "US-SYS-05", "PostgreSQL SHA-256 Audit Sink", "UAT-18, 27, 28", "PASSED"]
    ]
    style_sheet(ws_rtm, headers_rtm, rows_rtm)
    os.makedirs("04_Requirements", exist_ok=True)
    wb_rtm.save("04_Requirements/requirements_traceability.xlsx")

    # 4. Product Backlog
    wb_bkl = Workbook()
    ws_bkl = wb_bkl.active
    ws_bkl.title = "Product_Backlog"
    headers_bkl = ["Story ID", "Epic", "User Story Description", "MoSCoW", "Points", "Sprint", "Status"]
    rows_bkl = [
        ["ONB360-101", "EPIC-01", "Address auto-lookup via postal code (US-CAP-01)", "Must Have", 5, "Sprint 1.1", "Closed"],
        ["ONB360-102", "EPIC-02", "Real-time camera blur & glare gating (US-DOC-01)", "Must Have", 8, "Sprint 1.1", "Closed"],
        ["ONB360-103", "EPIC-02", "Automated OCR extraction & prefill (US-DOC-02)", "Must Have", 8, "Sprint 1.1", "Closed"],
        ["ONB360-104", "EPIC-02", "OCR expiration date validation (US-DOC-03)", "Must Have", 5, "Sprint 1.1", "Closed"],
        ["ONB360-201", "EPIC-03", "Fuzzy Jaro-Winkler sanctions screening (US-KYC-01)", "Must Have", 8, "Sprint 1.2", "Closed"],
        ["ONB360-202", "EPIC-03", "Phonetic double-metaphone name matching (US-KYC-02)", "Must Have", 5, "Sprint 1.2", "Closed"],
        ["ONB360-203", "EPIC-03", "PEP automated identification & L2 hold (US-KYC-03)", "Must Have", 8, "Sprint 1.2", "Closed"],
        ["ONB360-204", "EPIC-06", "Real-time core account provisioning API (US-SYS-01)", "Must Have", 8, "Sprint 1.2", "Closed"],
        ["ONB360-301", "EPIC-04", "Random Forest exception classifier (US-AI-01)", "Must Have", 13, "Sprint 1.3", "Closed"],
        ["ONB360-302", "EPIC-04", "WhatsApp 1-click camera remediation (US-AI-02)", "Must Have", 8, "Sprint 1.3", "Closed"],
        ["ONB360-401", "EPIC-05", "Unified Analyst single-pane workbench (US-OPS-01)", "Must Have", 8, "Sprint 1.4", "Closed"]
    ]
    style_sheet(ws_bkl, headers_bkl, rows_bkl)
    os.makedirs("05_Agile", exist_ok=True)
    wb_bkl.save("05_Agile/product_backlog.xlsx")
    wb_bkl.save("05_Agile/user_stories.xlsx")
    wb_bkl.save("05_Agile/sprint_plan.xlsx")

    # 5. UAT Results Matrix
    wb_uat = Workbook()
    ws_uat = wb_uat.active
    ws_uat.title = "UAT_Results"
    headers_uat = ["Test ID", "Requirement ID", "Scenario Description", "Preconditions", "Expected Result", "Actual Result", "Status", "Execution Date"]
    rows_uat = [
        ["UAT-01", "FR-001", "Positive: Clean mobile camera auto-snap", "Valid UK driving license", "Sharpness >= 150; auto-snaps < 1.5s", "Auto-snapped in 1.2s; sharpness = 182", "PASS", "2026-09-19"],
        ["UAT-02", "FR-001", "Negative: Blurry camera capture blocked", "Deliberate device motion", "Red warning overlay; submit disabled", "Red warning displayed; upload blocked", "PASS", "2026-09-19"],
        ["UAT-04", "FR-002", "Exception: Expired passport validation", "Passport expired May 2024", "Instant modal: Expired document", "Modal displayed in 650ms; blocked", "PASS", "2026-09-19"],
        ["UAT-07", "FR-010", "Positive: Low-risk STP automated clearance", "Clean applicant, Low Risk", "Screening clears; account created < 15m", "Account created in 4.2s; 0 human touch", "PASS", "2026-09-19"],
        ["UAT-10", "FR-010", "Regulatory: Politically Exposed Person hold", "Applicant is sitting MP", "Strictly prohibits STP; assigns L2 queue", "Case routed to L2 queue; 4h SLA set", "PASS", "2026-09-19"],
        ["UAT-11", "FR-015", "AI Triage: Blurry ID auto-remediation", "Low-risk retail, blurry bill", "AI class 0; WhatsApp link sent < 10s", "WhatsApp link dispatched in 6.4s", "PASS", "2026-09-19"],
        ["UAT-16", "FR-030", "Positive: Real-time Core API provisioning", "Approved payload to REST API", "Account created in < 1,500ms", "Account & IBAN returned in 1,240ms", "PASS", "2026-09-19"],
        ["UAT-18", "FR-035", "Positive: Cryptographic audit log creation", "Compliance decision event", "SHA-256 hash appended to audit table", "Hash block verified; tamper-evident", "PASS", "2026-09-19"]
    ]
    style_sheet(ws_uat, headers_uat, rows_uat)
    os.makedirs("09_UAT", exist_ok=True)
    wb_uat.save("09_UAT/test_plan.xlsx")
    wb_uat.save("09_UAT/UAT_results.xlsx")

    # 6. Financial ROI Model
    wb_roi = Workbook()
    ws_roi = wb_roi.active
    ws_roi.title = "Cost_Benefit_Model"
    headers_roi = ["Cost / Benefit Category", "AS-IS Annual Baseline ($)", "TO-BE Projected ($)", "Annual Variance ($)", "% Variance", "Key Drivers"]
    rows_roi = [
        ["L1 Operations Labor", 13910400.00, 1397760.00, 12512640.00, -89.95, "60% STP + Client-side CV eliminates 80% doc queues"],
        ["L2 Compliance Labor", 6789055.00, 1521000.00, 5268055.00, -77.60, "Fuzzy Jaro-Winkler screening eliminates false positives"],
        ["Customer Service Contacts", 1408658.00, 352164.50, 1056493.50, -75.00, "Proactive stage notifications eliminate status calls"],
        ["Identity Vendor APIs", 5096000.00, 2184000.00, 2912000.00, -57.14, "Modern bundled API pricing replaces legacy fees"],
        ["Manual Mailing / Admin", 763087.60, 0.00, 763087.60, -100.00, "100% digital self-service remediation via WhatsApp"],
        ["Cloud & AI SaaS OPEX", 0.00, 420000.00, -420000.00, 100.00, "Kafka, Cloud microservices & model monitoring"],
        ["TOTAL ANNUAL OPEX", 27967200.60, 5874924.50, 22092276.10, -78.99, "Massive operating margin expansion"],
        ["Initial Capital Investment", 2850000.00, 0.00, 0.00, 0.00, "CAPEX amortized over 3-year transformation horizon"],
        ["3-Year Net Present Value (NPV)", 49501858.44, 0.00, 0.00, 0.00, "Discount rate = 8.5% hurdle rate"],
        ["Internal Rate of Return (IRR)", 2.00, 0.00, 0.00, 0.00, "> 200.0% capital return rate"],
        ["Capital Payback Period", 2.0, 0.00, 0.00, 0.00, "2.0 Months to break even on capital spend"]
    ]
    style_sheet(ws_roi, headers_roi, rows_roi)
    os.makedirs("10_Business_Case", exist_ok=True)
    wb_roi.save("10_Business_Case/ROI_model.xlsx")
    print("All enterprise Excel workbooks created successfully.")

def create_pdf_artifacts():
    print("Generating formal executive PDF reports (.pdf)...")
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1F4E79'),
        spaceAfter=15
    )
    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2E75B6'),
        spaceBefore=12,
        spaceAfter=8
    )
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10
    )

    def generate_pdf(path, title, sections):
        doc = SimpleDocTemplate(path, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
        story = [Paragraph(title, title_style), Spacer(1, 10)]
        for h, text in sections:
            if h:
                story.append(Paragraph(h, h2_style))
            story.append(Paragraph(text, body_style))
        doc.build(story)

    # 1. Problem Statement PDF
    generate_pdf(
        "01_Business_Case/problem_statement.pdf",
        "ONBOARD360 — Operational Problem Statement & Business Case",
        [
            ("1. Operational Friction & Context", "NovaBank International processes 520,000 onboarding applications annually across UK/EU, US, APAC, and LatAm. The current onboarding lifecycle takes an average of 58.70 hours from application submission to account funding, with 89.3% (52.42 hours) consumed by idle queue buffers between disconnected departments."),
            ("2. The Rework & Defect Crisis", "First-pass yield stands at only 58.12%, forcing 33.35% (173,429 applications) into manual rework loops. Blurry images (42.1%) and expired identification (23.0%) drive over 65% of all rework cases. Customer drop-off reaches 16.25%, with 82.8% of inbound support inquiries being 'Where is my account?' status calls."),
            ("3. Financial & Strategic Impact", "Direct operating expenses exceed $27.96M annually ($67.45 per completed account). The ONBOARD360 initiative modernizes this architecture via client-side computer vision, fuzzy watchlist screening, and AI exception triage to compress cycle times under 24 hours and deliver $22.09M in annual recurring savings.")
        ]
    )

    # 2. Pain Point Analysis PDF
    generate_pdf(
        "03_Process_Analysis/pain_point_analysis.pdf",
        "ONBOARD360 — AS-IS Pain Point & Bottleneck Analysis",
        [
            ("1. Queue Buffer Congestion (Little's Law)", "Applying Little's Law (L = lambda * W) to the 520,000 annual application volume reveals an ongoing work-in-progress (WIP) of 3,485 active applications, with 3,111 applications queued idly in operations backlogs at any given moment."),
            ("2. Upstream Document Quality Failures", "Legacy mobile and web portals accept raw photos without evaluating focus, blur, or glare. Illegible uploads pass directly into manual L1 review queues, consuming 1.8 hours of analyst touch time per case and creating massive downstream bottlenecks."),
            ("3. Root Cause Isolation (Pareto Principle)", "Pareto analysis demonstrates that 83.2% of all rework volume is driven by three preventable flaws: Blurry Images (42.1%), Expired IDs (23.0%), and Address Mismatches (18.0%). Upstream client-side validation eliminates over 70% of rework volume.")
        ]
    )

    # 3. BRD PDF
    generate_pdf(
        "04_Requirements/BRD.pdf",
        "ONBOARD360 — Business Requirements Document (BRD)",
        [
            ("1. Purpose & Strategic Scope", "This document establishes the formal business requirements for the ONBOARD360 Transformation Platform at NovaBank International. The platform targets 60% Straight-Through Processing (STP) for digital retail accounts and an end-to-end cycle time under 24 hours."),
            ("2. Core Business Requirements", "BR-001 (Sub-24h Cycle Time), BR-002 (60% STP Enablement), BR-003 (Upfront Document Defect Elimination), BR-004 (Fuzzy Watchlist Screening), BR-005 (AI-Assisted Exception Triage), BR-006 (Omnichannel Session Continuity), BR-007 (Proactive Stage Notifications), BR-008 (Cryptographic Audit Logging), BR-009 (Unified Analyst Workbench), BR-010 (Unit Cost Reduction to $12.55)."),
            ("3. Acceptance Criteria & Governance", "All functional components must achieve 100% bidirectional traceability against the Requirements Traceability Matrix and pass formal UAT sign-off from Retail, Compliance, and Operations leadership.")
        ]
    )

    # 4. FRD PDF
    generate_pdf(
        "04_Requirements/FRD.pdf",
        "ONBOARD360 — Functional Requirements Document (FRD)",
        [
            ("1. System Functional Specifications", "Specifies the technical behaviors, API contracts, and validation algorithms: FR-001 (OpenCV WebAssembly image sharpness gating), FR-002 (Cloud OCR expiration parsing), FR-003 (Postal bureau prefill API), FR-010 (Jaro-Winkler sanctions matching), FR-015 (Random Forest exception classification), FR-020 (Redis session persistence), FR-025 (Kafka event notification dispatcher), FR-030 (Core ledger REST provisioning API), FR-035 (Immutable cryptographic audit sink)."),
            ("2. Non-Functional & Security Requirements", "Sub-1,500ms p95 API response latency under 150 TPS load; AES-256 encryption at rest; TLS 1.3 in transit; strict Role-Based Access Control (RBAC); 99.95% high availability SLA.")
        ]
    )

    # 5. Solution Architecture PDF
    generate_pdf(
        "07_Solution_Design/solution_architecture.pdf",
        "ONBOARD360 — Target Solution Architecture & Systems Blueprint",
        [
            ("1. Architectural Paradigm", "An event-driven microservices architecture built on Apache Kafka, containerized Python/FastAPI services, PostgreSQL 15 relational master storage, and Redis session caching."),
            ("2. Machine Learning & Human-in-the-Loop Governance", "The AI Exception Triage Engine scores and routes non-STP cases. Low-risk document defects are routed to automated WhatsApp self-service, while High-Risk, PEP, and sanctions alerts are strictly quarantined for human compliance review, ensuring 0% regulatory leakage."),
            ("3. Enterprise Integration Tier", "Synchronous REST adapters interface with legacy core banking ledgers for real-time IBAN provisioning and instant Apple Wallet card tokenization.")
        ]
    )

    # 6. Executive Presentation Review PDF (Rich Publication-Quality Version)
    def generate_rich_executive_review():
        pdf_path = "11_Executive_Presentation/ONBOARD360_Executive_Review.pdf"
        doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
        primary_color = colors.HexColor('#1F4E79')
        text_dark = colors.HexColor('#2C3E50')
        
        t_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=primary_color, spaceAfter=6)
        sub_style = ParagraphStyle('DocSubTitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#555555'), spaceAfter=12)
        s_h1 = ParagraphStyle('SectionH1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=primary_color, spaceBefore=10, spaceAfter=6, keepWithNext=True)
        b_style = ParagraphStyle('DocBody', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=text_dark, spaceAfter=6)
        c_style = ParagraphStyle('Callout', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8, leading=11, textColor=colors.HexColor('#1A365D'), backColor=colors.HexColor('#EDF2F7'), borderColor=colors.HexColor('#2E75B6'), borderWidth=1, borderPadding=6, spaceAfter=8)
        th_style = ParagraphStyle('TableHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.white, alignment=1)
        tc_style = ParagraphStyle('TableCell', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=text_dark)
        tcb_style = ParagraphStyle('TableCellBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=primary_color)

        story = [
            Paragraph('ONBOARD360 — Customer Onboarding & KYC Process Modernization', t_style),
            Paragraph('<b>Executive Report & Transformation Blueprint</b> | Lead Contributor: Hriday Singh Sobti (Senior Business Analyst & Solution Architect) | NovaBank International', sub_style),
            Spacer(1, 4),
            Paragraph('1. Executive Summary: The Strategic Mandate', s_h1),
            Paragraph('NovaBank International processes <b>520,000 onboarding applications annually</b> across UK/EU, North America, APAC, and Latin America. The legacy journey suffered from an average cycle time of <b>58.70 hours</b>, driven by an <b>89.3% idle queue wait delay (52.42 hours)</b>. A <b>33.35% rework defect rate</b> directly precipitated a <b>16.25% customer abandonment rate</b> and inflated unit processing costs to <b>$67.45 per completed account</b> ($27.97M annual direct operating cost).', b_style),
            Paragraph('<b>The ONBOARD360 Transformation Initiative</b> modernizes this fragmented journey into an intelligent, event-driven orchestration ecosystem. By coupling real-time computer vision document gating with automated fuzzy watchlist screening and AI-assisted exception triage, ONBOARD360 compresses average cycle times to <b>&lt; 24.0 hours</b> (&lt; 15 minutes for 60% straight-through processing), reduces unit processing costs to <b>$12.55</b> (-81.4%), and generates <b>$22,092,276 in annual net recurring cash savings</b> on an initial <b>$2.85M investment</b>, delivering a <b>3-Year NPV of $49.50M</b> (8.5% hurdle rate), an <b>IRR &gt; 200%</b>, and a <b>2.0-month payback period</b>.', b_style)
        ]
        scorecard_data = [
            [Paragraph('<b>Operational Metric</b>', th_style), Paragraph('<b>AS-IS Baseline</b>', th_style), Paragraph('<b>TO-BE Target</b>', th_style), Paragraph('<b>Net Variance</b>', th_style), Paragraph('<b>Classification</b>', th_style)],
            [Paragraph('Average Turnaround Time (TAT)', tcb_style), Paragraph('58.70 Hours', tc_style), Paragraph('&lt; 24.0 Hours (&lt;15m STP)', tc_style), Paragraph('-59.1% Lead Time', tc_style), Paragraph('Projected', tc_style)],
            [Paragraph('Idle Queue Wait Time Ratio', tcb_style), Paragraph('89.29% (52.42h)', tc_style), Paragraph('&lt; 25.00% (5.00h)', tc_style), Paragraph('-90.5% Queue Drop', tc_style), Paragraph('Projected', tc_style)],
            [Paragraph('Straight-Through Processing (STP)', tcb_style), Paragraph('0.0% (Batch)', tc_style), Paragraph('60.0% (Automated)', tc_style), Paragraph('+60.0 pts Automation', tc_style), Paragraph('Projected', tc_style)],
            [Paragraph('First-Pass Yield (FPY)', tcb_style), Paragraph('58.12% (302K)', tc_style), Paragraph('&ge; 78.00% (405K)', tc_style), Paragraph('+19.9 pts Yield Gain', tc_style), Paragraph('Projected', tc_style)],
            [Paragraph('Application Rework Rate', tcb_style), Paragraph('33.35% (173K)', tc_style), Paragraph('&le; 10.00% (52K)', tc_style), Paragraph('-70.0% Defect Cut', tc_style), Paragraph('Projected', tc_style)],
            [Paragraph('Customer Abandonment Rate', tcb_style), Paragraph('16.25% (84.5K)', tc_style), Paragraph('&le; 7.50% (39.0K)', tc_style), Paragraph('-53.8% Churn Cut', tc_style), Paragraph('Projected', tc_style)],
            [Paragraph('Direct Operating Unit Cost', tcb_style), Paragraph('$67.45 / Account', tc_style), Paragraph('$12.55 / Account', tc_style), Paragraph('-$54.90 / Account (-81.4%)', tc_style), Paragraph('Modelled', tc_style)],
            [Paragraph('Annual Direct Operating OPEX', tcb_style), Paragraph('$27,967,200.60', tc_style), Paragraph('$5,874,924.50', tc_style), Paragraph('+$22,092,276.10 Savings', tc_style), Paragraph('Modelled', tc_style)]
        ]
        t_sc = Table(scorecard_data, colWidths=[150, 95, 110, 110, 65])
        t_sc.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), primary_color),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D9D9D9')),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')])
        ]))
        story.extend([t_sc, Spacer(1, 10)])
        story.append(Paragraph('2. Key Findings & Pareto Defect Analysis (Figures 1-8)', s_h1))
        story.append(Paragraph('Empirical process mining proved that <b>89.3% of turnaround time was idle queue wait time (52.42 hours)</b>, with active analyst touch time accounting for only 6.29 hours (PCE = 10.71%). Furthermore, <b>83.15% of all rework loops were driven by three preventable upload flaws</b>: Blurry Images (42.09%), Expired IDs (23.04%), and Address Typos (18.02%).', b_style))
        pareto_data = [
            [Paragraph('<b>Defect Failure Mode</b>', th_style), Paragraph('<b>Annual Count</b>', th_style), Paragraph('<b>% Rework</b>', th_style), Paragraph('<b>Cum %</b>', th_style), Paragraph('<b>Root Cause & Architectural Remedy</b>', th_style)],
            [Paragraph('Blurry / Glare Image', tcb_style), Paragraph('72,994', tc_style), Paragraph('42.09%', tc_style), Paragraph('42.09%', tc_style), Paragraph('Client-side OpenCV WebAssembly real-time sharpness gating (FR-001)', tc_style)],
            [Paragraph('Expired Identification', tcb_style), Paragraph('39,964', tc_style), Paragraph('23.04%', tc_style), Paragraph('65.13%', tc_style), Paragraph('Automated Cloud OCR MRZ date expiration validation within 650ms (FR-002)', tc_style)],
            [Paragraph('Address Proof Mismatch', tcb_style), Paragraph('31,249', tc_style), Paragraph('18.02%', tc_style), Paragraph('83.15%', tc_style), Paragraph('Postal code REST bureau address lookup and prefill (FR-003)', tc_style)],
            [Paragraph('Incomplete Form Fields', tcb_style), Paragraph('20,716', tc_style), Paragraph('11.94%', tc_style), Paragraph('95.10%', tc_style), Paragraph('Interactive form validation and Redis cross-device session cache (FR-020)', tc_style)],
            [Paragraph('Name Typo / Mismatch', tcb_style), Paragraph('8,506', tc_style), Paragraph('4.90%', tc_style), Paragraph('100.00%', tc_style), Paragraph('Jaro-Winkler phonetic double-metaphone fuzzy sanctions matching (FR-010)', tc_style)]
        ]
        t_pt = Table(pareto_data, colWidths=[120, 65, 55, 50, 240])
        t_pt.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), primary_color),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D9D9D9')),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')])
        ]))
        story.extend([t_pt, Spacer(1, 10)])
        story.append(Paragraph('3. Financial Appraisal & Value Realization (Figures 11 & 12)', s_h1))
        story.append(Paragraph('Direct operating costs were modeled using Activity-Based Costing (ABC) and discounted cash flows (8.5% hurdle rate). Operations labor falls by $12.51M, compliance labor by $5.27M, support costs by $1.06M, and vendor fees by $2.91M, generating <b>$22,092,276.10 in net annual recurring cash savings</b> on an initial <b>$2.85M investment</b> (3-Year NPV $49.50M, IRR &gt; 200%, payback 2.0 months).', b_style))
        fin_data = [
            [Paragraph('<b>Financial Metric</b>', th_style), Paragraph('<b>Value</b>', th_style), Paragraph('<b>Financial Metric</b>', th_style), Paragraph('<b>Value</b>', th_style)],
            [Paragraph('Initial Capital Investment (CAPEX)', tcb_style), Paragraph('$2,850,000.00', tc_style), Paragraph('Annual Net Recurring Cash Savings', tcb_style), Paragraph('$22,092,276.10', tc_style)],
            [Paragraph('Hurdle Discount Rate', tcb_style), Paragraph('8.50%', tc_style), Paragraph('Year 1 Cash Inflow (80% realization)', tcb_style), Paragraph('$17,673,820.88', tc_style)],
            [Paragraph('3-Year Net Present Value (NPV)', tcb_style), Paragraph('<b>$49,501,858.44</b>', tc_style), Paragraph('Capital Payback Period', tcb_style), Paragraph('<b>2.0 Months</b>', tc_style)],
            [Paragraph('Internal Rate of Return (IRR)', tcb_style), Paragraph('<b>&gt; 200.0%</b>', tc_style), Paragraph('Conservative Scenario NPV (45% STP)', tcb_style), Paragraph('$36,063,893.83', tc_style)]
        ]
        t_fin = Table(fin_data, colWidths=[150, 115, 150, 115])
        t_fin.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), primary_color),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D9D9D9')),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')])
        ]))
        story.extend([t_fin, Spacer(1, 10)])
        story.append(Paragraph('4. Quality Assurance, Governance & Board Recommendation', s_h1))
        story.append(Paragraph('Achieved 100% bidirectional traceability (PNT-01..06 &rarr; BR-01..10 &rarr; FR-01..35 &rarr; Stories &rarr; UAT). Machine learning governance audited with <b>zero regulatory leakage</b> across 100 PEP/AML cases. Master automated test suite executes <b>160 test assertions with 100% pass rate in 5.0s</b>.', b_style))
        story.append(Paragraph('<b>Executive Recommendation:</b> Immediate approval of the $2.85M Phase 1 capital allocation is recommended. Controlled regional pilot cutover commences Month 9 in UK/EU Retail Channel, followed by global rollout in Month 12.', c_style))
        doc.build(story)
    generate_rich_executive_review()
    print("All formal executive PDF reports generated successfully.")

if __name__ == "__main__":
    create_excel_artifacts()
    create_pdf_artifacts()
