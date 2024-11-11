test_input="racecar"
s = test_input.lower().replace(" ", "")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
