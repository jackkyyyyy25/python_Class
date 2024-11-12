#4
def Q4(text_input):
       text_input = ''.join(char.lower() if char.isalnum() else '' for char in str(text_input))
       if text_input != text_input[::-1]:
          return 'Not Palindrome'
       return 'Palindrome'

text_input = 'racecar'
print(Q4(text_input))
