test_input="Hello, world! Hello everyone."
a=".?!,"
for i in a:
    test_input=test_input.replace(i,"")
list1=test_input.split()
n=set()
for i in range(len(list1)):
    n.add(list1[i])
print(len(n))
