employees = []
unsaved_changes = False


from employee_functions import add_employee, search_employee, update_employees, remove_employee, view_employee, employee_statistics, department_statistics

from file_functions import save_employees, retrieve_data


while True:
    print("\n====== EMPLOYEE MANAGEMENT SYSTEM ======")
    print("\n1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Remove Employee")
    print("6. Employee Statistics")
    print("7. Department Statistics")
    print("8. Save Employee's Data")
    print("9. Retrieve Employee's Data")
    print("10. Exit")

    choice = input("\nEnter an option: ")  

    if choice == "1":
        if add_employee(employees):
            unsaved_changes = True

    elif choice == "2":
        view_employee(employees)

    elif choice == "3":
        search_employee(employees)

    elif choice == "4":
        if update_employees(employees):
            unsaved_changes = True

    elif choice == "5":
        if remove_employee(employees):
            unsaved_changes = True

    elif choice == "6":
        employee_statistics(employees)

    elif choice == "7":
        department_statistics(employees)

    elif choice == "8":
        if save_employees(employees):
            unsaved_changes = False

    elif choice == "9":
        if unsaved_changes:
            warnings = input("You have unsaved changes.\nRetrieving will discard them.\nContinue? (y/n) ")

            if warnings == "n":
                continue

            elif warnings != "y":
                print("Invalid input!")
                continue

        if retrieve_data(employees):
            unsaved_changes = False
    
    elif choice == "10":
        print("\nGoodbye!!!")
        break

    else:
        print("\nInvalid Input. Try again")

