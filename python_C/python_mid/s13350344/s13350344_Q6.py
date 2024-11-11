test_input=[2, 3, 1, 2, 4, 3]
target = 7
n=len(test_input)
listsum=[0]*(n+1)
for i in range(n):
    listsum[i+1]=listsum[i]+test_input[i]
min_len=n+1
for start in range(n):
    for end in range(start+1,n+1):
        currsum=listsum[end]-listsum[start]
        if currsum>=target:
            min_len=min(min_len, end-start)
if min_len!= n+1:
    print(min_len)
else:
    print(0)
