test_input = [3, 0, 1]
#題目似乎有一點小怪，這題我直接參照AI。
n = max(test_input) 
expected_sum = (n * (n + 1)) // 2  
actual_sum = sum(test_input)  

missing_num = expected_sum - actual_sum  
print(missing_num)
