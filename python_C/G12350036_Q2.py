import os 
import unittest
import re
import io
from contextlib import redirect_stdout
#檔名有空白　學號打錯　
test_cases_q1 = [
    ("Hello, world! Hello everyone.", 3),
    ("Python programming is fun! Programming is amazing.", 5),
    ("One one one", 1),
    ("This is a simple sentence.", 5),
    ("Special characters: !@#$%^&*() should be ignored.", 5),
    ("A B C a b c", 3),
    ("The quick brown fox jumps over the lazy dog.", 8),
    ("Repeated words, repeated words, repeated.", 2),
    ("", 0),
    ("Case insensitivity test: TEST test", 1)
]

test_cases_q2 = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([1, 9, 3, 10, 2, 20], 3),
    ([5, 5, 5, 5], 1),
    ([10, 5, 12, 3, 55, 2, 4], 4),
    ([1, 2, 0, 1], 3),
    ([], 0),
    ([0], 1),
    ([1, 2, 3, 4, 5, 6, 7], 7),
    ([10, 12, 14, 15, 13, 16], 6),
    ([2, 5, 6, 7, 9, 8, 1], 6)
]

test_cases_q3 = [
    (1234, 10),
    (0, 0),
    (9999, 36),
    (1111, 4),
    (54321, 15),
    (1001, 2),
    (1234567890, 45),
    (888, 24),
    (101010, 3),
    (2468, 20)
]

test_cases_q4 = [
    ("racecar", "Palindrome"),
    ("hello", "Not Palindrome"),
    ("A man a plan a canal Panama", "Palindrome"),
    ("No lemon, no melon", "Palindrome"),
    ("", "Palindrome"),
    ("a", "Palindrome"),
    ("ab", "Not Palindrome"),
    ("madam", "Palindrome"),
    ("was it a car or a cat I saw", "Palindrome"),
    ("palindrome", "Not Palindrome")
]

test_cases_q5 = [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ([0], 1),
    ([0, 1, 2, 3, 4, 5, 7, 8, 9], 6),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
    ([1], 0),
    ([0, 2], 1),
    ([4, 3, 2, 0, 1], 5),
    ([6, 4, 5, 0, 1, 2, 7, 3], 8)
]

test_cases_q6 = [
    (([2, 3, 1, 2, 4, 3], 7), 2),
    (([1, 2, 3, 4, 5], 11), 3),
    (([1, 4, 4], 8), 2),
    (([1, 2, 3, 4, 5], 15), 5),
    (([2, 3, 1, 2, 4, 3], 100), 0),
    (([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15), 2),
    (([1, 1, 1, 1, 1, 1], 3), 3),
    (([4, 3, 1, 2, 6], 6), 1),
    (([1, 2, 3], 6), 3),
    (([2, 3, 5, 7, 10, 15], 20), 2)
]


q1_content = None
q2_content = None
missing_files = []

output_file_path = "output_results.txt"
main_folder_path = '/home/jacky/Work/python_class/python_C/python_mid/'  # 替換為您的主資料夾路徑


counter = 0
nofile = 0
with open(output_file_path, "w") as output_file:
    for student_folder in os.listdir(main_folder_path):
        student_file_path = os.path.join(main_folder_path, student_folder)
        


        if os.path.isdir(student_file_path):  
            print(f"進入學生資料夾: {student_folder}")

            q = []
            

        
            for q_num in range(1, 7):
                q_filename = f"Q{q_num}.py"
                #q_file_path = os.path.join(student_file_path, q_filename)
                student_code = student_folder + "_" + q_filename
                student_code_path = os.path.join(student_file_path, student_code)
                print(student_code_path)
                if os.path.isfile(student_code_path):
                    print(f"正在讀取檔案: {student_code_path}")
                    counter += 1
                    with open(student_code_path, 'r') as file:
                        original_code = file.read()
                    
                    if q_num == 1:
                        output_file.write(f'------------------------------\n')
                        counter_q = 0
                        test_cases = test_cases_q1
                    elif q_num == 2:
                        output_file.write(f'------------------------------\n')
                        counter_q = 0
                        test_cases = test_cases_q2
                    elif q_num == 3:
                        output_file.write(f'------------------------------\n')
                        counter_q = 0
                        test_cases = test_cases_q3
                    elif q_num == 4:
                        output_file.write(f'------------------------------\n')
                        counter_q = 0
                        test_cases = test_cases_q4
                    elif q_num == 5:
                        output_file.write(f'------------------------------\n')
                        counter_q = 0
                        test_cases = test_cases_q5
                    elif q_num == 6:
                        output_file.write(f'------------------------------\n')
                        counter_q = 0
                        test_cases = test_cases_q6
                    
                        for input_string, expected_output in test_cases:
                            modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code)
                            f = io.StringIO()
                            with redirect_stdout(f):
                                local_vars = {}
                                try:
                                    exec(modified_code, {}, local_vars)
                                except Exception as e:
                                    print(f"An error occurred while testing input: '{input_string}'. Error: {str(e)}")

                            result = int(f.getvalue().strip())  # 假設輸出是整

                            try:
                                self.assertEqual(result, expected_output, f"Test failed for input: {input_string}")
                            except AssertionError as e:
                                print(e)
                                
'''                    for input_string, expected_output in test_cases:
                        # 替換 test_input 變量的賦值
                        counter_q += 1
                        modified_code = re.sub(
                            r'test_input\s*=\s*".*?"', f'test_input="{input_string}"', original_code)
                        local_vars = {}
                        output_file.write(student_code)
                        output_file.write(f'題號：{counter_q}\n')
                        try:
                            exec(modified_code, {}, local_vars)
                            result = local_vars.get('number')  # 假設結果儲存在變量 'number' 中
                            
                            # 驗證輸出
                            if result == expected_output:
                                output_file.write(f"通過測試: {input_string}\n")
                            else:
                                output_file.write(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")
                        except Exception as e:
                           output_file.write(f"程式執行錯誤: {e}\n")
'''
                else:
                    print("not found")
                    nofile +=1
                    missing_files.append(student_code) 