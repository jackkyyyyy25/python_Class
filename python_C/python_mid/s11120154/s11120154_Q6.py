Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def min_subarray_len(nums, target):
...     n = len(nums)
...     min_len = float('inf')
...     current_sum = 0
...     left = 0
... 
...     for right in range(n):
...         current_sum += nums[right]
... 
...         while current_sum >= target:
...             min_len = min(min_len, right - left + 1)
...             current_sum -= nums[left]
...             left += 1
... 
...     return min_len if min_len != float('inf') else 0
... 
... # Test the function
... print(min_subarray_len([2, 3, 1, 2, 4, 3], 7))
