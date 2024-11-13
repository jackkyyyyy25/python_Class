import os 
import unittest
import re
import io
from contextlib import redirect_stdout
import string

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




# 測試案例
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

output_file_path = "output_results.txt"
final_file_path = "final_file.txt"
main_folder_path = '/home/jacky/Work/python_class/python_C/python_mid/'  # 替換為您的主資料夾路徑
counter = 0
nofile = 0
missing_files = []

# 定義測試函數
def run_test_Q1(original_code, output_file):
    test_cases = test_cases_q1
    counter_testcase = 0
    counter_correct = 0
    output_file.write(f'學號:{student_code}\n')

    for input_string, expected_output in test_cases:
        # 使用 re.sub 替換 test_input 的賦值，將 input_string 插入程式碼中
        modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code)

        f = io.StringIO()
        counter_testcase += 1
        output_file.write(f'<<題號: Q1')
        output_file.write(f'測資：{counter_testcase}>>\n')
        #output_file.write(f'{input_string}\n')
        
        # 使用 redirect_stdout 捕捉輸出
        with redirect_stdout(f):
            try:
                exec(modified_code)
            except Exception as e:
                output_file.write(f"執行錯誤，輸入: '{input_string}'\nError: {str(e)}\n")
                continue  # 繼續下一個測試案例

        result = f.getvalue().strip()      
        if result == str(expected_output):
            output_file.write(f"通過測試: {input_string}\n")
            counter_correct += 1
            
            #print(f"通過測試: {input_string}")
        else:
            output_file.write(f"測試失敗，輸入: {input_string}\n期望: {expected_output}，實際: {result}\n")
            #print(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")  
    output_file.write(f'****************************正確題數:{counter_correct}, 錯誤題數:{10-counter_correct}****************************\n')
    #final_file.write(f'{student_folder}:正確題數:{counter_correct}\n')


    Q.append(counter_correct)
    print(counter_correct)
    print(Q)
    return counter_correct

def run_test_Q2(original_code, output_file):
    test_cases = test_cases_q2
    counter_testcase = 0
    counter_correct = 0
    output_file.write(f'學號:{student_code}')

    for input_string, expected_output in test_cases:
        # 使用 re.sub 替換 test_input 的賦值，將 input_string 插入程式碼中
        modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code)

        f = io.StringIO()
        counter_testcase += 1
        output_file.write(f'<<題號: Q2')
        output_file.write(f'測資：{counter_testcase}>>\n')
        #output_file.write(f'{input_string}\n')
        
        # 使用 redirect_stdout 捕捉輸出
        with redirect_stdout(f):
            try:
                exec(modified_code)
            except Exception as e:
                output_file.write(f"執行錯誤，輸入: '{input_string}'\nError: {str(e)}\n")
                continue  # 繼續下一個測試案例

        result = f.getvalue().strip()      
        if result == str(expected_output):
            output_file.write(f"通過測試: {input_string}\n")
            counter_correct += 1
            
            #print(f"通過測試: {input_string}")
        else:
            output_file.write(f"測試失敗，輸入: {input_string}\n期望: {expected_output}，實際: {result}\n")
            #print(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")  
    output_file.write(f'****************************正確題數:{counter_correct}, 錯誤題數:{10-counter_correct}****************************\n')
    return counter_correct
    
def run_test_Q3(original_code, output_file):
    test_cases = test_cases_q3
    counter_testcase = 0
    counter_correct = 0
    output_file.write(f'學號:{student_code}\n')

    for input_string, expected_output in test_cases:
        # 使用 re.sub 替換 test_input 的賦值，將 input_string 插入程式碼中
        modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code)

        f = io.StringIO()
        counter_testcase += 1
        output_file.write(f'<<題號: Q3')
        output_file.write(f'測資：{counter_testcase}>>\n')
        #output_file.write(f'{input_string}\n')
        
        # 使用 redirect_stdout 捕捉輸出
        with redirect_stdout(f):
            try:
                exec(modified_code)
            except Exception as e:
                output_file.write(f"執行錯誤，輸入: '{input_string}'\nError: {str(e)}\n")
                continue  # 繼續下一個測試案例

        result = f.getvalue().strip()      
        if result == str(expected_output):
            output_file.write(f"通過測試: {input_string}\n")
            counter_correct += 1
            
            #print(f"通過測試: {input_string}")
        else:
            output_file.write(f"測試失敗，輸入: {input_string}\n期望: {expected_output}，實際: {result}\n")
            #print(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")  
    output_file.write(f'****************************正確題數:{counter_correct}, 錯誤題數:{10-counter_correct}****************************\n')
    return counter_correct

