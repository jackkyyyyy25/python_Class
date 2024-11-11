test_input = [100, 4, 200, 1, 3, 2]

sorted_nums = sorted(set(test_input))

longest_streak = 0
current_streak = 1 

for i in range(1, len(sorted_nums)):
    if sorted_nums[i] == sorted_nums[i - 1] + 1:
        current_streak += 1
    else:
        longest_streak = max(longest_streak, current_streak)
        current_streak = 1

longest_streak = max(longest_streak, current_streak)

print(longest_streak)