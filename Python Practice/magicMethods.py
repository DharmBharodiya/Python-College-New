#magic methods are also called as Dunder method(Double UnderScore) because they've two underscores before and after their name
# this methods are automatically called by the method, and you can change the behaviour of them of how they should behave when they're called on for certain objects of your class
# they are called as the magic methods because python automatically invokes these methods without the need for them to be called separetely

class Boy():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self):
        print(f"{self.name} is of {self.age} years")

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __gt__(self, other):
        return self.age > other.age

    def __contains__(self, name):
        return self.name == name

    def __add__(self, other):
        return int(int(self.age) + int(other.age))


b1 = Boy("Dharm","19")
b3 = Boy("Dharm","19")
b2 = Boy("Dhruvin","20")

print(b1 == b3)
print(b2 > b1)

print("Dharm" in b1)

print(b1 + b3)