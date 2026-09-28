# FORESIGHT — Demand & Inventory Intelligence

## Project Overview

FORESIGHT is a demand and inventory intelligence platform designed to help identify stockout risks and support inventory planning.

The project uses Python, Pandas, Scikit-learn, and Streamlit to analyze sales data, forecast demand, and identify inventory risk.

## Problem Statement

The objective is to identify products that may face stockout risk and provide actionable inventory recommendations.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Git & GitHub

## Dataset

The project uses four simulated datasets:

- sales_daily
- sku_master
- calendar
- inventory_snapshots

> Note: The dataset used in this project is synthetic and was created for project development purposes.

## Project Workflow

1. Data loading and understanding
2. Data quality checks
3. Exploratory Data Analysis
4. Demand forecasting
5. Forecast evaluation
6. Inventory risk scoring
7. Recommended actions
8. Streamlit dashboard

## Forecasting

A seasonal-naive baseline was compared with a Random Forest regression model.

| Model | WAPE |
|---|---:|
| Seasonal Naive | 9.06% |
| Random Forest | 7.17% |

## Risk Analysis

The inventory risk analysis identified:

- 136 SKUs as Stockout Risk
- 64 SKUs as Healthy
- 0 SKUs as Overstock Risk

For stockout-risk products, the recommended action is **Reorder Now**.

## Dashboard

The Streamlit dashboard provides:

- Total SKU count
- Stockout risk count
- Healthy SKU count
- Overstock risk count
- Risk filtering
- SKU-level risk analysis
- Reorder recommendations
- Risk distribution visualization

## Project Structure

```text
project 1/
│
├── app/
│   └── app.py
│
├── FORESIGHT_synthetic_data/
│   ├── data/
│   │   └── raw/
│   ├── notebooks/
│   └── reports/
│       └── risk_scoring.csv
│
├── notebooks/
│   └── 1_data_understanding.ipynb
│
├── reports/
│
└── .gitignore