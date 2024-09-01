from abc import ABC, abstractmethod

class Animal(ABC):# animal interface

    @abstractmethod
    def eat():
        pass

    @abstractmethod
    def sleep():
        pass

        pass

class Dog(Animal):
    def eat(self):
        print("I eat bone.")

    def sleep(self):
        print("I sometimes sleep.")

class Cat(Animal):
    def eat(self):
        print("I drink milk.")
    
    def sleep(self):
        print("I meow and sleep.")

dog = Dog()
dog.eat()