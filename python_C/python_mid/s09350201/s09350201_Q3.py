#!/usr/bin/env python
# coding: utf-8

# In[4]:


#數字的總和
def sum_of_digits(n):
    total = 0
    
    # 將數字分解並相加
    while n > 0:
        total += n % 10  
        n //= 10         #去掉最後一位數
    
    return total


test_input = 1234
output = sum_of_digits(test_input)
print(output)


# In[ ]:




