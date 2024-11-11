test_Input = "Hello, world! Hello everyone."
test_Input =test_Input.lower()
Input = test_Input.split()

Out_array=[]

def Is_repeat(word,array):
    for i in array:
        if word==i:
            return False
    return True




for i in range(len(Input)):
    if not(64<ord(Input[i][-1])<123):
        Input[i]=Input[i][:-1]

Out_array.append(Input[0])
for i in Input:
    if Is_repeat(i,Out_array):
        Out_array.append(i)

print(len(Out_array))