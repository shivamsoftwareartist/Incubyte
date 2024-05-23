import unittest, re

def add(numbers):
    if not numbers:
        return 0
    numbers = numbers.replace('\n', ',')
    return sum(map(int, numbers.split(',')))

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
    
    



    

if __name__ == '__main__':
    unittest.main()
