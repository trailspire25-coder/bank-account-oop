name = input("What is your name?" )
age = int(input("How old are you?" ))

if age == 18:
    print("Hello " + name + ", you're a now an adult")

elif age <= 19:
    print("Hello " + name + ", you're a teenager")

else:
    print("Hello " + name + ", you're an adult")

