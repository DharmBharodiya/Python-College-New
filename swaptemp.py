a = 10
b = 20
print("Before swapping - a: ",a," b: ", b)

def swap(a, b):
    temp = a
    a = b
    b = temp
    print("After swapping - a: ", a, " b: ", b)

def swap2(a, b):
    temp = a
    a = b
    b = temp
    return a,b

def swap3(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b

swap(a, b)
print("After swapping: ", swap3(a,b))
