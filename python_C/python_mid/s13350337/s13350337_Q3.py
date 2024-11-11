test_input = 1234
total = 0
while test_input > 0:
    total += test_input % 10  
    test_input //= 10  
print(total)  
