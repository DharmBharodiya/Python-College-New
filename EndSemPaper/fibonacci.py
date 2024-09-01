def finonacci(n):
    fibonacciList = [0,1]
    #here [-1] => 1 and [-2] => 0
    while len(fibonacciList) < n:
        third = fibonacciList[-1] + fibonacciList[-2]
        fibonacciList.append(third)

    return fibonacciList

theList = finonacci(10)
print("The list of fibonacci numbers is: ", theList)