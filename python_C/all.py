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
    ("Case insensitivity test: TEST test", 3)
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
    ([10, 12, 14, 15, 13, 16], 5),
    ([2, 5, 6, 7, 9, 8, 1], 5)
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
                        
                    # 根據 q_num 設定不同的測試案例
                    if q_num == 1:
                        output_file.write(f'\n------------------------------\n')

                        test_cases = test_cases_q1
                    elif q_num == 2:
                        output_file.write(f'------------------------------\n')
                        
                        test_cases = test_cases_q2
                    elif q_num == 3:
                        output_file.write(f'------------------------------\n')
                        test_cases = test_cases_q3
                    elif q_num == 4:
                        output_file.write(f'------------------------------\n')
                        test_cases = test_cases_q4
                    elif q_num == 5:
                        output_file.write(f'------------------------------\n')
                        test_cases = test_cases_q5
                    elif q_num == 6:
                        output_file.write(f'------------------------------\n')
                        test_cases = test_cases_q6
                    
                    # 進行測試
                    counter_testcase = 0
                    for input_string, expected_output in test_cases:
                        modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code)
                        f = io.StringIO()
                        counter_testcase += 1
                        output_file.write(f'<<題號{q_num}>>\n')
                        output_file.write(f'測資：{counter_testcase}\n')
                        output_file.write(f'{student_code}\n')
                        with redirect_stdout(f):
                            local_vars = {}
                            
                            try:
                                exec(modified_code, {}, local_vars)
                            except Exception as e:
                                output_file.write(f"An error occurred while testing input: '{input_string}\n'Error: {str(e)}\n")
                        # 驗證結果
                        result = f.getvalue().strip()

                        if result == str(expected_output):
                            output_file.write(f"通過測試: {input_string}")
                            print(f"通過測試: {input_string}")
                        else:
                            output_file.write(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")
                            print(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")
'''                       
                        result = f.getvalue().strip()  # 假設輸出是整數
                        try:
                            self.assertEqual(result, expected_output, f"Test failed for input: {input_string}")
                        except AssertionError as e:
                            print(e)
                           
                else:
                    print("not found")
                    nofile += 1
                    missing_files.append(student_code)


            print('檔案總數', counter)
            print("not found 總數", nofile)

'''
            
if missing_files:
    print("\n找不到的檔案列表:")
    for missing_file in missing_files:
        print(missing_file)
            




