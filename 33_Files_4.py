employees = []

try:
    with open("employees.txt","r") as file:
        content = file.read().splitlines()
        for line in content:
            data = line.split(",")
            employee = {
            "name": data[0],
            "department": data[1],
            "salary": int(data[2])
                }
            employees.append(employee)

except FileNotFoundError:
    print("File does not exist yet.")

print(employees)

    