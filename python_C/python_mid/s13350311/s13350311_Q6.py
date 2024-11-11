#6.Subarray with Given Sum
def min_subarray_len(target, nums):
    n = len(nums)
    min_length = float('inf')  # Start with a large value for minimum length
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += nums[end]
        
        # Try to shrink the window until current_sum is less than target
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1
    
    # If min_length was updated, return it; otherwise, return 0
    return min_length if min_length != float('inf') else 0
test_input = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len(target,test_input))

