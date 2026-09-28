user = [] # Create an empty list to store employee names

while True: # Keep the program running until the user exist.
    print("\n======= Employee Manager =======") # Display Employee Manager menu.
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")
    
    choice = input("Choose an option: ") # Ask the user to choose an option.

    if choice == "1": # If the user chooses option 1:
        name = input("Enter Employee's name: ") # Ask the user to enter an emplyee's name.

        employee_data = {"name": name} # Save the Employee's name into the employee list
    
        user.append(employee_data)
        print("Employee successfully added") # Tell the employee was added successfully.
    
    elif choice == "2": # Else if user chooses option 2:
        if len(user) == 0: # Check whether the employee list is empty
            print("No user found.") # if empty, tell tell tell the user there are no employees yet
        else:
            print("\n======= Employee Manager ======")
            for i, u in enumerate(user, start=1):
               print(f"\nuser {i}:")
               for key, value in u.items():
                print(f"{key.capitalize()}: {value.capitalize()}") # Otherwise, display all employees name one by one.

    elif choice == "3": # else if the user chooses option 3:
        print("Goodbye") #say goodbye
        break # stop the program

    else:
        print("Invalid choice. Try again.") # Otherwise: tell them the choice was inalid and should try again
               
