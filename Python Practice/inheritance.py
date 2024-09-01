class Vehicle:
    '''this is a vehicle class'''
    mileage = 5.0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print("New Vehicle Created")

    def showMileage(self): 
        return self.mileage
    
    def getMileage(self):
        return self.mileage

class Car(Vehicle):

    def __init__(self,brand, model):
        # super().__init__(brand, name)#no need of self over here
        #or
        Vehicle.__init__(self, brand, model)#self is very important and needs to be here
        print("New Car Created")

    mileage = 6.0
    def showMileage(self):
        return self.mileage
    
v1 = Vehicle("Bajaj","Pulsar")
print(v1.showMileage())

print(c1.getMileage())

c1 = Car("Honda","City")
print(c1.showMileage())