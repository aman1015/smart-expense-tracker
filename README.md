# Smart Financial Intelligence Dashboard

A Streamlit-based financial analytics dashboard that automatically categorizes transactions, stores them in a database, and provides insights such as spending trends, anomaly detection, financial score, and monthly predictions.

---

# Overview

This project allows users to upload a bank statement CSV file and automatically generates financial insights including:

* Financial health score
* Weekly & monthly spending trends
* Category-wise spending breakdown
* Recurring transaction detection
* Anomaly detection
* Savings trend
* Monthly expense prediction
* Top spending categories

The system uses rule-based categorization, SQLite database storage, and Pandas-based analytics.

---

# Architecture

```
                ┌──────────────┐
                │   CSV Upload │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   Validator  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Security    │
                │ (clean text) │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │ Categorizer  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   Database   │
                │   SQLite     │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Analytics   │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │  Streamlit   │
                │ Dashboard UI │
                └──────────────┘
```

---

# Workflow

1. User uploads CSV file
2. Data validation checks required columns
3. Transaction descriptions cleaned
4. Auto categorization using rule engine
5. Categories inserted into database
6. Transactions stored in SQLite
7. Analytics computed
8. Charts and insights displayed

---

# Project Structure

```
Smart_expense/
│
├── app.py              # Main Streamlit UI
├── analytics.py        # Analytics engine
├── db.py               # SQLite database handler
├── validator.py        # CSV validation
├── categorizer.py      # Rule-based categorization
├── security.py         # Text cleaning
│
├── expense.db          # SQLite database (auto-created)
└── README.md
```

---

# CSV Format

Upload CSV with columns:

```
date,description,amount,type
2025-01-01,Swiggy,-450,debit
2025-01-02,Salary,50000,credit
2025-01-03,Uber,-200,debit
```

Required columns:

* date
* description
* amount
* type (credit/debit)

---

# Features

## Financial Score

Measures savings ratio

```
score = (income - expense) / income * 100
```

Shows financial health percentage.

---

## Weekly Trend

Groups transactions week-wise to show spending pattern.

---

## Monthly Trend

Shows month-wise spending growth.

---

## Category Split

Displays pie chart of spending by category.

---

## Income vs Expense

Compares credit vs debit totals.

---

## Savings Trend

Shows cumulative savings over time.

---

## Recurring Transactions

Detects repeated payments like:

* subscriptions
* rent
* EMI
* bills

---

## Anomaly Detection

Detects unusual transactions using:

```
mean + 2 * std
```

Flags large abnormal spending.

---

## Monthly Prediction

Predicts expected monthly spending:

```
daily_average * 30
```

---

# Database Schema

## Categories Table

```
id
category_name
```

## Transactions Table

```
id
date
description
amount
type
category_id
source_type
```

## Budgets Table

```
category_id
monthly_limit
month
year
```

---

# Installation

```bash
pip install streamlit pandas numpy matplotlib
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* SQLite
* Matplotlib

---

# Example Insights Generated

* Financial Score
* Expected Monthly Spend
* Weekly Spending Trend
* Category Pie Chart
* Top 5 Spending Categories
* Recurring Transactions
* Anomaly Detection

---

# Future Improvements

* Machine learning categorization
* Budget alerts
* Email notifications
* Multi-user login
* Cloud database
* AI financial advice

---

# Interview Description

Smart Financial Intelligence Dashboard that ingests transaction CSVs, automatically categorizes expenses, stores them in SQLite, and generates analytics including anomaly detection, financial scoring, and predictive monthly spending using Streamlit.

---
