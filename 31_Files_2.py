employees = ["Johsua","Ama", "Abena"]

with open("employees.txt", "w",) as file:
    for employee in employees:
        file.write(f"{employee}\n")


with open("employees.txt", "r",) as file:
    content = file.read()

employees = content.splitlines()
print(employees)