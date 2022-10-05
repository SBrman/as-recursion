def sumDivConq(numbers):
    length = len(numbers)
    if length == 0:
        return 0
    elif length == 1:
        return numbers[0]
    else:
        mid = length // 2
        return sumDivConq(numbers[:mid]) + sumDivConq(numbers[mid:])


if __name__ == "__main__":
    nums = list(range(1, 6))
    print(sumDivConq(nums))
