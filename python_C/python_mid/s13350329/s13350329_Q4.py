def palindrome_checker(test_input):
    if test_input.lower() == test_input.lower()[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

test_input = "racecar"
palindrome_checker(test_input)  
