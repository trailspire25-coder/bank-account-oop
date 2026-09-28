def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    return a ** b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose(+, -, *, /, **): ")

if operation == "+":
    print(add(num1, num2))

elif operation == "-":
    print(subtract(num1, num2))

elif operation == "*":
    print(multiply(num1, num2))

elif operation == "/":
    print(divide(num1, num2))

elif operation == "**":
    print(power(num1, num2))

else:
    print("Invalid operation")