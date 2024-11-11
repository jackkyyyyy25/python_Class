test_input = [100, 4, 200, 3, 2, 5]
test_input.sort()
j = 1
for i in range(len(test_input)):
    if test_input[i] == test_input[i-1] + 1:
        j = j + 1
print(j)