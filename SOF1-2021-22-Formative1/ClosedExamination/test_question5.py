
import unittest

from question_5 import add_triathlon_data


class Question5Test(unittest.TestCase):
                              
    def test_too_few_items(self):
        """Test if returns False when an entry does not have enough items
        """
        records = {}
        entry = ''
        self.assertFalse(add_triathlon_data('Alistair Brownlee, 1024, 3548', records),
                          'Should return False as not enough items in string')

    def test_too_many_items(self):
        """Test if returns False when an entry has too many items
        """
        records = {}
        entry = ''
        self.assertFalse(add_triathlon_data('Alistair, Brownlee, 1024, 3548, 1747', records),
                          'Should return False as too many items in string')

    def test_existing_athlete(self):
        """Test if returns False when trying to add an entry of an existing athlete.
        """
        records = {'Alistair Brownlee': {'swim': 1024, 'bike': 3548, 'run': 1747}, \
            'Javier Gomez': {'swim': 1020, 'bike': 3556, 'run': 1756}}
        entry = ''
        self.assertFalse(add_triathlon_data('Javier Gomez, 1030, 3550, 1740', records),
                          'Should return False as Javier Gomez alreadyin records')
        self.assertDictEqual(records, {'Alistair Brownlee': {'swim': 1024, 'bike': 3548, 'run': 1747}, \
            'Javier Gomez': {'swim': 1020, 'bike': 3556, 'run': 1756}}, 
            'The records dictionary should not have been modified.')


    def test_valid_entries(self):
        """Test if returns True when adding multiple valid entries.
        """
        entryset = ['Alistair Brownlee, 1024, 3548, 1747', \
            'Javier Gomez, 1020, 3556, 1756', 
            'Jonathan Brownlee, 1022, 3051, 1777', 
            'David Hauss, 1044, 3530, 1793', 
            'Laurent Vidal, 1047, 3522, 1801']
        records = {}
        for e in entryset:
            self.assertTrue(add_triathlon_data(e,records))

        expected = {'Alistair Brownlee': {'swim': 1024, 'bike': 3548, 'run': 1747}, \
            'Javier Gomez': {'swim': 1020, 'bike': 3556, 'run': 1756}, 
            'Jonathan Brownlee': {'swim': 1022, 'bike': 3051, 'run': 1777}, 
            'David Hauss': {'swim': 1044, 'bike': 3530, 'run': 1793}, 
            'Laurent Vidal': {'swim': 1047, 'bike': 3522, 'run': 1801}}
        self.assertDictEqual(expected, records)


    def test_invalid_items(self):
        """THIS TEST IS OPTIONAL AS IT REQUIRES KNOWLEDGE FROM WEEK 6
        Added here for those who want to have a go at it. 
        NO MARKS DEDUCTED if your code does not pass the test. 
        """
        records = {}
        entry = ''
        self.assertFalse(add_triathlon_data('Alistair, Brownlee, 1024, 3548', records),
                          'Should return False as second value in entry is not an int!')
        self.assertFalse(add_triathlon_data('Alistair Brownlee, 1024.5, 3548, 1747', records),
                          'Should return False as second value in entry is a float not an int!!')


if __name__ == '__main__':
    unittest.main()