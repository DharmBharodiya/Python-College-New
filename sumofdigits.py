#here we will find the sum of all the digits that is in an integer
# for example, integer = 123 then sum = 1 + 2 + 3 => 6
a = (int)(123) #the integer
i = 0
sum = (int)(0)
  

while a != 0:
    lastDigit = (int)(a % 10)
    a = (int)(a / 10)
    sum = sum + lastDigit

print("The sum is: ", sum)
