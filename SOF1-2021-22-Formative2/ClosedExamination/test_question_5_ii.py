import unittest
from question_5 import MarkDistribution

class TestQuestion5ii(unittest.TestCase):

    def testAddAllEmpty(self):
        """ Test that adding an empty list of marks does not change the 
        content of the attribute  marks. 
        """
        histo = MarkDistribution(100,0)
        histo.addAll([])
        self.assertEqual([], histo._marks)
        histo._marks = [1,1,30,40]
        histo.addAll([])
        # As the order of the marks does not matter, we can sort the lists 
        # before comparing them.
        self.assertEqual(sorted([1,1,30,40]), sorted(histo._marks))


    def testAddAllError(self):
        """ Test that adding a mark outside the range of allowed marks, 
        that is smaller than  min or greater than  max, raises a ValueError.
        """
        histo = MarkDistribution(100,0)
        self.assertRaises(ValueError, histo.addAll, [10,11,100,101])
        self.assertRaises(ValueError, histo.addAll, [-10,11,20])

    def testAddAllValidRange(self):
        """ Test that adding marks in the valid range modified the content of
        marks. Note it does not matter if you decided to sort the marks or 
        not. The test provided ignore the order in which you store the marks.
        """
        histo = MarkDistribution(100,0)
        histo.addAll([10, 20, 20, 30])

        # As the order of the marks does not matter, we can sort the lists 
        # before comparing them.
        self.assertListEqual(sorted([10,20,20,30]), sorted(histo._marks))
        
        histo.addAll([1, 30, 20, 40])
        self.assertListEqual(sorted([10,20,20,30,1, 30, 20, 40
        ]), sorted(histo._marks))

if __name__ == '__main__':
    unittest.main()
