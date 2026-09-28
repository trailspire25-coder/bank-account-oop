product_names = []
quantities = []
prices = []

total_inventory_value = 0

item_range = int(input("How many product do you want to enter: "))

while item_range <= 0:
    item_range = int(input("How many products do you want to enter: "))

for i in range(item_range):
    product = input("Enter product name: ")
    product_names.append(product)

    quantity = int(input("Enter quantity: "))
    quantities.append(quantity)

    price = int(input("Enter price: "))
    prices.append(price)


while True:
    print("\n======= INVENTORY SYSTEM =======")
    print("1. View Inventory")
    print("2. Search Product")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        for i in range(item_range):
    
            inventory_value = quantities[i] * prices[i]
            total_inventory_value += inventory_value

            print(f"\n{product_names[i]}")
            print(f"Quantity: {quantities[i]}")
            print(f"Price: {prices[i]}")
            print(f"Inventory Value: {inventory_value}")

    
            if quantities[i] <= 5:
                print("LOW STOCKS")

        print(f"Total value: {total_inventory_value}")

    elif choice == "2":
        search = input("\nEnter product to search: ")
        found = False
        for i in range(item_range):

            if search == product_names[i]:
                inventory_values = quantities[i] * prices[i]
                print(f"\nProduct: {product_names[i]}")
                print(f"Quantity: {quantities[i]}")
                print(f"Price: {prices[i]}")
                print(f"Inventory Value: {inventory_values}")
                found = True

                if quantities[i] <= 5:
                    print("LOW STOCKS")
                
        if found is False:
            print("Product not found")

    elif choice == "3":
        print("\nGoodbye!!!")
        break

    else:
        print("Invalid option. Try again!!!")


    







