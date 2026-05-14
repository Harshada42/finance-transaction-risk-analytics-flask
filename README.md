# finance-transaction-risk-analytics-flask

Finance transaction risk analytics web app built with Python, Flask, OOPS, and SQL to detect suspicious transactions and generate dashboard insights.

# Finance Transaction Risk Analytics System

## Project Overview

Finance Transaction Risk Analytics System is a Flask-based web application developed using Python, Object-Oriented Programming concepts, and SQL database integration. The project is designed to manage customer transaction data, analyze transaction behavior, detect potentially suspicious financial activity, and present useful insights through a web dashboard.

This project focuses on applying backend development, database handling, SQL analytics, and logical risk detection in a finance-related use case. It is suitable for demonstrating skills in Python, Flask, OOPS, SQL, analytical thinking, and data-driven problem solving.

---

## Objective

The main objective of this project is to build a simple finance analytics system that can:

- Store customer and transaction details in a SQL database
- Analyze transaction patterns using Python logic
- Identify high-risk or suspicious transactions
- Generate category-wise and location-wise transaction insights
- Display transaction summaries through a Flask dashboard
- Allow users to add new transactions through a web form

---

## Why This Project?

Financial systems process large volumes of transactions every day. Some transactions may be high-value, unusual, or location-based anomalies. This project simulates a basic transaction monitoring system that helps identify risky financial activity using rule-based analysis.

The project demonstrates how Python, Flask, OOPS, and SQL can be used together to build a small but practical finance data system.

---

## Tech Stack

- Python
- Flask
- SQLite Database
- SQL
- HTML
- CSS
- Object-Oriented Programming

---

## Key Features

### 1. Customer and Transaction Management

The system stores customer details and transaction records in a database.

Customer details include:

- Customer ID
- Name
- Age
- City
- Account Type

Transaction details include:

- Transaction ID
- Customer ID
- Amount
- Category
- Location
- Transaction Type

---

### 2. Add New Transaction

The application includes a Flask form that allows users to add a new transaction from the browser.

After adding a transaction, the record is inserted into the database and automatically displayed on the dashboard.

---

### 3. Transaction Risk Analysis

The system applies rule-based logic to calculate a risk score for each transaction.

Risk factors include:

- High transaction amount
- Transaction location different from the customer’s registered city
- High-risk transaction categories such as Crypto, Gambling, or Unknown

Based on the risk score, transactions are classified as:

- Low Risk
- Medium Risk
- High Risk

---

### 4. SQL-Based Analytics

The project uses SQL queries to generate meaningful transaction insights.

SQL operations used include:

- SELECT
- WHERE
- COUNT
- SUM
- AVG
- GROUP BY
- ORDER BY

The SQL analytics include:

- Category-wise spending summary
- Location-wise spending summary
- High-value transaction filtering

---

### 5. Dashboard

The Flask dashboard displays:

- Customer details
- Total number of transactions
- Total transaction amount
- Average transaction amount
- High-risk transaction count
- Medium-risk transaction count
- Low-risk transaction count
- All transactions with risk score and risk reasons
- Category-wise SQL analytics
- Location-wise SQL analytics
- High-value transactions

---

## OOPS Concepts Used

This project follows Object-Oriented Programming principles by separating responsibilities into different classes.

### Customer Class

Represents customer information such as customer ID, name, age, city, and account type.

### Transaction Class

Represents transaction information such as transaction ID, amount, category, location, and transaction type.

### RiskAnalyzer Class

Contains logic to calculate transaction risk score and classify transactions into Low, Medium, or High Risk.

### AnalyticsService Class

Generates summary-level analytics such as total transactions, total amount, average transaction amount, and risk counts.

### DatabaseService Class

Handles database operations such as creating tables, inserting sample data, inserting new transactions, and fetching SQL analytics.

---

## Project Workflow

1. The Flask application starts and initializes the database.
2. Sample customer and transaction data are inserted if the database is empty.
3. Transaction data is fetched from the SQL database.
4. Python OOPS classes convert database records into objects.
5. RiskAnalyzer calculates risk score and risk level for each transaction.
6. AnalyticsService generates summary metrics.
7. SQL queries generate category-wise, location-wise, and high-value transaction insights.
8. The dashboard displays the complete analysis.
9. Users can add new transactions through the web form.

---

## Project Routes

| Route | Description |
|---|---|
| `/` | Home route |
| `/dashboard` | Displays finance transaction risk analytics dashboard |
| `/add-transaction` | Form to add a new transaction |
| `/analyze-risk` | Returns transaction risk analysis in JSON format |
| `/sql-analytics` | Returns SQL-based analytics in JSON format |

---

## Folder Structure

```text
finance-risk-analytics-flask/
│
├── app.py
├── finance_risk.db
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── customer.py
│   ├── transaction.py
│   └── risk_analyzer.py
│
├── services/
│   ├── analytics_service.py
│   └── database_service.py
│
├── templates/
│   ├── dashboard.html
│   └── add_transaction.html
│
└── venv/
