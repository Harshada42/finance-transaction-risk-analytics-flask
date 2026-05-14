from flask import Flask, jsonify, render_template, request, redirect, url_for

from models.customer import Customer
from models.transaction import Transaction
from models.risk_analyzer import RiskAnalyzer
from services.analytics_service import AnalyticsService
from services.database_service import DatabaseService

app = Flask(__name__)


def initialize_database():
    database_service = DatabaseService()
    database_service.create_tables()
    database_service.insert_sample_data()


def get_data_from_database():
    database_service = DatabaseService()

    customer_data = database_service.get_customer_by_id(1)
    transaction_data = database_service.get_transactions_by_customer_id(1)

    customer = Customer(
        customer_id=customer_data["customer_id"],
        name=customer_data["name"],
        age=customer_data["age"],
        city=customer_data["city"],
        account_type=customer_data["account_type"]
    )

    transactions = []

    for item in transaction_data:
        transaction = Transaction(
            transaction_id=item["transaction_id"],
            customer_id=item["customer_id"],
            amount=item["amount"],
            category=item["category"],
            location=item["location"],
            transaction_type=item["transaction_type"]
        )

        transactions.append(transaction)

    return customer, transactions


def analyze_transactions():
    customer, transactions = get_data_from_database()
    analyzer = RiskAnalyzer()

    analysis_results = []

    for transaction in transactions:
        risk_result = analyzer.calculate_risk_score(transaction, customer)

        analysis_results.append({
            "transaction": transaction.get_transaction_info(),
            "risk_analysis": risk_result
        })

    analytics_service = AnalyticsService()
    summary = analytics_service.generate_summary(analysis_results)
    high_risk_transactions = analytics_service.get_high_risk_transactions(analysis_results)

    return customer, analysis_results, summary, high_risk_transactions


def get_sql_analytics():
    database_service = DatabaseService()

    category_summary = database_service.get_category_spending_summary(1)
    location_summary = database_service.get_location_spending_summary(1)
    high_value_transactions = database_service.get_high_value_transactions(1)

    return {
        "category_spending_summary": category_summary,
        "location_spending_summary": location_summary,
        "high_value_transactions": high_value_transactions
    }


@app.route("/")
def home():
    return "Finance Transaction Risk Analytics System is running!"


@app.route("/analyze-risk")
def analyze_risk():
    customer, analysis_results, summary, high_risk_transactions = analyze_transactions()

    return jsonify({
        "customer": customer.get_customer_info(),
        "summary": summary,
        "transactions": analysis_results,
        "high_risk_transactions": high_risk_transactions
    })


@app.route("/sql-analytics")
def sql_analytics():
    analytics = get_sql_analytics()
    return jsonify(analytics)


@app.route("/dashboard")
def dashboard():
    customer, analysis_results, summary, high_risk_transactions = analyze_transactions()
    sql_analytics = get_sql_analytics()

    return render_template(
        "dashboard.html",
        customer=customer.get_customer_info(),
        summary=summary,
        transactions=analysis_results,
        high_risk_transactions=high_risk_transactions,
        sql_analytics=sql_analytics
    )


@app.route("/add-transaction", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        location = request.form["location"]
        transaction_type = request.form["transaction_type"]

        database_service = DatabaseService()
        database_service.insert_transaction(
            customer_id=1,
            amount=amount,
            category=category,
            location=location,
            transaction_type=transaction_type
        )

        return redirect(url_for("dashboard"))

    return render_template("add_transaction.html")


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)