# FUTURE_ML_01
Machine Learning Internship Tasks for Future Interns - April 2025 Cohort
# Task 1: Sales Forecasting for Retail Business

# 📊 Sales Forecasting for Retail Business

## 🔍 Objective
To forecast daily sales for a retail business using historical sales data and identify trends, patterns, and seasonal behavior. This helps improve decision-making in inventory management, marketing, and operations.

---

## 🛠 Tools & Libraries Used
- **Python**
- **Facebook Prophet** – Time series forecasting
- **Pandas** – Data manipulation
- **Matplotlib** – Visualization

---

## 📁 Dataset
The dataset contains transactional sales records with the following relevant columns:
- `ORDERDATE`: Date of order
- `SALES`: Sales amount per day

Data was aggregated into daily totals before modeling.

---

## 🧪 Methodology

1. **Data Cleaning**
   - Converted `ORDERDATE` column to datetime format.
   - Grouped data by day and summed `SALES`.

2. **Modeling with Prophet**
   - Renamed columns to `ds` and `y` (as required by Prophet).
   - Trained model on full historical data.
   - Forecasted sales for the next 90 days.

3. **Visualization**
   - Plotted future sales forecast.
   - Analyzed seasonal effects: weekly and yearly trends.

---

## 📈 Forecast Output

### 🔮 Sales Forecast Graph

![Sales Forecast](./download%20(4).png)

- The blue line represents predicted sales.
- The shaded area shows the confidence interval (possible range of values).
- Black dots = actual sales data.
- Sales show noticeable **seasonal peaks** and **fluctuations** over time.

---

### 📅 Seasonal Decomposition

![Trend and Seasonality](./download%20(5).png)

- **Trend:** Slight overall growth over time.
- **Weekly Seasonality:** Higher sales on **Sundays and Thursdays**, lowest on **Saturdays**.
- **Yearly Seasonality:** Clear spikes in **November** and **March** — possibly due to promotions or peak shopping seasons.

---


## ✅ Key Insights
- There’s **strong seasonality** in both weekly and yearly patterns.
- Prophet effectively captured trends and uncertainty, making it suitable for retail demand forecasting.
- This model can be extended for **weekly or monthly sales**, or include holidays/promotions.

---

## 📌 Future Improvements
- Include external factors like promotions, holidays, or pricing changes.
- Try advanced models (e.g., XGBoost, LSTM) for comparison.
- Deploy model into a dashboard for real-time updates.

---
## 📤 Forecast Data Output
Forecasted data was saved to a CSV file:
```python
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("sales_forecast.csv", index=False)
