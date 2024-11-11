test_input="racecar"
test_input=test_input.lower()
test_input = ''.join(char for char in test_input.lower() if char.isalnum())
if test_input==test_input[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
