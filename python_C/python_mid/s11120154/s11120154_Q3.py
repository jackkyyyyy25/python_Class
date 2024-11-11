Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum_of_digits(test_input):
...     # Calculate the sum of each digit
...     total = sum(int(digit) for digit in str(test_input))
...     # Return the result
...     return total
... 
... # Test example
... print(sum_of_digits(1234))
