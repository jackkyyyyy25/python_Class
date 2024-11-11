def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 測試範例
test_input = 1234
print(sum_of_digits(test_input))  # 輸出: 10
