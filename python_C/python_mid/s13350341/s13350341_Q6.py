def smallest_subarray_with_sum(target, nums):
    if not nums or target <= 0:
        return 0
    
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(n):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

test_input = [2, 3, 2, 2, 4, 3]
target = 7
result = smallest_subarray_with_sum(target, test_input)
print(result)
