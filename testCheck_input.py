import unittest
from tic_tac_toe import check_input


class TestTicTacToe(unittest.TestCase):

    def test_check_input_valid(self):
        b = [[], ["", "X", "O", "X"], ["", "O", "X", "O"], ["", "X", "O", "X"]]
        coordinate = ["2", "2"]
        count = 1
        self.assertFalse(check_input(coordinate, b, count))