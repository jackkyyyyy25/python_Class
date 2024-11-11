def check_palindrome(test):
    new_test = ''.join(char.lower() for char in test if char.isalnum())
    return new_test == new_test[::-1]


test_input = "racecar"
if check_palindrome(test_input):
    print("Palindrome")
else:
    print("Not Palindrome")
