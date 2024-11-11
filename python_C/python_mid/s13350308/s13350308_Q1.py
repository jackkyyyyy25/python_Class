test_input = "Hello, world! Hello everyone."
test_input = test_input.lower()
test_input = test_input.replace(',','').replace('!','').replace('.','').split()
test_input = set(test_input)
print(len(test_input))

