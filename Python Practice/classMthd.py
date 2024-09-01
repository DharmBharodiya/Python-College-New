#class methods is to set or get the details of the class
#they can't access or modify specific instance data, as they are bound to the class instead of the objects

# the decorator @classmethod is to be used before defining one to speicyf that it is the class method
# and the default parameter in it should be 'cls' which is by convention or could be anything that you would like to name it

class ThisClass:
    @classmethod
    def classmthd(cls):
        return "This is a class method"
    
c1 = ThisClass()
print(c1.classmthd())

#or can be directly called without the reference of the object and using the class reference

print(ThisClass.classmthd())

#instance method cannot be called by the reference of the class but only with that of the instance

