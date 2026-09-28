def save_employees(employees):
    with open("Employee_Management_System\employees.txt") as file:
        for employee in employees:
            file.write(f"{employee['ID']},{employee['name']},{employee['department']},{employee['salary']}\n")
    print("\nEmployees data has been successfully saved.")
    return True

def retrieve_data(employees):
    try:
        with open("Employee_Management_System\employees.txt", "r") as file:
            employees.clear()
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
        return True

    except FileNotFoundError:
        print("\nFile does not exist yet.")
        return False    