import pandas as pd
import numpy as np

class Analytics:

    # Weekly Trend
    def weekly(df):

        df = df.copy()
        df["date"] = pd.to_datetime(df["date"]) 

        df["week"] = df["date"].dt.to_period("W").apply(lambda r: r.start_time)

        weekly = df.groupby("week")["amount"].sum().sort_index()

        return weekly.to_frame()


    # Monthly Trend
    def monthly(df):

        df = df.copy()
        df["date"] = pd.to_datetime(df["date"])

        df["month"] = df["date"].dt.to_period("M").apply(lambda r: r.start_time)

        monthly = df.groupby("month")["amount"].sum().sort_index()

        return monthly.to_frame()


    # Income vs Expense
    def income_vs_expense(df):

        result = df.groupby("type")["amount"].sum()

        return result.to_frame()


    # Category Split
    def category_split(df):

        return df.groupby("category_name")["amount"].sum().abs()


    # Daily Trend
    def daily_trend(df):

        df = df.copy()
        df["date"] = pd.to_datetime(df["date"])

        daily = df.groupby("date")["amount"].sum().sort_index()

        return daily.to_frame()


    # Savings Trend
    def savings_trend(df):

        df = df.copy()
        df["date"] = pd.to_datetime(df["date"])

        daily = df.groupby("date")["amount"].sum().sort_index()

        savings = daily.cumsum()

        return savings.to_frame()


    # Top 5
    def top5(conn):

        return pd.read_sql("""
        SELECT c.category_name,
               SUM(t.amount) total
        FROM transactions t
        JOIN categories c
        ON t.category_id = c.id
        GROUP BY c.category_name
        ORDER BY total DESC
        LIMIT 5
        """, conn)


    # Recurring
    def recurring(df):

        return df.groupby(
            ["description", "amount"]
        ).filter(lambda x: len(x) > 2)


    # Anomaly
    def anomaly(df):

        mean = df["amount"].mean()
        std = df["amount"].std()

        return df[df["amount"] > mean + 2 * std]


    # Financial Score
    def financial_score(df):

        income = df[df["type"] == "credit"]["amount"].sum()
        expense = abs(df[df["type"] == "debit"]["amount"].sum())

        savings = income - expense

        ratio = savings / income if income > 0 else 0

        return int(ratio * 100)


    # Prediction
    def prediction(df):

        df = df.copy()
        df["date"] = pd.to_datetime(df["date"])

        daily = df.groupby("date")["amount"].sum()

        avg = daily.mean()

        return avg * 30