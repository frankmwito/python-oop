# Bank Account Management

class BankAccount:
    def __init__(self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter any amount you wish to deposit: "))
        if account_number == self.account_number:
            self.balance += amount
            print(f"your balance is :  ksh {self.balance}")
        else:
            print("Invalid account number")
        
    def withdraw(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter amount you wish to withdraw: "))
        
        if account_number == self.account_number and amount >= self.balance:
            self.balance -= amount
        else:
            print("Invalid account number or insufficient balance")
            
    def check_balance(self):
        return self.balance
    
bank1 = BankAccount(input("Enter your name: "), int(input("Enter your account number: ")))

bank1.deposit()

bank1.withdraw()

bank1.check_balance()
            