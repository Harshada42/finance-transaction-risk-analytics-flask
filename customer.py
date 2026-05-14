class Customer:
    def __init__(self, customer_id, name, age, city, account_type):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.city = city
        self.account_type = account_type

    def get_customer_info(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "account_type": self.account_type
        }
  