#midterm#4
test_input="racecar"
def is_palindrome(test_input):
    return (test_input)==(test_input)[::-1]
if is_palindrome(test_input):
    print("palindrome")
else:
    print("not palindrome")  