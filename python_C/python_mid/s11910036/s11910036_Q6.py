# s11910036_Q6.py

test_input = [2, 3, 1, 2, 4, 3]
target = 7

def min_subarray_len(target, nums):
    min_length = float('inf')
    
    for start in range(len(nums)):
        current_sum = 0
        for end in range(start, len(nums)):
            current_sum += nums[end]
            if current_sum >= target:
                min_length = min(min_length, end - start + 1)
                break  

    return min_length if min_length != float('inf') else 0

print(min_subarray_len(target, test_input))
