-- ============================================================================
-- ONBOARD360 — Master KPI Reporting & Analytical SQL Queries
-- Document ID: SQL-KPI-001
-- Queries utilize CTEs, Window Functions, and Conditional Aggregations
-- ============================================================================

-- Query 1: Executive KPI Scorecard Summary
WITH kpi_base AS (
    SELECT
        COUNT(*) AS total_applications,
        COUNT(CASE WHEN status = 'APPROVED' THEN 1 END) AS approved_apps,
        COUNT(CASE WHEN status = 'ABANDONED' THEN 1 END) AS abandoned_apps,
        COUNT(CASE WHEN status = 'REJECTED' THEN 1 END) AS rejected_apps,
        COUNT(CASE WHEN status = 'APPROVED' AND rework_flag = FALSE THEN 1 END) AS first_pass_approvals,
        COUNT(CASE WHEN rework_flag = TRUE THEN 1 END) AS rework_apps,
        COUNT(CASE WHEN manual_review_flag = TRUE THEN 1 END) AS manual_review_apps,
        COUNT(CASE WHEN sla_breach_flag = TRUE THEN 1 END) AS sla_breaches,
        AVG(total_cycle_time_hours) AS avg_cycle_time_hrs,
        AVG(touch_time_hours) AS avg_touch_time_hrs,
        AVG(wait_time_hours) AS avg_wait_time_hrs,
        PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY total_cycle_time_hours) AS median_cycle_time_hrs,
        PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY total_cycle_time_hours) AS p90_cycle_time_hrs
    FROM applications
)
SELECT
    total_applications,
    ROUND(approved_apps * 100.0 / total_applications, 2) AS approval_rate_pct,
    ROUND(abandoned_apps * 100.0 / total_applications, 2) AS abandonment_rate_pct,
    ROUND(first_pass_approvals * 100.0 / total_applications, 2) AS first_pass_yield_pct,
    ROUND(rework_apps * 100.0 / total_applications, 2) AS rework_rate_pct,
    ROUND(manual_review_apps * 100.0 / total_applications, 2) AS manual_review_rate_pct,
    ROUND(sla_breaches * 100.0 / total_applications, 2) AS sla_breach_rate_pct,
    ROUND(avg_cycle_time_hrs, 2) AS mean_tat_hrs,
    ROUND(median_cycle_time_hrs::numeric, 2) AS median_tat_hrs,
    ROUND(p90_cycle_time_hrs::numeric, 2) AS p90_tat_hrs,
    ROUND(avg_touch_time_hrs, 2) AS avg_touch_hrs,
    ROUND(avg_wait_time_hrs, 2) AS avg_wait_hrs,
    ROUND((avg_touch_time_hrs / avg_cycle_time_hrs) * 100.0, 2) AS process_cycle_efficiency_pce_pct
FROM kpi_base;

-- Query 2: Pareto Distribution of Document Rework Drivers
WITH rework_counts AS (
    SELECT
        rework_reason,
        COUNT(*) AS reason_count
    FROM applications
    WHERE rework_flag = TRUE
    GROUP BY rework_reason
),
rework_pareto AS (
    SELECT
        rework_reason,
        reason_count,
        ROUND(reason_count * 100.0 / SUM(reason_count) OVER(), 2) AS pct_of_rework,
        ROUND(SUM(reason_count) OVER (ORDER BY reason_count DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) * 100.0 
              / SUM(reason_count) OVER(), 2) AS cumulative_pct
    FROM rework_counts
)
SELECT * FROM rework_pareto ORDER BY reason_count DESC;

-- Query 3: Channel Performance & Little's Law WIP Backlog
WITH channel_stats AS (
    SELECT
        channel,
        COUNT(*) AS total_apps,
        ROUND(AVG(total_cycle_time_hours), 2) AS avg_tat_hrs,
        ROUND(AVG(wait_time_hours), 2) AS avg_wait_hrs,
        ROUND(COUNT(CASE WHEN rework_flag = TRUE THEN 1 END) * 100.0 / COUNT(*), 2) AS rework_rate_pct,
        ROUND(COUNT(CASE WHEN status = 'ABANDONED' THEN 1 END) * 100.0 / COUNT(*), 2) AS abandon_rate_pct,
        ROUND(COUNT(CASE WHEN sla_breach_flag = TRUE THEN 1 END) * 100.0 / COUNT(*), 2) AS sla_breach_rate_pct
    FROM applications
    GROUP BY channel
)
SELECT
    channel,
    total_apps,
    rework_rate_pct,
    abandon_rate_pct,
    sla_breach_rate_pct,
    avg_tat_hrs,
    avg_wait_hrs,
    -- Little's Law: L = lambda * W (where lambda is arrival rate per hour = total_apps / 8760 hrs)
    ROUND((total_apps / 8760.0) * avg_tat_hrs, 0) AS estimated_avg_wip_units
FROM channel_stats
ORDER BY total_apps DESC;

-- Query 4: Customer Support Cost Escalation by SLA Breach & Rework
SELECT
    a.sla_breach_flag,
    a.rework_flag,
    COUNT(t.ticket_id) AS total_tickets,
    ROUND(SUM(t.cost_to_serve_usd), 2) AS total_support_cost_usd,
    ROUND(AVG(t.cost_to_serve_usd), 2) AS avg_cost_per_ticket_usd,
    ROUND(AVG(t.resolution_time_mins), 1) AS avg_resolution_mins
FROM applications a
INNER JOIN support_tickets t ON a.application_id = t.application_id
GROUP BY a.sla_breach_flag, a.rework_flag
ORDER BY total_support_cost_usd DESC;
