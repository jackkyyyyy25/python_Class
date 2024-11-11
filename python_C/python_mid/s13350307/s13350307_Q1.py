import string
test_input = "Hello, world!Hello everyone."
cleaned_test_input = test_input.lower().translate(str.maketrans('', '', string.punctuation))
words = cleaned_test_input.split()
unique_words = set(words)
unique_word_count = len(unique_words)
print(unique_word_count)