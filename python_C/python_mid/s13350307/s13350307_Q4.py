test_input = "racecar"
a = []
for ch in test_input:
    a.append(ch)
b = "".join(a)
if test_input == b:
    print("Palindrome")
else:
    print("Not Palindrome")