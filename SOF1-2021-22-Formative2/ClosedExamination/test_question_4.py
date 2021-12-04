import unittest
from question_4 import rodCutting

class TestQuestion4(unittest.TestCase):

    def testLengthZero(self):
        """ Test that the function returns 0 when the length of the rod is 0.
        """
        self.assertAlmostEqual([], rodCutting({2:5, 3:8, 4:14, 6:17}, 0))

    def testSimpleCase(self):
        """ Test that the function returns the correct value for the simple 
        case where the value of a segment of a rod is equal to its length. 
        Your result is sorted automatically, so you don't have to do it 
        yourself. As the order does not matter, It is easier to compare your 
        solution once it is sorted.
        """
        self.assertListEqual(sorted(rodCutting({2:5, 3:8, 4:14, 6:17}, 9)), [4,4])
        self.assertListEqual(sorted(rodCutting({2:5, 3:8, 6:16, 8: 25}, 9)), [8])

    def testMultipleSolutions(self):
        """ Test that the function returns one of the correct solution when
        there are more than optimal solutions.        
        As there are more than one possible solution, the test assert that 
        the returned list is within a list of all possible optimal solutions. 
        Your result is sorted automatically, so you don't have to do it 
        yourself. As the order does not matter, It is easier to compare your 
        solution once it is sorted.
        """
        self.assertIn(sorted(rodCutting({2:5, 3:8, 4:13, 6:17}, 9)), 
                      [[4,4], [2,3,4]])
        self.assertIn(sorted(rodCutting({2:5, 3:8, 6:16}, 9)),
                      [[3,6], [3,3,3]])


if __name__ == '__main__':
    unittest.main()

