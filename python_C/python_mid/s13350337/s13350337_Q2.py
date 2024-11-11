test_input = [100, 4, 200, 1, 3, 2]
longest = 0
for num in test_input:
    if num - 1 not in test_input:
        currentNum = num
        currentStreak = 1
        while currentNum + 1 in test_input:
            currentNum += 1
            currentStreak += 1
        longest = max(longest, currentStreak)
print(longest)  

