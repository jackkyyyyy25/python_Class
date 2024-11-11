test_input = [100, 4, 200, 1, 3, 2]

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0
    best_sequence = []
    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            sequence = [num]  
            while num + length in num_set:
                sequence.append(num + length)
                length += 1
            if length > longest:
                longest = length
                best_sequence = sequence  
    return longest, best_sequence

longest_length, sequence = longest_consecutive_sequence(test_input)
print( longest_length,f"(Longest sequence:{sequence})")

