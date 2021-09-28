class BankAccount:

        def __init__(self, name, email, account_balance, interest_rate): 
                self.name = name
                self.email = email
                self.account_balance = 0
                self.interest_rate = 0.05

        def deposit(self, amount):
                self.account_balance += amount
                return self

        def withdraw(self, amount):
                if (self.balance - amount) > 0:
                        self.account_balance -= amount
                else:
                        print("Insufficient Funds")
                return self
        
        def display_account_info(self):
                print(self.account_balance)

        def yield_interest(self):
                interest_yield = 0
                interest_yield += self.account_balance * self.interest_rate + self.account_balance
                print(interest_yield)

SarahAccount = BankAccount("SarahAccount", "sarah@fake.email", 100, 0.05)

MikeAccount = BankAccount("MikeAccount", "mike@fake.email", 100, 0.05)

SarahAccount.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest()

MikeAccount.deposit(200).deposit(600).withdraw(37).withdraw(50).withdraw(10).withdraw(15).yield_interest()
