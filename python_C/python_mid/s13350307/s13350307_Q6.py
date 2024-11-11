test_input = [2, 3, 1, 2, 4, 3]
target_sum = 7

n = len(test_input)
min_length = n + 1
current_sum = 0
start = 0

for end in range(n):
    current_sum += test_input[end]

    while current_sum >= target_sum:
        min_length = min(min_length, end - start + 1)
        current_sum -= test_input[start]
        start += 1

if min_length <= n:
    print(min_length)
else:
    print("0")
