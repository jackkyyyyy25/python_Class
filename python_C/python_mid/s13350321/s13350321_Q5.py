def find_missing_number(nums):
    n=len(nums)
    expected_sum=n*(n+1)//2
    actual_sum=sum(nums)
    missing_number=expected_sum-actual_sum
    return missing_number
test_input=[3, 0, 1]
print(find_missing_number(test_input))