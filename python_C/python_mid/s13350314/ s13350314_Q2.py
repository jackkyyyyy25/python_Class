#2
def Q2(text_input = []):
    # text_input = [100, 4, 200, 1, 3, 2]
    text_input.sort()
    for i in range(len(text_input)-1):
        if text_input[i] + 1 != text_input[i + 1]:
            return i + 1

text_input = [100, 4, 200, 1, 3, 2]
print(Q2(text_input))
