test_input = [2,3,1,2,4,3]
target = 7

stop=False

for i in range(1,len(test_input)+1):
    if stop:break
    for j in range(len(test_input)-i+1):
        sum_i=0
        for _ in range(i):
            sum_i+=test_input[j+_]
        if sum_i==target:
            print(i)
            stop = True
            break



