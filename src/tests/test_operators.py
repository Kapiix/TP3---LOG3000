import unittest
from backend.operators import subtract, multiply, divide

class TestOperators(unittest.TestCase):
   def test_subtract(self):
      """
      Vérifie que l'opérateur de soustraction fonctionne correctement.
      """
      expected = -2
      result = subtract(3, 5)
      self.assertEqual(result, expected)

   def test_multiply(self):
      """
      Vérifie que l'opérateur de multiplication fonctionne correctement.
      """
      expected = 8
      result = multiply(2, 4)
      self.assertEqual(result, expected)

   def test_divide(self):
      """
      Vérifie que l'opérateur de division fonctionne correctement.
      """
      expected = 2.5
      result = divide(5, 2)
      self.assertEqual(result, expected)
      