test_input="Hello, world! Hello everyone."
ans=['']
doc=[' ', ',', '.', '!', '?','"']
a=''
for i in test_input:
    if i not in doc:
        a+=i
    else:
        if a not in ans:
            ans.append(a)
        a=''
print(len(ans)-1)