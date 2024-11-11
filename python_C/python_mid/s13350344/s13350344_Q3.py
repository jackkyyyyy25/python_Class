test_input=1234
list1=[int(a) for a in str(test_input)]
total=0
for i in range(len(list1)):
    total+=list1[i]
print(total)
