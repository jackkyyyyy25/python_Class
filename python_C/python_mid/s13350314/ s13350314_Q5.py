#5
def Q5(text_input = []):
    text_input.sort()
    for i in range(len(text_input)-1):
        if text_input[i] + 1 != text_input[i + 1]:
            return text_input[i] + 1

text_input = [3,0,1]    
print(Q5(text_input))
