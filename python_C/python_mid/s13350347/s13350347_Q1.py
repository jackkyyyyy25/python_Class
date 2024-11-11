import string
test_input = "Hello, world! Hello everyone."
for char in string.punctuation:
    test_input = test_input.replace(char, '')
uniquewords = set(test_input.lower().split())
print(len(uniquewords))
