test_input = "Hello, world! Hello everyone."
print(len(set(test_input.lower().replace(",","").replace(".","").replace("!","").split())))
#set: 將單字列表轉為集合以去除重複。
#len: 計算集合的長度，得到不重複單字的數量。
