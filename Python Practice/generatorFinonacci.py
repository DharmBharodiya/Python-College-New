def fib(num):
    p, q = 0, 1
    while(p < num):
        yield p, q
        p, q = q, p+q

x = fib(10)
print("The fibonacci numbers are as followed.")

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x)) # this will throw an "StopIteration" error as the end of iterable is reached