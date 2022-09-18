def reverse(string):
    if len(string) in {0, 1}:
        return string
    head = string[0]
    tail = string[1:]
    return reverse(tail) + head


def reverse2(string):
    if len(string) in {0, 1}:
        return string
    tail = string[-1]
    head = string[:-1]
    return tail + reverse2(head)


print(reverse("abcdef"))
print(reverse("Hello, world!"))
print(reverse(""))
print(reverse("X"))

print()

print(reverse2("abcdef"))
print(reverse2("Hello, world!"))
print(reverse2(""))
print(reverse2("X"))
