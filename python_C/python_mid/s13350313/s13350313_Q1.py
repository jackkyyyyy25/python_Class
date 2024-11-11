import string

test_input = "Hello, world! Hello everyone."

def count_unq_wrds(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()

    words = cleaned_text.split()
    
    unq_wrds = set(words)
    
    print(f"{len(unq_wrds)}" " (unique words:", ", ".join(unq_wrds),")")

count_unq_wrds(test_input)
