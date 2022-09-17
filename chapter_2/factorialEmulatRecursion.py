callStack = []
callStack.append({"returnAddress": "start", "number": 5})
returnValue = None


while len(callStack) > 0:
    number = callStack[-1]['number']
    returnAddress = callStack[-1]['returnAddress']

    if returnAddress == "start":
        if number == 1:
            returnValue = 1
            callStack.pop()
            continue
        else:
            callStack[-1]['returnAddress'] = 'after recursive call'
            callStack.append({'returnAddress': 'start', 'number': number-1})
            continue
    elif returnAddress == 'after recursive call':
        returnValue = number * returnValue
        callStack.pop()
        continue

print(returnValue)



