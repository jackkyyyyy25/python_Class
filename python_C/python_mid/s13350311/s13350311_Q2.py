#2.Longest Consecutive Sequence in a List
def longest_consecutive_sequence(nums):
    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Check if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update longest streak found
            longest_streak = max(longest_streak, current_streak)

    return longest_streak
test_input = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(test_input))  # Output should be 4, as the longest sequence is [1, 2, 3, 4]


