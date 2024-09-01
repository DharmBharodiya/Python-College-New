class vehicle():
    '''this class is for defining the vehicles of all kind'''#docstring
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def printDetails(self):
        print(" Brand: ", self.brand, "\n", "Model: ", self.model)

    def emptyFunction(self):
        pass

print(vehicle.__doc__)#prints the docstring of the class Vehicle
v1 = vehicle("Bajaj","Pulsar")
v1.printDetails()

#changing the attributes for the object properties
v1.brand = "Honda"
v1.printDetails()

#deleting the particular properties of the object
print("Brand: ", v1.brand)
del v1.brand
print("Brand: ", v1.brand)

