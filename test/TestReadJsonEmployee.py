from libs.JsonFileFactory import JsonFileFactory
from models.Employee import Employee
from models.FulltimeEmployee import FullTimeEmployee
from models.ParttimeEmployee import PartTimeEmployee


def convert_to_employee(obj):
    """Chuyển dictionary thành đối tượng Employee phù hợp dựa trên classname"""
    class_map = {
        "FullTimeEmployee": FullTimeEmployee,
        "PartTimeEmployee": PartTimeEmployee,
        "Employee": Employee
    }

    classname = obj.get("classname", "Employee")  # Lấy classname, mặc định là Employee
    employee_class = class_map.get(classname, Employee)  # Chọn class phù hợp

    # Xóa key "classname" để tránh lỗi
    obj.pop("classname", None)

    # Loại bỏ các key không hợp lệ với class Employee
    if employee_class == Employee:
        obj.pop("months_worked", None)
        obj.pop("days_worked", None)

    return employee_class(**obj)  # Tạo object từ class tương ứng

jff = JsonFileFactory()
filename = "../datasets/employees.json"

# Đọc dữ liệu từ JSON
data = jff.read_data(filename, dict)  # Đọc thành list[dict]

# Chuyển đổi từng dictionary thành đúng class Employee
employees = [convert_to_employee(emp) for emp in data]

print("Danh sách Employee sau khi đọc file:")
for e in employees:
    print(e)