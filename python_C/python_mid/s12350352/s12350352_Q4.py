test_input="racecar"

def check(word):
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

check(test_input)