import string
test_input = "Hello, world! Hello everyone."
test_input = test_input.translate(str.maketrans('', '', string.punctuation)).lower()
words = test_input.split()
unique_words = set(words)
unique_words_count = len(unique_words)
print(unique_words_count) 