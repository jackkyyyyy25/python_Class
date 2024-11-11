test_input = [3, 0, 1]

n = len(test_input)
expected_sum = n * (n + 1) // 2
actual_sum = sum(test_input)

print(expected_sum - actual_sum)