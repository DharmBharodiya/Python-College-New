def Addition(a,b) : 
    print(a, " + ", b, " = ", a + b) 
 
def Subtraction(a,b) : 
    print(a, " - ", b, " = ", a - b) 
 
def Multiplication(a,b) : 
    print(a, " * ", b, " = ", a * b) 
 
def Division(a,b) : 
    print(a, " / ", b, " = ", a / b) 
 
a = int(input("Enter a : ")) 
b = int(input("Enter b : ")) 
 
print("Enter your choice\n " "1 --> Addition\n 2 --> Subtraction\n 3 --> Multiplication\n 4 --> Division : ") 
choice = int(input()) 
 
if (choice == 1) : 
    Addition(a,b) 
elif (choice == 2) : 
    Subtraction(a,b) 
elif (choice == 3) : 
    Multiplication(a,b) 
elif (choice == 4) : 
    Division(a,b) 
else : 
    print("Invelid Choice..!")