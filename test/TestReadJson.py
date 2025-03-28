from libs.JsonFileFactory import JsonFileFactory
from models.Product import Product

jff = JsonFileFactory()
filename = "../datasets/products.json"
product_list = jff.read_data(filename, Product)

print("Reading data from json file: ")
for p in product_list:
    print(p)