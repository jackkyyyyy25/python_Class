test_input = [2, 3, 1, 2, 4, 3]
target = 7
#滑動窗口不是給新手寫的，但AI建議我用，我試著學了ㄏㄏ。
min_length = len(test_input) + 1
current_sum = 0 #初始化為0，用來計算當前窗口中的總和。
start = 0 #子陣列的初始位置(滑動窗口)。

for end in range (len(test_input)): #end是窗口的右邊界。
    current_sum += test_input[end]
    
    while current_sum >= target:

        min_length = min(min_length, end - start + 1)

        current_sum -= test_input[start]
        start += 1

if min_length > len(test_input):
    print(0)
else:
    print(min_length)

