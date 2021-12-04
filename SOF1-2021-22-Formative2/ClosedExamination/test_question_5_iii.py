import unittest
from question_5 import MarkDistribution

class TestQuestion5iii(unittest.TestCase):

    def testGetdistribution(self):
        """ Test that the getDistribution returns the correct output when the 
        number of bin divides the range of marks. We test three different 
        number of bins (2, 4, 5) for a range of marks of 20.
        """
        # In order to avoid calling add_all for setting up the test (in case 
        # you got it wrong), I set up _marks in two ways, ordered and unordered. 
        # then I test both to see if getDistribution works with at least one 
        # representation.
        # I use histoOrdered for the ordered representation and histo for the 
        # unordered. At least one of them must work.
        histoOrdered= MarkDistribution(20,0)
        histoOrdered._marks = [0,1,2,5,8,8,8,15,20,20] 
        histo= MarkDistribution(20,0)
        histo._marks = [8,8,0,5,8,15,20,1,2,20]
        distribution4 = [('0-4', 3), ('5-9', 4), ('10-14', 0), ('15-20', 3)]

        # Check if at least one of them work. If at least one of them give 
        # the right distribution, passed is True.
        passed = (distribution4 == histo.getDistribution(4)) \
                or (distribution4 == histoOrdered.getDistribution(4))
        self.assertTrue(passed)

        distribution5 = [('0-3', 3), ('4-7', 1), ('8-11', 3), ('12-15', 1), 
                         ('16-20', 2)]
        passed = (distribution5 == histo.getDistribution(5)) \
                or (distribution5 == histoOrdered.getDistribution(5))
        self.assertTrue(passed)

        distribution2 = [('0-9', 7), ('10-20', 3)]
        passed = (distribution2 == histo.getDistribution(2)) \
                or (distribution2 == histoOrdered.getDistribution(2))
        self.assertTrue(passed)

    def testGetdistribution_error(self):
        """ Test if the method getDistribution raises a ValueError if the range
        of marks is not a multiple of the number of bins.
        """
        histo = MarkDistribution(100,0)
        self.assertRaises(ValueError, histo.getDistribution, 15)
        histo2 = MarkDistribution(60,10)
        self.assertRaises(ValueError, histo2.getDistribution, 20)


if __name__ == '__main__':
    unittest.main()
