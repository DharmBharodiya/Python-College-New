class BankAccount:
    # accountNumber = None
    # name = None
    # balance = None

    #constructor created
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    # method to deposit into the account
    def deposit(self, depositAmount):
        print("Depositing amount..")
        self.balance += depositAmount
        print("Deposit Successfull.")

    # method to withdraw from the account
    def withdraw(self, withdrawAmount):
        if self.balance <= withdrawAmount:
            print("Insufficient balance to proceed with the withdrawal.")
        else:
            print("Withdrawing amount..")
            self.balance -= withdrawAmount
            print("Withdrawal Successfull.")

    def display(self):
        print(f"Name: {self.name} | Account-No.: {self.accountNumber} | Balance: {self.balance}")


dharm = BankAccount(1,"Dharm",196500)
dharm.display()
dharm.deposit(20000)
dharm.withdraw(10000)
dharm.display()
