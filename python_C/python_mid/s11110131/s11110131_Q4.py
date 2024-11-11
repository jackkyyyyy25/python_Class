def is_palindrome(test_input):
  
    cleaned_input = test_input.replace(" ", "").lower()
    
    if cleaned_input == cleaned_input[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

test_input = "racecar" 
result = is_palindrome(test_input)
print(result)
