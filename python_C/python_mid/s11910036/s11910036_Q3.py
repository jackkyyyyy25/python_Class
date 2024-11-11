# s11910036_Q3.py
test_input = 1234

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(test_input))
