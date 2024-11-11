test_input = [2, 3, 1, 2, 4, 3]
target = 7
n = len(test_input)
min_length = float('inf')
current_sum = 0
start = 0
for end in range(n):
    current_sum += test_input[end]
    while current_sum >= target:
        min_length = min(min_length, end - start + 1)
        current_sum -= test_input[start]
        start += 1
if min_length == float('inf'):
    print(0)
else:
    print(min_length)
