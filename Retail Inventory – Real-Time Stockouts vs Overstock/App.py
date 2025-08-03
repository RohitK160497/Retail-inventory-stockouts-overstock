import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load inventory simulation output
df = pd.read_csv('C:\Stevens EM\Projects\Retail Inventory – Real-Time Stockouts vs Overstock\inventory_simulation.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar
st.sidebar.header("📦 Retail Inventory Dashboard")
sku_selected = st.sidebar.selectbox("Select Product SKU", sorted(df['SKU'].unique()))

# Filter for selected SKU
sku_df = df[df['SKU'] == sku_selected].sort_values('Date')

# KPIs
total_days = len(sku_df)
stockout_days = sku_df['Stockout'].sum()
overstock_days = (sku_df['Remaining_Inventory'] > sku_df['Remaining_Inventory'].mean() * 1.5).sum()

# Main Title
st.title("⚠️ Inventory Alerts")

col1, col2 = st.columns(2)
col1.metric("📉 Stockout Days (%)", f"{(stockout_days / total_days) * 100:.2f}%")
col2.metric("📈 Overstock Days (%)", f"{(overstock_days / total_days) * 100:.2f}%")

st.markdown("### 📊 Inventory Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(sku_df['Date'], sku_df['Remaining_Inventory'], label='Remaining Inventory', color='blue')
ax.axhline(y=0, color='red', linestyle='--', label='Stockout Threshold')
ax.set_xlabel("Date")
ax.set_ylabel("Units")
ax.set_title(f"Inventory for {sku_selected}")
ax.legend()
st.pyplot(fig)

# Optional table
st.markdown("### 🔍 Simulation Data")
st.dataframe(sku_df)
