def min_subarray_length(target, test_input):
    n = len(test_input)
    min_length = float('inf')  
    current_sum = 0
    left = 0  

    for right in range(n):
        current_sum += test_input[right] 

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)  
            current_sum -= test_input[left]  
            left += 1

    return min_length if min_length != float('inf') else 0


test_input = [2, 3, 1, 2, 4, 3] 
target = 7                             
result = min_subarray_length(target, test_input)
print(result)
