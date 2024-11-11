test_input = 1234

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(test_input))
