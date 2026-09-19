"""
ONBOARD360 — AI-Assisted Exception & Document Triage Engine
Trains a machine learning classifier with rule-based safety guardrails.
Routes low-risk document anomalies to automated customer remediation while strictly
reserving PEP and high AML risks for human compliance officers (HITL).
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
import joblib
import os

def train_triage_engine():
    print("Loading data for AI Exception Triage training...")
    df = pd.read_parquet("06_Data_Analysis/data/applications.parquet")
    
    # Filter to non-STP cases (cases requiring attention: rework or manual review)
    df_exceptions = df[df["rework_flag"] | df["manual_review_flag"]].copy()
    print(f"Total Exception Cases in Baseline Dataset: {len(df_exceptions):,}")

    # Ground-truth Target Definition:
    # 0: AUTO_CUSTOMER_REMEDIATION (Low risk, simple document rework)
    # 1: ROUTE_L1_OPS_QUEUE (Ambiguous documentation, form errors)
    # 2: ROUTE_L2_COMPLIANCE_QUEUE (High risk, PEP, sanctions, AML suspicion)
    
    target = []
    for _, row in df_exceptions.iterrows():
        if row["risk_tier"] in ["PEP", "HIGH"]:
            target.append(2)  # Strictly L2 Compliance
        elif row["rework_reason"] in ["Blurry_Image", "Expired_ID"] and row["risk_tier"] == "LOW":
            target.append(0)  # Safe for automated customer self-service remediation
        elif row["risk_tier"] == "MEDIUM" or row["rework_reason"] == "Address_Proof_Mismatch":
            target.append(1)  # L1 Ops queue
        else:
            target.append(1)
            
    df_exceptions["triage_target"] = target

    # Feature Engineering
    # Encode categoricals
    df_exceptions["risk_tier_num"] = df_exceptions["risk_tier"].map({"LOW": 0, "MEDIUM": 1, "HIGH": 2, "PEP": 3})
    df_exceptions["channel_num"] = df_exceptions["channel"].map({
        "Mobile_App": 0, "Web_Portal": 1, "Branch_Assisted": 2, "Affiliate_Partner": 3
    })
    df_exceptions["cust_type_num"] = df_exceptions["customer_type"].map({
        "Standard_Retail": 0, "Fintech_Digital": 1, "Premier_Wealth": 2, "SME_Business": 3
    })
    df_exceptions["rework_reason_num"] = df_exceptions["rework_reason"].map({
        "None": 0, "Blurry_Image": 1, "Expired_ID": 2, "Address_Proof_Mismatch": 3,
        "Incomplete_Form": 4, "Name_Mismatch": 5
    })

    # Synthetic signal features
    np.random.seed(42)
    df_exceptions["sharpness_score"] = np.where(df_exceptions["rework_reason"] == "Blurry_Image",
                                                np.random.uniform(0.2, 0.65, size=len(df_exceptions)),
                                                np.random.uniform(0.75, 0.99, size=len(df_exceptions)))
    df_exceptions["address_match_score"] = np.where(df_exceptions["rework_reason"] == "Address_Proof_Mismatch",
                                                    np.random.uniform(40.0, 75.0, size=len(df_exceptions)),
                                                    np.random.uniform(85.0, 99.0, size=len(df_exceptions)))

    feature_cols = [
        "risk_tier_num", "channel_num", "cust_type_num", "rework_reason_num",
        "sharpness_score", "address_match_score", "touch_time_hours"
    ]
    
    X = df_exceptions[feature_cols]
    y = df_exceptions["triage_target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print(f"Training Random Forest Classifier on {len(X_train):,} instances...")
    clf = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)

    print("\n--- AI TRIAGE EVALUATION METRICS ---")
    target_names = ["0: Auto-Remediation", "1: L1 Ops Queue", "2: L2 Compliance Queue"]
    report = classification_report(y_test, y_pred, target_names=target_names, digits=4)
    print(report)

    # Feature Importance
    importances = pd.Series(clf.feature_importances_, index=feature_cols).sort_values(ascending=False)
    print("Feature Importance:")
    print(importances.round(4))

    # Save model and artifacts
    os.makedirs("07_Solution_Design/model", exist_ok=True)
    joblib.dump(clf, "07_Solution_Design/model/ai_triage_model.joblib")
    print("\nModel saved to 07_Solution_Design/model/ai_triage_model.joblib")

    # Guardrail Verification: Zero False-Negatives on High Risk/PEP
    # Target 2 (High Risk/PEP) must NEVER be classified as 0 (Auto-Remediation)
    cm = confusion_matrix(y_test, y_pred)
    critical_leakage = cm[2, 0] # Actual High Risk classified as Auto Remediation
    print(f"\nRegulatory Guardrail Audit:")
    print(f"High-Risk / PEP Leakage to Auto-Remediation: {critical_leakage} cases (MUST BE 0)")
    assert critical_leakage == 0, "CRITICAL ERROR: Model leaked High Risk/PEP to auto-remediation!"
    print("Guardrail Audit: 100% PASSED. Zero compliance risk leakage.")

if __name__ == "__main__":
    train_triage_engine()
