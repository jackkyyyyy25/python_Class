test_input = [2, 3, 1, 2, 4, 3]
target = 7

# 獲取陣列長度
n = len(test_input)

# 初始化最小長度為無窮大，當前和為0，起始索引為0
min_length = float('inf')
current_sum = 0
start = 0

# 遍歷每個元素，使用結束索引 'end'
for end in range(n):
    # 將當前元素加入當前和
    current_sum += test_input[end]
    
    # 當前和大於或等於目標和時，嘗試縮小子陣列
    while current_sum >= target:
        # 更新最小長度
        min_length = min(min_length, end - start + 1)
        # 從當前和中減去起始索引的元素，並移動起始索引
        current_sum -= test_input[start]
        start += 1

# 如果最小長度未更新，則返回0；否則返回最小子陣列的長度
result = min_length if min_length != float('inf') else 0
# 輸出結果
print(result)
