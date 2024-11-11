test_input = [3, 0, 1]
n = len(test_input)
missing_number = None
for i in range(n + 1):
    if i not in test_input:
        missing_number = i
        break
print(missing_number)  
