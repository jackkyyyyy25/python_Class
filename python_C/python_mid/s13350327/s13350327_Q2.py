test_input = [1, 9, 3, 10, 2, 20]
ans = set(test_input)
longest_streak = 0
longest_sequence = []

for test_input in ans:
    if test_input - 1 not in ans:
        current_num = test_input
        current_streak = 1
        current_sequence = [current_num]
        while current_num + 1 in ans:
            current_num += 1
            current_streak += 1
            current_sequence.append(current_num)

        if current_streak > longest_streak:
            longest_streak = current_streak
            longest_sequence = current_sequence

print("test_input = [100,4,200,1,3,2]")
print("The longest consecutive sequence is:", longest_sequence)
