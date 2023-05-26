import unittest

def min(n1, n2):
    min_of_numbers = n1 + n2
    return min_of_numbers

    class MinTestCase(unittest.TestCase):
     def test_positive_numbers(self):
        result = min(5, 10)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = min(-5, -10)
        self.assertEqual(result, -10)

    def test_zero(self):
        result = min(0, 10)
        self.assertEqual(result, 0)

    def test_equal_numbers(self):
        result = min(5, 5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
