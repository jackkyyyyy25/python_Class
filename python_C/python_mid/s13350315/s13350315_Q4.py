test_input = "racecar"
s = test_input.lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")