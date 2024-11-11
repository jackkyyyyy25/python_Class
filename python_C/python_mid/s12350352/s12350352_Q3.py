test_input=1234

def summ(num):
    num_list=[]
    num = str(num)
    for digit in num:
        digit=int(digit)
        num_list.append(digit)
    print(sum(num_list))

summ(test_input)