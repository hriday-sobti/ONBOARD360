-- ============================================================================
-- ONBOARD360 — PostgreSQL DDL Schema & Relational Tables
-- Document ID: SQL-DDL-001
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS onboard360;
SET search_path TO onboard360, public;

-- 1. Customers Master Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(36) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    customer_type VARCHAR(20) NOT NULL CHECK (customer_type IN ('Standard_Retail', 'Premier_Wealth', 'SME_Business', 'Fintech_Digital')),
    country VARCHAR(3) NOT NULL,
    region VARCHAR(10) NOT NULL CHECK (region IN ('UK_EU', 'US', 'APAC', 'LATAM')),
    risk_category VARCHAR(10) NOT NULL CHECK (risk_category IN ('LOW', 'MEDIUM', 'HIGH', 'PEP')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- 2. Applications Core Transaction Fact Table
CREATE TABLE IF NOT EXISTS applications (
    application_id VARCHAR(36) PRIMARY KEY,
    customer_id VARCHAR(36) NOT NULL REFERENCES customers(customer_id) ON DELETE RESTRICT,
    application_date TIMESTAMP WITH TIME ZONE NOT NULL,
    channel VARCHAR(20) NOT NULL CHECK (channel IN ('Mobile_App', 'Web_Portal', 'Branch_Assisted', 'Affiliate_Partner')),
    product_type VARCHAR(25) NOT NULL CHECK (product_type IN ('Checking_Standard', 'Premier_Checking', 'Savings_HighYield', 'SME_Operating_Account')),
    status VARCHAR(20) NOT NULL CHECK (status IN ('APPROVED', 'REJECTED', 'ABANDONED', 'PENDING_REVIEW')),
    risk_tier VARCHAR(10) NOT NULL CHECK (risk_tier IN ('LOW', 'MEDIUM', 'HIGH', 'PEP')),
    rework_flag BOOLEAN NOT NULL DEFAULT FALSE,
    rework_reason VARCHAR(50) NOT NULL DEFAULT 'None',
    manual_review_flag BOOLEAN NOT NULL DEFAULT FALSE,
    review_team VARCHAR(25) NOT NULL DEFAULT 'None',
    touch_time_hours NUMERIC(6, 2) NOT NULL CHECK (touch_time_hours >= 0),
    wait_time_hours NUMERIC(6, 2) NOT NULL CHECK (wait_time_hours >= 0),
    total_cycle_time_hours NUMERIC(6, 2) NOT NULL CHECK (total_cycle_time_hours >= 0),
    sla_breach_flag BOOLEAN NOT NULL DEFAULT FALSE,
    has_support_ticket BOOLEAN NOT NULL DEFAULT FALSE
);

-- 3. Manual Reviews Table
CREATE TABLE IF NOT EXISTS manual_reviews (
    review_id VARCHAR(36) PRIMARY KEY,
    application_id VARCHAR(36) NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    queue_name VARCHAR(30) NOT NULL,
    analyst_id VARCHAR(20) NOT NULL,
    duration_minutes NUMERIC(6, 1) NOT NULL CHECK (duration_minutes >= 0),
    decision VARCHAR(25) NOT NULL CHECK (decision IN ('APPROVE', 'REJECT', 'REQUEST_REWORK', 'ESCALATE_L2'))
);

-- 4. Support Tickets Table
CREATE TABLE IF NOT EXISTS support_tickets (
    ticket_id VARCHAR(36) PRIMARY KEY,
    application_id VARCHAR(36) NOT NULL REFERENCES applications(application_id) ON DELETE CASCADE,
    channel VARCHAR(15) NOT NULL CHECK (channel IN ('In_App_Chat', 'Phone_IVR', 'Email_Helpdesk')),
    issue_category VARCHAR(35) NOT NULL,
    resolution_time_mins INTEGER NOT NULL CHECK (resolution_time_mins >= 0),
    cost_to_serve_usd NUMERIC(6, 2) NOT NULL CHECK (cost_to_serve_usd >= 0)
);

-- Indexes for Analytical Performance
CREATE INDEX IF NOT EXISTS idx_apps_date ON applications(application_date);
CREATE INDEX IF NOT EXISTS idx_apps_status ON applications(status);
CREATE INDEX IF NOT EXISTS idx_apps_channel ON applications(channel);
CREATE INDEX IF NOT EXISTS idx_apps_region_tier ON applications(risk_tier, manual_review_flag);
CREATE INDEX IF NOT EXISTS idx_rev_app_id ON manual_reviews(application_id);
CREATE INDEX IF NOT EXISTS idx_tck_app_id ON support_tickets(application_id);
