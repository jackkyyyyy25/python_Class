def isPalindrome(test_input):
    return test_input==test_input[::-1]

test_input="racecar"
ans=isPalindrome(test_input)

if ans:
    print("Palindrome")
else :
    print("Nor Palindrome")
