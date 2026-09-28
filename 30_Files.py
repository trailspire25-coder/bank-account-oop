with open("employees.txt", "w") as file:
    file.write("Joe\nYaw\nAma\nBen\nEva\nMart\nAbena\nFred\n")

with open("employees.txt", "r") as file:
    content = file.read()
    employees = content.splitlines()
print(employees)