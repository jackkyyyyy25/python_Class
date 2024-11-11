test_input = [2,3,1,2,4,3]
target = 7 
test_input.sort()

for item in test_input: 
    for i in range(0,len(test_input)):
        if item[i] >= target: 
            test_input.remove(item[i])
