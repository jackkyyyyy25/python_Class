#!/usr/bin/env python
# coding: utf-8

# In[1]:


#計算單字量
def count_unique_words(paragraph):
    paragraph = paragraph.lower() #將文字轉成小寫
    #去除標點符號，保留字母和空格
    cleaned_paragraph = ""
    for char in paragraph:
        if char.isalnum() or char.isspace():  #isalnum() 保留字母和數字
            cleaned_paragraph += char
    
    #以空格分割文字
    words = cleaned_paragraph.split()
    #使用 set() 儲存唯一單字
    unique_words = set(words)
    return len(unique_words), unique_words

test_input = "Hello, word! Hello everyone"
count, unique_words = count_unique_words(test_input)
print(f"{count} (unique words: {', '.join(unique_words)})")


# In[ ]:




