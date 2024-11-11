def find_missing_number(test_input):
    n = len(test_input)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(test_input)
    missing_number = total_sum - actual_sum
    return missing_number

test_input = [3, 0, 1]  
result = find_missing_number(test_input)
print(result)
