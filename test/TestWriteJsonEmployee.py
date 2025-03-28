from models.FulltimeEmployee import FullTimeEmployee
from models.ParttimeEmployee import PartTimeEmployee
from libs.JsonFileFactory import JsonFileFactory

employees = [
    FullTimeEmployee("N001", "Nguyễn Văn Huy", "1990-02-15", "0912345678", "Pha chế", "2021-05-10", 2),
    PartTimeEmployee("N002", "Trần Thị Lan", "1998-07-22", "0923456789", "Phục vụ", "2023-03-12", 12),
    FullTimeEmployee("N003", "Lê Quốc Bảo", "1985-11-10", "0934567890", "Phục vụ", "2020-08-01", 2),
    PartTimeEmployee("N004", "Phạm Minh Anh", "2001-09-05", "0945678901", "Pha chế", "2022-06-18", 10),
    FullTimeEmployee("N005", "Hoàng Thị Kim", "1993-05-30", "0956789012", "Thu ngân", "2019-12-25", 2),
    FullTimeEmployee("N006", "Võ Thành Đạt", "1988-03-12", "0967890123", "Phục vụ", "2018-07-10", 2),
    PartTimeEmployee("N007", "Lý Hồng Phúc", "2002-01-18", "0978901234", "Pha chế", "2023-01-15", 15),
    FullTimeEmployee("N008", "Đặng Minh Khoa", "1995-06-22", "0989012345", "Pha chế", "2020-03-05", 2),
    PartTimeEmployee("N009", "Nguyễn Thanh Trúc", "1999-10-10", "0990123456", "Phục vụ", "2022-09-30", 8),
    FullTimeEmployee("N010", "Bùi Ngọc Duy", "1986-12-25", "0901234567", "Thu ngân", "2017-11-15", 2)
]

print("DANH SÁCH NHÂN VIÊN:")
for emp in employees:
    print(emp)

jff = JsonFileFactory()
filename = "../datasets/employees.json"
jff.write_data(employees, filename)