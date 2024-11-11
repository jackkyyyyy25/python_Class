#!/usr/bin/env python
# coding: utf-8

# In[2]:


#找缺失號碼
def find_missing_number(nums):
    n = len(nums)  
    expected_sum = n * (n + 1) // 2  #計算0到n的總和
    actual_sum = sum(nums)  #計算總和
    
    missing_number = expected_sum - actual_sum  #計算缺失的數字
    return missing_number


test_input =[3,0,1]
output = find_missing_number(test_input)
print(output)


# In[ ]:




