test_input="Hello, world! Hello everyone."
test_input=test_input.lower()
for char in ",.!?;:'\"":
    test_input=test_input.replace(char,"")
words=test_input.split()
unique_words=set(words)
unique_word_count=len(unique_words)
print(unique_word_count)

