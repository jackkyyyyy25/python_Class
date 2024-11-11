test_input = [2, 3, 1, 2, 4, 3]
target = 7

def min_subarray_length(test_input, target):
    n = len(test_input)
    left = 0
    current_sum = 0
    min_length = float('inf')
    smallest_subarray = []

    for right in range(n):
        current_sum += test_input[right]

        while current_sum >= target:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                smallest_subarray = test_input[left:right + 1]

            current_sum -= test_input[left]
            left += 1

    return min_length if min_length != float('inf') else 0, smallest_subarray


length, subarray = min_subarray_length(test_input, target)
if length != 0:
    print(f"{length} (smallest subarray {subarray})")
else:
    print(0)
