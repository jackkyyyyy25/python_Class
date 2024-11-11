#1.Unique Words Counter
import string

def count_unique_words(paragraph):
    # 移除标点符号并将文本转换为小写
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = paragraph.translate(translator).lower()
    
    # 将文本分割为单词，并使用集合找到唯一单词
    words = cleaned_text.split()
    unique_words = set(words)
    
    # 返回唯一单词的数量和格式化的字符串
    return len(unique_words), ','.join(sorted(unique_words))

# 示例用法
test_input = "Hello, world! Hello everyone."
count, unique_words_string = count_unique_words(test_input)
print(count,f"unique words: {unique_words_string}")
