import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("Personal Finance Dashboard")
st.write("Track, visualize, and analyze your spending patterns.")

df = pd.read_csv("data/sample_expenses.csv")

st.subheader("Raw Expense Data")
st.dataframe(df)