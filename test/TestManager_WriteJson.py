from libs.JsonFileFactory import JsonFileFactory
from models.Manager import Manager

managers=[]
managers.append(Manager("M1","Huỳnh Mai","mai","132"))
managers.append(Manager("M2","Lê Kim Khoa","khoa","112"))
managers.append(Manager("M3","Phạm Quang Vinh ","vinh","294"))
managers.append(Manager("M4","Lương Ngọc Tâm ","tam","124"))
managers.append(Manager("M5","Đỗ Thùy Trang","trang","123"))

print("Danh sách Manager:")
for m in managers:
    print(m)
jff=JsonFileFactory()
filename="../datasets/managers.json"
jff.write_data(managers,filename)
