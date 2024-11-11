import string

# Function to count unique words
def count_unique_words(paragraph):
    
    cleaned_paragraph = paragraph.translate(str.maketrans('', '', string.punctuation)).lower()
    
    words = cleaned_paragraph.split()
    
    unique_words = set(words)
    
    return len(unique_words)


test_input = "Hello, world! Hello everyone."

print("Number of unique words:", count_unique_words(test_input))
