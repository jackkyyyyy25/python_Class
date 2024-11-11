#5.Find the Missing Number
def find_missing_number(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Test the example
test_input = [3, 0, 1]
print(find_missing_number(test_input))  
