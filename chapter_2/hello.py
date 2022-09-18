NUMBER = 5

print("Code in a loop:")
i = 0
while i < NUMBER:
    print(i, "Hello World")
    i += 1

print("Code in a function:")
def hello(i=0):
    print(i, "Hello World")
    i += 1
    if i >= NUMBER:
        return
    else:
        hello(i)
hello()
