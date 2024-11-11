def is_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# 測試範例
test_input = "racecar"
is_palindrome(test_input)  # 輸出: "Palindrome"
