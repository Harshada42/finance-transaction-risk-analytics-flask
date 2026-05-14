import sqlite3


class DatabaseService:
    def __init__(self, db_name="finance_risk.db"):
        self.db_name = db_name

    def get_connection(self):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection

    def create_tables(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                city TEXT,
                account_type TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                amount REAL,
                category TEXT,
                location TEXT,
                transaction_type TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """)

        connection.commit()
        connection.close()

    def insert_sample_data(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM customers")
        customer_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM transactions")
        transaction_count = cursor.fetchone()[0]

        if customer_count == 0:
            cursor.execute("""
                INSERT INTO customers (customer_id, name, age, city, account_type)
                VALUES (?, ?, ?, ?, ?)
            """, (1, "Aarav Sharma", 28, "Pune", "Savings"))

        if transaction_count == 0:
            sample_transactions = [
                (101, 1, 75000, "Online Shopping", "Delhi", "Debit"),
                (102, 1, 1500, "Groceries", "Pune", "Debit"),
                (103, 1, 95000, "Crypto", "Mumbai", "Debit"),
                (104, 1, 5000, "Restaurant", "Pune", "Credit"),
                (105, 1, 62000, "Unknown", "Bangalore", "Debit")
            ]

            cursor.executemany("""
                INSERT INTO transactions 
                (transaction_id, customer_id, amount, category, location, transaction_type)
                VALUES (?, ?, ?, ?, ?, ?)
            """, sample_transactions)

        connection.commit()
        connection.close()

    def get_customer_by_id(self, customer_id):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT customer_id, name, age, city, account_type
            FROM customers
            WHERE customer_id = ?
        """, (customer_id,))

        customer = cursor.fetchone()
        connection.close()

        return dict(customer) if customer else None

    def get_transactions_by_customer_id(self, customer_id):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT transaction_id, customer_id, amount, category, location, transaction_type
            FROM transactions
            WHERE customer_id = ?
        """, (customer_id,))

        transactions = cursor.fetchall()
        connection.close()

        return [dict(transaction) for transaction in transactions]

    def get_category_spending_summary(self, customer_id):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                category,
                COUNT(*) AS transaction_count,
                SUM(amount) AS total_amount,
                AVG(amount) AS average_amount
            FROM transactions
            WHERE customer_id = ?
            GROUP BY category
            ORDER BY total_amount DESC
        """, (customer_id,))

        results = cursor.fetchall()
        connection.close()

        return [dict(row) for row in results]

    def get_location_spending_summary(self, customer_id):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                location,
                COUNT(*) AS transaction_count,
                SUM(amount) AS total_amount
            FROM transactions
            WHERE customer_id = ?
            GROUP BY location
            ORDER BY total_amount DESC
        """, (customer_id,))

        results = cursor.fetchall()
        connection.close()

        return [dict(row) for row in results]

    def get_high_value_transactions(self, customer_id, amount_limit=50000):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                transaction_id,
                customer_id,
                amount,
                category,
                location,
                transaction_type
            FROM transactions
            WHERE customer_id = ?
            AND amount > ?
            ORDER BY amount DESC
        """, (customer_id, amount_limit))

        results = cursor.fetchall()
        connection.close()

        return [dict(row) for row in results]

    def insert_transaction(self, customer_id, amount, category, location, transaction_type):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COALESCE(MAX(transaction_id), 100) + 1 FROM transactions")
        new_transaction_id = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO transactions 
            (transaction_id, customer_id, amount, category, location, transaction_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            new_transaction_id,
            customer_id,
            amount,
            category,
            location,
            transaction_type
        ))

        connection.commit()
        connection.close()

        return new_transaction_id