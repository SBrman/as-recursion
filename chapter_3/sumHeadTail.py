def sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        head = numbers[0]
        tail = numbers[1:]
        return head + sum(tail)

nums = list(range(1, 6))
print(f"Sum of {nums} is {sum(nums)}")

nums = [5, 2, 4, 8]
print(f"Sum of {nums} is {sum(nums)}")

nums = [1, 10, 100, 100]
print(f"Sum of {nums} is {sum(nums)}")
