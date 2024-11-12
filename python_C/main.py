import unittest
import re
import io
from contextlib import redirect_stdout

class TestStudentCode(unittest.TestCase):
    def test_input_cases(self):
        # 讀取學生的代碼
        with open('G12350036_Q1.py', 'r') as file:
            original_code = file.read()

        test_cases = [
            ("Hello, world! Hello everyone.", 3),
            ("Python programming is fun! Programming is amazing.", 4),
            ("One one one", 1),
            ("This is a simple sentence.", 5),
            ("Special characters: !@#$%^&*() should be ignored.", 5),
            ("A B C a b c", 3),
            ("The quick brown fox jumps over the lazy dog.", 8),
            ("Repeated words, repeated words, repeated.", 2),
            ("", 0),
            ("Case insensitivity test: TEST test", 1)
            ]

        test_cases_1 = [
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
        
        for input_string, expected_output in test_cases:
            # 替換 test_input 變量的賦值
            # 確保 input_string 以字串格式插入
            modified_code = re.sub(r'test_input\s*=\s*.*', f'test_input={repr(input_string)}', original_code)

            # 使用 StringIO 來捕捉 print 的輸出
            f = io.StringIO()
            with redirect_stdout(f):
                local_vars = {}
                try:
                    exec(modified_code, {}, local_vars)
                except Exception as e:
                    print(f"An error occurred while testing input: '{input_string}'. Error: {str(e)}")

            result = int(f.getvalue().strip())  # 假設輸出是整數

            try:
                self.assertEqual(result, expected_output, f"Test failed for input: {input_string}")
            except AssertionError as e:
                print(e)
'''
            # 使用 exec() 執行修改後的代碼並捕獲輸出
            local_vars = {}
            try:
                exec(modified_code, {}, local_vars)
                result = local_vars.get('number')
                print(result)
                # 驗證輸出
                self.assertEqual(result, expected_output)
            except AssertionError as e:
                print(f"Test failed for input: '{input_string}'. Expected {expected_output}, but got {result}.")
            except Exception as e:
                print(f"An error occurred while testing input: '{input_string}'. Error: {str(e)}")
'''

if __name__ == '__main__':
    unittest.main()
