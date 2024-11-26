# b) Declare a class Person having name as member. Derive two classes
#   a. Businessman - having income and number of people
#                   involved in his business as members.
#   b. Employee - having income as a member.
#   c. Create objects of both the classes and compare the income and print the
#                name of one having greater income.
class Person:
    def __init__(self,name):
        self.name = name

class Businessman(Person):
    def __init__(self, name,income,no_of_members):
        super().__init__(name)
        self.income = income
        self.no_of_members = no_of_members

class Empolyee(Person):
    def __init__(self, name,income):
        super().__init__(name)
        self.income = income
def income_comparison(o1,o2):
    if(o1.income>o2.income):
        print(o1.name,"income is greater than the",o2.name )
    elif(o1.income<o2.income):
        print(o2.name,"income is greater than the",o1.name )
    else:
        print(o1.name,"income is equal to the ",o2.name )

obj1 = Businessman("Dharm",10000000,"6")
obj2 = Empolyee("Dhruvan",7000000)
income_comparison(obj1,obj2)
