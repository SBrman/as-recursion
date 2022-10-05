def mergesort(items):
    length = len(items)

    if length in {0, 1}:
        return items

    mindex = length // 2
    left = mergesort(items[:mindex])
    right = mergesort(items[mindex:])
    
    sortedList = []
    lindex, rindex = 0, 0

    while len(sortedList) < len(items):
        if left[lindex] < right[rindex]:
            sortedList.append(left[lindex])
            lindex += 1
        else:
            sortedList.append(right[rindex])
            rindex += 1

        if lindex == len(left):
            while rindex != len(right):
                sortedList.append(right[rindex])
                rindex += 1
            break
        elif rindex == len(right):
            while lindex != len(left):
                sortedList.append(left[lindex])
                lindex += 1
            break
    return sortedList


if __name__ == "__main__":
    spam = [2, 9, 8, 5, 3, 4, 7, 6]
    print(mergesort(spam))
