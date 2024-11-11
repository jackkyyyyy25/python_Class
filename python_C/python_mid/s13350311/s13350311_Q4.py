#4.Palindrome Checker
def is_palindrome(test_input):
    # Normalize the input by removing spaces and converting to lowercase
    normalized_input = test_input.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    if normalized_input == normalized_input[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Example usage
test_input = "racecar"
is_palindrome(test_input)


