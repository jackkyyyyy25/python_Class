test_input = [100, 4, 200, 1, 3, 2]
test_input.sort()
a = test_input
print(a)
n=0
current_s = 1
longest_s = 0

n = a[0]
a.remove(a[0])
for i in a:
    if ｉ-1 == n:
        n +=1
        current_s +=1
    else:
        current_s = 1
        n = i
    longest_s = max(current_s,longest_s)
output = longest_s
print(output)
    
