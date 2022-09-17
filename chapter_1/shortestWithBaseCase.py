def shortestWithBaseCase(makeRecursiveCall):
    print(f'shortestWithRecursiveCase({makeRecursiveCall}) called.')

    if not makeRecursiveCall:
        print("Returning from base case.")
        return
    else:
        shortestWithBaseCase(False)
        print("Returning from recursive case.")
        return

if __name__ == "__main__":
    print()
    print("Calling shortestWithBaseCase(False)")
    shortestWithBaseCase(False)
    print()

    print("Calling shortestWithBaseCase(True)")
    shortestWithBaseCase(True)
    print()

