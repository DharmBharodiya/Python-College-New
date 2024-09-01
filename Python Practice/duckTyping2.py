class Animal():
    def speak(self):
        print("animal is speaking")

class Dog(Animal):
    def speak(self):
        print("BARKKKK")

class Cat(Animal):
    def speak(self):
        print("MEOWOWWWWW")

class Car():
    def speak(self):
        print('VROOOM VROOM')

# here the car is not of the type animal, and still its methd will be called because it has the same set of methods as that of the other animals, hence as it is behacing and looking like animal, it is considered as the one --> this is the basic concept of the duck typing
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()