test_input = "Hello, world! Hello everyone."
import re
def count_unique_words(test_input):
    test_input = test_input.lower()
    test_input = re.sub(r'[^\w\s]', '', test_input)
    words = test_input.split()
    unique_words = set(words)
    return len(unique_words)
print(count_unique_words(test_input))  

