test_input =  [100, 4, 200, 1, 3, 5]
test_input.sort()
sequence = []
for i in range(len(test_input) - 1):
    if (test_input[i] + 1 == test_input[i + 1]):
        sequence.append(test_input[i])
sequence.append(sequence[-1] + 1)
print(sequence)