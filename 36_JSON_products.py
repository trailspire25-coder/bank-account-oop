import json

total_value = 0

with open("products.json", "r") as file:
    products = json.load(file)
    
    for product in products:
        print(product["name"], product["price"], product["stock"])
        total_value += product["price"] * product["stock"]
    print(total_value)

    products[0]["stock"] = 2

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)
print(products[0]["stock"])