#Q6 計算需要多少個test_input中的元素相加達到目標數字

test_input = [2, 3, 1, 2, 4, 3]
target = 7
minl = float('inf')     #設初始最小值為無限大
start = 0 
current = 0         #設當前值為0
n = len(test_input)     #計算test_input的長度

for i in range(n):
    current += test_input[i]        #加總目前偵測到的數字

    while current >= target:        #當current大於target
        minl = min(minl, i - start + 1)     
        current -= test_input[start]        #減去test_input第start位元素來減少current
        start += 1
print(minl)

#結果為2
