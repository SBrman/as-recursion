def findSubstringIterative(substring, string):
    i = 0
    length = len(substring)
    while i < len(string):
        if string[i:i+length] == substring:
            return i
        i += 1
    return -1 


def findSubstringRecursive(substring, string, i=0):
    length = len(substring)
    if i >= len(string):
        return -1
    if string[i:i+length] == substring:
        return i
    else:
        return findSubstringRecursive(substring, string, i+1)


if __name__ == "__main__":
    print(findSubstringIterative('substring', 'Find the index of the substring in this sentence.'))
    print(findSubstringRecursive('substring', 'Find the index of the substring in this sentence.'))
