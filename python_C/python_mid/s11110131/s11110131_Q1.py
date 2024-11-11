import re

def many_words(test_input):
    clean_input = re.sub(r'[^\w\s]', '', test_input).lower()
    words = clean_input.split()
    uni_words = set(words)
    return len(uni_words)
test_input = "Hello, world! Hello everyone"
print(many_words(test_input))
