users = []

while True:
    name = input("Enter name (or 'done' to stop): ")
    
    if name.lower() == "done":
        break
    
    age = input("Enter age: ")
    country = input("Enter country: ")

    user = {
        "name": name,
        "age": age,
        "country": country
    }

    users.append(user)

print("\n--- All User ---")

for u in users:
    print("\nUser: ")
    for key, value in u.items():
        print(f"{key}: {value}")