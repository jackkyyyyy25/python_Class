def longest_consecutive(num_list):
    num_set = set(num_list)
    longest_sequence = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_sequence = max(longest_sequence, current_streak)

    return longest_sequence


test_input = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(test_input))
