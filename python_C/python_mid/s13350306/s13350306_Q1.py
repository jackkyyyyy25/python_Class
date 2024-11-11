import re

def count_unique_words(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    
    unique_words = set(words)
    
    return len(unique_words)

test_input = "Hello, world! Hello everyone."
print(count_unique_words(test_input))  
