import unittest
from io import StringIO
from unittest.mock import patch
from tic_tac_toe import print_board


class TestTicTacToe(unittest.TestCase):

    def test_print_board(self):
        b = [[], ["", "X", "O", "X"], ["", "O", "X", "O"], ["", "X", "O", "X"]]
        expected_output = "---------\n| X O X |\n| O X O |\n| X O X |\n---------\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print_board(b)
            self.assertEqual(fake_output.getvalue(), expected_output)

