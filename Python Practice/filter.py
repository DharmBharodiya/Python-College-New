def evenNum(num):
    if num%2 == 0:
        return True
    else:
        return False
    
theList = [1,2,4,5,6,7,4,33455,67,345,4]
evenList = list(filter(evenNum, theList))
print(evenList)