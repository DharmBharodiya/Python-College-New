theList = [1,2,3,4,1,2,2,3,3,3,4,5,6]

count_dict = {}

for element in theList:
    count = theList.count(element)
    count_dict[element] = count

print(count_dict)