test_input = [3, 0, 1]
n = len(test_input)
sum_n = n * (n + 1) //2
sum_test_input = sum(test_input)
missing = sum_n - sum_test_input
print("test_input = [3, 0, 1]")
print("missing number is:", missing)
