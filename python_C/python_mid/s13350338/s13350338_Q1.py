import string

test_input = "Hello, world! Hello everyone."

normalized_input = test_input.lower()
normalized_input = normalized_input.translate(str.maketrans('', '', string.punctuation))

unique_words = set(normalized_input.split())

unique_word_count = len(unique_words)

print(unique_word_count)