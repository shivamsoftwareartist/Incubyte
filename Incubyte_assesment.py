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
    number_list = list(map(int, re.split(delimiter, numbers)))
    
    negative_numbers = [num for num in number_list if num < 0]
    if negative_numbers:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
    
    return sum(number_list)

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

    #Case 6: Test negative numbers not allowed
    def test_add_negative_numbers(self):

        #For one negative number
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")

        # Checking if the exception message is same as given
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2")

        #for multiple negative number
        with self.assertRaises(ValueError) as context:
            add("-1,2,-3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -1, -3")

if __name__ == '__main__':
    unittest.main()
