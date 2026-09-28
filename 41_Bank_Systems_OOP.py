class BankAccount:
    bank_name = "Ghana National Bank"

    def __init__(self, account_number, owner, balance):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be a number.")
        if not isinstance(owner, str):
            raise ValueError("Account name must be a text.")
        if balance < 0:
            raise ValueError("Account Balance must not be negative.") 

        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        if deposit < 0:
            raise ValueError("Deposit must not be negative.")
        self.balance += deposit
        return True

    def withdrawal(self, withdrawal):
        if withdrawal < 0:
            raise ValueError("Withdrawal must not be negative.")
        if withdrawal > self.balance:
            raise ValueError("Withdrawal must not be more than deposit.")
        
        self.balance -= withdrawal
        return True

    def display_balance(self):
        print(f"{self.owner}'s current balance: {self.balance}")

    def transfer(self, other_account, amount):
        self.withdrawal(amount)
        other_account.deposit(amount)
        return True
    
    def display_bank(self):
        print(f"Bank: {self.bank_name}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def display_balance(self):  
        super().display_balance()
        print(f"Interest rate: {self.interest_rate}%")

    def apply_interest(self):
        result = self.balance * (self.interest_rate/100)
        self.balance += result
        return True 


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        return True

    def display_accounts(self):
        for account in self.accounts:
            print(f"{account.owner}'s current balance: {account.balance}")

    def find_account(self, account_number):
        for account in self.accounts:
            if account_number == account.account_number:
                return account
            
        return False

    def remove_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)
            return True
        return False

    def transfer_money(self, from_account_number, to_account_number, amount):
        sender = self.find_account(from_account_number)
        reciever = self.find_account(to_account_number)
        if sender and reciever:
            return sender.transfer(reciever, amount)
        return False
            


bank = Bank("Ghana National Bank")
account1 = BankAccount(111, "Joshua", 3000)
account2 = BankAccount(100, "Benard", 100)
savings1 = SavingsAccount(233, "Salomay", 4000, 40)


bank.add_account(account1)
bank.add_account(account2)
bank.add_account(savings1)
bank.display_accounts()

bank.transfer_money(111, 100, 444)

bank.display_accounts()

account = bank.find_account(111)
if account:
    account.display_balance()
else:
    print("Account not found.")

account = bank.remove_account(111)
if account:
    bank.display_accounts()
else:
    print("Account not found.")

savings1.deposit(1000)
savings1.withdrawal(500)
savings1.display_balance()

savings1.apply_interest()
savings1.display_balance()

account1.display_balance()
account2.display_bank()

try:
    result = account1.transfer(account2, 3990)
    if result:
        print("Transfer Successfull.")

except ValueError as e:
    print(e)
    

account1.display_balance()
account2.display_balance()
try:
    result = account1.deposit(324)
    if result:
        print("Deposit Successful.")
except ValueError as e:
    print(e)


account1.display_balance()

account1.withdrawal(2000)
account1.display_balance()

try:
    results = account1.withdrawal(100)
    if results:
        print("Withdrawal Successful.")
except ValueError as e:
    print(e)