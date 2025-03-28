from libs.JsonFileFactory import JsonFileFactory
from models import Customer

jff = JsonFileFactory()
filename = "../datasets/customer.json"
product_list = jff.read_data(filename, Customer)

print("Reading data from json file: ")
for p in product_list:
    print(p)