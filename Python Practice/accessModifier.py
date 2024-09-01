class Employee:
    name = None
    _job = None#protected

    def __init__(self, name, job, age):
        self.name = name#public
        self._job = job#protected
        self.__age = age#private

    def getName(self):
        return self.name
    def getJob(self):
        return self._job
    def getAge(self):
        return self.__age
    
e1 = Employee("Rohan","Pune",23)


#could easily access the public variables
print(e1.name)
#as in the same package, protected variables can be accessed
print(e1._job)

#this will throw an error because the private variables cannot be accessed outside of the class
# print(e1.__age)

#though the private variables can be accessed by the class methods, "getter" methods basically
print(e1.getAge())

#name mangling in python
print(e1._Employee__age)

#name mangling - here the python automatically generates a new name for the class when the variable is declared with prefix(__) as it would form the private variables, and to save it from outside and unwanted modifications the python generates this name which starts with(_classname__property-name)






