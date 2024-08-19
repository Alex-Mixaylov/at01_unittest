import unittest
from main import add, subtract, multiply, divide, check, dividezero

# def test_add(self):
#     self.assertEqual(add(2, 5), 7)
#     self.assertNotEqual(add(3, 7), 9)
# def test_subtract(self):
#      self.assertEqual(subtract(7, 4), 3)
#     self.assertEqual(subtract(4, 2), 1)
# def test_multiply(self):
#     self.assertEqual(multiply(2, 5), 12)
#     self.assertEqual(multiply(3, 6), 18)
# def test_divide(self):
#     self.assertEqual(divide(4, 2), 3)
#     self.assertEqual(divide(20, 5), 4)
# def test_divide(self):
#     self.assertTrue(check(2))
#     self.assertTrue(check(6))
#     self.assertTrue(check(220))
#     self.assertTrue(not check(1))
#     self.assertTrue(not check(3))
#     self.assertTrue(not check(57))

class TestMath(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def dividezero(self):
        self.assertRaises(ValueError, divide, 6, 0)
        self.assertRaises(TypeError, divide, 6, 0)



if __name__ == '__main__':
    unittest.main()