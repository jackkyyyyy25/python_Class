#3
def Q3(text_input):
    sum = 0
    for digit in str(text_input):
        sum += int(digit)
    return sum

text_input = 1234
print(Q3(text_input))
