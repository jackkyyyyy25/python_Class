def sum_of_numbers(num):
    return sum(int(digit) for digit in str(num))


test_input = 1234
print(sum_of_numbers(test_input))
