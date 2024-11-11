def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0


# 測試範例
test_input = [2, 3, 2, 2, 4, 3]
target = 7
print(min_subarray_len(target, test_input))  # 輸出: 2
