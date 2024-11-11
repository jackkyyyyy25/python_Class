test_input = "Hello, world! Hello everyone"
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for char in punctuation: 
    test_input = test_input.replace(char, "")

list1 = test_input.split()
list1.sort()
j = 0
for i in range(len(list1)):
    j += 1 
    if list1[i] == list1[i-1]:
        j = j-1
    
print(j)