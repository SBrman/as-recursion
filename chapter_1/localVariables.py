def a():
    spam = "Ant"
    print("a: Spam is " + spam)
    b()
    print("a: Spam is " + spam)


def b():
    spam = "Bobcat"
    print("b: Spam is " + spam)
    c()
    print("b: Spam is " + spam)

def c():
    spam = "Coyote"
    print("c: Spam is " + spam)


if __name__ == "__main__":
    a()
