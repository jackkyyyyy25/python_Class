test_input = [100,4,200,1,3,2]
test_input.sort()
long = 1
current = 1
for i in range (1,len(test_input)):
    if test_input[i] == test_input[i-1] + 1:
        current += 1
    elif test_input[i] != test_input[i - 1]:
        long = max(long,current)
        current = 1
a = max(long,current)
print(a)

