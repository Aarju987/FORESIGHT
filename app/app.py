import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="FORESIGHT - Inventory Intelligence",
    layout="wide"
)

st.title("📦 FORESIGHT — Demand & Inventory Intelligence")
st.write("NorthBay Living | Inventory Risk Dashboard")

# Load risk data
BASE_DIR = Path(__file__).resolve().parent.parent
risk_file = next(BASE_DIR.rglob("risk_scoring.csv"))
risk_df = pd.read_csv(risk_file)

# KPIs
total_skus = len(risk_df)
stockout = (risk_df["risk"] == "Stockout Risk").sum()
healthy = (risk_df["risk"] == "Healthy").sum()
overstock = (risk_df["risk"] == "Overstock Risk").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total SKUs", total_skus)
col2.metric("Stockout Risk", stockout)
col3.metric("Healthy", healthy)
col4.metric("Overstock Risk", overstock)

st.divider()

# Filters
st.subheader("🔎 SKU Risk Analysis")

selected_risk = st.selectbox(
    "Filter by Risk",
    ["All", "Stockout Risk", "Overstock Risk", "Healthy"]
)

if selected_risk == "All":
    filtered_df = risk_df
else:
    filtered_df = risk_df[risk_df["risk"] == selected_risk]

st.dataframe(
    filtered_df[
        [
            "sku_id",
            "daily_forecast",
            "lead_time_days",
            "lead_time_demand",
            "on_hand_units",
            "on_order_units",
            "risk",
            "recommended_action"
        ]
    ],
    use_container_width=True
)

st.divider()

st.subheader("🚨 Reorder Now")

reorder_df = risk_df[
    risk_df["recommended_action"] == "Reorder Now"
]

st.dataframe(
    reorder_df[
        [
            "sku_id",
            "daily_forecast",
            "lead_time_days",
            "lead_time_demand",
            "available_units",
            "recommended_action"
        ]
    ],
    use_container_width=True
)
st.subheader("📊 Risk Distribution")

risk_counts = risk_df["risk"].value_counts()

st.bar_chart(risk_counts)