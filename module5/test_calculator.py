import unittest
from calculator import add

class TestCalculator(unittest.TestCase): #create test classes

    def test_add(self):
        self.assertEqual(add(2, 3), 5) #check for expected result

if __name__ == "__main__":
    unittest.main()
