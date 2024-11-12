test_input = [2,3, 1, 2, 4, 3]
target = 7
s = 0
current_n = 0
smallest = len(test_input) + 1  

left = 0  

for right in range(len(test_input)):
    s += test_input[right] 
    current_n += 1 

    
    while s >= target:
        smallest = min(smallest, current_n)
        s -= test_input[left]  
        left += 1 
        current_n -= 1 


if smallest == len(test_input) + 1:
    print(0) 
else:
    print(smallest) 
