test_input = "12321"

def palindrome_checker(test_input):
    if test_input == test_input[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(palindrome_checker(test_input))
