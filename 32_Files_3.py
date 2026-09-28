with open("employees.txt", "r") as file:
    employees = file.read().splitlines()

print(employees)

if "Ama" in employees:
    employees.remove("Ama")

with open("employees.txt", "w") as file:
    for employee in employees:
        file.write(f"{employee}\n")

for i, value in enumerate(employees, start=1):
    print(i,".",value)