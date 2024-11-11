def is_palindrome(s):
    normalized_s = ''.join(s.split()).lower()
    
    if normalized_s == normalized_s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

test_input = "racecar"
output = is_palindrome(test_input)
print(output) 
