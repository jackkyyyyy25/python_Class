# s11910036_Q1.py


test_input = "Hello, world! Hello everyone."

def unique_word_counter(text):
    text = text.lower()
    punctuation = [',', '!', '.', '?', ';', ':', '-', '(', ')', '"', "'"]
    for mark in punctuation:
        text = text.replace(mark, '')
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

print(unique_word_counter(test_input))
