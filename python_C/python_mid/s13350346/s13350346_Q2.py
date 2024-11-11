#midterm#2
def longest(nums):
     if not nums:
          return 0

     numset=set(nums)
     longeststreak=0
     for num in numset:
          if (num-1) not in numset:
               current=num
               currentstreak=1

               while (current+1) in numset:
                    current+=1
                    currentstreak+=1
               longeststreak=max(longeststreak,currentstreak)
     return longeststreak

test_input=[100,4,200,1,3,2]
print(longest(test_input))        