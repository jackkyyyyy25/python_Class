def min_subarray_len(target, nums):
    left = 0
    total = 0
    min_length = float('inf')

    for right in range(len(nums)):
        total += nums[right] 
        
        
        while total >= target:
            min_length = min(min_length, right - left + 1)  
            total -= nums[left]  
            left += 1 

    return min_length if min_length != float('inf') else 0  


test_input = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len(target, test_input))