test_input = [3, 0, 1]
test_input.sort()
max = test_input[-1]
for i in range(max + 1):
    if i not in test_input:
       print(i, "\t".expandtabs(2), end="") 
