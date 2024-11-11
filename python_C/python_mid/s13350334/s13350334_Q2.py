def t(n):
    ns=set(n)
    lon=0
    for i in n:
        if i-1 not in ns:
            l=1
            while i+l in ns:
                l+=1
            lon=max(lon,l)

    return lon
test_input= [100, 4, 200, 1, 3, 2]
print(t(test_input))