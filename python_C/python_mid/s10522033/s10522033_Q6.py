test_input = [2, 3, 1, 2, 4, 3]
target = 7

def min_subarray_length(nums, target):
    n = len(nums)
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += nums[end]
        
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1

    return min_length if min_length != float('inf') else 0

print(min_subarray_length(test_input, target))
