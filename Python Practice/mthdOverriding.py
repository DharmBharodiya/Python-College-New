class Vehicle():

    def run(self):
        print("i'm running.")

    def stop(self):
        print("stopppped.")

class Car(Vehicle):

    def run(self):
        print("Car is running")

    def stop(self):
        print("Car stopppped.")

class Bike(Vehicle):

    def run(self):
        print("Car is running")

    def stop(self):
        print("Car stopppped.")

c1 = Car()
b1 = Bike()
v1 = Vehicle()

c1.run()
c1.stop()

b1.run()
b1.stop()

v1.run()
v1.stop()





