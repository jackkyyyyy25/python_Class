test_input = [100, 4, 200, 1, 3, 2]
num_set = set(test_input)
max_length = 0
for num in test_input:

    if num - 1 not in num_set:
        current_num = num
        current_length = 1
        
        while current_num + 1 in num_set:
            current_num += 1
            current_length += 1

        max_length = max(max_length, current_length)

print(max_length)
