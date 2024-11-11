test_input=[100,4,200,1,3,2]
a=sorted(test_input)
for i in range(len(a)):
    now=a[i]
    streak=1
    while (now+1) in a:
        now+=1
        streak+=1
    print(streak)
    

