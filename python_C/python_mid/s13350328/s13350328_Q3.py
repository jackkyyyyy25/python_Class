
test_input = 1234
sum = 0
while test_input > 0:
    sum = sum + test_input % 10
    test_input = test_input // 10
print(sum)