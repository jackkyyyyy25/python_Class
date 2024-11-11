test_input="Hello, world! Hello everyone."
a=test_input
b=a.lower().replace(',', '').replace('.', '').replace('!', '').split()
w=set(b)
w=len(w)
print(w)