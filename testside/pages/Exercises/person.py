class Person:
    # A class representing a person
    def __init__(self, first_name, last_name, account):
        self.first_name = first_name
        self.last_name = last_name
        self.account = account


class Account:
    # A class representing an Account
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Sorry you can't withdraw more than you have in your account")
        else:
            self.balance -= amount


roshan_account = Account()
roshan = Person("Roshan", "Hausammann", roshan_account)

roshan.account.deposit(50)
print(roshan.account.balance)
roshan.account.withdraw(50)
print(roshan.account.balance)
print(roshan.account.balance)
