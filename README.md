
# Finance Transaction Risk Analytics System using Flask

A Python Flask-based finance analytics web application that stores customer transactions, analyzes transaction behavior, identifies suspicious financial activity, and displays risk insights through a dashboard.

This project demonstrates **Python, Flask, SQL, SQLite, Object-Oriented Programming, backend development, rule-based risk detection, and dashboard-based analytics** in a finance-related use case.

---

## Project Overview

Financial institutions process many transactions every day. Some transactions may appear risky because of high transaction amount, unusual location, or suspicious transaction category.

This project simulates a basic finance transaction monitoring system. It stores customer and transaction data in a SQLite database, applies rule-based risk scoring, classifies transactions into risk levels, and displays the results through a Flask dashboard.

The system helps identify transactions that may need further review.

---

## Objectives

The main objectives of this project are:

- Store customer and transaction data in a SQL database
- Analyze transaction behavior using Python logic
- Detect potentially suspicious financial transactions
- Classify transactions as Low Risk, Medium Risk, or High Risk
- Generate transaction summary metrics
- Perform SQL-based category and location analysis
- Display all insights through a Flask web dashboard
- Allow users to add new transactions through a web form

---

## Tech Stack

- Python
- Flask
- SQLite
- SQL
- HTML
- CSS
- Object-Oriented Programming
- Rule-Based Risk Analysis

---

## Key Features

### 1. Customer Management

The application stores customer information such as:

- Customer ID
- Name
- Age
- City
- Account Type

---

### 2. Transaction Management

The application stores transaction records with details such as:

- Transaction ID
- Customer ID
- Amount
- Category
- Location
- Transaction Type

---

### 3. Add New Transaction

The project includes a web form where users can add new transactions.

After submitting the form:

- The transaction is inserted into the SQLite database
- The dashboard is updated automatically
- Risk score and risk level are calculated for the new transaction

---

### 4. Rule-Based Risk Analysis

The system calculates a risk score for each transaction using rule-based logic.

Risk factors include:

- High-value transaction
- Transaction location different from the customer’s registered city
- High-risk categories such as Crypto, Gambling, or Unknown

---

## Risk Scoring Logic

| Risk Factor | Score Added |
|---|---:|
| Transaction amount greater than 50,000 | 40 |
| Transaction location different from customer city | 30 |
| Category is Crypto, Gambling, or Unknown | 30 |

---

## Risk Classification

| Risk Score | Risk Level |
|---:|---|
| 0 - 39 | Low Risk |
| 40 - 69 | Medium Risk |
| 70 and above | High Risk |

---

## Example Risk Detection

Example transaction:

```text
Amount: 95,000
Category: Crypto
Location: Mumbai
Customer City: Pune
```

Risk calculation:

```text
High-value transaction: +40
Different location: +30
High-risk category: +30
Total Risk Score: 100
Risk Level: High Risk
```

---

## SQL-Based Analytics

The project uses SQL queries to generate transaction insights.

SQL analytics include:

- Category-wise spending summary
- Location-wise spending summary
- High-value transaction filtering
- Transaction count
- Total transaction amount
- Average transaction amount

SQL concepts used:

- SELECT
- WHERE
- COUNT
- SUM
- AVG
- GROUP BY
- ORDER BY

---

## Dashboard Features

The Flask dashboard displays:

- Customer details
- Total number of transactions
- Total transaction amount
- Average transaction amount
- High-risk transaction count
- Medium-risk transaction count
- Low-risk transaction count
- All transactions with risk score and risk level
- Risk reasons for each transaction
- Category-wise spending analytics
- Location-wise spending analytics
- High-value transactions

---

## Project Workflow

```text
User opens Flask app
        |
        v
SQLite database is initialized
        |
        v
Sample customer and transaction data is inserted
        |
        v
Transaction data is fetched from database
        |
        v
Python OOP classes convert records into objects
        |
        v
RiskAnalyzer calculates risk score and risk level
        |
        v
AnalyticsService generates summary metrics
        |
        v
SQL queries generate category and location insights
        |
        v
Flask dashboard displays complete analysis
```

---

## Application Routes

