import re

def unique_word_count(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    unique_words = set(words)
    return len(unique_words)

# 測試範例
test_input = "Hello, world! Hello everyone."
print(unique_word_count(test_input))  # 輸出: 3
