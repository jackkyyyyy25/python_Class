test_input = [3, 0, 1]

# 計算數組的長度 n
n = len(test_input)

# 根據公式計算從 0 到 n 的數字總和
expected_sum = n * (n + 1) // 2

# 計算數組中實際數字的總和
actual_sum = sum(test_input)

# 找出缺少的數字
missing_number = expected_sum - actual_sum

# 輸出缺少的數字
print(missing_number)

