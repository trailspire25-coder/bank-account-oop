# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter a Year: "))

if year%4 == 0 and year%100!= 0:
    print(f"{year} is a Leap Year!")

else:
    print(f"{year} is not a Leap Year!")