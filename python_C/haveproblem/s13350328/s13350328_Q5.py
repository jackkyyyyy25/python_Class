test_input = [3 , 0 , 1, 5, 6 ,7 , 9]
test_input.sort()
for i in range(len(test_input)-1):
    if test_input[i] != test_input[i+1] - 1:
        print(test_input[i] + 1)
        