test_input = [2, 3, 2, 2, 4, 3]
target = 7
min_lenth = float('inf')
current_sum = 0
l = 0
for  r in range(len(test_input)):
    current_sum +=test_input[r]
    while current_sum >= target:
        min_lenth = min(min_lenth,r - l +1)
        current_sum -= test_input[l]
        l +=1
if min_lenth == float('inf'):
    print(-1)
else:
    print(min_lenth)