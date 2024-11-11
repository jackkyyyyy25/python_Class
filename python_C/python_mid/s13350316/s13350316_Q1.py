test_input = "Hello, world! Hello everyone."
punctuation = ",.!?;:"
for p in punctuation:
    test_input = test_input.replace(p, "")
words = test_input.lower().split()
unique_words = set(words)
unique_words_count = len(unique_words)
print(unique_words_count)