def run_test_Q4(original_code, output_file):
    test_cases = test_cases_q4
    counter_testcase = 0
    counter_correct = 0
    output_file.write(f'學號:{student_code}\n')

    for input_string, expected_output in test_cases:
        # 使用 re.sub 替換 test_input 的賦值，將 input_string 插入程式碼中
        modified_code = re.sub(r'^test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code, flags=re.MULTILINE)

        f = io.StringIO()
        counter_testcase += 1
        output_file.write(f'<<題號: Q4')
        output_file.write(f'測資：{counter_testcase}>>\n')
        #output_file.write(f'{input_string}\n')
        
        # 使用 redirect_stdout 捕捉輸出
        with redirect_stdout(f):
            try:
                exec(modified_code)
            except Exception as e:
                output_file.write(f"執行錯誤，輸入: '{input_string}'\nError: {str(e)}\n")
                continue  # 繼續下一個測試案例

        result = f.getvalue().strip()      
        if result == str(expected_output):
            output_file.write(f"通過測試: {input_string}\n")
            counter_correct += 1
            
            #print(f"通過測試: {input_string}")
        else:
            output_file.write(f"測試失敗，輸入: {input_string}\n期望: {expected_output}，實際: {result}\n")
            #print(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")  
    output_file.write(f'****************************正確題數:{counter_correct}, 錯誤題數:{10-counter_correct}****************************\n')
    return counter_correct

def run_test_Q5(original_code, output_file):
    test_cases = test_cases_q5
    counter_testcase = 0
    counter_correct = 0
    output_file.write(f'學號:{student_code}\n')

    for input_string, expected_output in test_cases:
        # 使用 re.sub 替換 test_input 的賦值，將 input_string 插入程式碼中
        modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code)

        f = io.StringIO()
        counter_testcase += 1
        output_file.write(f'<<題號: Q5')
        output_file.write(f'測資：{counter_testcase}>>\n')
        #output_file.write(f'{input_string}\n')
        
        # 使用 redirect_stdout 捕捉輸出
        with redirect_stdout(f):
            try:
                exec(modified_code)
            except Exception as e:
                output_file.write(f"執行錯誤，輸入: '{input_string}'\nError: {str(e)}\n")
                continue  # 繼續下一個測試案例

        result = f.getvalue().strip()      
        if result == str(expected_output):
            output_file.write(f"通過測試: {input_string}\n")
            counter_correct += 1
            
            #print(f"通過測試: {input_string}")
        else:
            output_file.write(f"測試失敗，輸入: {input_string}\n期望: {expected_output}，實際: {result}\n")
            #print(f"測試失敗，輸入: {input_string}，期望: {expected_output}，實際: {result}\n")  
    output_file.write(f'****************************正確題數:{counter_correct}, 錯誤題數:{10-counter_correct}****************************\n')
    return counter_correct

def run_test_Q6(original_code, output_file):
    test_cases = test_cases_q6
    counter_testcase = 0
    counter_correct = 0
    output_file.write(f'學號:{student_code}\n')

    for (nums, target_value), expected_output in test_cases:
        # 替換測試案例中的 test_input 和 target
        modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(nums)}', original_code)
        modified_code = re.sub(r'target\s*=\s*.*', f'target={repr(target_value)}', modified_code)


        f = io.StringIO()
        counter_testcase += 1
        output_file.write(f'<<題號: Q6 測資：{counter_testcase}>>\n')
        
        # 使用 redirect_stdout 捕捉輸出
        with redirect_stdout(f):
            try:
                exec(modified_code)
            except Exception as e:
                output_file.write(f"執行錯誤，輸入: '{(nums, target_value)}'\nError: {str(e)}\n")
                continue  # 繼續下一個測試案例

        result = f.getvalue().strip()
        if result == str(expected_output):
            output_file.write(f"通過測試: {(nums, target_value)}\n")
            counter_correct += 1
        else:
            output_file.write(f"測試失敗，輸入: {(nums, target_value)}\n期望: {expected_output}，實際: {result}\n")
    
    output_file.write(f'****************************正確題數:{counter_correct}, 錯誤題數:{10-counter_correct}****************************\n')
    return counter_correct
    Q.append(counter_correct)

# 主程式部分
# 主程式部分
Q = []

with open(output_file_path, "w") as output_file, open(final_file_path, "w") as final_file:
    for student_folder in os.listdir(main_folder_path):
        student_file_path = os.path.join(main_folder_path, student_folder)

        if os.path.isdir(student_file_path):  
            print(f"進入學生資料夾: {student_folder}")
            final_file.write(f"\n學生學號：{student_folder}\n")  # 記錄學生學號
            a = []
            for q_num in range(1, 7):
                q_filename = f"Q{q_num}.py"
                student_code = student_folder + "_" + q_filename
                student_code_path = os.path.join(student_file_path, student_code)
                print(student_code_path)

                if os.path.isfile(student_code_path):
                    print(f"正在讀取檔案: {student_code_path}")
                    counter += 1
                    with open(student_code_path, 'r') as file:
                        original_code = file.read()
                    
                    # 執行 Q1-Q6 測試
                    if q_num == 1:
                        correct_count = run_test_Q1(original_code, output_file)
                    elif q_num == 2:
                        correct_count = run_test_Q2(original_code, output_file)
                    elif q_num == 3:
                        correct_count = run_test_Q3(original_code, output_file)
                    elif q_num == 4:
                        correct_count = run_test_Q4(original_code, output_file)
                    elif q_num == 5:
                        correct_count = run_test_Q5(original_code, output_file)
                    elif q_num == 6:
                        correct_count = run_test_Q6(original_code, output_file)

                    a.append(correct_count)

                    output_file.write("---------------------------\n")
                    final_file.write(f"題號: Q{q_num} - 正確題數: {correct_count} / 測資數量\n")  # 記錄每一題的正確數
                    
                else:
                    output_file.write(f'沒有找到 {student_code}\n')
                    final_file.write(f'沒有找到 {student_code}\n')
                    nofile += 1
                    missing_files.append(student_code)
            total_correct = sum(a)
            print("總正確題數:", total_correct)
            final_file.write(f"總正確題數: {total_correct}\n")
        # if missing_files:
        #     output_file.write("\n找不到的檔案列表:\n")
        #     final_file.write("\n找不到的檔案列表:\n")
        #     for missing_file in missing_files:
        #         output_file.write(f"{missing_file}\n")
        #         final_file.write(f"{missing_file}\n")
        #         print(missing_file)

print("總測試檔案數:", counter)
print("找不到的檔案數:", nofile)
