#midterm#1
import string
def countunique(paragraph):
     trans=str.maketrans('','',string.punctuation)
     cleanpara=paragraph.translate(trans).lower()
     words=cleanpara.split()
     uniqueword=set(words)
     return len(uniqueword)     
test_input= "Hello, world! Hello everyone."
print(countunique(test_input))