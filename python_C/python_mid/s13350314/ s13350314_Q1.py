#1
def Q1(text_input):
    text_input = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text_input)
    words = text_input.split()
    unique_words = set(words)
    return len(unique_words)

text_input = "Hello, world! Hello everyone."
print(Q1(text_input))
    