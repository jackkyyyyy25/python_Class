test_input = [3, 3, 1, 4, 1,7]
target = 7
test_input.sort()
def find_min_subarray(arr, target):
    n = len(arr)
    left = right = 0
    curr_sum = 0
    min_len = float('inf')
    
    while right < n:
        curr_sum += arr[right]
        
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= arr[left]
            left += 1
            
        right += 1
    
    return min_len if min_len != float('inf') else 0

print(find_min_subarray(test_input, target))  