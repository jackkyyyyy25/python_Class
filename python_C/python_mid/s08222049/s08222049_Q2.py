test_input=[100, 4, 200, 1, 3, 2]
if not test_input:
    h = 0
else:
   a =list(test_input)
   ac=a.sort()
   b=len(a)
   c=[]
   d=0
   i=0
   for i in range(1,b):
       e=a[i]-a[i-1]
       if e==1:
           d=d+1
       elif e>1:
           c.append(d)
           d==0
           
   c.append(d)
   h=max(c)
      

print(h)
