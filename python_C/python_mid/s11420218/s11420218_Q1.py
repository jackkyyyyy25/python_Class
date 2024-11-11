test_input = "Hello, world! Hello everyone."
test_input = test_input.split(" ")
unique_words = set()

for word in test_input: 
    clean_word = "".join(char for char in word if char.isalnum()).lower()
    if clean_word: 
        unique_words.add(clean_word)
unique_count = len(unique_words)
print(unique_count)