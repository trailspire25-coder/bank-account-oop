balance = 1000
pin = 1234

userinput = int(input("Enter Pin: "))

if pin == userinput:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ") 

        if choice == "1": 
            print(f"Your Current Balance is GHs {balance}")

        elif choice == "2":
            deposit = int(input("Enter deposit amount: "))

            if deposit > 0:
                balance = balance + deposit
                print("Deposit Successfull!") 
                print(f"New Balance: GHs {balance}")

            else:
                print("Invalid Deposit Amount")  

        elif choice == "3":
            withdrawal = int(input("Enter withdrawal amount: GHs "))
            
            if withdrawal > balance:
                
                print("Insufficient funds")

            elif withdrawal <= 0:
                print("Invalid Withdrawal Amount")

            else:
                balance = balance - withdrawal
                print("Withdrawal Successfull!")
                print(f"New Balance: GHs {balance}")

        elif choice == "4":
            print("Thank you for using the ATM")
            break

        else:
            print("Invalid Input")
else:
        print("Incorrect PIN!")