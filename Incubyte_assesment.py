import unittest, re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter = ','
    if numbers.startswith('//'):
        parts = numbers.split('\n', 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    
    numbers = numbers.replace('\n', delimiter)
    return sum(map(int, re.split(delimiter, numbers)))

class TestStringCalculator(unittest.TestCase):
    '''
    here unittest.Testcase provides assertEqual which checks both arguments are equal else return assertion error in case they are not equal
    '''
    #Case 1: Empty String
    def test_add_empty_string(self):
        self.assertEqual(add(""), 0)
    
    #Case 2: Add Single Number
    def test_add_single_number(self):
        a = self.assertEqual(add("1"), 1)

    #Case 3: Add Two Number
    def test_add_two_number(self):
        a = self.assertEqual(add("1,2"), 3)

    #Case 4: Test New Line
    def test_add_newline_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    #Case 5: Test Custom Deliminator
    def test_add_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

        #Add another test case pipe | (not mention in problem statement)
        self.assertEqual(add("//|\n1|2|3"), 6)
    
if __name__ == '__main__':
    unittest.main()
