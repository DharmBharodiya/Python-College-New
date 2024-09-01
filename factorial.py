num = int(input("Enter a number to find factorial of"))

def factIterative(num):
    fact = 1
    for i in range(1, num + 1):#the loop should must go till the number itself
        fact = fact * i
    return fact

def factRecursive(num):
    fact = 1
    if num == 0 or num == 1:#the facotorial is undefined for the negative numbers
        return 1
     
    return num * factRecursive(num - 1) 
     
print("Factorial of 6 is: ", factIterative(num))
     
