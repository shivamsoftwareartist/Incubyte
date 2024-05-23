def add(numbers):
    if not numbers:
        return 0
    return sum(map(int, numbers.split(',')))

#Case 1: Check for empty string
def test_empty_string():
    addition = add("")
    print("addition=", addition)
a = test_empty_string()