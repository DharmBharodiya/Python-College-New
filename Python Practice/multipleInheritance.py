class Doctor:
    name = "John"
class Engineer:
    name = "Elon"

class Person(Doctor, Engineer):
    def printNames(self):
        print("Doctor Name: ", Doctor.name)
        print("Engineer Name: ", Engineer.name)

p1 = Person()
p1.printNames()

#method reolustion order(MRO) in python

# this describes or denotes the way a programming language resolves a method or attribute

# it defines the order in which the base classes are searched when executing a method
# it goes form top to bottom: as in first the method is searched in the class and if not found then in the immediate super class
# and it also goes from left to right: as in if a class inherits more than one class then whatever class was referred first during inheritance time, according the classes will be checked for the method
