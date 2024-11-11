import os 
import unittest

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

q1_content = None
q2_content = None
missing_files = []

main_folder_path = '/home/jacky/Work/python_class/python_C/python_mid/'  # 替換為您的主資料夾路徑


counter = 0
nofile = 0
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
            else :
                print("not found")
                nofile +=1
                missing_files.append(student_code)  # 將找不到的檔案記錄到列表中

    print(counter)
    print(nofile)
            
if missing_files:
    print("\n找不到的檔案列表:")
    for missing_file in missing_files:
        print(missing_file)
            




