test_input = [0, 1, 3]
def find_missing_number(test_input):
    n = len(test_input)
    total_xor = 0
    for i in range(n + 1):
        total_xor ^= i
    actual_xor = 0
    for num in test_input:
        actual_xor ^= num
    return total_xor ^ actual_xor
print(find_missing_number(test_input))
