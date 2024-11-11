test_input=[3, 0, 1]
test_input.sort()
a=0
for i in range(len(test_input)-1):
    if test_input[i]+1==test_input[i+1]:
        continue
    else:
        a=i+1
print(a)
