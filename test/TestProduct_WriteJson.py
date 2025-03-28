from libs.JsonFileFactory import JsonFileFactory
from models.Product import Product

products = []

products.append(Product("ST123", "Black Coffee", "Beverage", 12, 10))
products.append(Product("ST124", "Latte", "Beverage", 15, 8))
products.append(Product("ST125", "Cappuccino", "Beverage", 14, 12))
products.append(Product("ST126", "Green Tea", "Beverage", 10, 15))
products.append(Product("ST127", "Orange Juice", "Beverage", 11, 9))

products.append(Product("FD201", "Croissant", "Food", 8, 20))
products.append(Product("FD202", "Cheese Cake", "Food", 18, 6))
products.append(Product("FD203", "Muffin", "Food", 10, 14))
products.append(Product("FD204", "Sandwich", "Food", 12, 10))
products.append(Product("FD205", "French Fries", "Food", 9, 25))

for p in products:
    print(p)

jff = JsonFileFactory()
filename = "../datasets/products.json"
product_list = jff.write_data(products, filename)