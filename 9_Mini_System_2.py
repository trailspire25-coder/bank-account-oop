users = []

while True:
    print("\n--- MENU ---")
    print("1. Add User")
    print("2. View User")
    print("3. Delete User")
    print("4. Edit User")
    print("5. Search User")
    print("6. Exit")

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
        if len(users) == 0:
            print("No users to delete.")
        
        else:
            print("\n--- Users ---")

            for i, u in enumerate(users, start=1):
                print(f"{i}. {u['name']}")
            
            delete_num = int(input("Enter user number to delete: "))

            if 1 <= delete_num <= len(users):
                remove_user = users.pop(delete_num - 1)
                print(f"{remove_user['name']} deleted successfully!")

            else:
                print("Invalid number.")

    elif choice == "4":
        if len(users) == 0:
            print("No user to edit.")
        
        else:
            print("\n--- Users ---")

            for i, u in enumerate(users, start=1):
                print(f"{i}. {u['name']}")

            edit_num = int(input("Enter user name to edit: "))

            if 1 <= edit_num <= len(users):

                users[edit_num - 1]["name"] = input("New name: ")
                users[edit_num - 1]["age"] = input("New age: ")
                users[edit_num - 1]["country"] = input("New country: ")

                print("User updated successfully!")

            else:
                print("invalid number.")

    elif choice == "5":
        search_name = input("Enter name to search:")

        found = False

        for u in users:
            if u["name"].lower() == search_name.lower():

                print("\nUsers Found:")
                for key, value in u.items():
                    print(f"{key}: {value}")
                
                found =  True
        if not found:
            print("User not found.")

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid chioce. Try again.")