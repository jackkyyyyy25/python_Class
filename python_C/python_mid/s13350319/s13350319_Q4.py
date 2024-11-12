def check_palindrome(test_input: str):
    normalized_input = test_input.lower()
    reversed_input = normalized_input[::-1]
    if normalized_input == reversed_input:
        print("Palindrome")
    else:
        print("Not Palindrome")

test_input = "racecar"

check_palindrome(test_input)