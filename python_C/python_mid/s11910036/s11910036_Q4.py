# s11910036_Q4.py

test_input = "racecar"

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

if is_palindrome(test_input):
    print("Palindrome")
else:
    print("Not Palindrome")
