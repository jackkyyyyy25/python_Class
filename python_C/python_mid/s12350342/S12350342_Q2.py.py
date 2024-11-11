test_input=[100,4,250,1,3,2]
class Solution(object):
   def longestConsecutive(self, a):
      a = set(a)
      longest = 0
      for i in a:
         if i-1 not in a:
            current = i
            streak = 0
            while i in a:
               i+=1
               streak+=1
               longest = max(longest,streak)
      return longest
    
ob = Solution()
print(ob.longestConsecutive(test_input))
