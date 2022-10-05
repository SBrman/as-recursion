def quicksort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1
    if left >= right:
        return 
    
    pivot = items[right]
    i = left
    for j in range(left, right):
        if items[j] <= pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    
    items[right], items[i] = items[i], items[right]

    quicksort(items, left, i - 1)
    quicksort(items, i + 1, right)


if __name__ == "__main__":
    spam = [0, 7, 6, 3, 1, 2, 5, 4]
    quicksort(spam)
    print(spam)
