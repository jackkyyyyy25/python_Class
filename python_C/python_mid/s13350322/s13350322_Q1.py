test_input = "Hello, world! Hello everyone."

word_list = []
word = ""

for char in test_input:
    # 如果是字母，就加到 word 裡面
    if char.isalpha():
        word += char.lower()
    elif word:
        word_list.append(word)
        word = ""
if word:
    word_list.append(word)

print(len(set(word_list)))
