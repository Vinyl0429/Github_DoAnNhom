class Bill:
    def __init__(self, customer_name, phone_number, pdf_file_name):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.pdf_file_name = pdf_file_name

    def to_dict(self):
        """Chuyển đổi đối tượng Bill thành dict để lưu vào JSON"""
        return {
            "customer_name": self.customer_name,
            "phone_number": self.phone_number,
            "pdf_file": self.pdf_file_name
        }