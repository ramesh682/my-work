

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Invalid withdraw amount!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Ramesh", 1000)

account.deposit(500)
account.withdraw(300)
print("Final Balance:", account.get_balance())
