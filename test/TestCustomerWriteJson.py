from libs.JsonFileFactory import JsonFileFactory
from models.Customer import Customer

customers = []
customers.append(Customer("C001", "Nguyen Van A", "0123456789", 100))
customers.append(Customer("C002", "Tran Thi B", "0987654321", 200))
customers.append(Customer("C003", "Le Van C", "0345678912", 150))
customers.append(Customer("C004", "Pham Thi D", "0567891234", 180))
customers.append(Customer("C005", "Hoang Van E", "0678912345", 220))

print("Danh sách khách hàng:")
for a in customers :
    print(a)
jff=JsonFileFactory()
filename="../dataset/customers.json"
jff.write_data(customers,filename)