#Q1:Unique Words Counter
test_input = "Hello, world! Hello everyone."

for char in '.,!?"\'':  
    test_input = test_input.replace(char, ' ')
test_input = test_input.lower()

words = test_input.split()

unique_words = set(words)

unique_count = len(unique_words)

print(f"{unique_count} (unique words: {', '.join(unique_words)})")
