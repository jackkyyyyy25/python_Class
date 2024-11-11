test_input = [3, 0, 1]
test_input.sort()
n = 0
while True:
    n += 1
    if (test_input[n] + 1) == test_input[n + 1]:
        continue
    else:
        num = test_input[n] + 1
        print(num)
        break
