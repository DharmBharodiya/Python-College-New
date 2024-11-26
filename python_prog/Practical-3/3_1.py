def FactorialUsingLoop(n) : 
    fact = 1 
    while(n > 0) : 
        fact *= n 
        n -= 1 
    return fact 
 
def FactorialUsingRecursion(n) : 
    if (n == 0) : 
        return 1 
    else : 
        return FactorialUsingRecursion(n-1)*n 
     
n = int(input("Enter a number : ")) 
print("Finding the factorial of a number using iterative formula...!") 
result = FactorialUsingLoop(n) 
print("Factorial of ", n, " is = ", result) 
print("Finding the factorial of a number using recursive formula...!") 
result = FactorialUsingRecursion(n) 
print("Factorial of ", n, " is = ", result) 