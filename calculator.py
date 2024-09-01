a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))

print("Press \n 1. for additon \n 2. for substraction \n 3. for multiplication \n 4. for division\n")
userInput = int(input())


def addition(a, b):
    return a + b

def substraction(a, b):
    if(a > b):
        return a - b
    elif(a < b):
        return b - a
    else:
        return 0
    
def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

match userInput:
    case 1:
        print("The addition is: ", addition(a, b))
    case 2:
        print("The substraction is: ", substraction(a, b))
    case 3:
        print("The multiplication is:  ", multiplication(a, b))
    case 4:
        print("The division is: ", division(a, b))
    case _:
        print("No input given")