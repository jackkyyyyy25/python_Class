test_input=[100, 4, 200, 1, 3, 2]
test_input.sort()
i=0
while i < len(test_input):
    if test_input[i+1]==test_input[i]+1:
        i+=1
    else:
        break
if i == 0:
    print(0)
else:
    print(len(test_input[0:i+1]))