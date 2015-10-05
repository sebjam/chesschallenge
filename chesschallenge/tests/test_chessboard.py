import unittest

import fixtures

from .main import ChessChallenge


class ChessChallengeTest(unittest.TestCase):

    def test_chessboard_output_one(self):
        pieces = {'Kings': 2, 'Rook': 1}
        chess_challenge = ChessChallenge(width=3, height=3, pieces=pieces)

        self.assertItemsEqual(
            chess_challenge.valid_boards, fixtures.test1_boards)

    def test_chessboard_output_two(self):
        pieces = {'Rook': 1, 'Knights': 4}
        chess_challenge = ChessChallenge(width=3, height=3, pieces=pieces)

        self.assertItemsEqual(
            chess_challenge.valid_boards, fixtures.test1_boards)
