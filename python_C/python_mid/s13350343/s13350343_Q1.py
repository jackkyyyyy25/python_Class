test_input = "Hello, world! Hello everyone. "

import re

def unique_words_counter(test_input):
    #將所有字母轉成小寫並移除標點符號
    words = re.findall(r'\b\w+\b', test_input.lower())
    unique_words = set(words)
    return len(unique_words)
print(unique_words_counter(test_input))

