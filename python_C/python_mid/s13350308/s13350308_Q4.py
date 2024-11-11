test_input = "racecar"
a = test_input.lower()
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
