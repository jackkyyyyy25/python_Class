def solve2(x):
    n  = len(x)
    sum1 = n * (n + 1) // 2
    sum2 = sum(x)
    missing_number = sum1 -sum2
    return missing_number

            
        
test_input = [3,0,1]
n = sorted(test_input)
print(solve2(n))