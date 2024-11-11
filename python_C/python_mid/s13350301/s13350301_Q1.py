test_input = "Hello, world! Hello everyone."
test_input = test_input.lower()
a = test_input.split()
import re
def remove_punctuation(a):
    return [re.sub(r'[^\w\s]', '', word) for word in a]
b = remove_punctuation(a)
print(b)
