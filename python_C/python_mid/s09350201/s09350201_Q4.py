#!/usr/bin/env python
# coding: utf-8

# In[2]:


#檢查回文
def is_palindrome(s):
    #將字串轉成小寫並去除空格
    s = s.lower().replace(" ", "")
    
    #檢查字符串是否與其反向字符串相同
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

test_input = "racecar"
output = is_palindrome(test_input)
print(output)


# In[ ]:




