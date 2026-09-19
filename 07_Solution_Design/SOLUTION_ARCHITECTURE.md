# ONBOARD360 — Technical Solution Architecture & Systems Blueprint
**Document ID:** SOL-ARC-001  
**Version:** 1.0.0 (Baselined)  

---

## 1. Enterprise System Component Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      OMNICHANNEL PRESENTATION TIER                          │
│  ┌─────────────────────────┐  ┌────────────────────────┐  ┌──────────────┐  │
│  │ Mobile App (iOS/Android)│  │ Customer Web Portal    │  │ Branch Portal│  │
│  │ • Client-side OpenCV    │  │ • WebAssembly Vision   │  │ • Assisted   │  │
│  │ • Real-time frame guide │  │ • Guided form autofill │  │   onboarding │  │
│  └────────────┬────────────┘  └───────────┬────────────┘  └──────┬───────┘  │
└───────────────┼───────────────────────────┼──────────────────────┼──────────┘
                │                           │                      │
                ▼                           ▼                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 ENTERPRISE API GATEWAY & SECURITY PERIMETER                 │
│  • TLS 1.3 / mTLS  • OAuth2 / JWT Auth  • Rate Limiting  • WAF & DDoS Shield│
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MICROSERVICES & ORCHESTRATION TIER                       │
│  ┌────────────────────────┐  ┌───────────────────────┐  ┌────────────────┐  │
│  │ Workflow Orchestrator  │  │ Automated KYC/AML     │  │ AI Exception   │  │
│  │ • Temporal / Camunda   │  │ • Jaro-Winkler Fuzzy  │  │   Triage Svc   │  │
│  │ • State Machine Engine │  │ • Bureau REST Client  │  │ • Scikit-Learn │  │
│  └────────────┬───────────┘  └───────────┬───────────┘  └───────┬────────┘  │
│               │                          │                      │           │
│               └──────────────────────────┼──────────────────────┘           │
│                                          ▼                                  │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ Event Streaming Backbone: Apache Kafka (Topics: app-events, kyc-alerts)│  │
│  └───────────────────────────────────────┬───────────────────────────────┘  │
└──────────────────────────────────────────┼──────────────────────────────────┘
                                           │
             ┌─────────────────────────────┴─────────────────────────────┐
             ▼                                                           ▼
┌───────────────────────────┐                               ┌───────────────────────────┐
│     DATA & AUDIT TIER     │                               │   LEGACY CORE BANKING     │
│ • PostgreSQL 15 (Master)  │                               │ • Mainframe Core Ledger   │
│ • Parquet / S3 Data Lake  │                               │ • Card Management System  │
│ • Immutable Audit Log Sink│                               │ • REST / ISO 20022 Adapter│
└───────────────────────────┘                               └───────────────────────────┘
```

---

## 2. Key Interface & API Contracts

### A. Document Verification Endpoint (`POST /api/v1/documents/verify`)
* **Request**: Multipart payload with document image, customer UUID, and document type.
* **Processing**: Server-side OCR + MRZ parsing + Tamper detection.
* **Response**: `200 OK` with extracted text, expiration date, confidence score, and verification disposition.

### B. AI Exception Triage Endpoint (`POST /api/v1/triage/classify`)
* **Request**: JSON payload containing application features:
  ```json
  {
    "application_id": "APP-1004521",
    "customer_type": "Standard_Retail",
    "risk_tier": "LOW",
    "channel": "Mobile_App",
    "image_sharpness_score": 0.62,
    "glare_ratio": 0.09,
    "rework_reason": "Blurry_Image",
    "address_match_score": 92.0
  }
  ```
* **Response**: `200 OK` with classification and routing instructions:
  ```json
  {
    "recommended_action": "AUTO_CUSTOMER_REMEDIATION",
    "confidence_score": 0.942,
    "target_queue": "Customer_Self_Service_WhatsApp",
    "rationale": "High confidence low-risk blurry image. Auto-remediation link dispatched.",
    "human_review_mandated": false
  }
  ```
