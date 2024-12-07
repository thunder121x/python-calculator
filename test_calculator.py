import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        
    #add cases
    def test_add(self):
        self.assertEqual(self.calc.add(1, 9), 10)
    def test_add2(self):
        self.assertEqual(self.calc.add(-5, 1), -4)

    #subtract cases
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 4), -3)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(0,  0), 0)

    #multiply cases
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(1, 0), 0)

    #divide cases
    def test_divide(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(0, 5), 0)
        
    
    #modulo cases
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(7, -3), 1)

if __name__ == '__main__':

    unittest.main()
