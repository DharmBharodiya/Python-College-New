class account:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance
        print("Welcome",self.account_no,"To 0ur Bank")
    
    def showbalance(self):
        print("Balance :",self.balance)
    
    def withdraw(self,withdraw):
        self.balance = self.balance - withdraw
        print("Withdraw ",withdraw,"New Balance :",self.balance )
    
    def deposit(self,deposit):
        self.balance = self.balance + deposit
        print("Deposit",deposit,"New Balance",self.balance)
    
    def transfer(self,acc,amount):
        self.balance=self.balance-amount
        acc.balance = acc.balance + amount
        print("New Balance",self.account_no,":",self.balance,"New Balance",acc.account_no,":",acc.balance)

Dev = account(1,10500)
Dev.showbalance()
Dev.withdraw(1000)
Dev.deposit(5000)
Dharm = account(2,50000)
Dev.transfer(Dharm,50)