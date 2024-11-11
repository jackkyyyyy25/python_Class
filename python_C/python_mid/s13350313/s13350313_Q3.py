def sum_of_digits(n):

    return sum(int(digit) for digit in str(abs(n))) 

test_input = 1234
output = sum_of_digits(test_input)
print(f"The sum of the digits in {test_input} is {output}.")  
