#1
test_input = "Hello, world! Hello everyone."
normalized_input = test_input.lower()  
for char in ".,!;?":
    normalized_input = normalized_input.replace(char, " ")
words = normalized_input.split()
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(len(unique_words)) 
