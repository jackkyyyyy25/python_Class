test_input = 1234
def sum_of_digits(test_input):
    return sum(int(digit) for digit in str(test_input))
print(sum_of_digits(test_input)) 
