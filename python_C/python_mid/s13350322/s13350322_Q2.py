test_input = [100, 4, 200, 1, 3, 2]

num_set = set(test_input)
longest = 0

for num in num_set:
    # 如果 num-1 不在集合中，說明 num 是連續序列的起始點
    if num - 1 not in num_set:
        current_num = num
        current_streak = 1

        # 向右找連續序列
        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1

        longest = max(longest, current_streak)

print(longest)
