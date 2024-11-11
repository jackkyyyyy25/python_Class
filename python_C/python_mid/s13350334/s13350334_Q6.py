test_input=[2, 3, 1, 2, 4, 3]
target = 7
def m(target,n):
    l=0
    cs=0
    ml=float('inf')
    for r in range(len(n)):
        cs+=n[r]
        while cs>=target:
            ml=min(ml,r-l+1)
            cs-=n[l]
            l+=1
    return ml if ml !=float('inf') else 0
result=m(target,test_input)
print(result)