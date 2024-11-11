test_input=[100,4,200,1,3,2]
nums=set(test_input)
longest_streak=0
longest_sequence=[]
for i in nums:
    if i-1 not in nums:
        current_num=i
        current_streak=1
        current_sequence=[current_num]
        
        while current_num +1 in nums:
            current_num +=1
            current_streak +=1
            current_sequence.append(current_num)

        if current_streak>longest_streak:
            longest_streak=current_streak
            longest_sequence=current_sequence
            
print(longest_streak,"(The longest sequence is",longest_sequence,")")
