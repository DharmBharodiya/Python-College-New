#a program that accepts a string and coutns the numbner of upper and lower case letters

theStr = input("Enter a string.")

def checkTheString(theStr):
    
    checkDict = {'upper':0,'lower':0}

    for x in theStr:
        if x.isupper():
            checkDict['upper'] += 1
        elif x.islower():
            checkDict['lower'] += 1

    return checkDict

lettersOfString = checkTheString(theStr)
print('UpperCase: ', lettersOfString['upper'], " LowerCase: ", lettersOfString['lower'])