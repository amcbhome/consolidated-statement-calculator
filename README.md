# consolidated-statement-calculator
# Consolidation Refresher: 5 Workings Calculator

This application is a pedagogical tool designed to assist accounting students in understanding the **Consolidated Statement of Financial Position (CSFP)**. It follows the standard **"5 Workings" methodology** as outlined in the [ACCA technical guidance](https://www.accaglobal.com/uk/en/student/exam-support-resources/fundamentals-exams-study-resources/f3/technical-articles/preparing-simple-consolidated-financial-statements.html).

---

## 🚀 Step-by-Step Guide

### 1. Define the Scenario
Input the fundamental financial data for the Parent (P) and Subsidiary (S):
* **Cost of Investment:** The amount paid by the parent to acquire the subsidiary.
* **NCI at Acquisition:** The Non-Controlling Interest measured at fair value at the date of acquisition.
* **Net Assets:** The book value of the subsidiary's net assets at both acquisition and the current reporting date.

### 2. Calculate the 5 Workings
Once you click **"Generate Consolidation Results"**, the app automatically derives the five core pillars of consolidation:
* **W1: Group Structure:** Defines the percentage of ownership.
* **W2: Post-Acquisition Profit:** Calculates the movement in subsidiary net assets since the date of acquisition.
* **W3: Goodwill:** Determines the residual value of the investment.
* **W4: Closing NCI:** Calculates the equity interest attributable to minority shareholders.
* **W5: Group Retained Earnings:** Aggregates the parent's earnings with its share of the subsidiary's growth.

### 3. Review the Required Outputs
The app extracts the relevant figures into a **Consolidated Statement of Financial Position (Extract)**, allowing you to see exactly where each working figure maps to the final group balance sheet.

---

## 🧠 Advanced Considerations
In complex scenarios, the 5 Workings must be adjusted for standard accounting adjustments:
* **Inter-group Trading & PUP:** Elimination of intra-group sales and adjustment for unrealized profit in inventory.
* **Fair Value Adjustments:** Adjusting subsidiary asset values to fair value at acquisition and accounting for resulting depreciation.
* **Goodwill Impairment:** Adjusting for any loss in value in goodwill post-acquisition.

[attachment_0](attachment)

---

## 🛠️ How to run locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/consolidation-refresher.git](https://github.com/your-username/consolidation-refresher.git)
    cd consolidation-refresher
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

---
*Developed as an educational resource aligned with ACCA accounting standards.*
