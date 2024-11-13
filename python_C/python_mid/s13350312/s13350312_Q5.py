test_input=[0, 1]
num=sorted(test_input)

for i in range(len(num)):
    if num[i]+1!=num[i+1]:
        print(num[i]+1)
        break