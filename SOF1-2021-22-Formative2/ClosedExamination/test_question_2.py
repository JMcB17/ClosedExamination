import unittest
from question_2 import hammingDistance

class TestQuestion2(unittest.TestCase):

    def testSameSequences(self):
        """ Test if a distance of 0 is returned when the sequences are 
        identical.
        """
        self.assertAlmostEqual(0, hammingDistance('lilian', 'lilian'), delta=0.000001)
        self.assertAlmostEqual(0, hammingDistance('1011001', '1011001'), delta=0.000001)

    def testCaseSensitive(self):
        """ Test that the function is case sensitive. That is, the lower 
        case and upper case characters are considered different.
        """
        self.assertAlmostEqual(1, hammingDistance('Lilian', 'lilian'), delta=0.000001)
        self.assertAlmostEqual(2, hammingDistance('Lilian', 'liLian'), delta=0.000001)

    def testGeneralCase(self):
        """ Test that the function calculates the right distance for 
        different sequences.
        """
        self.assertAlmostEqual(3, hammingDistance('karolin', 'kathrin'), delta=0.000001)
        self.assertAlmostEqual(5, hammingDistance('10101', '01010'), delta=0.000001)

    def testInvalidSequencesLength(self):
        """ Test that the function raise a ValueError if the sequences 
        provided are not comparable, that is do not have the same length.
        """
        self.assertRaises(ValueError, hammingDistance, 'caroline', 'catherine')
        self.assertRaises(ValueError, hammingDistance, 'catherine', 'caroline')


if __name__ == '__main__':
    unittest.main()

