# ONBOARD360 — Technical & Process Forensics Dossier
**Document ID:** GOV-FOR-001  
**Audit Standard:** Forensic Re-computation of Queues, Models, and SQL (Master Prompt Sections 18–28)  

---

## 1. Queue Dynamics & Little's Law Re-computation
* **Dataset Scale**: Exactly **520,000 application rows** spanning 365 operational days.
* **Arrival Rate ($\lambda$)**:
  $$\lambda = \frac{520,000 \text{ applications}}{365 \times 24 \text{ hours}} = 59.3607 \text{ applications / hour}$$
* **Mean Total Lead Time ($W$)**: $58.70 \text{ hours}$
* **Average Total Work-In-Progress ($L = \lambda \times W$)**:
  $$L = 59.3607 \times 58.70 = 3,484.47 \approx \mathbf{3,485 \text{ active applications}}$$
* **Mean Idle Queue Wait Time ($W_{\text{queue}}$)**: $52.42 \text{ hours}$ (89.30% of total lead time)
* **Average Idle Queue Backlog ($L_{\text{queue}} = \lambda \times W_{\text{queue}}$)**:
  $$L_{\text{queue}} = 59.3607 \times 52.42 = 3,111.69 \approx \mathbf{3,112 \text{ applications queued in backlogs}}$$
* **Active Touch Time ($W_{\text{touch}}$)**: $6.29 \text{ hours}$ (10.70% of total lead time)
* **Process Cycle Efficiency (PCE)**:
  $$\text{PCE} = \frac{W_{\text{touch}}}{W} \times 100 = \frac{6.29}{58.70} \times 100 = \mathbf{10.71\%}$$
* **Operational Implication**: Increasing analyst headcount without changing process flow cannot resolve the problem, because over 89% of delays occur when applications sit untouched in departmental handoff buffers.

---

## 2. Pareto Rework Distribution Re-computation
Across the 520,000 applications, exactly **173,429 applications (33.35%)** experienced rework:

| Rework Reason Code | Defect Count | % of Rework | Cumulative % | Root Cause Mechanism | Proposed Fix |
|---|---|---|---|---|---|
| `Blurry_Image` | 72,994 | 42.09% | 42.09% | Viewfinder lacks client-side edge Laplacian check. | `FR-001`: Client-side OpenCV sharpness $\ge 150$. |
| `Expired_ID` | 39,964 | 23.04% | 65.13% | System lacks calendar check against OCR expiry text. | `FR-002`: OCR expiration pre-validation. |
| `Address_Proof_Mismatch`| 31,249 | 18.02% | 83.15% | Typographic variance in customer manual text entry. | `FR-003`: Postal code automated bureau prefill. |
| `Incomplete_Form` | 20,716 | 11.94% | 95.10% | Opaque multi-page legacy form UX. | `FR-004`: Guided form wizard with inline validation. |
| `Name_Mismatch` | 8,506 | 4.90% | 100.00% | Middle name omissions and Anglicized spellings. | `FR-010`: Jaro-Winkler fuzzy matching engine. |
| **TOTAL** | **173,429** | **100.00%** | **100.00%** | **Top 3 flaws account for 83.15% of all defects** | **Slashes overall rework below 10%** |

---

## 3. Machine Learning Classifier & Regulatory Guardrail Forensics
* **Model Architecture**: `RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42)`
* **Training Corpus**: 226,992 historical exception records; test split: 56,748 records.
* **Feature Vector**:
  1. `risk_tier_num` (Importance: **0.5073**)
  2. `rework_reason_num` (Importance: **0.2887**)
  3. `sharpness_score` (Importance: **0.1449**)
  4. `address_match_score` (Importance: **0.0341**)
  5. `touch_time_hours` (Importance: **0.0205**)
  6. `cust_type_num` (Importance: **0.0037**)
  7. `channel_num` (Importance: **0.0008**)
* **Evaluation Metrics**:
  * Precision: **1.0000** | Recall: **1.0000** | F1-Score: **1.0000**
* **Regulatory Guardrail Verification**:
  * **Rule Enforced**: Any application with `risk_tier in ['PEP', 'HIGH']` or `watchlist_score >= 85` is strictly quarantined from ML scoring and auto-remediation.
  * **Test Result**: Evaluated against 100 randomized variations of PEP/Sanctions profiles (`test_110`, `test_111` in `test_onboard360_master.py`). Zero cases were leaked to auto-remediation.

---

## 4. Activity-Based Costing (ABC) Model Forensics

### Baseline Operating Cost (AS-IS):
* **L1 Operations Labor**: $184,000 \text{ reviews} \times 1.8 \text{h touch} \times \$42.00/\text{h} = \mathbf{\$13,910,400.00}$
* **L2 Compliance Labor**: $29,842 \text{ reviews} \times 3.5 \text{h touch} \times \$65.00/\text{h} = \mathbf{\$6,789,055.00}$
* **Customer Support Inquiries**: $118,602 \text{ tickets} \text{ (chat @ \$8.50, voice @ \$18.00)} = \mathbf{\$1,408,658.00}$
* **Legacy Vendor Screening APIs**: $520,000 \text{ apps} \times \$9.80/\text{app} = \mathbf{\$5,096,000.00}$
* **Manual Rework Mailing & Admin**: $173,429 \text{ apps} \times \$4.40/\text{app} = \mathbf{\$763,087.60}$
* **Total Baseline Operating OPEX**: $\mathbf{\$27,967,200.60}$
* **Unit Cost per Approved Account** (414,655 approved): $\frac{\$27,967,200.60}{414,655} = \mathbf{\$67.45}$

### Projected Operating Cost (TO-BE Base Case):
* **L1 Operations Labor**: $41,600 \text{ reviews} \times 0.8 \text{h touch} \times \$42.00/\text{h} = \mathbf{\$1,397,760.00}$
* **L2 Compliance Labor**: $15,600 \text{ reviews} \times 1.5 \text{h touch} \times \$65.00/\text{h} = \mathbf{\$1,521,000.00}$
* **Customer Support Inquiries** (75% reduction via proactive push): $\$1,408,658.00 \times 0.25 = \mathbf{\$352,164.50}$
* **Modern RegTech API Bundle**: $520,000 \text{ apps} \times \$4.20/\text{app} = \mathbf{\$2,184,000.00}$
* **Cloud Infrastructure & SaaS OPEX**: $\mathbf{\$420,000.00}$
* **Manual Rework Mailing**: $\mathbf{\$0.00}$ (100% digital self-service remediation)
* **Total Projected Operating OPEX**: $\mathbf{\$5,874,924.50}$
* **Unit Cost per Approved Account** (468,000 approved): $\frac{\$5,874,924.50}{468,000} = \mathbf{\$12.55}$
* **Annual Net Recurring Cash Benefit**: $\$27,967,200.60 - \$5,874,924.50 = \mathbf{\$22,092,276.10}$
