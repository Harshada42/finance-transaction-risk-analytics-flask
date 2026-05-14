class Transaction:
    def __init__(self, transaction_id, customer_id, amount, category, location, transaction_type):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.amount = amount
        self.category = category
        self.location = location
        self.transaction_type = transaction_type

    def get_transaction_info(self):
        return {
            "transaction_id": self.transaction_id,
            "customer_id": self.customer_id,
            "amount": self.amount,
            "category": self.category,
            "location": self.location,
            "transaction_type": self.transaction_type
        }
    