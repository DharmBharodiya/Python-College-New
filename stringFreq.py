theString = "rrrrrrrrrhhhhhhhh"
alphaDict = {}

for i in theString:

    if i in alphaDict:
        alphaDict[i] += 1
    else:
        alphaDict[i] = 1

print(alphaDict)