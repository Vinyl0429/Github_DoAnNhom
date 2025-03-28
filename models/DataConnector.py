from copy import deepcopy

from libs.JsonFileFactory import JsonFileFactory
from models.Customer import Customer
from models.Employee import Employee
from models.FulltimeEmployee import FullTimeEmployee
from models.Manager import Manager
from models.ParttimeEmployee import PartTimeEmployee
from models.Product import Product


class DataConnector:
    @staticmethod
    def get_all_products():
        jff = JsonFileFactory()
        filename = "../datasets/products.json"
        product_list = jff.read_data(filename, Product)
        return product_list

    @staticmethod
    def get_all_employees():
        """Đọc danh sách nhân viên từ JSON và chuyển thành danh sách đối tượng Employee phù hợp"""

        class_map = {
            "FullTimeEmployee": FullTimeEmployee,
            "PartTimeEmployee": PartTimeEmployee,
            "Employee": Employee
        }

        jff = JsonFileFactory()
        filename = "../datasets/employees.json"

        # Đọc dữ liệu từ JSON (list[dict])
        data = jff.read_data(filename, dict)

        employees = []
        for emp_data in data:
            # Tạo bản sao để tránh chỉnh sửa trực tiếp
            emp_dict = deepcopy(emp_data)

            # Xác định class tương ứng
            classname = emp_dict.pop("classname", "Employee")  # Mặc định là Employee
            employee_class = class_map.get(classname, Employee)

            # Loại bỏ các key không hợp lệ với Employee
            if employee_class == Employee:
                emp_dict.pop("day_absence", None)
                emp_dict.pop("shifts_week", None)

            # Tạo object từ class phù hợp
            employees.append(employee_class(**emp_dict))

        return employees

    def get_all_managers(self):
        jff = JsonFileFactory()
        filename = "../datasets/managers.json"
        return jff.read_data(filename, Manager)

    def login(self, username, password):
        """Đăng nhập dựa trên username & password"""
        employees = self.get_all_managers()
        for e in employees:
            if e.UserName == username and e.Password == password:
                return e
        return None

    def updatePassword(self, username, new_password):
        """
        Cập nhật mật khẩu cho nhân viên trong file JSON.
        Trả về True nếu cập nhật thành công, False nếu không tìm thấy username.
        """
        jff = JsonFileFactory()
        filename = "../datasets/managers.json"
        employees = self.get_all_managers()

        for e in employees:
            if e.UserName == username:
                e.Password = new_password  # Cập nhật mật khẩu
                jff.write_data(employees, filename)  # Ghi vào JSON
                return True

        return False  # Không tìm thấy username

    # Hàm đọc dữ liệu khách hàng từ file JSON
    def get_customers_data(self):
        customers_json = "../datasets/customers.json"
        jff = JsonFileFactory()

        try:
            customers_data_list = jff.read_data(customers_json, Customer)
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu từ {customers_json}: {e}")
            customers_data_list = []  # Nếu có lỗi, tạo danh sách rỗng

        return customers_data_list

