test_input = 1234

sum_of_digits = sum(int(digit) for digit in str(test_input))
#str: 將原本的整數轉為字串型態，好讓系統在字串中直接取數。
#將每個字串中的數字取樣並進行加總，最後輸出結果。

print(sum_of_digits)
