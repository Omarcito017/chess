from chess.board import Board
from chess.color import Color


class Game:
    """The class Game represents the actual flow of gameplay of Chess."""

    def __init__(self):
        self.board = Board()
        self.board.initialize_pieces(Color.WHITE)
        self.board.initialize_pieces(Color.BLACK)
