class savingsbank:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("An amount lesser than zero cannot be deposited")
        self.balance = self.balance + amount
    
    def withdraw(self,amount):
        if amount < 0:
            raise ValueError("An amount lesser than zero cannot be withdrawn")
        if amount > self.balance:
            raise ValueError("An amount greater than balance cannot be withdrawn")
        self.balance = self.balance - amount
    
    def get_balance(self):
        return self.balance
    def get_account_number(self):
        return self.account_number
    
number = "10031910"
acc = savingsbank(number,0)

print(f"The account number of the bank account is {acc.get_account_number()}")
print(f"The bank account's balance is {acc.get_balance()}")

try:
    amount = 500
    acc.deposit(amount)
    print(f"The balance of the bank account is {acc.get_balance()}")
except ValueError as e:
    print(f"Error is {e}")

try:
    amount = 5000
    acc.withdraw(amount)
    print(f"The balance of the bank account is {acc.get_balance()}")
except ValueError as e:
    print(f"Error is {e}")
    
