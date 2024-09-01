a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
greater = 0
if a > b and a > c:
    greater = a
elif b > a and b > c:
    greater = b
else:
    greater = c

print("The greatest element among all is: ", greater)