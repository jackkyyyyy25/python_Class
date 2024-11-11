test_input = "racecar"
s = test_input.lower()
reversed_s = s[::-1]
if s == reversed_s:
    print("Palindrome")
else:
    print("Not Palindrome")
