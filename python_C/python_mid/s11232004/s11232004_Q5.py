def find_missing_number(num_list):
    n = len(num_list)
    total_sum = n * (n + 1) // 2
    real_sum = sum(num_list)
    missing_number = total_sum - real_sum
    return missing_number


test_input = [3, 0, 1]
print(find_missing_number(test_input))
