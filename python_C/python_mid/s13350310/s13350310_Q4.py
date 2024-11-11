#Q4 判斷字串是否為回文單字

test_input = "racecar"

if test_input == test_input[::-1] :     #判斷字串反轉是否等於原字串
    print("Palindrome")     #是則輸出Palindrome
else:
    print("Not Palindrome")    #不是則輸出Not Palindrome 

#結果為 Palindrome
