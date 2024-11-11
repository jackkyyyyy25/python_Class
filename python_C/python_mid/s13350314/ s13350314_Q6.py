#6
def Q6(text_input, target):
    sum = 0
    start = 0
    min_length = len(text_input) + 1
    for i in range(len(text_input)):
        sum += text_input[i]
        while sum >= target:
            min_length = min(min_length, i - start + 1)
            sum -= text_input[start]
            start += 1
    return min_length

text_input = [2, 3, 1, 2, 4, 3]
print(Q6(text_input, 7))
