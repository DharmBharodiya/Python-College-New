def gcdFind(a, b):

    if(a>b):
        min = b
    else:
        min = a

    for i in range(2, min + 1):
        if a%i == 0 and b%i == 0:
            return i
        else:
            return -1
        
a = 20
b = 40
if(gcdFind(a,b) == -1):
    print(f"No GCD of {a} & {b}")
else:
    print(f"The GCD of {a} & {b} is ", gcdFind(a,b))
