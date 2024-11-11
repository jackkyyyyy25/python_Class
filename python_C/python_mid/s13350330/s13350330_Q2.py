#2
test_input = [100, 4, 200, 1, 3, 2]
if not test_input:
    longest_streak = 0
else:
    test_input.sort()
    longest_streak = 1  
    current_streak = 1  
    for i in range(1, len(test_input)):
        if test_input[i] == test_input[i - 1] + 1:
            current_streak += 1  
        elif test_input[i] != test_input[i - 1]:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1  
    longest_streak = max(longest_streak, current_streak)
print(longest_streak) 
