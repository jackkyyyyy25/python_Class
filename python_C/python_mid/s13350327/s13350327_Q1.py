test_input = "."
words = test_input.lower().replace(",","").replace("!","").replace(".","")
ans = len(set(test_input.lower().replace(",","").replace("!","").replace(".","").split()))
print(words)
print("唯一單字數:",ans)
