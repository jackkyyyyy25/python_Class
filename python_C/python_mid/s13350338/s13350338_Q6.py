test_input = [2, 3, 1, 2, 4, 3]
target = 7

n = len(test_input)
min_length = float('inf')
current_sum = 0
left = 0

for right in range(n):
    current_sum += test_input[right]

    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= test_input[left]
        left += 1

if min_length != float('inf'):
    print(min_length)
else:
    print(0)