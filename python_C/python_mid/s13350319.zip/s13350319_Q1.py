import string

def unique_words_counter(test_input):
    test_input = test_input.lower()
    test_input = test_input.translate(str.maketrans('', '', string.punctuation))
    words = test_input.split()
    unique_words = set(words)
    return len(unique_words)

test_input = "Hello, world! Hello everyone."
print(unique_words_counter(test_input))