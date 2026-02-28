import unittest
from backend.operators import subtract, multiply, divide

class TestOperators(unittest.TestCase):
   def test_subtract(self):
      expected = -2
      result = subtract(3, 5)
      self.assertEqual(result, expected)

   def test_multiply(self):
      expected = 8
      result = multiply(2, 4)
      self.assertEqual(result, expected)

   def test_divide(self):
      expected = 2.5
      result = divide(5, 2)
      self.assertEqual(result, expected)
      