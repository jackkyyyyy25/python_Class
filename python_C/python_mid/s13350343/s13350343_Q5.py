test_input = [3 ,0 ,1]

def find_missing_number(test_input):
    n = len(test_input)
    #使用高斯求和公式計算0到n的總和
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(test_input)
    return expected_sum - actual_sum

print(find_missing_number(test_input))
