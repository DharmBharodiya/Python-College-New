def fib(num):
    p, q = 0, 1
    while(p < num):
        yield p, q
        p, q = q, p+q

x = fib(5)

for i in x:
    print(i)