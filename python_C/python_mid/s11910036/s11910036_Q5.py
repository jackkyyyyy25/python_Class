# s11910036_Q5.py

test_input = [3, 0, 1]

def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(find_missing_number(test_input))
