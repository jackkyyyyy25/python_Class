def find_missing_number(test_input):
    n = len(test_input)
    total = ( n * (n+1) ) //2
    real = sum(test_input)
    miss = total - real
    return miss

test_input = [3, 0, 1]
print(find_missing_number(test_input))