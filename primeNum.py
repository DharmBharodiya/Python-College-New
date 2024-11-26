def primeNumCheck(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
num = 30

print(f"Is {num} a prime number: ", primeNumCheck(num))
# if primeNumCheck(num):
#     print(f"{num} is a prime number")
# else:
#     print(f'{num} is not a prime number')
