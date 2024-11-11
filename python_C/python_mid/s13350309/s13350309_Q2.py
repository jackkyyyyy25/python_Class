def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in nums_set:  # 只有當前數是序列起點時才計算
            length = 1
            while num + length in nums_set:
                length += 1
            longest = max(longest, length)

    return longest

# 測試範例
test_input = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(test_input))  # 輸出: 4
