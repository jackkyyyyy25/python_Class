test_input=[3,0,1]
n=len(test_input)
num_set=set(test_input)
for number in range(n+1):
        if number not in num_set:
            print(number)
            break

