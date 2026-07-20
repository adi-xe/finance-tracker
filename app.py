import streamlit as st
import pandas as pd

from src.preprocessing import clean_expenses
from src.clustering import create_spending_clusters
from src.visualizations import (
    spending_by_category_chart,
    monthly_spending_chart,
    category_pie_chart,
    cluster_scatter_chart
)

st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("Personal Finance Dashboard")
st.write("Track, visualize, and analyze your spending patterns.")

uploaded_file = st.sidebar.file_uploader("Upload your expenses CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_expenses.csv")

df = clean_expenses(df)

number_of_clusters = st.sidebar.slider(
    "Number of spending clusters",
    min_value=2,
    max_value=6,
    value=3
)

df = create_spending_clusters(df, number_of_clusters)

total_spending = df["amount"].sum()
average_spending = df["amount"].mean()
largest_expense = df["amount"].max()

col1, col2, col3 = st.columns(3)

col1.metric("Total Spending", f"£{total_spending:,.2f}")
col2.metric("Average Expense", f"£{average_spending:,.2f}")
col3.metric("Largest Expense", f"£{largest_expense:,.2f}")

st.subheader("Visual Analysis")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.plotly_chart(spending_by_category_chart(df), use_container_width=True)

with chart_col2:
    st.plotly_chart(category_pie_chart(df), use_container_width=True)

st.plotly_chart(monthly_spending_chart(df), use_container_width=True)

st.subheader("Spending Clusters")
st.plotly_chart(cluster_scatter_chart(df), use_container_width=True)

st.subheader("Expense Data")
st.dataframe(df)