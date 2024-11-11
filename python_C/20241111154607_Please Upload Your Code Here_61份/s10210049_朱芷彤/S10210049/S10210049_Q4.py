test_input = "racecar"

def is_palindrome(s):
    return "Palindrome" if s == s[::-1] else "Not Palindrome"

print(is_palindrome(test_input))
