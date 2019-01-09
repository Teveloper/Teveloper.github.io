# myCalculator unit test
import unittest
import myCalculator

class MyCalcTest(unittest.TestCase):
    def test_add(self):
        c = myCalculator.add(10, 20)
        self.assertEqual(c, 30)

    def test_substract(self):
        c = myCalculator.substract(50, 10)
        self.assertEqual(c, 40)
    
    def test_multiply(self):
        c = myCalculator.multiply(5, 10)
        self.assertEqual(c, 50)
    
    def test_divide(self):
        c = myCalculator.divide(20, 5)
        self.assertEqual(c, 4)

if __name__ == '__main__':
    unittest.main()
