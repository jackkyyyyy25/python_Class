test_input = [100, 4, 200, 1, 3, 2]
test_input.sort()
thelist = set()  

for i in range(1, len(test_input)): 
    if test_input[i] == test_input[i-1] + 1:
        thelist.add(test_input[i-1])  
        thelist.add(test_input[i])    

print(len(thelist)) 