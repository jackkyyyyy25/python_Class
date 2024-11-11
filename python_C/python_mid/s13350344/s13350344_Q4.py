test_input="racecar"
list1=list(test_input)
list2=list1[:]
list2.reverse()
if list1==list2:
    print("Palindrome")
else:
    print("Not Palindrome")
