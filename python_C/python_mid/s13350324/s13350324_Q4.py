test_input = "racecar"
#輸入字串。
if test_input == test_input[::-1]:
    print("Palindrome")
#利用切片語法將字串反轉，來判定是否為回文。
else:
    print("Not Palindrome")
