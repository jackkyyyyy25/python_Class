Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def find_missing_number(nums):
...     n = len(nums) + 1
...     expected_sum = n * (n + 1) // 2
...     actual_sum = sum(nums)
...     return expected_sum - actual_sum
... 
... # Test the function
... print(find_missing_number([1, 2, 4, 5, 6]))  
