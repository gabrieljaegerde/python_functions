import unittest
from main import sum_numbers

class TestMain(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(1, 2), 3)
        self.assertEqual(sum_numbers(-1, 1), 0)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
