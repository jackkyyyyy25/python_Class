def is_palindrome(s):
  s = ''.join(c.lower() for c in s if c.isalnum())

  left, right = 0, len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1

  return True
test_input = "racecar"
if is_palindrome(test_input):
  print("Palindrome")
else:
  print("Not Palindrome")