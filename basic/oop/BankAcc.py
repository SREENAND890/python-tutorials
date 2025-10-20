class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print(" Invalid withdrawal amount.")
        elif amount > self.balance:
            print("balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of  successful. balance: {self.balance}")



BA=BankAccount("john",4000)
print(BA.withdraw(200))