def exponentByIteration(a, n):
    res = 1
    for _ in range(n):
        res *= a
    return res


print(exponentByIteration(3, 6))
print(exponentByIteration(10, 3))
print(exponentByIteration(17, 10))
