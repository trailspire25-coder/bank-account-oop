numbers = []

even_count = 0
odd_count = 0
totalnumber = 0

userrange = int(input("How many numbers do you wish to enter: "))

while userrange <= 0:
    userrange = int(input("How many numbers do you wish to enter: ")) 

for i in range(userrange):
    number = int(input("Enter number : "))
    numbers.append(number)

for num in numbers:
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

for num in numbers:
     totalnumber += num
     
largestnumber = max(numbers)
smallestnumber = min(numbers)
average = totalnumber / len(numbers)

print(f"Numbers: {numbers}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Largest number: {largestnumber}")
print(f"Smallest number: {smallestnumber}")
print(f"Total number: {totalnumber}")
print(f"Average number: {average}")