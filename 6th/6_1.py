class account:
    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.balance = balance
        # print("Welcome, ", self.name," to DBIB")

    def showbalance(self):
        return self.balance
    
    def withdraw(self, withdrawamt):
        if(self.balance > withdrawamt):
            self.balance = self.balance - withdrawamt
            print("Withdrawal successfull.")
            print("New Balance: ", self.showbalance())
        else:
            print("Balance insufficient. Withdrawal not possible.")

    def deposit(self, depositamt):
        print("Depositing.....")
        self.balance = self.balance + depositamt
        print("Deposit Successfull.")
        print("Balance: ", self.showbalance())

    def transfer(self, desacc, transferamt):
        if(self.balance > transferamt):
            self.balance = self.balance - transferamt
            desacc.balance = desacc.balance + transferamt
            print(transferamt, " was debited from ", self.accno, " to ", desacc.accno, " succesfully.")
            print("Current Balance on ", self.accno, ": ", self.balance)
            print("Current Balance in ", desacc.accno, ": ", desacc.balance)


dev = account("Dev", 122017, 100345)
dhruvin = account("Dhruvin",1220034, 87987)

print("Balance of ", dev.name, " is: ", dev.showbalance())

dev.deposit(1000)

# print("Balance of ", dhruvin.name, " is: ", dhruvin.showbalance())
dhruvin.deposit(60000)
dhruvin.withdraw(60000)

dev.transfer(dhruvin, 50000)