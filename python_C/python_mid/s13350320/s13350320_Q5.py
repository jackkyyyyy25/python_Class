test_input = [3,0,1]

for i in range(1,len(test_input)-1):
    if test_input[i]==0:
        print(abs(test_input[i-1]-test_input[i+1])//2+min(test_input[i-1],test_input[i+1]))