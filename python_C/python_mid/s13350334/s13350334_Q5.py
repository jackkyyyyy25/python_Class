test_input=[3,0,1]
a=test_input
def l(a):
    n=len(a)
    s=(1+n)*n/2
    z=sum(a)
    m=s-z
    return m
print(l(a))
print(len(a))