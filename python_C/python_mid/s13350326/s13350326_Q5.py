test_input=[3, 0, 1]
n=len(test_input)
total_sum=n*(n+1)//2
missing_number = total_sum -sum(test_input)
print(missing_number)