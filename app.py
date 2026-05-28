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
    pap = na_reporting - na_acq
    gw = (cost_inv + nci_fv_acq) - na_acq
    nci_closing = nci_fv_acq + (0.20 * pap)
    gre = p_re + (0.80 * pap)

    st.subheader("2. The 5 Workings")
    workings = pd.DataFrame({
        "Working": ["W1: Group Structure", "W2: Post-Acq Profit", "W3: Goodwill", "W4: Closing NCI", "W5: Group RE"],
        "Calculation": ["80% P / 20% NCI", f"{na_reporting} - {na_acq}", f"({cost_inv} + {nci_fv_acq}) - {na_acq}", f"{nci_fv_acq} + (20% * {pap})", f"{p_re} + (80% * {pap})"],
        "Result (£)": [format_currency(x) if x != 0 else "80%/20%" for x in [0, pap, gw, nci_closing, gre]]
    })
    st.table(workings)

    st.subheader("3. Required Output: Consolidated Statement of Financial Position (Extract)")
    outputs = pd.DataFrame({
        "Item": ["Non-Current Assets: Goodwill", "Non-Current Assets: PPE (P+S)", "Equity: Group RE", "Equity: NCI"],
        "Source": ["W3", "P + S", "W5", "W4"],
        "Total (£)": [format_currency(gw), "700,000", format_currency(gre), format_currency(nci_closing)]
    })
    st.table(outputs)

st.divider()

st.subheader("4. Advanced Considerations & Common Errors")

st.write("Beyond the 5 Workings, be aware of these common pitfalls and technical requirements:")

with st.expander("Common Errors in Exams"):
    st.write("""
    1. **Double Counting:** Attempting to add the Parent's investment in the subsidiary to the assets (Investment must be eliminated).
    2. **Time Apportionment:** Failing to pro-rate subsidiary profits when the acquisition occurs mid-year.
    3. **NCI Share:** Forgetting to apply the NCI % to the *post-acquisition* profit (W4).
    4. **PUP Omission:** Forgetting to deduct Unrealized Profit from the *seller's* retained earnings.
    5. **Goodwill Impairment:** Failing to charge impairment to Group Retained Earnings (W5).
    """)

with st.expander("Inter-group Trading & Unrealized Profit (PUP)"):
    st.write("All intra-group sales/purchases must be eliminated. PUP must be deducted from the seller's retained earnings.")

with st.expander("Fair Value Adjustments & Depreciation"):
    st.write("Adjust assets to fair value at acquisition; any surplus must be depreciated against post-acquisition profits.")

with st.expander("Impairment of Goodwill"):
    st.write("Goodwill must be tested annually; impairment losses reduce both Group Retained Earnings (W5) and Goodwill (W3).")

st.info("Remember: Always eliminate the investment in the subsidiary against the equity of the subsidiary at acquisition.")
