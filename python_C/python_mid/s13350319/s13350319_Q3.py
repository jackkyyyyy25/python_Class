def sum_of_digits(test_input: int):
    total = 0
    test_input = abs(test_input)

    while test_input > 0:
        total += test_input%10
        test_input //= 10

    print (total)

test_input = 1234
sum_of_digits(test_input)