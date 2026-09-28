from employee import Employee 


def add_employee(employees):
    try:
        ID = int(input("\nEnter Employee's ID number: "))
        name = input("Enter Employee's name: ")
        salary = int(input("Enter Employee's salary: "))
        department = input("Enter Employee's department: ")

    except ValueError:
        print("\nInvalid Input Value.")
        return False
    
    for employee in employees:
        if ID == employee.ID:
            print("\nEmployee ID already exist. Enter a new ID.")
            return False
    
    try:
        employee = Employee(ID, name, department, salary)
    except ValueError as e:
        print(f"\n{e}")
        return False
    
    employees.append(employee)
    print("\nEmployee Added successfully")
    return True


def view_employee(employees):
    if not employees:
        print("\nNo Employee Available")
        return
    
    for key, employee in enumerate(employees, start=1):
        print(f"\n{key}. ", end="")
        employee.display_info()


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
        if search in employee.name.lower():
            print(f'\nEmployee ID: {employee.ID}. Employees name: {employee.name} - Employee department: {employee.department} - Employee salary: {employee.salary}')
            found = True
            return
        
    if not found:
        print("\nEmployee not found")


def update_employees(employees):
    if not employees:
        print("\nNo Employee Available")
        return False
    
    old_name = input("\nEnter the name to be updated: ").lower()
    found = False

    for employee in employees:
        if old_name == employee.name.lower():
            try:
                while True:
                    new_ID = int(input("\nEnter Employee's ID number: "))
                    id_taken = False
                    for other_employee in employees:
                        if other_employee.ID == new_ID and other_employee is not employee:
                            id_taken = True
                            break
                    if id_taken:
                        print("\nID already Exist. Try a new one.")
                    else:
                        break
                                
                new_name = input("\nEnter Employee's name: ")
                new_department = input("Enter Employee's department: ")
                new_salary = int(input("Enter Employee's salary: "))
            except ValueError:
                print("\nInvalid Input Value.")
                return False
            
            try:
                employee.update_info(new_ID, new_name, new_department, new_salary)
                
            except ValueError as e:
                print(f"\n{e}")
                return False

            print("\nSuccessfully Updated")
            found = True
            return True 

    if not found:
        print("\nEmployee not found")

            
def remove_employee(employees):
    if not employees:
        print("\nNo Employee Available.")
        return False

    remove_name = input("\nEnter Employee's name to be remove: ").strip()
    if not remove_name:
        print("\nPlease enter an Employee's name.")
        return False
    
    for employee in employees:
        if remove_name.lower() == employee.name.lower():
            employees.remove(employee)
            print("\nSuccessfully deleted")
            return True

    else:
        print("\nEmployee not found.")
        return False    


def employee_statistics(employees):
    if not employees:
        print("\nNo Employee Available")
        return
    
    total_employees = len(employees)

    total_salary = 0
    fourkplus_employees = 0

    highest_salary = employees[0].salary
    highest_paid_employee = employees[0].name

    lowest_salary = employees[0].salary
    lowest_paid_employee = employees[0].name

    for employee in employees:
        total_salary += employee.salary

        if employee.salary > highest_salary:
            highest_salary = employee.salary
            highest_paid_employee = employee.name

        if employee.salary < lowest_salary:
            lowest_salary = employee.salary
            lowest_paid_employee = employee.name

        if employee.salary > 4000:
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
        department = employee.department

        if department not in department_count:
            department_count[department] = 0
        department_count[department] += 1

    for key, value in department_count.items():
        print(f"{key}: {value}")
