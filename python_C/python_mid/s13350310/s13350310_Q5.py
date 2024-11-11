#Q5 找到串列中缺少的整數

test_input = [3, 0, 1]

n = len(test_input)     #計算test_input長度

total = n * (n + 1) // 2        #計算應有總和
input_total = sum(test_input)       #計算test_input實際總和
missing = total - input_total       #計算缺失整數

print(missing)

#結果為2
