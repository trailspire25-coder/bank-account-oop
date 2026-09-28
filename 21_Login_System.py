correct_username = "admin"
correct_password = "1234"
attempts = 3

while attempts > 0:
    user_name = input("\nEnter Username: ")
    password = input("Enter Password: ")

    if correct_username == user_name and correct_password == password:
        print("\nLogin successful!")
        print("Welcome admin!")
        break

    else:     
        attempts -= 1     # i did reference this
        print("\nIncorrect username or password")
        print(f"Attempts remaining: {attempts}")

        if attempts == 0:
            print("Account Locked")

     
       