test_input = "racecar"
processed_input = test_input.replace(" ", "").lower()
if processed_input == processed_input[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
