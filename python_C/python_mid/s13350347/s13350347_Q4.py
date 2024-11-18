test_input = "hello"
word = test_input.replace(" ", "").lower()
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
