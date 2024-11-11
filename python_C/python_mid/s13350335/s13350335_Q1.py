test_input = "Hello, world! Hello everyone."
test_input = test_input.lower()
punctuation = ".,!?;:'\"()[]{}<>-"
for char in punctuation:
    test_input = test_input.replace(char,'')
output = len(set(test_input.split()))

print(output)
