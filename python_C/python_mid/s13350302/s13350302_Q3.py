#Q3:Simple Arithmetic -Sum of Digits
test_input = 1234

input_str = str(test_input)

sum_of_digits = 0

for char in input_str:
    sum_of_digits += int(char)

print(f'{sum_of_digits}')
