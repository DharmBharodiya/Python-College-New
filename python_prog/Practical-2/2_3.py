a = input("Enter a : ") 
a = int(a) 
b = input("Enrer b : ") 
b = int(b) 
print("Before swapping : a = ",a," & b = ",b) 
a = a + b 
b = a - b 
a = a - b 
print("After swapping : a = ",a," & b = ",b) 

# or a, b = b, a