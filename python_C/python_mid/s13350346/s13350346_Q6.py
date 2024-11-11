#midterm#6
def minimal_len(target,num):
    n=len(num)
    minlen=float('inf')
    current=0
    start=0
    for end in range(n):
        current+=num[end]
    while current >= target:
            minlen=min(minlen,end-start+1)
            current-=num[start]
            start+=1
    return minlen if minlen != float('inf') else 0

test_input=[2,3,1,2,4,3]
target=7
print(minimal_len(target,test_input))