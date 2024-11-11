test_input = "racecar"
not_palindrome = 0
for i in range(len(test_input)):
    if test_input[i] != test_input[len(test_input)-i-1]:
        not_palindrome += 1
        break
if not_palindrome == 0:
    print("Palindrome")
else:
    print("Not Palindrome")
            
