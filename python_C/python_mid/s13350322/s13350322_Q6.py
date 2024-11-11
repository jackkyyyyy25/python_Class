test_input = [2, 3, 1, 2, 4, 3]
target = 7

n = len(test_input)
left, right, current_sum = 0, 0, 0
min_len = float('inf')

while right < n:
    current_sum += test_input[right]

    while current_sum >= target:
        min_len = min(min_len, right - left + 1)
        current_sum -= test_input[left]
        left += 1

    right += 1

print(min_len if min_len != float('inf') else 0)