import re
test_input='Hello,world!Hello everyone'
words=re.findall(r'\b\w+\b',test_input.lower())
unique_words=set(words)
print(len(unique_words))


