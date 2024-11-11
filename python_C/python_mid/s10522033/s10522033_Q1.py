import re
test_input = "Hello, world! Hello everyone."
def unique_words_counter(test_input):
    
    words = re.findall(r'\b\w+\b', test_input.lower())
    unique_words = set(words)
    return len(unique_words)

print(unique_words_counter(test_input))

