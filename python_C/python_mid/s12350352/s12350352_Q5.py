test_input = [3, 0, 1]

def missing_number(test_input):
    n = len(test_input)  
    total_sum = n * (n + 1) // 2  
    current_sum = sum(test_input)  
    missing_number = total_sum - current_sum
    return missing_number

print(missing_number(test_input))
