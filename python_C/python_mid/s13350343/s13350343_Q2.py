test_input = [100, 4, 200, 1, 3, 2]

def longest_consecutive_sequence(test_input):
    num_set = set(test_input)
    longest_streak = 0

    for num in num_set:
        #檢查是否為序列的起始
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print(longest_consecutive_sequence(test_input))
