from functools import reduce

numbers = [1,2,1,1,1,3,4,2,3]
countDict = {}

for num in numbers:

    if num in countDict:
        countDict[num] += 1
    else:
        countDict[num] = 1

print(countDict)

oddOccur = reduce(lambda x,y: x ^ y, numbers)
print("The odd occurence number is: ", oddOccur)