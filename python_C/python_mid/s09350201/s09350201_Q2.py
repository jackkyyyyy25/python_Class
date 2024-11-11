#!/usr/bin/env python
# coding: utf-8

# In[8]:


#找出最長連續數列
def longest_consecutive_sequence(nums):
    num_set = set(nums) #使用 set() 去除重複元素並加速查詢
    longest_streak = 0
    longest_sequence = []

    #找尋該元素開頭的連續序列
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            current_sequence = [num]
            
            #依次檢查接下來的數是否連續
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                current_sequence.append(current_num)
            
            # 更新最長連續序列的長度和內容
            if current_streak > longest_streak:
                longest_streak = current_streak
                longest_sequence = current_sequence
    
    return longest_streak, longest_sequence


test_input = test_input = [100, 4, 200, 1, 3, 2]
length, sequence = longest_consecutive_sequence(test_input)
print(f"{length} (The longest sequence is {sequence})")


# In[ ]:




