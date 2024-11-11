test_input = [3, 0, 1]
test_input = sorted(test_input)
for i in range(test_input[0],test_input[-1]):
    if i not in test_input:
        print(i)