from functools import reduce

def added(a, b):
    return a + b

theList = [45,63,234,67,34]
totalSum = reduce(lambda a, b: a + b, theList)
print("The summation of the list is: ", totalSum)