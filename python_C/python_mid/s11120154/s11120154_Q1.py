Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def unique_words_count(test_input):
...     # Remove punctuation and convert text to lowercase
...     words = re.findall(r'\b\w+\b', test_input.lower())
...     # Use a set to get unique words
...     unique_words = set(words)
...     # Return the number of unique words
...     return len(unique_words)
... 
... # Test example
... print(unique_words_count("Hello, world! Hello everyone."))  # Output: 3
