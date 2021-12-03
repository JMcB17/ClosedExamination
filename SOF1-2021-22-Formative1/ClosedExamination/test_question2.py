
import unittest

from question_2 import seconds_to_time


class Question2Test(unittest.TestCase):
                              
    def test_time_too_big(self):
        """Test if return None if time greater or equal to 100 hours
        """
        self.assertIsNone(seconds_to_time(360000),
                          "Should return None if time greater or equal to 100 hours.")

    def test_HoursMinutesSecondes(self):
        """Test if output is correct for time greater than an hour, and less
        than 100 hours
        """
        self.assertEqual('99:59:59', seconds_to_time(359999))
        self.assertEqual('01:02:03', seconds_to_time(3723))
        self.assertEqual('01:00:03', seconds_to_time(3603))


    def test_MinutesSecondes(self):
        """Test if output is correct for time below an hour and time smaller
        than a minute.
        """
        self.assertEqual('59:59', seconds_to_time(3599))
        self.assertEqual('02:03', seconds_to_time(123))
        self.assertEqual('02:33', seconds_to_time(153))
        self.assertEqual('01:00', seconds_to_time(60))
        self.assertEqual('00:59', seconds_to_time(59))



if __name__ == '__main__':
    unittest.main()

