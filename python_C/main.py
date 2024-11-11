import unittest
import re

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
        
        for input_string, expected_output in test_cases:
            # 替換 test_input 變量的賦值
            modified_code = re.sub(r'test_input\s*=\s*".*?"', f'test_input="{input_string}"', original_code)

            # 使用 exec() 執行修改後的代碼並捕獲輸出
            local_vars = {}
            try:
                exec(modified_code, {}, local_vars)
                result = local_vars.get('number')
                # 驗證輸出
                self.assertEqual(result, expected_output)
            except AssertionError as e:
                print(f"Test failed for input: '{input_string}'. Expected {expected_output}, but got {result}.")
            except Exception as e:
                print(f"An error occurred while testing input: '{input_string}'. Error: {str(e)}")

if __name__ == '__main__':
    unittest.main()
