import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from db import Database
from validator import Validator
from categorizer import Categorizer
from analytics import Analytics
from security import Security

db = Database()

st.set_page_config(layout="wide")
st.title("Smart Financial Intelligence Dashboard")

file = st.file_uploader("Upload CSV")

if file:

    df = pd.read_csv(file)

    st.subheader("Preview")
    st.dataframe(df)

    errors = Validator.validate(df)

    if errors:
        for e in errors:
            st.error(e)
        st.stop()

    df["description"] = df["description"].apply(Security.clean_text)

    df["category"] = df["description"].apply(
        Categorizer.categorize)

    for c in df["category"].unique():
        db.insert_categories(c)

    cats = db.fetch("select * from categories")

    df = df.merge(cats,
                left_on="category",
                right_on="category_name")

    df.rename(columns={"id":"category_id"}, inplace=True)

    df["source_type"] = "csv"

    db.insert_transactions(df[
        ["date","description","amount","type",
         "category_id","source_type"]
    ])

    data = db.fetch("""
    SELECT t.*,c.category_name
    FROM transactions t
    JOIN categories c
    ON t.category_id=c.id
    """)

    st.divider()
    st.header("Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    score = Analytics.financial_score(data)
    pred = Analytics.prediction(data)

    income = data[data["type"]=="credit"]["amount"].sum()
    expense = abs(data[data["type"]=="debit"]["amount"].sum())

    col1.metric("Financial Score", score)
    col2.metric("Total Income", f"₹{income:,.0f}")
    col3.metric("Total Expense", f"₹{expense:,.0f}")
    col4.metric("Expected Monthly", f"₹{pred:,.0f}")

    st.divider()
    st.header("Spending Trends")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Weekly Trend")
        st.line_chart(Analytics.weekly(data))

    with col2:
        st.subheader("Monthly Trend")
        st.line_chart(Analytics.monthly(data))


    st.divider()
    st.header("Category Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Category Pie Chart")
        cat = Analytics.category_split(data)

        fig, ax = plt.subplots()
        ax.pie(cat, labels=cat.index, autopct='%1.1f%%')
        st.pyplot(fig)

    with col2:
        st.subheader("Top Spending Categories")
        top = Analytics.top5(db.conn)
        st.bar_chart(top.set_index("category_name"))


    st.divider()
    st.header("Cash Flow")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Income vs Expense")
        st.bar_chart(Analytics.income_vs_expense(data))

    with col2:
        st.subheader("Savings Trend")
        st.line_chart(Analytics.savings_trend(data))


    st.divider()
    st.header("Advanced Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Recurring Transactions")
        st.dataframe(Analytics.recurring(data))

    with col2:
        st.subheader("Anomaly Detection")
        st.dataframe(Analytics.anomaly(data))


    st.divider()
    st.header("Smart Insight")

    top = data.groupby("category_name")["amount"].sum().idxmax()

    st.success(f"You spend most on: {top}")