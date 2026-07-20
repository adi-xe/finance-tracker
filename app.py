import streamlit as st
from src.data_loader import load_expenses
from src.preprocessing import clean_expenses

st.set_page_config(
    page_title="Personal Finance Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("Personal Finance Dashboard")
st.write("Track, visualize, and analyze your spending patterns.")

df = load_expenses("data/sample_expenses.csv")
df = clean_expenses(df)

st.subheader("Cleaned Expense Data")
st.dataframe(df)