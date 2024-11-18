test_input = [0]
n = len(test_input)
realsum = n * (n + 1) // 2
testsum = sum(test_input)

miss = realsum - testsum
print(miss)
