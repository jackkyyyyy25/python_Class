import re

def count_unique_words(test_input):
    
    normalized_text = test_input.lower()
    
    words = re.findall(r'\b\w+\b', normalized_text)
    
    unique_words = set(words)
    
    return len(unique_words)


test_input = "Hello, world! Hello everyone."
print(count_unique_words(test_input))