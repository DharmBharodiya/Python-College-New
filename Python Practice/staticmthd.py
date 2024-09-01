#unlike the other two methods, this does not requrire any strict first parameter
# this is bound to the class rather than to the instance, also it does not help in changing the states of the class either
# it is there because it needs to be there in that classs

#the decorator @staticmethod is to be used prior to the definition of the static method

# used bascially as utility methods, also which could help the instance and class methods do various other stuffs with the use of static ones

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    @staticmethod
    def is_valid_transaction(amount):
        return amount > 0

    def deposit(self, amount):
        if BankAccount.is_valid_transaction(amount):
            self.balance += amount
            return f"${amount} deposited. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if BankAccount.is_valid_transaction(amount):
            if amount > self.balance:
                return "Insufficient funds"
            self.balance -= amount
            return f"${amount} withdrawn. New balance: ${self.balance}"
        return "Invalid withdrawal amount"

# Creating an instance of BankAccount
account = BankAccount("Alice", 1000)

# Using instance methods and static method
print(account.deposit(200))  # Output: $200 deposited. New balance: $1200
print(account.withdraw(-50))  # Output: Invalid withdrawal amount
