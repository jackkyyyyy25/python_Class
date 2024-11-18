test_input = "Python programming is fun! Programming is amazing."

def count_unique_words(test_input):
    test_input = test_input.lower()

    valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789 "
    cleaned_chars = []
    for char in test_input:
        if char in valid_chars:
            cleaned_chars.append(char) 
        else:
            cleaned_chars.append(' ')

    cleaned_input = ''.join(cleaned_chars)
    words = cleaned_input.split()

    unique_words = []
    seen_words = set()

    for word in words:
        if word not in seen_words:
            seen_words.add(word)
            unique_words.append(word)

    print(f"{len(unique_words)} (unique words: {', '.join(unique_words)})")

count_unique_words(test_input)






