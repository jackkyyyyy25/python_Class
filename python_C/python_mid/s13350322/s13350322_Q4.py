test_input = "racecar"

isPalindrome = True

for i in range(len(test_input) // 2):
    if (test_input[i] != test_input[-i - 1]):
        isPalindrome = False
        break

print("Palindrome" if isPalindrome else "Not Palindrome")