| Route | Description |
|---|---|
| `/` | Home route to check if the application is running |
| `/dashboard` | Displays the finance transaction risk analytics dashboard |
| `/add-transaction` | Opens the form to add a new transaction |
| `/analyze-risk` | Returns risk analysis results in JSON format |
| `/sql-analytics` | Returns SQL-based analytics in JSON format |

---

## Object-Oriented Programming Concepts Used

This project uses Object-Oriented Programming to separate responsibilities into different classes.

### Customer Class

Represents customer information such as customer ID, name, age, city, and account type.

### Transaction Class

Represents transaction details such as transaction ID, customer ID, amount, category, location, and transaction type.

### RiskAnalyzer Class

Contains the logic for calculating transaction risk score and assigning risk level.

### AnalyticsService Class

Generates summary-level metrics such as total transactions, total amount, average amount, and risk counts.

### DatabaseService Class

Handles database operations such as table creation, sample data insertion, transaction insertion, and SQL analytics queries.

---

## Repository Structure

```text
finance-transaction-risk-analytics-flask/
│
├── README.md
├── app.py
├── customer.py
├── transaction.py
├── risk_analyzer.py
├── analytics_service.py
├── database_service.py
├── dashboard.html
├── add_transaction.html
└── finance_risk.db
```

---

## Main Files

### app.py

The main Flask application file. It defines routes, initializes the database, fetches data, performs risk analysis, and renders the dashboard.

### customer.py

Contains the `Customer` class for storing customer information.

### transaction.py

Contains the `Transaction` class for storing transaction details.

### risk_analyzer.py

Contains the `RiskAnalyzer` class, which calculates risk score and risk level.

### analytics_service.py

Contains the `AnalyticsService` class, which generates transaction summaries and filters high-risk transactions.

### database_service.py

Contains the `DatabaseService` class, which manages SQLite database operations and SQL analytics.

### dashboard.html

HTML template for displaying the finance transaction risk analytics dashboard.

### add_transaction.html

HTML form for adding new transactions.

---

## How to Run the Project

### Prerequisites

Make sure Python is installed on your system.

Install Flask:

```bash
pip install flask
```

---

### Steps to Run

1. Clone the repository:

```bash
git clone https://github.com/Harshada42/finance-transaction-risk-analytics-flask.git
```

2. Go to the project folder:

```bash
cd finance-transaction-risk-analytics-flask
```

3. Run the Flask application:

```bash
python app.py
```

4. Open the application in your browser:

```text
http://127.0.0.1:5000/
```

5. Open the dashboard:

```text
http://127.0.0.1:5000/dashboard
```

6. Add a new transaction:

```text
http://127.0.0.1:5000/add-transaction
```

---

## Sample Data

The project includes sample customer and transaction records.

Example customer:

```text
Name: Aarav Sharma
City: Pune
Account Type: Savings
```

Example transactions:

```text
Online Shopping - 75,000 - Delhi
Groceries - 1,500 - Pune
Crypto - 95,000 - Mumbai
Restaurant - 5,000 - Pune
Unknown - 62,000 - Bangalore
```

---

## Example Output

Example dashboard summary:

```text
Total Transactions: 5
Total Amount: 238,500
Average Transaction Amount: 47,700
High Risk Transactions: 3
Medium Risk Transactions: 0
Low Risk Transactions: 2
```

---

## Finance and Risk Analytics Relevance

This project is relevant to finance, data analytics, and risk-monitoring use cases because it demonstrates how transaction data can be analyzed to identify suspicious patterns.

It shows practical understanding of:

- Transaction monitoring
- Fraud-risk indicators
- Rule-based risk scoring
- SQL analytics
- Backend development
- Dashboard reporting
- Data-driven decision support

---

## Skills Demonstrated

- Python programming
- Flask web development
- SQL query writing
- SQLite database integration
- Object-Oriented Programming
- Backend application design
- Data analysis logic
- Risk classification
- Dashboard development
- Debugging and application flow design


## Future Enhancements

Possible improvements for this project:

- Add user login and authentication
- Add support for multiple customers
- Add transaction date and time analysis
- Add fraud trend visualization charts
- Add machine learning-based fraud prediction
- Add CSV upload for bulk transactions
- Add role-based dashboard access
- Add pagination and search filters
- Add transaction export to CSV
- Add API documentation
- Add unit tests for risk scoring logic
- Deploy the app on Render, Railway, or PythonAnywhere














