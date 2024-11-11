test_input =  [100, 4, 200, 1, 3, 2]
test_input = sorted(test_input)
count = []
s = 1
for i in range(1,len(test_input)):
    if test_input[i] == test_input[i-1]+1:
        s +=1
    else:
        count.append(s)
        s = 1
count.append(s)

print(max(count))