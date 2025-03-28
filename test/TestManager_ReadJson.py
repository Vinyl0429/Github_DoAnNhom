from libs.JsonFileFactory import JsonFileFactory
from models.Manager import Manager


jff=JsonFileFactory()
filename="../datasets/managers.json"
managers=jff.read_data(filename,Manager)
print("Danh sách Manager sau khi đọc file:")
for m in managers:
    print(m)