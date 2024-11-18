test_input=[1, 4, 4]
target=3
n=len(test_input)
prefix_sum=[0]*(n+1)
a=[]
for i in range(1,n+1):
    prefix_sum[i]=prefix_sum[i-1]+test_input[i-1]

min_length= float('inf')

for start in range(n):
    for end in range(start+1,n+1):
        if prefix_sum[end]-prefix_sum[start]>=target:
            min_length=min(min_length, end-start)
            a=test_input[start:end]
            break
if min_length==float('inf'):
    min_length=0
print(min_length,"(smallest subarray",a,")")
        
    
