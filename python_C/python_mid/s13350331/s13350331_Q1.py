import string
test_input = "Hello,world! Hello everyone."
cleaned_input = test_input.translate(str.maketrans('', '', string.punctuation)).lower()
words = cleaned_input.split()
unique_words = set(words)
print(len(unique_words))
