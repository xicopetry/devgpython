#!/usr/bin/env python

from collections import namedtuple
import unittest
import main
from mock import Mock


class TestMain(unittest.TestCase):

    def test_main(self):
        test_list = [
            '1',
            '1 2 10 I',
            '3 1 11 C',
            '1 2 19 R',
            '1 2 21 C',
            '1 1 25 C',
            '4 1 25 I',
            '',
        ]
        # Mock the effect of raw_input
        main.raw_input = Mock(side_effect=test_list)
        output = main.main()
        expected_result = [
            '1 2 66',
            '3 1 11',
            '4 0 0'
        ]
        self.assertEquals(output, expected_result)

    def test_filter_inputs(self):
        """
        Test the function filter inputs.
        It should receive a list of the user inputs and return an other list.
        The list that is returned containing only valid inputs, in namedtuples,
        and sorted by the contestant name and the order it was submited.
        The order is important, because of the penalty time, that is computed
        as the the number of minutes it took until the first correct submission
        for a problem was received, plus 20 minutes for each incorrect
        submission prior to the correct solution.
        """
        test_list = [
            '1 1 10 I',  # index 0
            '1 1 21 C',  # index 1
            '4 2 10 C',  # index 2
            '2 2 10 C',  # index 3
            '1 2 10 C',  # index 4
            '3 1 11 C',  # index 5
        ]
        result_received = main.filter_inputs(test_list)
        Input = namedtuple(
                'Input', ['contestant', 'problem', 'time', 'letter', 'index']
        )
        expected_result = [
            Input(contestant=1, problem=1, time=10, letter='I', index=0),
            Input(contestant=1, problem=1, time=21, letter='C', index=1),
            Input(contestant=1, problem=2, time=10, letter='C', index=4),
            Input(contestant=2, problem=2, time=10, letter='C', index=3),
            Input(contestant=3, problem=1, time=11, letter='C', index=5),
            Input(contestant=4, problem=2, time=10, letter='C', index=2)
        ]
        self.assertEquals(result_received, expected_result)

    def test_incorrect_after_correct(self):
        """
        Test if will discart all the incorrect inputs received for a problem
        after receive a correct one
        """
        test_list = [
            '1',
            '1 2 10 I',
            '3 1 11 C',
            '1 2 19 R',
            '1 2 21 C',
            '1 1 25 C',
            '1 2 10 I',  # This incorret will not be considered
            '4 1 25 I',
            '3 1 10 I',  # This incorret will not be considered
            '',
        ]
        # Mock the effect of raw_input
        main.raw_input = Mock(side_effect=test_list)
        output = main.main()
        expected_result = [
            '1 2 66',
            '3 1 11',
            '4 0 0'
        ]
        self.assertEquals(output, expected_result)


if __name__ == '__main__':
    unittest.main()
