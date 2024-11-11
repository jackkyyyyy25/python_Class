test_input = " Hello, world! Hello everyone."

# 移除標點符號，並將字串轉換為小寫
cleaned_input = ""
for char in test_input:
    if char.isalnum() or char.isspace():  # 保留字母、數字和空格
        cleaned_input += char.lower()

# 分割字串
words = cleaned_input.split()

# 使用集合來獲取唯一單詞
unique_words = set(words)

# 計算
print(len(unique_words))  
