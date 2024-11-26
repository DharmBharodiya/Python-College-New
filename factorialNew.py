num = 10

def factIterative(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

def factRecursive(num):
    if num == 0 or num == 1:
         return 1
    return num * factRecursive(num - 1)

factFinder = factIterative(num)
print("Iterative Approach: ", factFinder)

factFinder2 = factRecursive(num)
print("Recursive Approach: ", factFinder2)

     