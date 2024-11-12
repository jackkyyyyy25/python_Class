def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
test_input = 1234
result = sum_of_digits(test_input)
print(f"The sum of the digits of {test_input} is: {result}")
