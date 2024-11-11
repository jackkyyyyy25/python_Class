test_input = [3, 0, 1]
def find_missing_number(test_input):
    n = len(test_input)
    sum_n = n * (n + 1) // 2 
    sum_actual = sum(test_input)     
    return sum_n - sum_actual  
print(find_missing_number(test_input))
