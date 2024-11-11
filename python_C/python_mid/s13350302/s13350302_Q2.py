#Q2:Longest Consecutive Sequence in a List
test_input = [100, 4, 200, 1, 3, 2]

num_set = set(test_input)

longest_streak = 0
longest_sequence = []

for num in num_set:
    if num - 1 not in num_set:
        current_num = num
        current_streak = 1
        current_sequence = [current_num]
        
        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1
            current_sequence.append(current_num)
        
        if current_streak > longest_streak:
            longest_streak = current_streak
            longest_sequence = current_sequence

print(f"{longest_streak} (The longest sequence is {longest_sequence})")
