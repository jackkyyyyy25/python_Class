def find_missing_number(nums):
    n = len(nums)  
    expected_sum = n * (n + 1) // 2 
    actual_sum = sum(nums)  
    missing_number = expected_sum - actual_sum 
    return missing_number

test_input = [0, 1, 2, 4] 
print(find_missing_number(test_input))  
