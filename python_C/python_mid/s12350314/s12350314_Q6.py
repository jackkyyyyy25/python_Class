test_input = [2, 3, 1, 2, 4, 3]
target = 7
left = 0
blog = 0
min_length = float('inf')
for right in range(len(test_input)):
    blog += test_input[right]
    while blog >= target:
        min_length = min(min_length, right - left + 1)
        blog -= test_input[left]
        left += 1
if min_length == float('inf'):
    print(0)
else:
    print(min_length)