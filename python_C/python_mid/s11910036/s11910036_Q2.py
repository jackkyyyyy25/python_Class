# s11910036_Q2.py

test_input = [100, 4, 200, 1, 3, 2]

def longest_consecutive_sequence(nums):
    if not nums:
        return 0
    
    nums.sort()
    longest_streak = 1
    current_streak = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        elif nums[i] == nums[i - 1] + 1:
            current_streak += 1
        else:
            longest_streak = max(longest_streak, current_streak)
            current_streak = 1

    longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

print(longest_consecutive_sequence(test_input))
