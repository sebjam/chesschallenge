import copy


class ChessChallenge(object):

    """Builds chessboards and outputs them.

    """
    def __init__(self, width, height, pieces):
        self.valid_boards = []
        self.width = width
        self.height = height
        self.original_pieces = copy.copy(pieces)
        self._place_pieces(pieces)

    def _place_pieces(self, pieces, board=None, unavailable_positions=None):
        if not unavailable_positions:
            unavailable_positions = self._refresh_positions(
                self._empty_board(),
            )

        if not board:
            board = self._empty_board()

        # TODO: Place pieces on board and append to valid_boards

    def _refresh_positions(
            self, unavailable_positions, piece=None, y=None, x=None):
        # TODO: Given the piece make the x,y unavailable and then calculate the
        # potential hit positions and make them unavailable.
        return unavailable_positions

    def _empty_board(self):
        return [[[] for w in range(self.width)] for h in range(self.height)]
