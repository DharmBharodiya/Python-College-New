#method overloading is not possible in python, instead the latest update method is always called in the case when multiple methods might be having the same name

def add(a,b):
    return a+b
def add(a,b,c):
    return a+b+c

#this will throw an exception because the latest updated method takes three arguments and we have passed only two based on the other method
print(add(2,3))
