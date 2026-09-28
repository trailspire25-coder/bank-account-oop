employees = []
unsaved_changes = False


def add_employee(employees):
    global unsaved_changes
    try:
        ID = int(input("\nEnter Employee's ID number: "))
        name = input("Enter Employee's name: ")
        salary = int(input("Enter Employee's salary: "))
        department = input("Enter Employee's department: ")

    except ValueError:
        print("\nInvalid Input Value.")
        return
    
    for employee in employees:
        if ID == employee["ID"]:
            print("\nEmployee ID already exist. Enter a new ID.")
            return
    
    employee = {
        "ID": ID,
        "name": name,
        "department": department,
        "salary": salary
    }
    employees.append(employee)
    print("\nEmployee Added successfully")
    unsaved_changes = True


def view_employee(employees):
    if not employees:
        print("\nNo Employee Available")
        return
    
    for key, employee in enumerate(employees, start=1):
        print(f'\n{key}. Employee ID: {employee["ID"]} - Employees name: {employee["name"]} - Employee department: {employee["department"]} - Employee salary: {employee["salary"]}')

    
def search_employee(employees):
    if not employees:
        print("\nNo Employee Available")
        return

    search = input("\nEnter the Employee's name: ").lower()
    if not search:
        print("\nPlease enter an Employee's name.")
        return
    
    found = False
    for employee in employees:
        if search in employee["name"].lower():
            print(f'\nEmployee ID: {employee["ID"]}. Employees name: {employee["name"]} - Employee department: {employee["department"]} - Employee salary: {employee["salary"]}')
            found = True
            return
        
    if not found:
        print("\nEmployee not found")


def update_employees(employees):
    global unsaved_changes
    if not employees:
        print("\nNo Employee Available")
        return
    
    old_name = input("\nEnter the name to be updated: ").lower()
    found = False

    for employee in employees:
        if old_name == employee["name"].lower():
            try:
                while True:
                    new_ID = int(input("\nEnter Employee's ID number: "))
                    id_taken = False
                    for other_employee in employees:
                        if other_employee["ID"] == new_ID and other_employee is not employee:
                            id_taken = True
                            break
                    if id_taken:
                        print("\nID already Exist. Try a new one.")
                    else:
                        break
                                
                new_name = input("\nEnter Employee's name: ")
                new_salary = int(input("Enter Employee's salary: "))
                new_department = input("Enter Employee's department: ")
            except ValueError:
                print("\nInvalid Input Value.")
                return
            
            employee["ID"] = new_ID
            employee["name"] = new_name
            employee["department"] = new_department
            employee["salary"] = new_salary
            print("\nSuccessfully Updated")
            found = True
            unsaved_changes = True
            return 

    if not found:
        print("\nEmployee not found")

            
def remove_employee(employees):
    global unsaved_changes
    if not employees:
        print("\nNo Employee Available.")
        return

    remove_name = input("\nEnter Employee's name to be remove: ").strip()
    if not remove_name:
        print("\nPlease enter an Employee's name.")
        return
    
    for employee in employees:
        if remove_name.lower() == employee["name"].lower():
            employees.remove(employee)
            print("\nSuccessfully deleted")
            unsaved_changes = True
            break

    else:
        print("\nEmployee not found.")


def employee_statistics(employees):
    if not employees:
        print("\nNo Employee Available")
        return
    
    total_employees = len(employees)

    total_salary = 0
    fourkplus_employees = 0

    highest_salary = 0
    highest_paid_employee = ""

    lowest_salary = 1000000000000
    lowest_paid_employee = ""

    for employee in employees:
        total_salary += employee["salary"]

        if employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            highest_paid_employee = employee["name"]

        if employee["salary"] < lowest_salary:
            lowest_salary = employee["salary"]
            lowest_paid_employee = employee["name"]

        if employee["salary"] > 4000:
            fourkplus_employees += 1

    average_salary = total_salary / total_employees

    print(f"\nTotal Employees: {total_employees}")
    print(f"Total Salary: {total_salary}")
    print(f"Average Salary: {average_salary:.2f}")

    print(f"\nHighest Paid Employee: {highest_paid_employee} - {highest_salary}")

    print(f"\nLowest Paid Employee: {lowest_paid_employee} - {lowest_salary}")

    print(f"\n{fourkplus_employees}  employees earn more than 4000.")


def department_statistics(employees):
    if not employees:
            print("\nNo Employee Available")
            return

    department_count = {}

    for employee in employees:
        department = employee["department"]

        if department not in department_count:
            department_count[department] = 0
        department_count[department] += 1

    for key, value in department_count.items():
        print(f"{key}: {value}")


def save_employees(employees):
    global unsaved_changes
    with open("employees.txt", "w") as file:
        for employee in employees:
            file.write(f"{employee['ID']},{employee['name']},{employee['department']},{employee['salary']}\n")
    print("\nEmployees data has been successfully saved.")
    unsaved_changes = False


def retrieve_data(employees):
    global unsaved_changes
    while True: 
        
        if unsaved_changes:
            warnings = input("You have unsaved changes.\nRetrieving will discard them.\nContinue? (y/n) ")
            if warnings == "n":
                return
            elif warnings != "y":
                print("Invalid input!")
                continue
            
            employees.clear()
        try:
            with open("employees.txt", "r") as file:
                content = file.read().splitlines()

            for line in content:
                data = line.split(",")
                employee = {
                    "ID": int(data[0]),
                    "name": data[1],
                    "department": data[2],
                    "salary": int(data[3])
                }
                employees.append(employee)
            print("\nEmployees data has been successfully retrieved.")
            unsaved_changes = False
            break

        except FileNotFoundError:
            print("\nFile does not exist yet.")
            break



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
        add_employee(employees)

    elif choice == "2":
        view_employee(employees)

    elif choice == "3":
        search_employee(employees)

    elif choice == "4":
        update_employees(employees)

    elif choice == "5":
        remove_employee(employees)

    elif choice == "6":
        employee_statistics(employees)

    elif choice == "7":
        department_statistics(employees)

    elif choice == "8":
        save_employees(employees)

    elif choice == "9":
            retrieve_data(employees)
    
    elif choice == "10":
        print("\nGoodbye!!!")
        break

    else:
        print("\nInvalid Input. Try again")

