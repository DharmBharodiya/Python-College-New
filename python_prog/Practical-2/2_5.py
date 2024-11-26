Num = int(input("Enter a number : ")) 
sum = 0 
while (Num > 0) : 
    rem = Num % 10 
    sum += rem 
    Num //= 10 
print("Sum of Digits = ",sum)