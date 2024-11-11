test_input = [3, 0, 1]
test_input.sort()
first = test_input[0]
for i in range(len(test_input)):
    if test_input[i] != first + i:
        print(first + i)
        break

