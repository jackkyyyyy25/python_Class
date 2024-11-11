test_input="Hello, world! Hello everyone."
t1=test_input.replace(",","")
t2=t1.replace("!","")
t3=t2.replace(".","")
test1=t3.lower()
test2=test1.split()
print(test2.count("hello"),test2.count("world"),test2.count("everyone"))