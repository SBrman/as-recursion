def exponentWithPowerRule(a, n):
    operationStack = []
    while n > 1:
        if n % 2 == 0:
            operationStack.append('square')
            n = n // 2
        else:
            operationStack.append('multiply')
            n -= 1
    
    result = a
    while operationStack:
        operation = operationStack.pop()
        if operation == 'multiply':
            result *= a
        if operation == 'square':
            result *= result

    return result


if __name__ == "__main__":
    print(exponentWithPowerRule(3, 6))
    print(exponentWithPowerRule(10, 3))
    print(exponentWithPowerRule(17, 10))
