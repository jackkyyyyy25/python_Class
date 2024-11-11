def min_subarray(num_list, target_num):
    left = 0
    current_sum = 0
    length = float('inf')

    for right in range(len(num_list)):
        current_sum += num_list[right]

        while current_sum >= target_num:
            length = min(length, right - left + 1)
            current_sum -= num_list[left]
            left += 1

    return length if length != float('inf') else 0


test_input = [2, 3, 2, 2, 4, 3]
target = 7
print(min_subarray(test_input, target))
