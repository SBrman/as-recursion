def exponentByRecursion(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    
    res = exponentByRecursion(a, n//2)
    return res * res * exponentByRecursion(a, n%2)

print(exponentByRecursion(3, 6))
print(exponentByRecursion(10, 3))
print(exponentByRecursion(17, 10))
