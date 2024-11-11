test_input = [100, 4, 200, 1, 3, 2]
test_input.sort()
n = 0
lis1 = []
while n < len(test_input):
    current_sequence = [test_input[n]]
    while n + 1 < len(test_input) and test_input[n + 1] == test_input[n] + 1:
        current_sequence.append(test_input[n + 1])
        n += 1
    if len(current_sequence) > len(lis1):
        lis1 = current_sequence
    n += 1
print(len(lis1))