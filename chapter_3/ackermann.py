def ackermann(m, n, indent=None):
    if indent is None:
        indent = 0

    print(' '*indent + f"ackermann({m}, {n})")

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1, indent + 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1, indent + 1), indent + 1)


if __name__ == "__main__":

    print("Starting with m=1, n=1:")
    print(ackermann(1, 1))

    print("Starting with m=2, n=3:")
    print(ackermann(2, 3))
    
