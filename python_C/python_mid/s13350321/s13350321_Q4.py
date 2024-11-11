def is_palindrome(s):
    if s.lower()==s.lower()[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
test_input="racecar"
is_palindrome(test_input)
