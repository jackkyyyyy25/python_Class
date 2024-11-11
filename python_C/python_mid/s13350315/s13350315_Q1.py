
import re
test_input="Hello, world! Hello everyone."
def unique_words(test_input):
    words = re.findall(r'\b\w+\b', test_input.lower())
    unique_words_set = set(words)
    return unique_words_set
unique_words_set = unique_words(test_input)
print("唯一的單字:", unique_words_set)



