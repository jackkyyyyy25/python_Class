#Q1 判斷字串含有多少個單字

test_input =  "Hello, world! Hello everyone."

import re

cleaned = re.sub(r'[^\w\s]', '', test_input).lower()        #去除標點符號並全部轉成小寫
words = cleaned.split()     #依照空格位置分開每個單字
unique = set(words)     #整理words成集合

print(len(unique))

#結果為3

