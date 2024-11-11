test_input=[100, 4, 200, 1, 3, 2]
num=sorted(test_input)

length=[]
l=1
for i in range(len(num)-1):
    if num[i]+1==num[i+1]:
        l+=1
    else:
        length.append(l)
        l=1
length.append(l)
print(max(length))