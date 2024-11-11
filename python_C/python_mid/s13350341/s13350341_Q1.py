import string
def unique_words_count(paragraph):
    paragraph = paragraph.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_paragraph = paragraph.translate(translator)
    words = cleaned_paragraph.split()
    unique_words = set(words)
    return len(unique_words)
test_input = "Hello, world! Hello everyone."
result = unique_words_count(test_input)
print(result) 

    