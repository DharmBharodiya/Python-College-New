class Animal:
    pass

class Dog(Animal):
    pass

class BabyDog(Dog):
    pass

print(BabyDog.__mro__)