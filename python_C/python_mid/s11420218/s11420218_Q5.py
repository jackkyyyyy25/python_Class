test_input = [3,0,1]
test_input.sort()

for item in test_input: 
    for i in range(1,len(test_input)):
        if test_input[i] != test_input[i-1] + 1: 
            integer = test_input[i] -1 
print(test_input[i]-1)