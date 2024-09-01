class Bird:
    def fly(self):
        print("With wings")
class Airplane:
    def fly(self):
        print("With fuel")
class Fish:#here the fish don't fly but it still fits in to this because it is acting like other flying objects such as Bird and Airplane, i.e, the properties and the methods are same as that of the other one
    #hence it if walks and quacks like a duck then it is a duck
    # so if it has properties and attributes like something, then the other thing is also that thing(something)
    def fly(self):
        print("With nothing")

for theFuckingObject in Bird(), Airplane(), Fish():
    theFuckingObject.fly()