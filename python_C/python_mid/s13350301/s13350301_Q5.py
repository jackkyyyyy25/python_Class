def smallest_subarray_with_sum(test_input, target):
    n = len(test_input)
    left = 0
    current_sum = 0
    min_length = float('inf')  
    for right in range(n):
        current_sum += test_input[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= test_input[left]
            left += 1
    return min_length if min_length != float('inf') else 0
test_input = [2, 3, 1, 2, 4, 3]
target = 7
print(smallest_subarray_with_sum(test_input, target))