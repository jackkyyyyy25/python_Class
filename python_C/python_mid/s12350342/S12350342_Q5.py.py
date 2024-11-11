def missingNumber(nums):
    n = len(nums)
    expectedsum = n * (n + 1) // 2
    actualsum = sum(nums)
    return expectedsum - actualsum
test_input = [3, 0, 1]
result = missingNumber(test_input)
print(f"The missing number is: {result}")
