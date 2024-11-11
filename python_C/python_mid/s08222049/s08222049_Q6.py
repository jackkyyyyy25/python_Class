test_input, target =  [2, 3, 1, 2, 4, 3],7
min_length = float('inf')
for start in range(len(test_input)):
    current_sum = 0 
    for end in range(start, len(test_input)):
        current_sum += test_input[end] 
        if current_sum >= target:
            min_length = min(min_length, end - start + 1)
            if sum(test_input)-1<=target<sum(test_input):
                min_length = min(min_length, end - start)
            break 

output = min_length if min_length != float('inf') else 0

print(output)  
