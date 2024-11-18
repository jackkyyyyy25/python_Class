test_input = [4, 3, 1, 2, 6]
target = 8
n = len(test_input)
left = 0
currentsum = 0
minlength = float('inf')
for right in range(n):
    currentsum += test_input[right]
    while currentsum >= target:
        minlength = min(minlength, right - left + 1)
        currentsum -= test_input[left]
        left += 1
if minlength != float('inf'):
    print(minlength)
else:
    print("0")
