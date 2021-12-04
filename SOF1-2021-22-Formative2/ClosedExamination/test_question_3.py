import unittest
from question_3 import getWordsIndices

class TestQuestion3(unittest.TestCase):

    def sameIndices(self, expected, actual):
        """ This is a convenience function to compare the two dictionaries passed
        in parameters. It is needed to ensure that the word passed as keys of
        the dictionary are not case sensitive. 
        
        For example, given:
        expected = {'One': [2,7]} and actual = {'one':[2, 7]} the function call
        sameIndices(expected, actual) would return True. 
        
        On the other hand, given:
        expected = {'One': [2]} and actual = {'one':[3]} the function call
        sameIndices(expected, actual) would raise an AssertionError meaning
        the test has failed.
        """
        self.assertEqual(len(expected), len(actual))
        for word in actual:
            self.assertListEqual(expected[word.lower()], actual[word])

        return True
    

    def testSingleWord(self):
        """ Test that given an input containing only one word, the correct
        result is returned.
        """
        self.assertTrue(self.sameIndices({'one':[0]}, 
                                          getWordsIndices('data//oneWord.txt')))

    def testNonExistingFile(self):
        """ Test that the function returns None if the file does not exist or
        there is an exception whilst reading the file.
        """
        self.assertIsNone(getWordsIndices('doesNotExist.txt'))

    def testSingleWordStartWithSpace(self):
        """ Test that given an input containing only one word and starting with
        a blank space, the correct result is returned. Watch out for the shift
        in the indices.
        """
        self.assertTrue(self.sameIndices({'one':[1]}, 
                                          getWordsIndices('data//oneSpaceAndOneWord.txt')))

    def testTwoWordsSingleSpace(self):
        """ Test that the correct output is returned when there is no duplicate
        words and a single blank space between words.
        """
        self.assertTrue(self.sameIndices({'one':[0], 'two':[4]}, 
                                          getWordsIndices('data//twoWords.txt')))

    def testTwoWordsMultipleSpace(self):
        """ Test that the correct output is returned when there is no duplicate
        words and multiple blank spaces between words.
        """
        self.assertTrue(self.sameIndices({'one':[0], 'two':[6]}, 
                                          getWordsIndices('data//twoWordsTwoSpaces.txt')))

    def testMultipleWordsMultipleIndicies(self):
        """ Test that the correct output is returned when there are duplicate 
        words and multiple indices for the same word. Note that the function 
        should be case incensitive, for example 'One' and 'one' are considered
        to be the same word.
        """
        self.assertTrue(self.sameIndices({'one':[0, 14], 'two':[4], 'three':[8, 19]}, 
                                          getWordsIndices('data//multipleWords.txt')))


if __name__ == '__main__':
    unittest.main()

