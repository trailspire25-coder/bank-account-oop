# User will input (2numbers).Write a program to swap the numbers

num1 = int(input("Input Number 1: "))
num2 = int(input("Input Number 2: "))

temp = num2
num2 = num1
num1 = temp

print(f"Number 1 is {num1}")
print(f"Number 2 is {num2}")