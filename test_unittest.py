import unittest
from main import calculate_remainder

# Тестирование остатка от деления. Возвращает остаток от деления dividend на divisor.
class TestCalculateRemainder(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(calculate_remainder(10, 3), 1)
        self.assertNotEqual(calculate_remainder(20, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(calculate_remainder(-10, 3), -1)
        self.assertEqual(calculate_remainder(-20, 5), 0)

    def test_mixed_sign_numbers(self):
        self.assertEqual(calculate_remainder(10, -3), 1)
        self.assertEqual(calculate_remainder(-10, -3), -1)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_remainder(10, 0)

    def test_zero_dividend(self):
        self.assertEqual(calculate_remainder(0, 3), 0)


if __name__ == '__main__':
    unittest.main()
