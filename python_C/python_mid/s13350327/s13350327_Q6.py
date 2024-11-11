test_input = [2,3,1,2,4,3]
target = 7
n = len(test_input)
min_length = float('inf')
current_sum = 0
start = 0
smallest_subarray = [] 
for end in range(n):
    current_sum += test_input[end]
    while current_sum >= target:
        if end - start + 1 < min_length:
            min_length = end - start + 1
            smallest_subarray = test_input[start:end + 1]

        current_sum -= test_input[start]
        start += 1

if smallest_subarray:
    print("The smallest subarray with the target sum is:", smallest_subarray)
else:
    print("No subarray found with the target sum.")
