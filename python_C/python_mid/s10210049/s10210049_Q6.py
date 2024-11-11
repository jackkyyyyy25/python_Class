test_input = [2, 3, 2, 2, 4, 3]
target = 7
def min_subarray_len(nums, target):
    left = 0
    total = 0
    min_len = float('inf')
    best_subarray = []
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            current_len = right - left + 1
            if current_len < min_len:
                min_len = current_len
                best_subarray = nums[left:right+1] 
            total -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0, best_subarray

min_length, subarray = min_subarray_len(test_input, target)
print( min_length,f"(smallest subarray{subarray})")

