test_input = "Hello, world! Hello everyone"
test_input2 = test_input.translate(str.maketrans('', '', ',!'))
test_input3 = set(test_input2.split())
print(len(test_input3))
