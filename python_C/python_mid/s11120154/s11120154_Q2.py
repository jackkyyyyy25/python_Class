Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def longest_consecutive(test_input):
...     # Use a set for quick lookups
...     num_set = set(test_input)
...     longest_streak = 0
... 
...     for num in num_set:
...         if num - 1 not in num_set:
...             current_num = num
...             current_streak = 1
... 
...             while current_num + 1 in num_set:
...                 current_num += 1
...                 current_streak += 1
... 
...             longest_streak = max(longest_streak, current_streak)
... 
...     return longest_streak
... 
... # Test example
... print(longest_consecutive([100, 4, 200, 1, 3, 2]))
