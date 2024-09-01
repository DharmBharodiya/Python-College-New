class Person:
    def __init__(self, name):
        self.name = name

class Businessman(Person):
    def __init__(self, name, income, noOfMembers):
        super().__init__(name)
        self.income = income
        self.noOfMembers = noOfMembers

class Employee(Person):
    def __init__(self, name, income):
        super().__init__(name)
        self.income = income

def compareIncome(p1, p2):
    if(p1.income > p2.income):
        print(p1.name,"'s income is greater than ", p2.name)
    elif(p1.income < p2.income):
        print(p2.name,"'s income is greater than ", p1.name)
    elif(p1.income == p2.income):
        print(p1.name, "'s income is equal to ", p2.name)

#instantiation
b1 = Businessman("Aayushi", 50000, 15)
e1 = Employee("Dev", 100000)

compareIncome(b1, e1)