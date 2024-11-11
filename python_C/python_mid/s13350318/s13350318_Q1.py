import string

test_input="Hello, world! Hello everyone."
translator=str.maketrans('','',string.punctuation)
cleaned_paragraph=test_input.translate(translator).lower()
words=cleaned_paragraph.split()
unique=set(words)
output="{}(unique words: {})". format(len(unique),', '. join(sorted(unique)))
print(output)
