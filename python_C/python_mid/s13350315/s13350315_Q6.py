test_input = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
current_sum = 0
min_length = float('inf')

for right in range(len(test_input)):
    current_sum += test_input[right]

    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= test_input[left]
        left += 1

result = min_length if min_length != float('inf') else 0
print("最小子數組的長度:", result)
