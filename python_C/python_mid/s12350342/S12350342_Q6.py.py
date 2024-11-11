def min_subarray_len(target, nums):
    n = len(nums)
    min_length = float('inf')  # Initialize with infinity to find the minimum
    left = 0
    current_sum = 0

    # Sliding window
    for right in range(n):
        current_sum += nums[right]  # Expand the window by adding the right element
        
        # Shrink the window from the left as much as possible while keeping the sum >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)  # Update minimum length
            current_sum -= nums[left]  # Shrink the window by removing the left element
            left += 1  # Move the left pointer to the right

    # If min_length was updated, return it; otherwise, return 0 (no such subarray found)
    return min_length if min_length != float('inf') else 0

# Example input
test_input = [2, 3, 1, 2, 4, 3]
target = 7

# Call the function and print the result
result = min_subarray_len(target, test_input)
print(f"The length of the smallest subarray with sum at least {target} is: {result}")
