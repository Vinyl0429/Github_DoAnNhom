from libs import DataConnector
from models.Customer import Customer


class CustomerManager:
    @staticmethod
    def add_customer(customer_id, name, phone):
        customers = DataConnector.get_all_customers()
        if any(c.customer_id == customer_id for c in customers):
            print("Customer ID already exists!")
            return
        new_customer = Customer(customer_id, name, phone)
        customers.append(new_customer)
        DataConnector.save_all_customers(customers)
        print("Customer added successfully!")

    @staticmethod
    def update_customer(customer_id, name=None, phone=None):
        customers = DataConnector.get_all_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                if name:
                    customer.name = name
                if phone:
                    customer.phone = phone
                DataConnector.save_all_customers(customers)
                print("Customer updated successfully!")
                return
        print("Customer not found!")

    @staticmethod
    def delete_customer(customer_id):
        customers = DataConnector.get_all_customers()
        customers = [c for c in customers if c.customer_id != customer_id]
        DataConnector.save_all_customers(customers)
        print("Customer deleted successfully!")

    @staticmethod
    def add_transaction(customer_id, amount):
        customers = DataConnector.get_all_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                points_earned = int(amount / 10)  # 10% số tiền giao dịch
                customer.points += points_earned
                customer.history.append({"amount": amount, "points_earned": points_earned})
                DataConnector.save_all_customers(customers)
                print("Transaction added, points updated!")
                return
        print("Customer not found!")

    @staticmethod
    def view_transaction_history(customer_id):
        customers = DataConnector.get_all_customers()
        for customer in customers:
            if customer.customer_id == customer_id:
                print("Transaction History:", customer.history)
                return
        print("Customer not found!")