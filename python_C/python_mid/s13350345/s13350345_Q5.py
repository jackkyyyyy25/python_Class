test_input=[3, 0, 1]
test_input.sort()
i=0
while i <= len(test_input):
    if test_input[i]+1 == test_input[i+1]:
        i += 1
    else:
        break
print(test_input[i]+1)