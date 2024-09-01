from functools import reduce

numbers = [5,10,15,20]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)