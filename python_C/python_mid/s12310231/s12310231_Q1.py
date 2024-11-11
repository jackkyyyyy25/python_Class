import string
test_input= "Hello, world! Hello everyone."
translator = str.maketrans('', '', string.punctuation)
test_input = test_input.translate(translator)
words=test_input.split()
unique_words=set(words)
print(unique_words)

