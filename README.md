#  Trader Behavior & Sentiment Analysis

##  Overview

This project analyzes trader behavior using historical trading data and Bitcoin market sentiment (Fear/Greed Index). The goal is to understand how market sentiment affects trading performance, risk-taking, and decision-making.

---

##  Dataset
The project uses two datasets:

* **Bitcoin Market Sentiment** (Fear / Greed classification)
* **Historical Trader Data** (trade-level data including PnL, size, side, etc.)

---

##  Methodology

1. **Data Preparation**

   * Cleaned missing values and removed duplicates
   * Converted timestamps to daily format
   * Merged sentiment and trading data

2. **Feature Engineering**

   * Daily PnL per trader
   * Win rate
   * Average trade size
   * Trade frequency
   * Long/Short ratio

3. **Exploratory Data Analysis (EDA)**

   * Compared performance across Fear vs Greed
   * Analyzed trading behavior patterns

4. **Segmentation**

   * Clustered traders using KMeans
   * Identified behavioral groups

5. **Predictive Modeling**

   * Built Random Forest model
   * Predicted next-day profitability (profit/loss)

---

##  Key Insights

* Traders take **larger positions during Greed periods**, increasing risk
* **Fear periods show more stable performance**
* High trading frequency does **not guarantee profits**
* Behavioral features (trade size, frequency) are more predictive than sentiment

---

##  Strategy Recommendations

1. Reduce position size during Greed periods to control risk
2. Focus on consistent trading instead of frequent trading
3. Avoid large outlier trades to maintain stable returns

---

 How to Run

### 1. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

### 2. Run the dashboard

```bash
streamlit run app.py
```

---

## Outputs

* Performance analysis by sentiment
* Trader behavior insights
* Clustering visualization
* Predictive model results

---

## Limitations

* Dataset is small and imbalanced
* Model struggles to predict loss cases
* Results are exploratory, not financial advice

---

## Author

Pooja Mohite

