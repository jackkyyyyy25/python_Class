test_input="racecar"
i=0
x=-1
while i <= len(test_input)-1:
    if test_input[i] == test_input[x]:
        i+=1
        x-=1
    else:
        break
if i == len(test_input):
    print("Palindrome")
else:
    print("Not Palindrome")

    

    