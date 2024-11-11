test_input=[100, 4, 200, 1, 3, 2]
test_input.sort()
a=1
for i in range(len(test_input)-1):
    if test_input[i]+1==test_input[i+1]:
        a+=1
    else:
        continue
print(a)
