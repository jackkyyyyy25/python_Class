#6
test_input = [2, 3, 1, 2, 4, 3]
target = 7
min_length = float('inf')  
current_sum = 0            
start = 0                  
for end in range(len(test_input)):
    current_sum += test_input[end]  
    while current_sum >= target:
        min_length = min(min_length, end - start + 1)
        current_sum -= test_input[start]  
        start += 1                        
result = min_length if min_length != float('inf') else 0
print(result)
