def fib(number):
    a, b = 1, 1
    print(f"{a=}, {b=}")
    for i in range(1, number):
        a, b = b, a+b
        print(f"{a=}, {b=}")
    return a

print(fib(10))
