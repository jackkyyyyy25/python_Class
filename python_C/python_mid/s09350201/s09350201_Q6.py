#!/usr/bin/env python
# coding: utf-8

# In[7]:


#最小子數組與總和
def smallest_subarray_with_sum(nums, target):
    n = len(nums)
    current_sum = 0
    left = 0 
    min_length = None  #使用None作為標記，表示尚未找到有效的子數組
    smallest_subarray = []  #用來儲存最小子數組

    for right in range(n):
        print(type(nums[right]))
        print(type(current_sum))
        current_sum += nums[right] 
        
        #當前總和達到或超過目標時，開始縮小範圍
        while current_sum >= target:
            #如果 min_length 尚未設置，或當前子數組的長度更小，則更新
            if min_length is None or (right - left + 1) < min_length:
                min_length = right - left + 1  # 更新最小長度
                smallest_subarray = nums[left:right + 1]  # 記錄當前最小子數組
            
            current_sum -= nums[left]  #去掉左邊的元素
            left += 1  #左指針向右移動

    if min_length is not None:
        return min_length, smallest_subarray  #返回最小長度及其內容
    else:
        return 0, []  #若無則返回0及空子數組


test_input = [2, 3, 1, 2, 4, 3]
target =7
length, subarray = smallest_subarray_with_sum(test_input, target)
if length > 0:
    print(f"{length} (smallest subarray {subarray})")
else:
    print()



# In[ ]:




