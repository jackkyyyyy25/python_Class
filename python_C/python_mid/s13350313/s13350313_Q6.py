def min_subarray_len(target, nums):
    left = 0 
    current_sum = 0  
    min_length = float('inf')  
    min_subarray = []  

    for right in range(len(nums)):
        current_sum += nums[right]  

        while current_sum >= target:
            
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_subarray = nums[left:right + 1]  
            
            current_sum -= nums[left]  
            left += 1 

    return min_length, min_subarray if min_length != float('inf') else (0, [])

test_input = [2, 3, 1, 2, 4, 3]
target = 7
output_length, smallest_subarray = min_subarray_len(target, test_input)
print(f"{output_length}", "(smallest subarray:", f"{smallest_subarray})")  

