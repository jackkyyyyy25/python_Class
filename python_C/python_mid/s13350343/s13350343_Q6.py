test_input = [2, 3, 1, 2, 4, 3]
target = 7

def min_subarray_len(test_input, target):
    n = len(test_input)
    min_len = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += test_input[end]
        while current_sum >= target:
            min_len = min(min_len, end - start + 1)
            current_sum -= test_input[start]
            start += 1

    return min_len if min_len != float('inf') else 0

print(min_subarray_len(test_input, target))
