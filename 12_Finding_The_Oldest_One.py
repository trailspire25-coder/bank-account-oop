# User will input (3ages).Find the oldest one

age1 = int(input("Enter Age 1: "))
age2 = int(input("Enter Age 2: "))
age3 = int(input("Enter Age 3: "))

if age1 > age2 and age1 > age3:
    print("Age 1 is the oldest.")

elif age2 > age1 and age2 > age3:
    print("Age 2 is the oldest.")

elif age3 > age1 and age3 > age2:
    print("Age 3 is the oldest.")

elif age1 == age2 and age1 > age3:
    print("Age 1 and 2 are the oldest.")

elif age2 == age3 and age1 > age1:
    print("Age 2 and 3 are the oldest.")

elif age3 == age1 and age3 > age2:
    print("Age 1 and 3 are the oldest.")

else:
    print("All Ages are equal.")