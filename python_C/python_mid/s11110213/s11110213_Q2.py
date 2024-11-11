test_input = [100, 4, 200, 1, 3, 2]

# 使用集合來去除重複元素並加快查找速度
nums_set = set(test_input)
longest_streak = 0

# 遍歷每個數字
for num in nums_set:
    # 只從序列的起點開始計算
    if num - 1 not in nums_set:
        current_num = num
        current_streak = 1
        
        # 找到當前序列的長度
        while current_num + 1 in nums_set:
            current_num += 1
            current_streak += 1
        
        # 更新最長序列長度
        longest_streak = max(longest_streak, current_streak)

print(longest_streak)  # 輸出結果

