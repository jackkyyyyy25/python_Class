test_input =  "Special characters: !@#$%^&*() should be ignored."
words = test_input.lower().split()
cleaned_words = []

for word in words:
    cleaned_word = ""
    for char in word:
        if char.isalnum():
            cleaned_word += char
    if cleaned_word:  
        cleaned_words.append(cleaned_word)

unique_words_count = len(set(cleaned_words))
print(unique_words_count)