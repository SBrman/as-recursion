def binarySearch(item, items, left=None, right=None):

    print(f"Searching: {items[left:right+1]}")

    if left > right:
        return -1

    mid = (left + right) // 2
    if items[mid] == item:
        return mid
    if items[mid] > item:
        return binarySearch(item, items, left, mid - 1)
    elif items[mid] < item:
        return binarySearch(item, items, mid + 1, right)


if __name__ == "__main__":
    item = 13
    items = [1, 4, 8, 11, 13, 16, 19, 19]
    print(binarySearch(item, items, 0, len(items) - 1))
