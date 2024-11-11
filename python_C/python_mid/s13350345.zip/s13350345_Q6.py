test_input=[2, 3, 1, 2, 4, 3]
target=7

n = len(test_input)
min_len = float('inf')
current_sum = 0
start = 0
    
for i in range(n):
    current_sum += test_input[i]  
    
    while current_sum >= target:
        min_len = min(min_len, i - start + 1)
        current_sum -= test_input[start]  
        start += 1
if  min_len != float('inf'): 
    print(min_len)
else:
    print(0)