import string

def count_unique_words(paragraph):
    cleaned_text = paragraph.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()
    unique_words = set(words)
    return len(unique_words)
test_input = "Hello, world! Hello everyone."

unique_word_count = count_unique_words(test_input)
print(f"The number of unique words is: {unique_word_count}")
