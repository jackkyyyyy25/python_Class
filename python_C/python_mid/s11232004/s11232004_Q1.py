def count_words(test):
    word = test.replace(',', ' ').replace('!', ' ').replace('.', ' ').replace('?', ' ').lower().split()
    unique_words = set(word)
    return len(unique_words)


test_input = "Hello, world! Hello everyone."

print(count_words(test_input))
