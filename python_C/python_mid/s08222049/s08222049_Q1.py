test_input="Hello, world! Hello everyone."
a=test_input.lower()
b=a.replace("!", ",")
c=b.replace(" ", ",")
d=c.replace(".","")
e=d.split(",")
f = list(filter(None, e))
g=list(dict.fromkeys(f))
number=len(g)
print(number)