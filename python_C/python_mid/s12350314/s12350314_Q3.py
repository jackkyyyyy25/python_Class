test_input = 1234
result = []
sum = 0
for digit in str(test_input):
    result.append(int(digit))
for i in range(len(result)):
    sum += result[i]
print(sum)