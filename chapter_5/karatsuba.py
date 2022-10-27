import math


MULT_TABLE = {i: {j: i*j for j in range(10)} for i in range(10)}


def pad(number: str, padding: int, direction: str) -> str:
    if direction == 'left':
        return '0' * padding + number
    elif direction == 'right':
        return number + '0' * padding 


def equalize_number_lengths(x: str, y: str) -> tuple[str, str]:
    # Pad the the number to make both string length equal
    length_x, length_y = len(x), len(y)
    if length_x < length_y:
        padding = length_y - length_x
        x = pad(number=x, padding=padding, direction='left')
    elif length_y < length_x:
        padding = length_x - length_y
        y = pad(number=y, padding=padding, direction='left')
    return x, y


def karatsuba(x: int, y: int) -> int:
    """
    Multiply large integers without using the '*' operator.
    """
    
    # Get strings
    x, y = str(x), str(y)
    length_x, length_y = len(x), len(y)

    # Get both number string's lengths
    if length_x == 1 and length_y == 1:
        return MULT_TABLE[int(x)][int(y)]
    
    # Equalize the number lengths
    x, y = equalize_number_lengths(x, y)

    # Get a, b, c, d
    half = math.floor(len(x)/2)
    a, b = int(x[:half]), int(x[half:])
    c, d = int(y[:half]), int(y[half:])
    
    # Recursive calls
    res1 = karatsuba(a, c)
    res2 = karatsuba(b, d)
    res3 = karatsuba(a + b, c + d)

    # Get the step3 - step2 - step1
    res4 = res3 - res2 - res1

    # Pad step1 and step4 resutls
    res1_padding = (len(x) - half) + (len(x) - half)   # Can't use the multiply operator
    res1_padded = int(pad(number=str(res1), padding=res1_padding, direction='right'))

    res4_padding = len(x) - half
    res4_padded = int(pad(number=str(res4), padding=res4_padding, direction='right'))
    
    return res1_padded + res2 + res4_padded


if __name__ == "__main__":
    x = 1357
    y = 2468
    print(f'{x} * {y} = {karatsuba(x, y)}')

