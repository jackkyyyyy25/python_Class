def is_palindrome(s):
    normalized_s = s.lower()

    if normalized_s == normalized_s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

test_input = "racecar"
print(is_palindrome(test_input))

