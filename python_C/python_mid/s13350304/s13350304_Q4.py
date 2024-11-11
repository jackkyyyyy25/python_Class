def is_palinedrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
test_input = "racecar"
if is_palinedrome(test_input) == True:
    print('Palindrome')
else:
    print('not Palindrome')