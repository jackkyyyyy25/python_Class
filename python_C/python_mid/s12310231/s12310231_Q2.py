test_input=[100,4,200,1,3,2]
def longest_consecutive_sequence(test_input):
    if not test_input:
        return 0
    nums = set(test_input)
    max_length = 0
    for num in nums:
        if num - 1 not in nums:
            current_num = num
            current_length = 1
            while current_num + 1 in nums:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)    
    return max_length
print(longest_consecutive_sequence(test_input))
