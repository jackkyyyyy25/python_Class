test_input=[2, 3, 1, 2, 4, 3]
target = 7
ans=[]
for i in range(len(test_input)):
    num=0
    a=0
    for j in range(i,len(test_input)):
        num+=test_input[j]
        a+=1
    if num%7==0:
        ans.append(a)
print(min(ans))