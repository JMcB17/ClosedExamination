import unittest
from question_5 import MarkDistribution

class TestQuestion5i(unittest.TestCase):

    def testConstructor(self):
        """ Test that the object constructed has been assigned the correct 
        values for each attributes when values are provided in the parameters.
        """
        histo = MarkDistribution(100,0)
        self.assertAlmostEqual(100, histo._max, delta=0.000001)
        self.assertAlmostEqual(0, histo._min, delta=0.000001)
        self.assertEqual([], histo._marks)

        histo2 = MarkDistribution(50,10)
        self.assertAlmostEqual(50, histo2._max, delta=0.000001)
        self.assertAlmostEqual(10, histo2._min, delta=0.000001)
        self.assertEqual([], histo2._marks)

    def testConstructorDefaultValues(self):
        """ Test that the object constructed has been assigned the correct 
        DEFAULT values for each attributes when no values are provided in 
        parameters.
        """
        histo = MarkDistribution()
        self.assertAlmostEqual(100, histo._max, delta=0.000001)
        self.assertAlmostEqual(0, histo._min, delta=0.000001)

    def testConstructorError(self):
        """ Test that the constructor raises a ValueError if the minimum 
        marks is greater than or equal to the maximum mark.
        """
        self.assertRaises(ValueError, MarkDistribution, 0, 100)
        self.assertRaises(ValueError, MarkDistribution, 10, 10)

if __name__ == '__main__':
    unittest.main()
