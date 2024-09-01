def multiply(n):
    return lambda a: a * n

multiplicant = multiply(5)
print(multiplicant(3))