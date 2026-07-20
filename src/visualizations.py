import pandas as pd
import plotly.express as px


def spending_by_category_chart(df: pd.DataFrame):
    category_totals = (
        df.groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount", ascending=False)
    )

    fig = px.bar(
        category_totals,
        x="category",
        y="amount",
        title="Spending by Category",
        labels={"amount": "Amount (£)", "category": "Category"}
    )

    return fig


def monthly_spending_chart(df: pd.DataFrame):
    monthly_totals = (
        df.groupby("month", as_index=False)["amount"]
        .sum()
        .sort_values("month")
    )

    fig = px.line(
        monthly_totals,
        x="month",
        y="amount",
        markers=True,
        title="Monthly Spending Trend",
        labels={"amount": "Amount (£)", "month": "Month"}
    )

    return fig


def category_pie_chart(df: pd.DataFrame):
    category_totals = (
        df.groupby("category", as_index=False)["amount"]
        .sum()
    )

    fig = px.pie(
        category_totals,
        names="category",
        values="amount",
        title="Spending Share by Category"
    )

    return fig