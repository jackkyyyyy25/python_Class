def longest_consecutive_sequence(nums):
    if not nums:
        return 0, []  # 返回长度和序列

    num_set = set(nums)  # 将列表转换为集合以便于查找
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

    return longest_streak, longest_sequence

test_input = [100, 4, 200, 1, 3, 2]
length, sequence = longest_consecutive_sequence(test_input)
print(f"The longest sequence is {sequence} ")  
