test_input = "racecar"
reverseWord = ""

for ch in test_input: 
    reverseWord = ch + reverseWord
    
if reverseWord == test_input: 
    print("Palindrome.")
else: 
    print("Not Palindrome.")
