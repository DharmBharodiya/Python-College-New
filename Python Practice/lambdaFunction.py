from functools import reduce

def myfunc(n):
    return lambda a:a*n

doubleNum = myfunc(2)
print(doubleNum(11))

#filter() function

numList = [56,67,234,78,23,77]
oddList = list(filter((lambda num: num % 2 != 0), numList))

print(oddList)


newOddList = list(map((lambda num: num % 2 != 0), numList))
print(newOddList)

#reduce() function
result = reduce((lambda a,b: a+b),numList)
print("The result of reduce() function is: ", result)