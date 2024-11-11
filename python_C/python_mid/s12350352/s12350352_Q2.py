test_input = [100, 4, 200, 1, 3, 2]

def consecutive_sequence(test_input):

    nums_set = set(test_input)
    max_length = 0
    longest_sequence = []

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1
            current_sequence = [current_num]

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1
                current_sequence.append(current_num)

            if current_length > max_length:
                max_length = current_length
                longest_sequence = current_sequence

    print(f"{max_length} (The longest sequence is {longest_sequence})")

consecutive_sequence(test_input)
