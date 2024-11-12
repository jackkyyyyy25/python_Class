def smallest_subarray_with_target_sum(test_input, target):
    window_start = 0
    current_sum = 0
    min_length = float("inf") 

    for window_end in range(len(test_input)):
        current_sum += test_input[window_end] 

     
        while current_sum >= target:
            min_length = min(min_length, window_end - window_start + 1)  
            current_sum -= test_input[window_start] 
            window_start += 1 

   
    return min_length if min_length != float("inf") else 0


test_input = [2, 3, 1, 2, 4, 3]
target = 7
print(smallest_subarray_with_target_sum(test_input, target)) 
