def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

test_input = "racecar"
print(is_palindrome(test_input))
