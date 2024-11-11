import re
test_input = "Hello, world! Hello everyone."
str1 =re.sub(r'[^A-Za-z0-9 ]+', '',test_input)
lis1 = str1.split()
str2 = list(set(lis1))
print(len(str2))