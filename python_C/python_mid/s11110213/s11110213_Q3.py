test_input = 1234

# 計算數字的和
sum_of_digits = 0
n = test_input

while n > 0:
    sum_of_digits += n % 10  # 將最後一位數字加到和上
    n //= 10  # 去掉最後一位數字

# 輸出結果
print(sum_of_digits)

