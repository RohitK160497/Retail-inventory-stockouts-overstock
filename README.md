# 📦 Retail Inventory Analytics: Real-Time Stockouts vs Overstock

This end-to-end analytics project simulates real-time inventory behavior using SKU-level demand forecasts, lead times, and inventory policies. The goal is to detect and visualize potential **stockouts** and **overstock scenarios** in a retail business using real data pipelines and an interactive dashboard.

---

## 🧠 Problem Statement

Retail businesses constantly face challenges in maintaining optimal inventory levels.  
**Too little stock** → stockouts, lost sales.  
**Too much stock** → high carrying costs, waste.

This project answers:
- When will a product **run out of stock**?
- Where are we **overstocking unnecessarily**?
- Can we **simulate & visualize** real inventory risks over time?

---

## 🔧 Tools & Technologies

| Tool         | Use Case                            |
|--------------|-------------------------------------|
| **Python**   | Data wrangling, analysis, modeling  |
| **Pandas**   | Forecast & simulation pipeline      |
| **Seaborn**  | Visualizations                      |
| **Streamlit**| Interactive dashboard               |
| **Excel**    | Raw retail inventory data           |
| **VS Code**  | Development environment             |

---


---

## 🧪 Workflow Summary

### 1. **Data Cleaning & Preparation**
- Handled missing values, normalized SKU data
- Merged product + inventory + volume data from Excel

### 2. **Demand Forecasting**
- Modeled each SKU using **SARIMAX** for 90-day demand prediction
- Stored outputs per SKU for simulation

### 3. **Inventory Simulation**
- Used lead time, beginning inventory, LMIL & UMIL values
- Simulated daily inventory levels, reorder triggers, and stockouts
- Exported to `inventory_simulation.csv`

### 4. **Interactive Dashboard**
- Built with **Streamlit**
- Features:
  - Category filter
  - KPI Summary (Stockout %, Overstock %)
  - Inventory status over time per SKU

---

## 📸 Sample Outputs

### 📊 Inventory vs LMIL & UMIL
<img width="1784" height="784" alt="Inventory vs LMIL   UMIL" src="https://github.com/user-attachments/assets/3575e1fd-5ee6-4675-a2ef-1b8d5e333473" />


### 📈 Example Demand Forecast Plot for p1
<img width="1189" height="490" alt="Demand Forecast Plot for p1" src="https://github.com/user-attachments/assets/36b8b7b2-b2a9-45cf-8864-0d46e73c8c04" />

### Streamlit dashboard Example
<img width="1919" height="901" alt="Streamlit Dashboard" src="https://github.com/user-attachments/assets/cafefb40-a7ca-4e42-9d5d-5bf23e2305be" />



---


