test_input = [100, 4, 200, 1, 3, 2]
test_input.sort()

between_number=0

len_array=[]

for i in range(len(test_input)-1):
    print(between_number,test_input[i],test_input[i+1])
    if (between_number==0 or test_input[i+1]-test_input[i] != between_number) and (test_input[i]!=test_input[i+1]):
        between_number = test_input[i+1]-test_input[i]
        len_array.append(2)
    elif test_input[i+1]-test_input[i] == between_number:
        len_array[-1]+=1
    elif between_number==0 and test_input[i+1]==test_input[i]:
        len_array[-1]+=1
    else:
        len_array.append(1)
        between_number = test_input[i+1]-test_input[i]

print(max(len_array))



