#Q5:Find the Missing Number

test_input = [3, 0, 1]

n = len(test_input)

total_sum = (n * (n + 1)) // 2

array_sum = 0

for num in test_input:
    array_sum += num

missing_number = total_sum - array_sum

print(f"{missing_number}")
