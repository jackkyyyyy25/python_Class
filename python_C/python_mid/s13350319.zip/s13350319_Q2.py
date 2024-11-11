def longest_consecutive_sequence(test_input):

    nums_set = set(test_input)
    longest = 0
    
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1
            
            longest = max(longest, current_streak)
    
    return longest

test_input = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(test_input))