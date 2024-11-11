#3.Simple Arithmetic-Sum of Digits
def sum_of_digits(n):
    # Convert the integer to a string to easily iterate over each digit
    n = abs(n)  # Take the absolute value in case n is negative
    return sum(int(digit) for digit in str(n))

# Example usage
test_input = 1234
print(sum_of_digits(test_input))


