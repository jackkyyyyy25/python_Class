test_input = [100, 4, 200, 1, 3, 2]

num_set = set(test_input) #將數列轉為集合以便快速查找。
longest_s = 0 #初始化變數，用來儲存最長的連續序列長度。

for num in num_set:
    if num -1 not in num_set:
        c_num = num #num-1不在集合中就變成起點。
        c_s = 1 #初始化當前序列長度為1。

    while c_num + 1 in num_set:
        c_num += 1
        c_s += 1

    longest_s = max(longest_s, c_s)

print(longest_s)
#找到序列中符合規則的數，將其作為起點。
#依序往後找到2、3、4。然而5並不在序列中，因此停止。
#輸出1~4這連續序列的長度。
