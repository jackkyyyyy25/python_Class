test_input='racecar'

Palindrome=True

for i in range(int(len(test_input)//2)):
    if not(test_input[i]==test_input[-i-1]):Palindrome = False

if Palindrome:
    print("Palindrome")
else:
    print("No Palindrome")