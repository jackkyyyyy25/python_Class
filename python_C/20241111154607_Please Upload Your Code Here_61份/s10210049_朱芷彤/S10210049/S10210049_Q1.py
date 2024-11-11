test_input = "Hello, world! Hello everyone."
import re
words = re.findall(r'\b\w+\b', test_input.lower())
unique_words = set(words)
print(len(unique_words),f"(unique words:{unique_words})")
