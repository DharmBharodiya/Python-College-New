from abc import ABC, abstractmethod

class Polygon(ABC):
    # @abstractmethod #decorator is just there so it can be known that this is an abstract method
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print("Triangle has three sides.")

class Square(Polygon):
    def sides(self):
        print("Square has four sides.")

class Trapezium(Polygon):
    def sides(self):
        print("Trapezium has four sides.")

t = Triangle()
tr = Trapezium()
s = Square()

t.sides()
tr.sides()
s.sides()
