test_input = [2, 3, 1, 2, 4, 3]
target = 7
n = len(test_input)
min_length = float('inf')  
for i in range(n):
    current_sum = 0 
    for j in range(i, n):
        current_sum += test_input[j]  
        if current_sum >= target:
            min_length = min(min_length, j - i + 1)  
            break  
result = min_length if min_length != float('inf') else 0
print(result)  
