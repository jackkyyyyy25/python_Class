test_input="racecar"
a=''
for i in range(len(test_input)-1 , -1 , -1):
    a+=test_input[i]

if a==test_input:
    print('"Palindrome"')
else:
    print('"Not Palindrome"')