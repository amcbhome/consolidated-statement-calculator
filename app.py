import streamlit as st
import pandas as pd

def format_currency(val):
    return f"{int(val):,}"

st.set_page_config(page_title="Consolidation Refresher", layout="wide")

st.title("Consolidated Financial Statements: A Step-by-Step Guide")
st.markdown("""
This calculator is based on the [ACCA technical guidance for preparing consolidated financial statements](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f7/technical-articles/cons-fin-statements.html).
""")

# Scenario Definition
st.subheader("1. The Scenario")
st.write("Consider a Parent (P) acquiring 80% of a Subsidiary (S).")
col1, col2 = st.columns(2)
with col1:
    cost_inv = st.number_input("Cost of Investment (£)", value=150000, step=1000)
    nci_fv_acq = st.number_input("NCI at Fair Value at Acquisition (£)", value=35000, step=1000)
with col2:
    na_acq = st.number_input("Subsidiary Net Assets at Acquisition (£)", value=120000, step=1000)
    na_reporting = st.number_input("Subsidiary Net Assets at Reporting Date (£)", value=160000, step=1000)
    p_re = st.number_input("Parent Retained Earnings at Reporting Date (£)", value=200000, step=1000)

if st.button("Generate Consolidation Results"):
    # Underlying Logic
    pap = na_reporting - na_acq
    gw = (cost_inv + nci_fv_acq) - na_acq
    nci_closing = nci_fv_acq + (0.20 * pap)
    gre = p_re + (0.80 * pap)

    # 2. The 5 Workings
    st.subheader("2. The 5 Workings")
    workings = pd.DataFrame({
        "Working": ["W1: Group Structure", "W2: Post-Acq Profit", "W3: Goodwill", "W4: Closing NCI", "W5: Group RE"],
        "Calculation": ["80% P / 20% NCI", f"{na_reporting} - {na_acq}", f"({cost_inv} + {nci_fv_acq}) - {na_acq}", f"{nci_fv_acq} + (20% * {pap})", f"{p_re} + (80% * {pap})"],
        "Result (£)": [format_currency(x) if x != 0 else "80%/20%" for x in [0, pap, gw, nci_closing, gre]]
    })
    st.table(workings)

    # 3. Required Outputs
    st.subheader("3. Required Output: Consolidated Statement of Financial Position (Extract)")
    
    p_assets = 500000
    s_assets = 200000
    
    outputs = pd.DataFrame({
        "Item": ["Non-Current Assets: Goodwill", "Non-Current Assets: PPE (P+S)", "Equity: Group RE", "Equity: NCI"],
        "Source": ["W3", "P + S", "W5", "W4"],
        "Total (£)": [format_currency(gw), format_currency(p_assets + s_assets), format_currency(gre), format_currency(nci_closing)]
    })
    st.table(outputs)

st.divider()

st.subheader("4. Advanced Considerations (ACCA Standards)")

st.write("In complex consolidations, the '5 Workings' are adjusted for the following:")

with st.expander("Inter-group Trading & Unrealized Profit (PUP)"):
    st.write("""
    **Inter-group Trading:** All intra-group sales and purchases must be eliminated in full.
    **Unrealized Profit (PUP):** If the group has unsold inventory from inter-group sales at the reporting date, the profit element must be eliminated from the seller's retained earnings.
    """)

with st.expander("Fair Value Adjustments & Depreciation"):
    st.write("Subsidiary assets are measured at fair value at acquisition; any surplus is depreciated against post-acquisition profits.")

with st.expander("Impairment of Goodwill"):
    st.write("Goodwill must be tested annually; impairment losses reduce both Group Retained Earnings (W5) and Goodwill (W3).")

st.info("Remember: Always eliminate the investment in the subsidiary against the equity of the subsidiary at acquisition.")
