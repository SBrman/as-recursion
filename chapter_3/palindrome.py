def isPalindrome(string):
    if len(string) in {0, 1}:
        return True
    else:
        head = string[0]
        middle = string[1:-1]
        tail = string[-1]

        return head == tail and isPalindrome(middle)

texts = ["racecar", 'tacocat', 'palindrome']
for text in texts:
    print(f"{text} is a palindrome: {isPalindrome(text)}")
