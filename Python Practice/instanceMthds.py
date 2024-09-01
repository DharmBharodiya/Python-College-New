#to set or get details about the instance of a class
# 'self' parameter is of great importance in the instance methods

class ThisClass:
    def instance_method(self):
        return "This is an instance method"
    
    def instanceMthd2(self):
        '''using the __class__ attribute, which is used to access the class from the instance method itself'''
        print("Hello from the clss: ", self.__class__.__name__)
#instance methods can only be called by the reference of the instance of that particular class
i1 = ThisClass()
print(i1.instance_method())

i1.instanceMthd2()