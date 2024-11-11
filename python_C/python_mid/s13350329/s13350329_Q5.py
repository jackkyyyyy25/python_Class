def find_missing_number(test_input):
    n = len(test_input)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(test_input)
    return expected_sum - actual_sum

test_input = [3, 0, 1]
print(find_missing_number(test_input)) 
