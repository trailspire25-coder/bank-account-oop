from database import add_product, get_products, update_product, delete_product

def main():
    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Products")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "5":
            break

        elif choice == "1":
            name = input("\nEnter product name: ")
            price = float(input("Enter product price: "))

            add_product(name, price)

        elif choice == "2":
            products = get_products()
            for product in products:
                print(product)

        elif choice == "3":
            new_name = input("\nEnter new product name: ")
            new_price = float(input("Enter new product price: "))
            
            update_product(new_name, new_price)

        elif choice == "4":
            name = input("Enter product name: ")
            delete_product(name)

        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()