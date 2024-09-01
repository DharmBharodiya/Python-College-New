def increment(num):
    return num + 1

theList = [46,23,45,45,234,56,23]
addList = list(map(increment, theList))
print(addList)