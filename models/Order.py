class Order:
    def __init__(self, product_name, quantity, total_price):
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price

    def __str__(self):
        return f"{self.product_name} - SL: {self.quantity}, Tổng: {self.total_price} VND"

    def to_dict(self):
        """Chuyển đối tượng Order thành dict để lưu vào JSON."""
        return {
            "product_name": self.product_name,
            "quantity": self.quantity,
            "total_price": self.total_price
        }