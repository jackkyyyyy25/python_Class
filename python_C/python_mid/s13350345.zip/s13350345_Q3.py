test_input=1234
test=str(test_input)
sum=0
i=0
while i < len(test):
    sum+=eval(test[i])
    i+=1
test_input=sum
print(test_input)