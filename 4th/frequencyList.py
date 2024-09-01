theList = [1,2,3,4,4,1,1,1,2,3,5,6]
frequency = {}

for element in theList:
    if element in frequency:
        frequency[element] = frequency[element] + 1
    else:
        frequency[element] = 1

print("frequencies for elements of the list: ", theList, " are as followed.")
print(frequency)