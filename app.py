import streamlit as st
import pandas as pd

def calculate_consolidation(cost_inv, nci_fv_acq, na_acq, na_reporting, p_re):
    # W2: Post-Acquisition Profit
    post_acq_profit = na_reporting - na_acq
    
    # W3: Goodwill
    goodwill = (cost_inv + nci_fv_acq) - na_acq
    
    # W4: NCI Closing
    nci_closing = nci_fv_acq + (0.20 * post_acq_profit)
    
    # W5: Group Retained Earnings
    group_re = p_re + (0.80 * post_acq_profit)
    
    return post_acq_profit, goodwill, nci_closing, group_re

st.title("Consolidation Calculator (80% Subsidiary)")

# Inputs
col1, col2 = st.columns(2)
with col1:
    cost_inv = st.number_input("Cost of Investment (£)", value=150000)
    nci_fv_acq = st.number_input("NCI at FV at Acq (£)", value=35000)
    p_re = st.number_input("Parent Retained Earnings (£)", value=200000)
with col2:
    na_acq = st.number_input("Subsidiary Net Assets at Acq (£)", value=120000)
    na_reporting = st.number_input("Subsidiary Net Assets at Reporting (£)", value=160000)

if st.button("Calculate"):
    pap, gw, nci, gre = calculate_consolidation(cost_inv, nci_fv_acq, na_acq, na_reporting, p_re)
    
    st.subheader("Results")
    results = {
        "Working": ["Post-Acq Profit", "Goodwill", "Closing NCI", "Group Retained Earnings"],
        "Amount (£)": [pap, gw, nci, gre]
    }
    st.table(pd.DataFrame(results))

    st.info("""
    ### Other Key Considerations for Consolidation:
    * **PUP (Provision for Unrealised Profit):** Deduct from the profit of the entity that made the sale.
    * **Impairment:** If Goodwill is impaired, deduct from Group Retained Earnings and Goodwill value.
    * **Intra-group Trading:** Eliminate 100% of intra-group sales and receivables/payables.
    * **Fair Value Adjustments:** Adjust subsidiary assets to fair value at acquisition, then depreciate.
    """)
