import json
from employee import Employee 

def save_employees(employees):
    employee_data = []

    with open("Employee_Management_System_v2\employee.json", "w") as file:
        
        for employee in employees:
            employee = {
                    "ID": employee.ID,
                    "name": employee.name,
                    "department": employee.department,
                    "salary": employee.salary
                    }
            employee_data.append(employee)
        json.dump(employee_data, file, indent=4)
        
    print("\nEmployees data has been successfully saved.")
    return True

def retrieve_data(employees):
    try:
        with open("Employee_Management_System_v2\employee.json", "r") as file:    
            data = json.load(file)
        employees.clear()

        for employee in data:
            employee_object = Employee(employee["ID"], employee["name"], employee["department"], employee["salary"])
            employees.append(employee_object)
        print("\nEmployees data has been successfully retrieved.")
        return True

    except FileNotFoundError:
        print("\nFile does not exist yet.")
        return False    