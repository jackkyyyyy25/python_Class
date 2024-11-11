Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_palindrome(test_input):
...     # Convert the string to lowercase
...     test_input = test_input.lower()
...     # Check if the string is a palindrome
...     if test_input == test_input[::-1]:
...         return "Palindrome"
...     else:
...         return "Not Palindrome"
... 
... # Test example
... print(is_palindrome("racecar")) 
