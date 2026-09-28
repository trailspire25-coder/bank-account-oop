name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")

user = {
    "name": name,
    "age": age,
    "country": country
}

print("\n--- User Profile ---")

for key, value in user.items():
    print(f"{key}: {value}")
    