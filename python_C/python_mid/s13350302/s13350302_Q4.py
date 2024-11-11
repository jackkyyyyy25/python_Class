#Q4:Palindrome Checker
test_input = "racecar"

is_palindrome = True

reversed_input = ""

for char in test_input:
    reversed_input = char + reversed_input

if test_input == reversed_input:
    is_palindrome = True
else:
    is_palindrome = False

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
