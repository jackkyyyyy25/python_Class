#Q2 找出最長的連續數列

test_input = [100, 4, 200, 1, 3, 2]
test_input.sort()       #整理test_input

longest = 1         #最長起始值設為1
current = 1         #當前計算長度起始值設為1

for i in range(1,len(test_input)):
    
    if test_input[i] == test_input[i - 1] + 1:      #檢查第i位是否比前一位多1 
        current += 1        #current長度加1
    else: 
        longest = max(longest, current)     #取出最大值取代longest
        current = 1         #重置current

print(max(longest, current))

#結果為4
