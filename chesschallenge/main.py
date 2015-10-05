class ChessChallenge(object):

    """Builds chessboards and outputs them.

    """
    def __init__(self, width, height, pieces):
        self.valid_boards = []
        self.width = width
        self.height = height
        self.pieces = pieces
