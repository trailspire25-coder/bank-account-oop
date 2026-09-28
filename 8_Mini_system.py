users = []

while True:
    print("\n--- MENU ---")
    print("1. Add User")
    print("2. View User")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        country = input("Enter country: ")

        user ={
            "name": name,
            "age": age,
            "country": country
        }

        users.append(user)
        print("User added successfully!")

    elif choice == "2":
        if len(users) == 0:
            print("No users found.")
        else:
            print("\n--- All Users ---")
            for i, u in enumerate(users, start=1):
                print(f"\nUser {i}:")
                for key, value in u.items():
                    print(f"{key}: {value}")
    
    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid chioce. Try again.")