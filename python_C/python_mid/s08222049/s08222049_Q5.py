test_input=[3,0,1]
n = len(test_input)
full_set = set(range(n + 1))
array_set = set(test_input)
missing_numbers = full_set - array_set
a=list(missing_numbers)
b=a[0]
c=int(b)
print(c)
