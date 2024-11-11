test_input = [2, 3, 1, 2, 4, 3]
target = 7
def smallest_subarray_with_sum(test_input, target):
    n = len(test_input)
    current_sum = 0
    start = 0
    min_length = float('inf')
    for end in range(n):
        current_sum += test_input[end]          
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= test_input[start] 
            start += 1
    
    return min_length if min_length != float('inf') else 0  
print(smallest_subarray_with_sum(test_input, target))
