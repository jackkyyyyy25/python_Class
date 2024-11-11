test_input = "racecar"

def palindrome_checker(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome_checker(test_input)
