test_input = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
target = 15
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

