from datetime import datetime

class Customer:
    def __init__(self, name, phone, points=0, total_payment=0, last_transaction_time=None):
        self.name = name
        self.phone = phone
        self.points = points
        self.total_payment = total_payment
        self.last_transaction_time = last_transaction_time or datetime.now().strftime("%d/%m/%Y %H:%M")

    def __str__(self):
        return (f"Customer(Name: {self.name}, Phone: {self.phone}, "
                f"Points: {self.points}, Total Payment: {self.total_payment} VND, "
                f"Last Transaction: {self.last_transaction_time})")

    def add_transaction(self, total_payment):
        """Cập nhật giao dịch"""
        self.total_payment += total_payment
        self.points += total_payment // 1000
        self.last_transaction_time = datetime.now().strftime("%d/%m/%Y %H:%M")
