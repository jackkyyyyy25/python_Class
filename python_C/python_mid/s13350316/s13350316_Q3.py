test_input = 1234
n_str = str(test_input)
sum_of_digits = 0
for digit in n_str:
    sum_of_digits += int(digit)
print(sum_of_digits)
