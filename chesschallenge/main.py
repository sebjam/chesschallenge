class ChessChallenge(object):

    """Builds chessboards and outputs them.

    """
    def __init__(self, width, height, pieces):
        self.valid_boards = []
        self.width = width
        self.height = height
        self.pieces = pieces
        self._place_pieces(pieces)

    def _place_pieces(self, pieces, board=None, unavailable_positions=None):
        if not unavailable_positions:
            unavailable_positions = self._refresh_positions(
                self.empty_board(self.width, self.height),
            )

        if not board:
            board = self.empty_board()

        # TODO: Place pieces on board and append to valid_boards

    def _refresh_positions(
            self, unavailable_positions, piece=None, y=None, x=None):
        # TODO: Given the piece make the x,y unavailable and then calculate the
        # potential hit positions and make them unavailable.
        return unavailable_positions
